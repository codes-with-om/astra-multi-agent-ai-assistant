import json

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def create_calendar_event_from_mcp(
    title: str,
    start_time: str,
    end_time: str,
    description: str = "",
    timezone: str = "Asia/Kolkata"
):
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "app.mcp_servers.calendar_server"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool(
                "create_calendar_event",
                {
                    "title": title,
                    "start_time": start_time,
                    "end_time": end_time,
                    "description": description,
                    "timezone": timezone,
                }
            )

            raw_text = result.content[0].text
            return json.loads(raw_text)