import asyncio
import websockets
import json
import ssl
import random
import os
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
from rich import print

websocket_url = 'wss://spooky.ncore.pro:3001/spooky'

WEBHOOK_URL = ''

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


def announce(message):
    current_time = datetime.now().strftime("%H:%M:%S")  
    message_with_time = f'{message} - {current_time}'  
    
    print(f"[bright_green]Tök Announce küldve:[/bright_green] [orange3]{message_with_time}[/orange3]")

    try:
        webhook = DiscordWebhook(url=WEBHOOK_URL, content=message_with_time)

        random_image_num = random.randint(1, 45)
        image_url = f"https://nc-img.cdn.l7cache.com/spooky2k25/sp2025-{random_image_num}.png"
        embed = DiscordEmbed()
        embed.set_image(url=image_url)
        webhook.add_embed(embed)
        
        response = webhook.execute()
        
        if response.status_code not in [200, 204]:
            print(f"[bright_red]Hiba a Discord webhook küldése közben: {response.status_code} {response.content}[/bright_red]")

    except Exception as e:
        print(f"[bright_red]Hiba történt az announce függvényben: {e}[/bright_red]")


async def on_message(message):
    data = json.loads(message)
    if data['type'] == 'spooky':
        if data.get('recaptcha'):
            announce('Új captchás tök')
        else:
            announce('Új tök')

async def main():
    retry_interval = 5  
    
    while True:
        try:
            print(f"[bright_yellow]Socketre várakozunk... (Cél: {websocket_url})[/bright_yellow]")
            async with websockets.connect(websocket_url, ssl=ssl_context) as ws:
                print(f"[turquoise2]Sikeresen csatlakozva! Várakozás a tökökre...[/turquoise2]")
                
                while True:
                    try:
                        message = await ws.recv()
                        await on_message(message)
                    
                    except Exception as e_inner:
                        print(f"[bright_red]Hiba az üzenet feldolgozása közben: {e_inner}. A kapcsolat él tovább.[/bright_red]")
        
        except websockets.exceptions.ConnectionClosedError:
            print(f"[bright_red]A kapcsolat lezárult. Újracsatlakozás {retry_interval} másodperc múlva...[/bright_red]")
            await asyncio.sleep(retry_interval)
        
        except Exception as e_outer:
            print(f"[bright_red]Általános hiba: {e_outer}. Újracsatlakozás {retry_interval} másodperc múlva...[/bright_red]")
            await asyncio.sleep(retry_interval)


if __name__ == "__main__":
    if WEBHOOK_URL == 'YOUR_WEBHOOK_URL_HERE' or not WEBHOOK_URL:
        print(f"[bright_red]HIBA: Nincs beállítva a Discord Webhook URL![/bright_red]")
        print(f"[bright_yellow]Kérlek, írd be a WEBHOOK_URL változóba a script tetején a futtatás előtt.[/bright_yellow]")
    else:
        asyncio.run(main())
