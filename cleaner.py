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

for canal in res:
    if canal["type"] == 3:
        md_groups.append(canal)


def snowflake_to_timestamp(snowflake_id):
    timestamp = ((int(snowflake_id) >> 22) + 1420070400000) / 1000
    return datetime.fromtimestamp(timestamp)


def clean_groups():
    today = datetime.now()

    for canal in md_groups[:]:
        last_msg = snowflake_to_timestamp(canal["last_message_id"])

        if today - last_msg > timedelta(days_since_last_msg):
            print(f"Saliendo del grupo: {canal['name']}")
            requests.delete(
                f"https://discord.com/api/v10/channels/{canal['id']}", headers=headers
            )


clean_groups()
