from ty_extensions import Unknown
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

days_since_last_msg: int = 3

md_groups: list[Unknown] = []

token: str | None = os.getenv("DISCORD_TOKEN")

headers: dict[str, str | None] = {"Authorization": token}

response: Unknown = requests.get(
    "https://discord.com/api/v10/users/@me/channels", headers=headers
)

res: Unknown = response.json()

for channel in res:
    if channel["type"] == 3:
        md_groups.append(channel)


def snowflake_to_timestamp(snowflake_id):
    timestamp: int | float = ((int(snowflake_id) >> 22) + 1420070400000) / 1000
    return datetime.fromtimestamp(timestamp)


def clean_groups():
    today: datetime = datetime.now()
    count = 0

    for channel in md_groups[:]:
        last_msg: Unknown = snowflake_to_timestamp(channel["last_message_id"])

        if today - last_msg > timedelta(days=1):
            print(f"Deleting group: {channel['name']}")
            requests.delete(
                f"https://discord.com/api/v10/channels/{channel['id']}", headers=headers
            )
            count += 1

    if count == 0:
        print("No groups to delete matching the given requirements.")
    else:
        print(f"Has salido de {count} grupos")


clean_groups()
