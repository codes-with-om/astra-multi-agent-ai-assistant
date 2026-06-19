from datetime import datetime, timedelta


def convert_to_datetime(date_text: str, time_text: str):
    date_text = date_text.lower().strip()
    time_text = time_text.lower().strip()

    if date_text == "tomorrow":
        target_date = datetime.now() + timedelta(days=1)

        hour = None
        minute = 0

        if "pm" in time_text:
            hour = int(time_text.replace("pm", "").strip())

            if hour != 12:
                hour += 12

        elif "am" in time_text:
            hour = int(time_text.replace("am", "").strip())

            if hour == 12:
                hour = 0

        else:
            hour = int(time_text.strip())

        target_date = target_date.replace(
            hour=hour,
            minute=minute,
            second=0,
            microsecond=0
        )

        return target_date

    return None