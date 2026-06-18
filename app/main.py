from fastapi import FastAPI

from app.schemas.chat import ChatRequest,ChatResponse
from app.graph.builder import build_graph

app = FastAPI(
    title="ASTRA API",
    version="0.1.0"
)

graph = build_graph()

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "astra"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    initial_state = {
        "user_message": request.message,
        "plan": [],
        "route": "",
        "tool_results": [],
        "agent_result": "",
        "final_response": ""
    }

    final_state = graph.invoke(initial_state)

    return {
        "response": final_state["final_response"]
    }