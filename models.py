from typing import Optional
from pydantic import BaseModel

class ItemPlayLoad(BaseModel):
    item_id: optional[int]
    item_name: str
    quantity:int
    

