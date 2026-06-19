from datetime import datetime, timedelta


def convert_to_datetime(date_text: str, time_text: str):

    if date_text.lower() == "tomorrow":

        target_date = datetime.now() + timedelta(days=1)

        hour = 17

        if "pm" in time_text.lower():
            hour = int(time_text.lower().replace("pm", "").strip())

            if hour != 12:
                hour += 12

        elif "am" in time_text.lower():
            hour = int(time_text.lower().replace("am", "").strip())

        target_date = target_date.replace(
            hour=hour,
            minute=0,
            second=0,
            microsecond=0
        )

        return target_date

    return None