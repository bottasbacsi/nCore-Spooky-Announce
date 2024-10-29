import asyncio
import websockets
import json
import ssl
from discord_webhook import DiscordWebhook
from datetime import datetime

# Define the WebSocket URL
websocket_url = 'wss://spooky.ncore.pro:3001/spooky'

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Create a function to send announcements
def announce(message):
    current_time = datetime.now().strftime("%H:%M:%S")  # Get the current time
    message_with_time = f'{message} - {current_time}'  # Add the current time to the message
    print("Announcement:", message_with_time)  # You can replace this with any action you want
    webhook = DiscordWebhook(url='', content=message_with_time)
    webhook.execute()

# Define the on_message function to process incoming messages
async def on_message(message):
    data = json.loads(message)
    if data['type'] == 'spooky':
        if data.get('recaptcha'):
            announce('Új captchás tök')
        else:
            announce('Új tök')

# Define the main function to handle WebSocket connection and event loop
async def main():
    retry_interval = 5  # Retry interval in seconds
    while True:
        try:
            async with websockets.connect(websocket_url, ssl=ssl_context) as ws:
                while True:
                    message = await ws.recv()
                    await on_message(message)
        except websockets.exceptions.ConnectionClosedError:
            print("Connection closed. Retrying in {} seconds...".format(retry_interval))
            await asyncio.sleep(retry_interval)

# Start the event loop
asyncio.run(main())
