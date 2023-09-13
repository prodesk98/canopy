from abc import ABC, abstractmethod
from typing import Union, Iterable, Optional, List

from context_engine.llm.models import Function, ModelParams
from context_engine.models.api_models import ChatResponse, StreamingChatChunk
from context_engine.models.data_models import Messages, Query


class BaseLLM(ABC):
    def __init__(self,
                 model_name: str,
                 *,
                 model_params: Optional[ModelParams] = None,
                 ):
        self.model_name = model_name
        # TODO: consider removing altogether
        self.default_model_params = model_params or ModelParams()

    @abstractmethod
    def chat_completion(self,
                        messages: Messages,
                        *,
                        stream: bool = False,
                        max_tokens: Optional[int] = None,
                        model_params: Optional[ModelParams] = None,
                        ) -> Union[ChatResponse, Iterable[StreamingChatChunk]]:
        pass

    @abstractmethod
    def enforced_function_call(self,
                               messages: Messages,
                               function: Function,
                               *,
                               max_tokens: Optional[int] = None,
                               model_params: Optional[ModelParams] = None
                               ) -> dict:
        pass

    @abstractmethod
    async def achat_completion(self,
                               messages: Messages,
                               *,
                               stream: bool = False,
                               max_generated_tokens: Optional[int] = None,
                               model_params: Optional[ModelParams] = None,
                               ) -> Union[ChatResponse,
                                          Iterable[StreamingChatChunk]]:
        pass

    @abstractmethod
    async def agenerate_queries(self,
                                messages: Messages,
                                *,
                                max_generated_tokens: Optional[int] = None,
                                model_params: Optional[ModelParams] = None,
                                ) -> List[Query]:
        pass
