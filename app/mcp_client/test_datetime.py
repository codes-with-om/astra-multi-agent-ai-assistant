from app.utils.datetime_parser import convert_to_datetime

result = convert_to_datetime(
    "tomorrow",
    "5 PM"
)

print(result)