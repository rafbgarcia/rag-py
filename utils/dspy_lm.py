import os

import dspy
from dotenv import load_dotenv

load_dotenv(".env.local", override=True)


class DspyLM:
    @staticmethod
    def openai_o1_mini():
        api_key = os.environ.get("OPENAI_API_KEY")
        return dspy.LM(
            model="openai/o1-mini",
            api_key=api_key,
            max_tokens=30000,
            temperature=1.0,
        )

    @staticmethod
    def openai_4o_mini():
        api_key = os.environ.get("OPENAI_API_KEY")
        return dspy.LM(
            model="openai/gpt-4o-mini",
            max_tokens=15_000,
            api_key=api_key,
            model_type="chat",
        )

    @staticmethod
    def claude():
        api_key = os.environ.get("CLAUDE_API_KEY")
        return dspy.LM(
            model="anthropic/claude-3-5-sonnet-20241022",
            api_key=api_key,
            max_tokens=8000,
        )
