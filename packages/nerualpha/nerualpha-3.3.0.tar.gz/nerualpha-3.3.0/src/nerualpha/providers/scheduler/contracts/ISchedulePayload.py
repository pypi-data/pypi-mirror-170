from dataclasses import dataclass, field
from typing import Dict, List, Generic, TypeVar
from abc import ABC, abstractmethod



#interface
class ISchedulePayload(ABC):
    id:str
