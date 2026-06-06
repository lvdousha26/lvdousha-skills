---
name: ml_trainer
description: Python机器学习模型训练助手，支持数据预处理、模型训练、评估、保存完整流程，涵盖PyTorch和Scikit-learn框架
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash]
---

# ML Trainer - 机器学习训练助手

## 概述

这个skill帮助你完成Python机器学习项目的完整开发流程，包括数据预处理、模型构建、训练、评估和部署。支持PyTorch深度学习和Scikit-learn传统机器学习。

## 何时使用

当你的请求涉及以下内容时，Claude会激活此skill：
- "训练一个模型"、"模型训练"、"ML training"
- "数据预处理"、"特征工程"、"data preprocessing"
- "PyTorch"、"TensorFlow"、"scikit-learn"
- "模型评估"、"准确率"、"loss曲线"
- "保存/加载模型"、"checkpoint"
- "超参数调优"、"模型优化"

## 工作流程

### 阶段1：需求分析

1. **明确任务类型**
   - 分类/回归/聚类
   - 图像/文本/表格数据
   - 监督/无监督学习

2. **确定框架选择**
   - 深度学习 → PyTorch
   - 传统ML → Scikit-learn
   - 预训练模型 → Hugging Face

### 阶段2：项目结构

创建标准ML项目结构：
```
project/
├── data/               # 数据目录
│   ├── raw/           # 原始数据
│   ├── processed/     # 处理后数据
├── src/               # 源代码
│   ├── data.py        # 数据处理
│   ├── model.py       # 模型定义
│   ├── train.py       # 训练脚本
│   └── utils.py       # 工具函数
├── checkpoints/       # 模型检查点
├── logs/              # 训练日志
└── requirements.txt   # 依赖
```

### 阶段3：数据处理

**关键步骤：**
1. 数据加载与探索
2. 缺失值处理
3. 特征工程
4. 数据集划分（train/val/test）
5. 数据增强（可选）

**检查清单：**
- [ ] 数据已正确加载
- [ ] 特征类型正确识别（数值/类别/文本）
- [ ] 类别标签已编码
- [ ] 数据已标准化/归一化
- [ ] 划分比例合理（如70/15/15）

### 阶段4：模型构建

**PyTorch模型模板：**
- 继承`nn.Module`
- 实现`__init__`和`forward`
- 添加适当的激活函数和dropout

**Scikit-learn模板：**
- 选择合适的estimator
- 使用Pipeline组合预处理+模型
- 设置随机种子保证可复现性

### 阶段5：训练配置

**必须包含的配置：**
```python
config = {
    "batch_size": 32,
    "learning_rate": 0.001,
    "epochs": 100,
    "optimizer": "adam",
    "device": "cuda" if torch.cuda.is_available() else "cpu",
    "early_stopping_patience": 10,
    "random_seed": 42
}
```

### 阶段6：训练与监控

**关键监控指标：**
- Training/Validation loss
- Training/Validation accuracy
- Learning rate schedule
- Gradient norms（检测梯度爆炸）

**必须实现：**
- [ ] 训练循环
- [ ] 验证循环
- [ ] Early stopping
- [ ] Model checkpoint保存
- [ ] TensorBoard/WandB日志

### 阶段7：评估与保存

**评估内容：**
- 在测试集上评估
- 生成混淆矩阵/分类报告
- 可视化结果（ROC曲线、预测分布等）

**保存内容：**
- 最佳模型权重
- 训练配置
- 评估结果
- 预测示例

## 代码模板

### PyTorch训练模板

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

class Trainer:
    def __init__(self, model, config):
        self.model = model
        self.config = config
        self.device = torch.device(config["device"])
        self.model.to(self.device)

        self.optimizer = torch.optim.Adam(
            model.parameters(),
            lr=config["learning_rate"]
        )
        self.criterion = nn.CrossEntropyLoss()

    def train_epoch(self, train_loader):
        self.model.train()
        total_loss = 0
        for batch in train_loader:
            self.optimizer.zero_grad()
            # 前向传播
            loss = self._forward_batch(batch)
            # 反向传播
            loss.backward()
            self.optimizer.step()
            total_loss += loss.item()
        return total_loss / len(train_loader)

    def validate(self, val_loader):
        self.model.eval()
        total_loss = 0
        correct = 0
        with torch.no_grad():
            for batch in val_loader:
                loss = self._forward_batch(batch)
                total_loss += loss.item()
        return total_loss / len(val_loader)

    def train(self, train_loader, val_loader, epochs):
        best_loss = float('inf')
        patience_counter = 0

        for epoch in range(epochs):
            train_loss = self.train_epoch(train_loader)
            val_loss = self.validate(val_loader)

            # Early stopping
            if val_loss < best_loss:
                best_loss = val_loss
                self.save_checkpoint(f"checkpoint_epoch_{epoch}.pt")
                patience_counter = 0
            else:
                patience_counter += 1

            if patience_counter >= self.config.get("early_stopping_patience", 10):
                print(f"Early stopping at epoch {epoch}")
                break

    def save_checkpoint(self, path):
        torch.save({
            'model_state_dict': self.model.state_dict(),
            'optimizer_state_dict': self.optimizer.state_dict(),
            'config': self.config
        }, path)
```

### Scikit-learn训练模板

```python
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

class SKLearnTrainer:
    def __init__(self, model, config):
        self.model = model
        self.config = config
        self.pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('model', model)
        ])

    def train(self, X, y):
        X_train, X_val, y_train, y_val = train_test_split(
            X, y,
            test_size=self.config.get("val_size", 0.2),
            random_state=self.config.get("random_seed", 42)
        )

        self.pipeline.fit(X_train, y_train)

        val_score = self.pipeline.score(X_val, y_val)
        print(f"Validation score: {val_score:.4f}")

        return self.pipeline

    def hyperparameter_tune(self, X, y, param_grid):
        grid_search = GridSearchCV(
            self.pipeline,
            param_grid,
            cv=self.config.get("cv_folds", 5),
            n_jobs=-1
        )
        grid_search.fit(X, y)
        self.pipeline = grid_search.best_estimator_
        return grid_search.best_params_

    def evaluate(self, X_test, y_test):
        y_pred = self.pipeline.predict(X_test)
        print(classification_report(y_test, y_pred))

    def save_model(self, path):
        joblib.dump(self.pipeline, path)
```

## 最佳实践

### 数据处理
- 始终检查数据分布（类别平衡、异常值）
- 使用相同的preprocessor处理train/val/test
- 保存preprocessor用于推理时复用

### 模型训练
- 设置随机种子保证可复现性
- 使用学习率调度器
- 监控train/val差距检测过拟合
- 保存最佳checkpoint，不只是最后的

### 调试技巧
- 从小数据集/少epoch开始验证流程
- 打印输入输出shape
- 检查梯度流动（是否出现NaN/Inf）
- 使用torchinfo查看模型结构

### 性能优化
- 使用DataLoader的num_workers加速数据加载
- 混合精度训练（torch.cuda.amp）
- Gradient accumulation处理大batch size

## 常见问题

**问题：训练loss不下降**
- 检查learning rate是否过小/过大
- 确认loss函数是否正确
- 验证数据label是否正确

**问题：过拟合（train loss低，val loss高）**
- 增加dropout/data augmentation
- 减小模型复杂度
- 增加训练数据
- 使用正则化

**问题：GPU内存不足**
- 减小batch_size
- 使用gradient checkpointing
- 清理不需要的中间变量

## 示例请求

**好示例：**
- "帮我训练一个PyTorch图像分类模型，数据在data/images目录"
- "用scikit-learn做房价预测，需要数据预处理和模型评估"
- "调试这个训练脚本，loss一直是NaN"

**坏示例：**
- "训练模型"（缺少具体信息）
- "帮我写代码"（太宽泛）

## 相关资源

- PyTorch文档：https://pytorch.org/docs/
- Scikit-learn文档：https://scikit-learn.org/
- 模型模板：见`templates/`目录
- 示例代码：见`references/`目录
