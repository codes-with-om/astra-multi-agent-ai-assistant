from app.graph.state import AstraState

def planner_node(state: AstraState):
    return {
        "plan": [
            "Analyze user request",
            "Prepare final response"
        ]
    }

def response_node(state: AstraState):
    return {
        "final_response": f"ASTRA received your request: {state['user_message']}"
    }