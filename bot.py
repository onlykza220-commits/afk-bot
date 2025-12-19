import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online")

@bot.slash_command(description="Bot joins your voice channel and stays AFK")
async def afk(ctx):
    if not ctx.author.voice:
        await ctx.respond("❌ Join a voice channel first", ephemeral=True)
        return

    channel = ctx.author.voice.channel
    await channel.connect(self_deaf=True, self_mute=True)
    await ctx.respond(f"✅ AFK in **{channel.name}**")

bot.run(os.getenv("MTQ1MTUyMTc0MDExODE2MzUzOA.GbzC2-.kfkqfI9E-a9B1kPlXi-ErWLoku2PM-N7vKD-tA"))
