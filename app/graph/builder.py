from langgraph.graph import StateGraph, START, END

from app.graph.state import AstraState
from app.graph.nodes import planner_node, response_node


def build_graph():
    graph_builder = StateGraph(AstraState)

    graph_builder.add_node("Planner", planner_node)
    graph_builder.add_node("Response", response_node)

    graph_builder.add_edge(START, "Planner")
    graph_builder.add_edge("Planner", "Response")
    graph_builder.add_edge("Response", END)

    graph = graph_builder.compile()

    return graph