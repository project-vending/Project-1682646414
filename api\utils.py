python
from typing import List, Dict
from pydantic import BaseModel
from bson import ObjectId

# Define MongoDB object id validation function
def is_valid_mongo_id(id: str) -> bool:
    return ObjectId.is_valid(id)

# Define Base schema
class UserBase(BaseModel):
    name: str

# Define User schema with id
class User(UserBase):
    id: str

    class Config:
        orm_mode = True

# Define Product schema
class Product(BaseModel):
    id: str
    name: str
    description: str

    class Config:
        orm_mode = True

# Define Rating schema
class Rating(BaseModel):
    user_id: str
    product_id: str
    rating: float

    class Config:
        orm_mode = True

# Define Search query schema
class SearchQuery(BaseModel):
    query: str

# Define Search results schema
class SearchResult(BaseModel):
    id: str
    name: str
    score: float
