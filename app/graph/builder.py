from langgraph.graph import StateGraph, START, END

from app.graph.state import AstraState
from app.graph.nodes import (
    planner_node,
    router_node,
    email_agent_node,
    calendar_agent_node,
    contacts_agent_node,
    general_agent_node,
    response_node,
)

def route_request(state: AstraState):
    return state["route"]


def build_graph():
    graph_builder = StateGraph(AstraState)

    graph_builder.add_node("Planner", planner_node)
    graph_builder.add_node("Router", router_node)
    graph_builder.add_node("EmailAgent", email_agent_node)
    graph_builder.add_node("CalendarAgent", calendar_agent_node)
    graph_builder.add_node("ContactsAgent", contacts_agent_node)
    graph_builder.add_node("GeneralAgent", general_agent_node)
    graph_builder.add_node("Response", response_node)

    graph_builder.add_edge(START, "Planner")
    graph_builder.add_edge("Planner", "Router")

    graph_builder.add_conditional_edges(
        "Router",
        route_request,
        {
            "email": "EmailAgent",
            "calendar": "CalendarAgent",
            "contacts": "ContactsAgent",
            "general": "GeneralAgent",
        }
    )

    graph_builder.add_edge("EmailAgent", "Response")
    graph_builder.add_edge("CalendarAgent", "Response")
    graph_builder.add_edge("ContactsAgent", "Response")
    graph_builder.add_edge("GeneralAgent", "Response")

    graph_builder.add_edge("Response", END)

    graph = graph_builder.compile()

    return graph