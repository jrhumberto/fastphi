import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from model import get_answer_from_llm


class Prompt(BaseModel):
    prompt: str = ''


app = FastAPI(
    title='CommandRLLMAPI'
)


@app.post("/completion/")
async def get_answer(question: Prompt):
    answer = await get_answer_from_llm(question.prompt)
    return answer
