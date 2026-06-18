from app.graph.state import AstraState
from app.llm.groq_client import call_llm

def planner_node(state: AstraState):
    return{
        "plan":[
            "Understand user request",
            "Route request to the correct assistant agent",
            "Prepare final response"
        ]
    }

def router_node(state: AstraState):
    prompt = f"""
    You are the routing brain of ASTRA, a personal assistant.

    Classify the user request into exactly one route.

    Allowed routes:
    - email
    - calendar
    - contacts
    - general

    Rules:
    - If the user wants to draft, send, read, or manage email, return email.
    - If the user wants to schedule, create meeting, check availability, or manage calendar, return calendar.
    - If the user wants to find a person, phone number, or email address, return contacts.
    - If none match, return general.

    User request:
    {state["user_message"]}

    Return only one word:
    email, calendar, contacts, or general.
    """

    route = call_llm(prompt).strip().lower()

    if route not in ["email", "calendar", "contacts", "general"]:
        route = "general"

    return {
        "route": route
    }

def email_agent_node(state: AstraState):
    return{
        "agent_result": "Email agent selected. Email workflow will be handled here."
    }

def calendar_agent_node(state: AstraState):
    return {
        "agent_result": "Calendar agent selected. Calendar workflow will be handled here."
    }


def contacts_agent_node(state: AstraState):
    return {
        "agent_result": "Contacts agent selected. Contacts workflow will be handled here."
    }


def general_agent_node(state: AstraState):
    return {
        "agent_result": "General assistant selected. General response will be handled here."
    }


def response_node(state: AstraState):
    return {
        "final_response": f"Route selected: {state['route']}. {state['agent_result']}"
    }