import discord
from discord.ext import commands
from settings import DISCORD_TOKEN, SERVER_IP
from server_status import Server
from formatter import format_player_list

bot = commands.Bot(command_prefix="!")
server = Server()

# magic link to join bot to server https://discordapp.com/oauth2/authorize?client_id=<CLIENT_ID>&scope=bot

@bot.event
async def on_ready():
    print("Bot running")

@bot.command()
async def beep(ctx):
    """Checks if the bot is working"""
    await ctx.send("boop")

@bot.command()
async def ping(ctx):
    """Check if the minecraft server is up"""
    ping = server.ping()
    if ping:
        await ctx.send(f"Server responded in {ping}ms")
    else:
        await ctx.send("Server didn't ping back! :(")

@bot.command()
async def players(ctx):
    """Display a list of users currently on the server"""
    status = server.status()
    if status:
        players = status.players
        await ctx.send(format_player_list(players))
    else:
        await ctx.send("Server didn't respond! :(")

@bot.command()
async def ip(ctx):
    """Get the ip to the server"""
    await ctx.send(f"Server ip is: {SERVER_IP}")

bot.run(DISCORD_TOKEN)