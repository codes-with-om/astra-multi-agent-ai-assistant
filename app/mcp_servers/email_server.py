import base64
from email.message import EmailMessage

from googleapiclient.discovery import build
from mcp.server.fastmcp import FastMCP

from app.google_auth.auth import get_google_credentials


mcp = FastMCP("ASTRA Email MCP Server")


@mcp.tool()
def draft_email(
    to_email: str,
    subject: str,
    body: str
) -> dict:
    creds = get_google_credentials()

    service = build(
        "gmail",
        "v1",
        credentials=creds
    )

    message = EmailMessage()
    message.set_content(body)

    message["To"] = to_email
    message["From"] = "me"
    message["Subject"] = subject

    encoded_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    draft_body = {
        "message": {
            "raw": encoded_message
        }
    }

    draft = service.users().drafts().create(
        userId="me",
        body=draft_body
    ).execute()

    return {
        "status": "draft_created",
        "draft_id": draft.get("id"),
        "to_email": to_email,
        "subject": subject,
        "body": body
    }


if __name__ == "__main__":
    mcp.run()