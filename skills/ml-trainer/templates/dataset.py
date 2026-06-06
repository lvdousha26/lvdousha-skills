"""
PyTorch数据加载模板
支持CSV、图像、文本等常见数据类型
"""

import torch
from torch.utils.data import Dataset, DataLoader
import numpy as np
import pandas as pd
from PIL import Image
from pathlib import Path
import json
from typing import Tuple, Optional, Callable, List, Dict, Any


class CSVDataset(Dataset):
    """CSV数据集加载器"""

    def __init__(
        self,
        csv_path: str,
        target_col: str,
        feature_cols: List[str] = None,
        transform: Optional[Callable] = None
    ):
        """
        Args:
            csv_path: CSV文件路径
            target_col: 目标列名
            feature_cols: 特征列名列表，None表示使用所有非目标列
            transform: 数据转换函数
        """
        self.df = pd.read_csv(csv_path)
        self.target_col = target_col
        self.feature_cols = feature_cols or [c for c in self.df.columns if c != target_col]
        self.transform = transform

        self.features = self.df[self.feature_cols].values
        self.targets = self.df[target_col].values

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        x = self.features[idx].astype(np.float32)
        y = self.targets[idx]

        if self.transform:
            x = self.transform(x)

        return torch.tensor(x), torch.tensor(y)


class ImageDataset(Dataset):
    """图像数据集加载器

    支持两种目录结构:
    1. root/class1/image1.jpg, root/class2/image2.jpg ...
    2. root/images/image1.jpg (需要CSV标注)
    """

    def __init__(
        self,
        root_dir: str,
        annotation_file: Optional[str] = None,
        transform: Optional[Callable] = None,
        class_to_idx: Optional[Dict[str, int]] = None
    ):
        """
        Args:
            root_dir: 数据根目录
            annotation_file: 标注文件路径(CSV格式: filename,label)
            transform: 图像转换函数
            class_to_idx: 类别到索引的映射
        """
        self.root_dir = Path(root_dir)
        self.transform = transform
        self.samples = []
        self.classes = []
        self.class_to_idx = class_to_idx or {}

        if annotation_file:
            # 从CSV文件加载标注
            df = pd.read_csv(annotation_file)
            for _, row in df.iterrows():
                img_path = self.root_dir / row.iloc[0]
                label = row.iloc[1]
                self.samples.append((str(img_path), label))

            # 构建类别映射
            unique_labels = df.iloc[:, 1].unique()
            self.classes = sorted(unique_labels)
            self.class_to_idx = {c: i for i, c in enumerate(self.classes)}
        else:
            # 从目录结构加载
            for class_dir in sorted(self.root_dir.iterdir()):
                if class_dir.is_dir():
                    class_name = class_dir.name
                    if class_name not in self.class_to_idx:
                        self.class_to_idx[class_name] = len(self.classes)
                        self.classes.append(class_name)

                    class_idx = self.class_to_idx[class_name]
                    for img_path in class_dir.iterdir():
                        if img_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.bmp']:
                            self.samples.append((str(img_path), class_idx))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        img_path, label = self.samples[idx]

        # 加载图像
        image = Image.open(img_path).convert('RGB')

        if self.transform:
            image = self.transform(image)

        return image, torch.tensor(label)


class TextDataset(Dataset):
    """文本数据集加载器"""

    def __init__(
        self,
        texts: List[str],
        labels: List[int],
        tokenizer: Callable,
        max_length: int = 512
    ):
        """
        Args:
            texts: 文本列表
            labels: 标签列表
            tokenizer: 分词器函数
            max_length: 最大序列长度
        """
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]

        # 分词
        encoded = self.tokenizer(
            text,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        return {
            'input_ids': encoded['input_ids'].squeeze(0),
            'attention_mask': encoded['attention_mask'].squeeze(0)
        }, torch.tensor(label)


class NumpyDataset(Dataset):
    """NumPy数组数据集"""

    def __init__(
        self,
        data_path: str,
        label_path: Optional[str] = None,
        transform: Optional[Callable] = None
    ):
        """
        Args:
            data_path: 数据文件路径(.npy)
            label_path: 标签文件路径，None表示无标签数据
            transform: 数据转换函数
        """
        self.data = np.load(data_path)
        self.labels = np.load(label_path) if label_path else None
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        x = self.data[idx].astype(np.float32)

        if self.transform:
            x = self.transform(x)

        if self.labels is not None:
            y = self.labels[idx]
            return torch.tensor(x), torch.tensor(y)
        return torch.tensor(x)


def create_dataloaders(
    train_dataset: Dataset,
    val_dataset: Dataset = None,
    test_dataset: Dataset = None,
    batch_size: int = 32,
    num_workers: int = 4,
    pin_memory: bool = True
) -> Dict[str, DataLoader]:
    """创建DataLoader字典

    Args:
        train_dataset: 训练数据集
        val_dataset: 验证数据集
        test_dataset: 测试数据集
        batch_size: 批次大小
        num_workers: 数据加载进程数
        pin_memory: 是否锁页内存(GPU训练时建议开启)

    Returns:
        包含train/val/test DataLoader的字典
    """
    dataloaders = {}

    dataloaders['train'] = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        pin_memory=pin_memory
    )

    if val_dataset:
        dataloaders['val'] = DataLoader(
            val_dataset,
            batch_size=batch_size,
            shuffle=False,
            num_workers=num_workers,
            pin_memory=pin_memory
        )

    if test_dataset:
        dataloaders['test'] = DataLoader(
            test_dataset,
            batch_size=batch_size,
            shuffle=False,
            num_workers=num_workers,
            pin_memory=pin_memory
        )

    return dataloaders


def get_data_info(dataset: Dataset) -> Dict[str, Any]:
    """获取数据集信息"""
    info = {
        "size": len(dataset),
        "num_classes": None,
        "feature_shape": None
    }

    # 获取第一个样本
    sample = dataset[0]

    if isinstance(sample, tuple):
        x, y = sample
        info["feature_shape"] = list(x.shape) if hasattr(x, 'shape') else None
        info["num_classes"] = len(set(dataset.targets)) if hasattr(dataset, 'targets') else None
    elif isinstance(sample, dict):
        info["feature_shape"] = {k: list(v.shape) for k, v in sample.items() if hasattr(v, 'shape')}

    return info
