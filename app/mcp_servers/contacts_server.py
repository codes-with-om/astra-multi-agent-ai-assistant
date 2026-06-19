from mcp.server.fastmcp import FastMCP


mcp = FastMCP("ASTRA Contacts MCP Server")


CONTACTS = [
    {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "+1-555-0101"
    },
    {
        "name": "Sarah Khan",
        "email": "sarah@example.com",
        "phone": "+91-9876543210"
    }
]


@mcp.tool()
def search_contact(name: str) -> dict:
    search_name = name.lower()

    for contact in CONTACTS:
        if search_name in contact["name"].lower():
            return {
                "found": True,
                "contact": contact
            }

    return {
        "found": False,
        "contact": None
    }


if __name__ == "__main__":
    mcp.run()