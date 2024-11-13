import os
import logging
from utils.schema import ContentRequest, ContentResponse, ContentRatings,ContentRequestTesting
from utils.prompter import generate_general_response, generate_personalized_response,generate_personalized_response_testing
from utils.responder import responder_JSON

from dotenv import load_dotenv

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
)

load_dotenv()

app = FastAPI()

bearer_auth = HTTPBearer(auto_error=False)

auth_keys = os.environ["AUTH_TOKEN"]

# Authorization header
async def get_authorization_header(
    request: Request,
    bearer: HTTPAuthorizationCredentials = Depends(bearer_auth)
):
    auth_header = request.headers.get("Authorization")
    logging.info(f"Auth header: {auth_header}")
    if auth_header:
        if auth_header.removeprefix("Bearer ") not in auth_keys:
            raise HTTPException(
                status_code=401, detail="Unauthorized"
            )
        else:
            return auth_header
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")

# API endpoint for generating content for emails
@app.post('/generate_personalized_response', status_code=200)
async def generate_content(request: ContentRequest, _auth_header: str = Depends(get_authorization_header)):
    review = request.review
    ratings = request.ratings
    length = request.length
    food_items = request.food_items
    customer_name = request.customer_name
    additional_context=request.additional_context
    previous_replies=request.previous_replies

    system_prompt,prompt = generate_personalized_response(review, ratings, length, food_items, customer_name,additional_context,previous_replies)
    content = responder_JSON(system_prompt,prompt)
    return content

@app.post('/generate_personalized_response_testing', status_code=200)
async def generate_content(request: ContentRequestTesting, _auth_header: str = Depends(get_authorization_header)):
    review = request.review
    ratings = request.ratings
    length = request.length
    food_items = request.food_items
    customer_name = request.customer_name
    additional_context=request.additional_context
    previous_replies=request.previous_replies
    prompt=request.prompt
    system_prompt,prompt = generate_personalized_response_testing(review, ratings, length, food_items, customer_name,additional_context,previous_replies,prompt)
    content = responder_JSON(system_prompt,prompt)
    return content

@app.post('/generate_general_response', status_code=200)
async def generate_content(request: ContentRatings, _auth_header: str = Depends(get_authorization_header)) -> ContentResponse | list[ContentResponse]:
    ratings = request.ratings
    customer_name = request.name
    prompt = " "
    # content = responder_JSON(prompt)
    content = {}
    if ratings > 3:
        content["content"] = f"Hello {customer_name}, thank you for dining with us. We are glad to hear you had a satisfying experience at our restaurant. Your feedback is valuable to us. Would you mind sharing more details on your visit? Please follow this link. Thank you!"
    else:
        content["content"] = f"Dear {customer_name}, we are sorry to hear that you didn't have a great experience at our restaurant. Your feedback is valuable to us. Please take a moment to share more about your visit on the provided link."
    content_generated = {
        "prompt": prompt,
        "content": content
    }

    return content_generated

@app.post('/get_schema', status_code=200)
async def get_schema():
    schema = app.openapi()
    return schema

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', reload=True, port=8023)
