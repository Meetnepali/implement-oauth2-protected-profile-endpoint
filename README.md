# Guide to the Project

## Guidance for Task

You are working with a Python FastAPI-based backend for a content management system. Editors have requested a new bulk article publication feature. Your goal is to implement and properly validate a POST HTTP endpoint that supports bulk publishing of articles, reporting per-article results, and simulating asynchronous author notifications via background tasks. All code should be organized using routers and Pydantic models.

## Requirements

- Add a POST endpoint at `/api/v1/articles/bulk_publish` that receives a list of articles, validates them, and attempts to 'publish' all that pass validation.
- Use Pydantic models for input and output structure.
- Report individual success/failure for each article in the JSON response with explanatory messages.
- For each successfully published article, trigger (simulate) a background notification to the article's author.
- No actual authentication, database, or email logic is required; focus on endpoint, structure, validation, and background task simulation.
- Organize logic under routers and proper module structure.

## Verifying Your Solution

- Send a POST request with a list of articles to `/api/v1/articles/bulk_publish` and verify:
    - Each article is individually validated according to business rules (title: present and <=120 chars; body: >=250 chars; author: non-empty).
    - The response lists the status for each article, including validation error messages for those that failed.
    - Background tasks (simulated using print statements) are triggered for any valid articles, one email per article/author.
- Check the response structure matches the specification and that router/module separation is maintained as required.
