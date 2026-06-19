from typing import TypedDict

class AstraState(TypedDict, total=False):
    user_message: str
    plan: list
    route: str
    agent_result: str
    final_response: str
    calendar_event: dict

    pending_action: dict
    requires_approval: bool
    approved: bool