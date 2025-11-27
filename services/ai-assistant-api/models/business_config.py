from pydantic import BaseModel
from typing import List, Optional, Dict

class ServiceItem(BaseModel):
    name: str
    description: Optional[str] = None
    price: Optional[str] = None
    duration: Optional[str] = None  # e.g. "60 minutes"

class BusinessConfig(BaseModel):
    business_id: str
    name: str
    industry: str
    hours: Dict[str, str] = {}
    services: List[ServiceItem] = []
