import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client
from pyromod import listen


API_ID = int(os.environ.get("API_ID", "28776072"))
API_HASH = os.environ.get("API_HASH", "b3a786dce1f4e7d56674b7cadfde3c9d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7515672383:AAFatvmKT6ySYbK12-9rbl2FqnrJ0n2Bvsg")
API_KEY = os.environ.get("API_KEY", None)


def main():
    app = Client(name="String Session",
                 bot_token = BOT_TOKEN,
                 api_id = API_ID,
                 api_hash = API_HASH,
                 plugins = dict(root="plugins"),
                 workers = 100,
                 sleep_threshold = 15)

    app.run()


if __name__ == "__main__":
    main()
