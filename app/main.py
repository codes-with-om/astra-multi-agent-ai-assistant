from fastapi import FastAPI

from app.schemas.chat import ChatRequest,ChatResponse
from app.graph.builder import build_graph

app = FastAPI(
    title="ASTRA API",
    version="0.1.0"
)

graph = build_graph()

PENDING_ACTION = {}

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "astra"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    message = request.message.strip()
    lower_message = message.lower()

    approval_words = ["yes", "y", "approve", "approved", "go ahead", "proceed"]

    if lower_message in approval_words and PENDING_ACTION:
        initial_state = {
            **PENDING_ACTION,
            "approved": True,
        }

        PENDING_ACTION.clear()
        final_state = graph.invoke(initial_state)

        return {
            "response": final_state["final_response"]
        }

    initial_state = {
        "user_message": message,
        "plan": [],
        "route": "",
        "tool_results": [],
        "agent_result": "",
        "final_response": "",
        "approved": False,
        "requires_approval": False,
    }

    final_state = graph.invoke(initial_state)

    if final_state.get("requires_approval"):
        PENDING_ACTION.clear()
        PENDING_ACTION.update(final_state)

    return {
        "response": final_state["final_response"]
    }