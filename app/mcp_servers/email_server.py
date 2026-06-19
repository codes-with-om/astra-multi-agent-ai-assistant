from mcp.server.fastmcp import FastMCP


mcp = FastMCP("ASTRA Email MCP Server")


@mcp.tool()
def draft_email(to_name: str, subject: str, body: str) -> dict:
    """
    Create an email draft.
    """
    return {
        "status": "draft_created",
        "to_name": to_name,
        "subject": subject,
        "body": body
    }


if __name__ == "__main__":
    mcp.run()