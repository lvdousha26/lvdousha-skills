"""
PyTorch完整训练脚本模板
支持数据加载、训练、验证、保存等完整流程
"""

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from torch.cuda.amp import autocast, GradScaler
from pathlib import Path
import json
from tqdm import tqdm
from typing import Dict, Any
import time


class Trainer:
    """通用PyTorch训练器"""

    def __init__(
        self,
        model: nn.Module,
        train_loader: DataLoader,
        val_loader: DataLoader,
        config: Dict[str, Any],
        save_dir: str = "./checkpoints"
    ):
        self.model = model
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.config = config
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(parents=True, exist_ok=True)

        # 设备
        self.device = torch.device(
            config.get("device", "cuda" if torch.cuda.is_available() else "cpu")
        )
        self.model.to(self.device)

        # 优化器
        self.optimizer = self._create_optimizer()

        # 学习率调度器
        self.scheduler = self._create_scheduler()

        # 损失函数
        self.criterion = self._create_criterion()

        # Early stopping
        self.best_val_loss = float('inf')
        self.patience_counter = 0

        # 混合精度训练
        self.use_amp = config.get("use_amp", False)
        self.scaler = GradScaler() if self.use_amp else None

        # 训练历史
        self.history = {
            "train_loss": [],
            "val_loss": [],
            "train_acc": [],
            "val_acc": [],
            "lr": []
        }

    def _create_optimizer(self):
        """创建优化器"""
        opt_type = self.config.get("optimizer", "adam").lower()
        lr = self.config.get("learning_rate", 0.001)
        weight_decay = self.config.get("weight_decay", 1e-5)

        if opt_type == "adam":
            return torch.optim.Adam(
                self.model.parameters(),
                lr=lr,
                weight_decay=weight_decay
            )
        elif opt_type == "adamw":
            return torch.optim.AdamW(
                self.model.parameters(),
                lr=lr,
                weight_decay=weight_decay
            )
        elif opt_type == "sgd":
            return torch.optim.SGD(
                self.model.parameters(),
                lr=lr,
                momentum=0.9,
                weight_decay=weight_decay
            )
        else:
            raise ValueError(f"Unknown optimizer: {opt_type}")

    def _create_scheduler(self):
        """创建学习率调度器"""
        sched_type = self.config.get("scheduler", "plateau").lower()

        if sched_type == "plateau":
            return torch.optim.lr_scheduler.ReduceLROnPlateau(
                self.optimizer,
                mode='min',
                factor=0.5,
                patience=5,
                verbose=True
            )
        elif sched_type == "cosine":
            return torch.optim.lr_scheduler.CosineAnnealingLR(
                self.optimizer,
                T_max=self.config.get("epochs", 100)
            )
        elif sched_type == "step":
            return torch.optim.lr_scheduler.StepLR(
                self.optimizer,
                step_size=30,
                gamma=0.1
            )
        else:
            return None

    def _create_criterion(self):
        """创建损失函数"""
        loss_type = self.config.get("loss", "cross_entropy").lower()

        if loss_type == "cross_entropy":
            return nn.CrossEntropyLoss()
        elif loss_type == "mse":
            return nn.MSELoss()
        elif loss_type == "bce":
            return nn.BCEWithLogitsLoss()
        else:
            raise ValueError(f"Unknown loss function: {loss_type}")

    def train_epoch(self) -> tuple:
        """训练一个epoch"""
        self.model.train()
        total_loss = 0
        correct = 0
        total = 0

        pbar = tqdm(self.train_loader, desc="Training")
        for batch in pbar:
            # 将数据移到设备
            inputs, targets = self._move_to_device(batch)

            self.optimizer.zero_grad()

            # 混合精度训练
            if self.use_amp:
                with autocast():
                    outputs = self.model(inputs)
                    loss = self.criterion(outputs, targets)

                self.scaler.scale(loss).backward()
                self.scaler.step(self.optimizer)
                self.scaler.update()
            else:
                outputs = self.model(inputs)
                loss = self.criterion(outputs, targets)
                loss.backward()
                self.optimizer.step()

            # 统计
            total_loss += loss.item()
            if isinstance(self.criterion, nn.CrossEntropyLoss):
                _, predicted = outputs.max(1)
                correct += predicted.eq(targets).sum().item()
                total += targets.size(0)

            pbar.set_postfix({"loss": loss.item()})

        avg_loss = total_loss / len(self.train_loader)
        acc = correct / total if total > 0 else 0
        return avg_loss, acc

    @torch.no_grad()
    def validate(self) -> tuple:
        """验证"""
        self.model.eval()
        total_loss = 0
        correct = 0
        total = 0

        for batch in self.val_loader:
            inputs, targets = self._move_to_device(batch)
            outputs = self.model(inputs)
            loss = self.criterion(outputs, targets)

            total_loss += loss.item()

            if isinstance(self.criterion, nn.CrossEntropyLoss):
                _, predicted = outputs.max(1)
                correct += predicted.eq(targets).sum().item()
                total += targets.size(0)

        avg_loss = total_loss / len(self.val_loader)
        acc = correct / total if total > 0 else 0
        return avg_loss, acc

    def _move_to_device(self, batch):
        """将批次数据移到设备"""
        if isinstance(batch, (tuple, list)):
            return [x.to(self.device) for x in batch]
        elif isinstance(batch, dict):
            return {k: v.to(self.device) for k, v in batch.items()}
        else:
            return batch.to(self.device)

    def train(self):
        """完整训练流程"""
        epochs = self.config.get("epochs", 100)
        patience = self.config.get("early_stopping_patience", 10)

        print(f"开始训练 - 设备: {self.device}")
        print(f"模型参数量: {sum(p.numel() for p in self.model.parameters()):,}")
        print("=" * 50)

        start_time = time.time()

        for epoch in range(epochs):
            print(f"\nEpoch {epoch + 1}/{epochs}")

            # 训练
            train_loss, train_acc = self.train_epoch()

            # 验证
            val_loss, val_acc = self.validate()

            # 记录历史
            self.history["train_loss"].append(train_loss)
            self.history["val_loss"].append(val_loss)
            self.history["train_acc"].append(train_acc)
            self.history["val_acc"].append(val_acc)
            self.history["lr"].append(self.optimizer.param_groups[0]["lr"])

            # 学习率调度
            if self.scheduler is not None:
                if isinstance(self.scheduler, torch.optim.lr_scheduler.ReduceLROnPlateau):
                    self.scheduler.step(val_loss)
                else:
                    self.scheduler.step()

            # 打印结果
            print(f"Train Loss: {train_loss:.4f} | Train Acc: {train_acc:.4f}")
            print(f"Val Loss: {val_loss:.4f} | Val Acc: {val_acc:.4f}")
            print(f"LR: {self.optimizer.param_groups[0]['lr']:.6f}")

            # 保存最佳模型
            if val_loss < self.best_val_loss:
                self.best_val_loss = val_loss
                self.patience_counter = 0
                self.save_checkpoint("best_model.pt")
                print("✓ 保存最佳模型")
            else:
                self.patience_counter += 1

            # Early stopping
            if self.patience_counter >= patience:
                print(f"\nEarly stopping at epoch {epoch + 1}")
                break

            # 定期保存
            if (epoch + 1) % self.config.get("save_interval", 10) == 0:
                self.save_checkpoint(f"checkpoint_epoch_{epoch + 1}.pt")

        training_time = time.time() - start_time
        print(f"\n训练完成! 用时: {training_time / 60:.2f}分钟")
        print(f"最佳验证损失: {self.best_val_loss:.4f}")

        # 保存训练历史
        self.save_history()

    def save_checkpoint(self, filename: str):
        """保存检查点"""
        checkpoint = {
            "model_state_dict": self.model.state_dict(),
            "optimizer_state_dict": self.optimizer.state_dict(),
            "epoch": len(self.history["train_loss"]),
            "best_val_loss": self.best_val_loss,
            "config": self.config,
            "history": self.history
        }

        if self.scheduler is not None:
            checkpoint["scheduler_state_dict"] = self.scheduler.state_dict()

        save_path = self.save_dir / filename
        torch.save(checkpoint, save_path)

    def load_checkpoint(self, filename: str):
        """加载检查点"""
        checkpoint = torch.load(self.save_dir / filename, map_location=self.device)

        self.model.load_state_dict(checkpoint["model_state_dict"])
        self.optimizer.load_state_dict(checkpoint["optimizer_state_dict"])

        if "scheduler_state_dict" in checkpoint and self.scheduler is not None:
            self.scheduler.load_state_dict(checkpoint["scheduler_state_dict"])

        self.best_val_loss = checkpoint.get("best_val_loss", float('inf'))
        self.history = checkpoint.get("history", self.history)

        print(f"已加载检查点: {filename}")

    def save_history(self):
        """保存训练历史"""
        history_path = self.save_dir / "training_history.json"
        with open(history_path, "w") as f:
            json.dump(self.history, f, indent=2)


def train_from_config(model, train_loader, val_loader, config_path: str):
    """从配置文件开始训练"""
    with open(config_path, "r") as f:
        config = json.load(f)

    trainer = Trainer(model, train_loader, val_loader, config)
    trainer.train()

    return trainer
