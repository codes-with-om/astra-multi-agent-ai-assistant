from mcp.server.fastmcp import FastMCP
from googleapiclient.discovery import build

from app.google_auth.auth import get_google_credentials


mcp = FastMCP("ASTRA Contacts MCP Server")

@mcp.tool()
def search_contact(name: str) -> dict:
    creds = get_google_credentials()

    service = build(
        "people",
        "v1",
        credentials=creds
    )

    results = service.people().connections().list(
        resourceName="people/me",
        personFields="names,emailAddresses,phoneNumbers"
    ).execute()

    contacts = results.get("connections", [])

    search_name = name.lower()

    for contact in contacts:

        names = contact.get("names", [])

        if not names:
            continue

        contact_name = names[0]["displayName"]

        if search_name in contact_name.lower():

            emails = contact.get("emailAddresses", [])
            phones = contact.get("phoneNumbers", [])

            return {
                "found": True,
                "contact": {
                    "name": contact_name,
                    "email": (
                        emails[0]["value"]
                        if emails
                        else "No Email"
                    ),
                    "phone": (
                        phones[0]["value"]
                        if phones
                        else "No Phone"
                    )
                }
            }

    return {
        "found": False,
        "contact": None
    }

if __name__ == "__main__":
    mcp.run()