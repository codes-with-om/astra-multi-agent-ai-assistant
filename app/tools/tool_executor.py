from app.tools.fake_contacts import search_contact


def execute_tool(tool_name: str, tool_input: dict):
    if tool_name == "search_contact":
        return search_contact(tool_input["name"])

    raise ValueError(f"Unknown tool: {tool_name}")