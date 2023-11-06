from telethon.sync import TelegramClient, events
from discord import Webhook
import discord
import aiohttp
import os

# pip install telethon
# pip install -U py-cord

# telegram api application config
app_name = 'put your app name here'
app_id = app id here
app_hash = 'app hash ehre'

# discord webhook link
webhook_url = 'discord webhook here'

# channel ids/names that are beeing tracked
channelNames = ['me', 'test']

with TelegramClient(app_name, app_id, app_hash) as client:

    # prints information upon start
    def start() -> None:
        me = client.get_me()
        print(f"Logged in as @{me.username}!")
        print(f"Now scanning {channelNames} ...")

    # interate over channels and print id:title
    def cache_chats() -> None:
        print("You are in the following channels [id:title]:")
        for dialog in client.iter_dialogs():
            if dialog.is_channel:
                print(f"{dialog.id}:{dialog.title}")
        print('')

    # perform actions when new message in channels
    @client.on(events.NewMessage(chats=channelNames))
    async def handler(event) -> None:
        embed = await create_embed(event)
        await send_webhook(embed, event)

    # creates discord embed for new message
    async def create_embed(event):
        embed = discord.Embed(
            title="A new telegram message has been tracked!",
            description=f"A new message has been sent to one of your tracked chats:",
            color=discord.colour.Color.nitro_pink()
        )
        username = (await event.get_sender()).username
        embed.add_field(name="Username", value=f"[@{username}](https://t.me/{username})")
        embed.add_field(name="Channel", value=await get_channel(event))
        embed.add_field(name="Timestamp", value=f"<t:{await get_timestamp(event)}:R>")
        if event.text != '':
            embed.add_field(name="Message content", value=event.text)

        return embed

    # gets unix timestamp for message
    async def get_timestamp(event) -> int:
        time = int(event.date.timestamp())
        return time

    # gets channel name for message
    async def get_channel(event) -> str:
        if hasattr(await event.get_chat(), 'title'):
            return (await event.get_chat()).title
        else:
            return (await event.get_chat()).username

    # sends embed to discord webhook
    async def send_webhook(embed, event) -> None:
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(webhook_url, session=session)

            if event.photo:
                path, photo = await get_photo(event)
                await webhook.send(embed=embed)
                await webhook.send(file=photo)
                photo.close()
                os.remove(path)
            else:
                await webhook.send(embed=embed)

    # download photo of message and return path and file
    async def get_photo(event):
        path = await event.download_media()
        file = discord.File(path)
        return path, file

    cache_chats()
    start()
    client.run_until_disconnected()
