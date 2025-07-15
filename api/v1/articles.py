from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import JSONResponse
from typing import List
from models.article import ArticleIn, BulkPublishResult, ArticleResult

router = APIRouter(prefix="/api/v1/articles", tags=["articles"])

def send_publication_email(author: str, article_title: str):
    print(f"Simulated email: Publication notification sent to '{author}' for article '{article_title}'")

@router.post("/bulk_publish", response_model=BulkPublishResult)
def bulk_publish_articles(
    articles: List[ArticleIn],
    background_tasks: BackgroundTasks
):
    results = []
    for idx, article in enumerate(articles):
        errors = []
        # Validation: title required, max 120
        if not article.title or not article.title.strip():
            errors.append("Title is required.")
        elif len(article.title) > 120:
            errors.append("Title exceeds 120 characters.")
        # Validation: body at least 250 chars
        if len(article.body or "") < 250:
            errors.append("Body must be at least 250 characters.")
        # Validation: author non-empty
        if not article.author or not article.author.strip():
            errors.append("Author is required.")
        if errors:
            results.append(ArticleResult(status="error", errors=errors, details=None))
        else:
            # Simulate publish logic (would be DB logic normally)
            background_tasks.add_task(send_publication_email, article.author, article.title)
            results.append(ArticleResult(status="success", errors=None, details={"title": article.title, "author": article.author}))
    return BulkPublishResult(results=results)
