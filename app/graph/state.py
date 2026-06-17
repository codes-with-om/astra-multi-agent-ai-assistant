from typing import TypedDict

class AstraState(TypedDict):
    user_message: str
    plan: list[str]
    tool_results: list[str]
    final_response: str