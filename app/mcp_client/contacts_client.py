import json

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def search_contact_from_mcp(name: str):
    server_params = StdioServerParameters(
        command="python",
        args=["app/mcp_servers/contacts_server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool(
                "search_contact",
                {
                    "name": name
                }
            )

            raw_text = result.content[0].text
            parsed_result = json.loads(raw_text)

            return parsed_result