import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import json


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["app/mcp_servers/contacts_server.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()

            result = await session.call_tool(
                "search_contact",
                {
                    "name": "John"
                }
            )

            print("Tool result:")
            raw_text = result.content[0].text
            parsed_result = json.loads(raw_text)

            print("Parsed result:")
            print(parsed_result)

            print("Available tools:")
            for tool in tools.tools:
                print("-", tool.name)


if __name__ == "__main__":
    asyncio.run(main())