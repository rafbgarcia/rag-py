from typing import Literal

import dspy
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

from utils.dspy_lm import DspyLM
from utils.lance import Lance

model = SentenceTransformer("all-mpnet-base-v2")

dspy.configure(lm=DspyLM.openai_4o_mini())


class Content(BaseModel):
    type: str
    text: str


class Message(BaseModel):
    content: list[Content]
    role: str


class Signature(dspy.Signature):
    """
    - You are a NextJS expert coding assistant.
    - Be concise. Output markdown with. Follow coding best practices.
    - When it makes sense to, split the code into multiple files to make it clearer.
    - Use vector_search to query one concept at a time, e.g. "route handlers", "server actions", "optimistic updates", etc.
    """

    messages: list[Message] = dspy.InputField()
    response: str = dspy.OutputField(desc="Your response to the user")


class Model(dspy.Module):
    def __init__(self):
        super().__init__()

        self.generate_answer = dspy.ReAct(Signature, tools=[self.vector_search])

    def vector_search(
        self,
        query: str,
        version: Literal["15", "14", "13"] = "15",
        router: Literal["pages", "app"] = "app",
    ):
        db = Lance()
        id = f"nextjs_{router}_router"
        results = db.search(query, id, str(version))
        return results

    def forward(self, messages: str):
        pred = self.generate_answer(messages=messages)
        return pred
