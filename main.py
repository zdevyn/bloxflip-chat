import requests
import cloudscraper
from discord_webhook import DiscordEmbed, DiscordWebhook
import time

webhook_url = "https://discord.com/api/webhooks/x/x/x"
url = "https://api.bloxflip.com/chat/history"

scraper = cloudscraper.create_scraper()



while True:
    api = scraper.get(url)
    response = api.json()
    message = response['messages']
    userid = messages['bloxFlipUser']['robloxId']
    for messages in message:

        thumburl = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={userid}&size=50x50&format=Png&isCircular=false").json()['data'][0]['imageUrl']
        webhook = DiscordWebhook(url=webhook_url)
        embed = DiscordEmbed(title=messages['bloxFlipUser']['robloxUsername'],description=messages['content'])
        embed.set_thumbnail(thumburl)
        webhook.add_embed(embed)
        webhook.execute()
        time.sleep(1)
