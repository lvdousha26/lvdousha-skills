"""
Scikit-learn训练脚本模板
支持分类、回归、聚类等常见任务
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix, mean_squared_error, r2_score
import joblib
import json
from pathlib import Path
from typing import Dict, Any, Tuple
import matplotlib.pyplot as plt
import seaborn as sns


class SKLearnModel:
    """Scikit-learn模型封装类"""

    def __init__(self, model, model_type: str = "classifier", config: Dict[str, Any] = None):
        """
        Args:
            model: sklearn模型实例
            model_type: 模型类型 (classifier/regressor/cluster)
            config: 配置字典
        """
        self.model = model
        self.model_type = model_type
        self.config = config or {}
        self.pipeline = None
        self.is_fitted = False

        # 记录元数据
        self.metadata = {
            "model_type": model_type,
            "feature_names": None,
            "label_names": None,
            "metrics": {}
        }

    def build_pipeline(self, preprocessors=None):
        """构建训练流水线"""
        if preprocessors is None:
            preprocessors = [('scaler', StandardScaler())]

        steps = preprocessors + [('model', self.model)]
        self.pipeline = Pipeline(steps)
        return self.pipeline

    def train(self, X: np.ndarray, y: np.ndarray,
              test_size: float = 0.2,
              random_state: int = 42) -> Dict[str, float]:
        """训练模型"""
        # 划分数据集
        X_train, X_val, y_train, y_val = train_test_split(
            X, y,
            test_size=test_size,
            random_state=random_state,
            stratify=y if self.model_type == "classifier" else None
        )

        # 构建流水线
        if self.pipeline is None:
            self.build_pipeline()

        # 训练
        self.pipeline.fit(X_train, y_train)
        self.is_fitted = True

        # 评估
        metrics = self._evaluate(X_train, y_train, X_val, y_val)

        # 交叉验证
        cv_scores = cross_val_score(
            self.pipeline, X_train, y_train,
            cv=self.config.get("cv_folds", 5),
            scoring=self.config.get("scoring", None)
        )

        metrics["cv_mean"] = cv_scores.mean()
        metrics["cv_std"] = cv_scores.std()

        # 打印结果
        self._print_results(metrics)

        return metrics

    def _evaluate(self, X_train, y_train, X_val, y_val) -> Dict[str, float]:
        """评估模型性能"""
        metrics = {}

        if self.model_type == "classifier":
            train_score = self.pipeline.score(X_train, y_train)
            val_score = self.pipeline.score(X_val, y_val)

            y_pred = self.pipeline.predict(X_val)

            metrics["train_score"] = train_score
            metrics["val_score"] = val_score

            # 详细分类报告
            self.metadata["metrics"]["classification_report"] = \
                classification_report(y_val, y_pred, output_dict=True)

        elif self.model_type == "regressor":
            train_pred = self.pipeline.predict(X_train)
            val_pred = self.pipeline.predict(X_val)

            metrics["train_r2"] = r2_score(y_train, train_pred)
            metrics["val_r2"] = r2_score(y_val, val_pred)
            metrics["train_rmse"] = np.sqrt(mean_squared_error(y_train, train_pred))
            metrics["val_rmse"] = np.sqrt(mean_squared_error(y_val, val_pred))

        return metrics

    def hyperparameter_tune(self, X: np.ndarray, y: np.ndarray,
                           param_grid: Dict[str, list],
                           cv: int = 5) -> Dict[str, Any]:
        """超参数调优"""
        if self.pipeline is None:
            self.build_pipeline()

        grid_search = GridSearchCV(
            self.pipeline,
            param_grid,
            cv=cv,
            n_jobs=-1,
            verbose=1,
            return_train_score=True
        )

        grid_search.fit(X, y)

        # 更新模型
        self.pipeline = grid_search.best_estimator_

        print(f"\n最佳参数: {grid_search.best_params_}")
        print(f"最佳分数: {grid_search.best_score_:.4f}")

        return {
            "best_params": grid_search.best_params_,
            "best_score": grid_search.best_score_,
            "cv_results": grid_search.cv_results_
        }

    def predict(self, X: np.ndarray):
        """预测"""
        if not self.is_fitted:
            raise ValueError("模型尚未训练，请先调用train()方法")
        return self.pipeline.predict(X)

    def predict_proba(self, X: np.ndarray):
        """预测概率（仅分类器）"""
        if self.model_type != "classifier":
            raise ValueError("只有分类器支持概率预测")
        return self.pipeline.predict_proba(X)

    def save(self, path: str):
        """保存模型"""
        save_data = {
            "pipeline": self.pipeline,
            "metadata": self.metadata,
            "config": self.config
        }
        joblib.dump(save_data, path)
        print(f"模型已保存到: {path}")

    @classmethod
    def load(cls, path: str):
        """加载模型"""
        save_data = joblib.load(path)

        instance = cls(
            model=save_data["pipeline"].named_steps['model'],
            model_type=save_data["metadata"]["model_type"],
            config=save_data.get("config", {})
        )
        instance.pipeline = save_data["pipeline"]
        instance.metadata = save_data["metadata"]
        instance.is_fitted = True

        return instance

    def _print_results(self, metrics: Dict[str, float]):
        """打印训练结果"""
        print("=" * 50)
        print("训练结果")
        print("=" * 50)

        if self.model_type == "classifier":
            print(f"训练集准确率: {metrics['train_score']:.4f}")
            print(f"验证集准确率: {metrics['val_score']:.4f}")
            print(f"交叉验证均值: {metrics['cv_mean']:.4f} (±{metrics['cv_std']:.4f})")

        elif self.model_type == "regressor":
            print(f"训练集 R²: {metrics['train_r2']:.4f}")
            print(f"验证集 R²: {metrics['val_r2']:.4f}")
            print(f"训练集 RMSE: {metrics['train_rmse']:.4f}")
            print(f"验证集 RMSE: {metrics['val_rmse']:.4f}")

        print("=" * 50)


class DataLoader:
    """数据加载和预处理工具"""

    @staticmethod
    def load_csv(path: str, target_col: str = None) -> Tuple[np.ndarray, np.ndarray]:
        """从CSV加载数据"""
        df = pd.read_csv(path)

        if target_col:
            X = df.drop(columns=[target_col]).values
            y = df[target_col].values
            return X, y
        return df.values

    @staticmethod
    def encode_labels(y: np.ndarray) -> Tuple[np.ndarray, LabelEncoder]:
        """编码标签"""
        le = LabelEncoder()
        y_encoded = le.fit_transform(y)
        return y_encoded, le

    @staticmethod
    def split_data(X: np.ndarray, y: np.ndarray,
                   test_size: float = 0.2,
                   val_size: float = 0.1,
                   random_state: int = 42) -> Tuple:
        """划分训练/验证/测试集"""
        # 先划分出测试集
        X_temp, X_test, y_temp, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )

        # 再从剩余数据中划分验证集
        val_ratio = val_size / (1 - test_size)
        X_train, X_val, y_train, y_val = train_test_split(
            X_temp, y_temp, test_size=val_ratio, random_state=random_state
        )

        return X_train, X_val, X_test, y_train, y_val, y_test


def quick_train(model_type: str, X: np.ndarray, y: np.ndarray,
                model_name: str = "rf") -> SKLearnModel:
    """快速训练函数

    Args:
        model_type: 模型类型 (classifier/regressor)
        X: 特征数据
        y: 标签数据
        model_name: 模型名称
            分类器: 'rf'(随机森林), 'lr'(逻辑回归), 'svm', 'knn', 'xgboost'
            回归器: 'rf'(随机森林), 'lr'(线性回归), 'ridge', 'lasso', 'xgboost'
    """
    from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
    from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge, Lasso
    from sklearn.svm import SVC, SVR
    from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

    # 模型映射
    models = {
        "classifier": {
            "rf": RandomForestClassifier(n_estimators=100, random_state=42),
            "lr": LogisticRegression(max_iter=1000, random_state=42),
            "svm": SVC(random_state=42),
            "knn": KNeighborsClassifier()
        },
        "regressor": {
            "rf": RandomForestRegressor(n_estimators=100, random_state=42),
            "lr": LinearRegression(),
            "ridge": Ridge(random_state=42),
            "lasso": Lasso(random_state=42, max_iter=10000)
        }
    }

    model = models[model_type][model_name]
    trainer = SKLearnModel(model, model_type)

    trainer.train(X, y)

    return trainer
