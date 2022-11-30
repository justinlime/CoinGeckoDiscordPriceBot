import discord
import requests
import json
import os
from discord.ext import commands, tasks

intents = discord.Intents.default()
bot = commands.Bot(intents=intents)
url = "https://api.coingecko.com/api/v3/simple/price"

with open('info.json', 'r') as u:
    info = json.load(u)
    api = info['api']
    coin = info['coin']
    id = info['id']
    length = info['length']
    updatefreq = info['updatefreq']
    print('info loaded')

params = {
    'ids' : id,
    'vs_currencies' : "usd"
}

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{coin} Price"))
    change_status.start()
    print("BOT RUNNING")

@tasks.loop(seconds=updatefreq)
async def change_status():
    price = str(requests.get(url,params=params).json()[id]['usd'])[0:length]
    print(price)
    for guild in bot.guilds:
        await guild.me.edit(nick=price)
    print(f"updated {coin}")

bot.run(api)
