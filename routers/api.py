import dspy
from fastapi import APIRouter
from pydantic import BaseModel

from routers.model import Message, Model

router = APIRouter()


class Params(BaseModel):
    messages: list[Message]


@router.post("/")
async def root(params: Params):
    program = Model().activate_assertions()
    pred = program(messages=params.messages)

    dspy.inspect_history(1)

    return {"text": pred.answer}
