import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

days_since_last_msg = 3

md_groups = []

token = os.getenv("DISCORD_TOKEN")

headers = {"Authorization": token}

response = requests.get(
    "https://discord.com/api/v10/users/@me/channels", headers=headers
)

res = response.json()

for channel in res:
    if channel["type"] == 3:
        md_groups.append(channel)


def snowflake_to_timestamp(snowflake_id):
    timestamp = ((int(snowflake_id) >> 22) + 1420070400000) / 1000
    return datetime.fromtimestamp(timestamp)


def clean_groups():
    today = datetime.now()
    count = 0

    for channel in md_groups[:]:
        last_msg = snowflake_to_timestamp(channel["last_message_id"])

        if today - last_msg > timedelta(days=1):
            print(f"Deleting group: {channel['name']}")
            requests.delete(
                f"https://discord.com/api/v10/channels/{channel['id']}", headers=headers
            )
            count += 1

    print(f"You've deleted {count} groups.")


clean_groups()
