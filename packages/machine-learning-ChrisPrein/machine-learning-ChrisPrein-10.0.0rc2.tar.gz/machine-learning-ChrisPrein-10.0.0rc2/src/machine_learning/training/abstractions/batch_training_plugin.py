from abc import ABC, abstractmethod
from dataclasses import dataclass
from logging import Logger
from typing import Dict, Generic, List, Tuple, Deque, Union

from ...evaluation.abstractions.evaluation_service import Score

from ...modeling.abstractions.model import Model, TInput, TTarget
from ...evaluation.contexts.evaluation_context import *

TModel = TypeVar('TModel', bound=Model)

@dataclass
class TrainingContext(Generic[TInput, TTarget, TModel]):
    model: TModel
    dataset_name: str
    current_epoch: int
    current_batch_index: int
    train_losses: Deque[Union[float, Dict[str, float]]]
    continue_training: bool

@dataclass
class MultiTrainingContext(Generic[TInput, TTarget, TModel]):
    current_dataset_index: int

class BatchTrainingPlugin(Generic[TInput, TTarget, TModel], ABC):
    pass

class PreMultiLoop(BatchTrainingPlugin[TInput, TTarget, TModel]):
    @abstractmethod
    def pre_multi_loop(self, logger: Logger, context: MultiTrainingContext):
        pass

class PostMultiLoop(BatchTrainingPlugin[TInput, TTarget, TModel]):
    @abstractmethod
    def post_multi_loop(self, logger: Logger, context: MultiTrainingContext):
        pass

class PreMultiTrainStep(BatchTrainingPlugin[TInput, TTarget, TModel]):
    @abstractmethod
    def pre_multi_train_step(self, logger: Logger, context: MultiTrainingContext):
        pass

class PostMultiTrainStep(BatchTrainingPlugin[TInput, TTarget, TModel]):
    @abstractmethod
    def post_multi_train_step(self, logger: Logger, context: MultiTrainingContext):
        pass

class PreLoop(BatchTrainingPlugin[TInput, TTarget, TModel]):
    @abstractmethod
    def pre_loop(self, logger: Logger, trainingContext: TrainingContext[TInput, TTarget, TModel]):
        pass

class PostLoop(BatchTrainingPlugin[TInput, TTarget, TModel]):
    @abstractmethod
    def post_loop(self, logger: Logger, trainingContext: TrainingContext[TInput, TTarget, TModel]):
        pass

class PreEpoch(BatchTrainingPlugin[TInput, TTarget, TModel]):
    @abstractmethod
    def pre_epoch(self, logger: Logger, trainingContext: TrainingContext[TInput, TTarget, TModel]):
        pass

class PostEpoch(BatchTrainingPlugin[TInput, TTarget, TModel]):
    @abstractmethod
    def post_epoch(self, logger: Logger, trainingContext: TrainingContext[TInput, TTarget, TModel]):
        pass

class PreTrain(BatchTrainingPlugin[TInput, TTarget, TModel]):
    @abstractmethod
    def pre_train(self, logger: Logger, trainingContext: TrainingContext[TInput, TTarget, TModel]):
        pass

class PostTrain(BatchTrainingPlugin[TInput, TTarget, TModel]):
    @abstractmethod
    def post_train(self, logger: Logger, trainingContext: TrainingContext[TInput, TTarget, TModel]):
        pass

