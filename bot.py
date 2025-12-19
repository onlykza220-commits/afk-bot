import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} is online")

@bot.command()
async def afk(ctx):
    if not ctx.author.voice:
        await ctx.send("❌ ادخل روم صوتي أول")
        return

    channel = ctx.author.voice.channel
    await channel.connect(self_deaf=True, self_mute=True)
    await ctx.send(f"✅ AFK في {channel.name}")

bot.run(os.getenv("DISCORD_TOKEN"))

