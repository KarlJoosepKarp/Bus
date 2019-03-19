"""Bus bot"""
from discord.ext.commands import Bot
import discord
from discord.ext import commands
from transport import Location

bus_stations = {
    "keemia": [59.3969, 24.6664],
    "baltijaam": [59.4398, 24.7378],
    "vambola": [59.3997, 24.6901],
    "akadeemiatee": [59.4013, 24.6599],
    "lepistiku": [59.4031, 24.6988],
    "bussijaam": [59.4268, 24.7709]}

Client = discord.Client()
bot = commands.Bot(command_prefix="!")


@bot.event
async def bot_ready():
    """Check"""
    print("Bot is ready for action")


@bot.event
async def on_message(message):
    """Message in and message out to discord"""
    # [keemia,lepistiku]
    message_list = str(message.content).split(",")
    print(message_list)
    if message_list[0] in bus_stations.keys() and message_list[1] in bus_stations.keys():
        print("okei")
        loc1 = Location()
        await bot.send_message(message.channel, loc1.next_departures(message_list[0], message_list[1]))


bot.run("NTU2MTA2MTgxNzMxNDE4MTEz.D250zw.lRRtfAv5uI4pLi5TzkYzF-ZV27Q")
