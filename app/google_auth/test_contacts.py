from googleapiclient.discovery import build

from app.google_auth.auth import get_google_credentials


def get_contacts():
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

    print(f"Found {len(contacts)} contacts\n")

    for contact in contacts[:10]:
        names = contact.get("names", [])
        emails = contact.get("emailAddresses", [])
        phones = contact.get("phoneNumbers", [])

        name = (
            names[0]["displayName"]
            if names
            else "No Name"
        )

        email = (
            emails[0]["value"]
            if emails
            else "No Email"
        )

        phone = (
            phones[0]["value"]
            if phones
            else "No Phone"
        )

        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print(f"Email: {email}")
        print("-" * 40)


if __name__ == "__main__":
    get_contacts()