from abc import ABC, abstractmethod
from typing import Dict, Any

class HttpRequesterInterface(ABC):

    @abstractmethod
    def request_from_page(self) -> Dict[str, Any]:
        pass
