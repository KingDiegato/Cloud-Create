import time
import asyncio
import discord
import datetime

from core import bot

from discord import Interaction

@bot.tree.command(name='ping', description='Check Latency with the Bot')
async def ping(interaction: Interaction):
    latency = round(bot.latency * 1000)
    start_time = time.time()
    await asyncio.sleep(0.1)
    measured_time = time.time() - start_time
    end = round(measured_time * 1000)
    if latency < 250:
        color = discord.Color.blue()
    elif latency < 450:
        color = discord.Color.green()
    elif latency < 600:
        color = discord.Color.orange()
    elif latency < 800:
        color = discord.Color.red()
    else:
        color = discord.Color.dark_red()

    embed = discord.Embed(title=f":ping_pong: Pong!",
                          color=color, timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Websocket",
                    value=f"```json\n{latency} ms```", inline=False)
    embed.add_field(
        name="Typing", value=f"```json\n{end} ms```", inline=False)
    await interaction.response.send_message(embed=embed)