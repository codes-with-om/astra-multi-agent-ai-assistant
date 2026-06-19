import json

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def draft_email_from_mcp(to_name: str, subject: str, body: str):
    server_params = StdioServerParameters(
        command="python",
        args=["app/mcp_servers/email_server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool(
                "draft_email",
                {
                    "to_name": to_name,
                    "subject": subject,
                    "body": body
                }
            )

            raw_text = result.content[0].text
            return json.loads(raw_text)