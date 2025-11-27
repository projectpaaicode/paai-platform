from fastapi import APIRouter
from pydantic import BaseModel
from utils.openai_client import ask_openai  # << fixed import

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    business_id: str = "default"

@router.post("/chat")
async def chat_endpoint(data: ChatRequest):
    """
    Simple chat endpoint that forwards the user's message
    to OpenAI and returns the reply.
    """
    reply = ask_openai(
        message=data.message,
        business_id=data.business_id,
    )
    return {"reply": reply}
