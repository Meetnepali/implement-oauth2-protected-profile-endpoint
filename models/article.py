from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class ArticleIn(BaseModel):
    title: str
    body: str
    author: str

class ArticleResult(BaseModel):
    status: str  # 'success' or 'error'
    errors: Optional[List[str]] = None
    details: Optional[Dict[str, Any]] = None

class BulkPublishResult(BaseModel):
    results: List[ArticleResult]