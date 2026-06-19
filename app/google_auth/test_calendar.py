from datetime import datetime, timedelta

from googleapiclient.discovery import build

from app.google_auth.auth import get_google_credentials


def create_test_event():
    creds = get_google_credentials()

    service = build(
        "calendar",
        "v3",
        credentials=creds
    )

    start_time = datetime.now() + timedelta(days=1)
    end_time = start_time + timedelta(hours=1)

    event = {
        "summary": "ASTRA Test Meeting",
        "description": "This event was created by ASTRA during Calendar API testing.",
        "start": {
            "dateTime": start_time.isoformat(),
            "timeZone": "Asia/Kolkata",
        },
        "end": {
            "dateTime": end_time.isoformat(),
            "timeZone": "Asia/Kolkata",
        },
    }

    created_event = service.events().insert(
        calendarId="primary",
        body=event
    ).execute()

    print("Event created successfully")
    print("Event ID:", created_event.get("id"))
    print("Event Link:", created_event.get("htmlLink"))


if __name__ == "__main__":
    create_test_event()