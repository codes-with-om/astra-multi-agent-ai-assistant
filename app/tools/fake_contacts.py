FAKE_CONTACTS = [
    {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "+1-555-0101"
    },
    {
        "name": "Sarah Khan",
        "email": "sarah@example.com",
        "phone": "+91-9876543210"
    }
]


def search_contact(name: str):
    name = name.lower()

    for contact in FAKE_CONTACTS:
        if name in contact["name"].lower():
            return contact

    return None