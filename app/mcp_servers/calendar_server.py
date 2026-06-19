from googleapiclient.discovery import build
from mcp.server.fastmcp import FastMCP

from app.google_auth.auth import get_google_credentials


mcp = FastMCP("ASTRA Calendar MCP Server")


@mcp.tool()
def create_calendar_event(
    title: str,
    start_time: str,
    end_time: str,
    description: str = "",
    timezone: str = "Asia/Kolkata",
    attendee_email: str = ""
) -> dict:
    creds = get_google_credentials()

    service = build(
        "calendar",
        "v3",
        credentials=creds
    )

    event = {
        "summary": title,
        "description": description,
        "start": {
            "dateTime": start_time,
            "timeZone": timezone,
        },
        "end": {
            "dateTime": end_time,
            "timeZone": timezone,
        },
    }

    if attendee_email:
        event["attendees"] = [
            {
                "email": attendee_email
            }
        ]

    created_event = service.events().insert(
        calendarId="primary",
        body=event,
        sendUpdates="all"
    ).execute()

    return {
        "status": "event_created",
        "event_id": created_event.get("id"),
        "event_link": created_event.get("htmlLink"),
        "title": title,
        "start_time": start_time,
        "end_time": end_time,
        "attendee_email": attendee_email or "No attendee email"
    }


if __name__ == "__main__":
    mcp.run()