from mcp.server.fastmcp import FastMCP
from googleapiclient.discovery import build

from app.google_auth.auth import get_google_credentials


mcp = FastMCP("ASTRA Contacts MCP Server")


@mcp.tool()
def search_contact(name: str) -> dict:
    creds = get_google_credentials()
    service = build("people", "v1", credentials=creds)

    search_name = name.lower().strip()
    page_token = None
    total_checked = 0

    while True:
        params = {
            "resourceName": "people/me",
            "pageSize": 1000,
            "personFields": "names,emailAddresses,phoneNumbers",
        }

        if page_token:
            params["pageToken"] = page_token

        results = service.people().connections().list(**params).execute()

        contacts = results.get("connections", [])
        total_checked += len(contacts)

        for contact in contacts:
            names = contact.get("names", [])
            if not names:
                continue

            contact_name = names[0].get("displayName", "")

            if search_name in contact_name.lower():
                emails = contact.get("emailAddresses", [])
                phones = contact.get("phoneNumbers", [])

                return {
                    "found": True,
                    "total_checked": total_checked,
                    "contact": {
                        "name": contact_name,
                        "email": emails[0].get("value", "No Email") if emails else "No Email",
                        "phone": phones[0].get("value", "No Phone") if phones else "No Phone",
                    },
                }

        page_token = results.get("nextPageToken")

        if not page_token:
            break

    return {
        "found": False,
        "total_checked": total_checked,
        "contact": None,
    }


if __name__ == "__main__":
    mcp.run()