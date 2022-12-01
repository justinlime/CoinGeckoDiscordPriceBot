import discord
import requests
import json
import os
from discord.ext import commands, tasks

with open('info.json', 'r') as u:
    info = json.load(u)
    api = info['api']
    id = info['id']
    length = info['length']
    updatefreq = info['updatefreq']
    print('info loaded')

intents = discord.Intents.default()
bot = commands.Bot(intents=intents)
url = f"https://api.coingecko.com/api/v3/coins/{id}"

@bot.event
async def on_ready():
    change_status.start()
    print("BOT RUNNING")

@tasks.loop(seconds=updatefreq)
async def change_status():
    data = requests.get(url).json()
    price = str(data['market_data']['current_price']['usd'])[0:length]
    change = str(data['market_data']['price_change_percentage_24h'])
    if change[0] != '-':
        change = f'+{change}'
    change = change[0:6]
    for guild in bot.guilds:
        await guild.me.edit(nick=price)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, 
    name=f"24h: {change}%"))
    print(f"updated {id} with price {price} and 24h percentage change {change}")
    
bot.run(api)
