"""check ping in ms"""
import time
import datetime

from discord import Interaction, Embed, Color

from core import bot

color_cases = [
    {"latency": 250, "color": Color.blue()},
    {"latency": 450, "color": Color.green()},
    {"latency": 600, "color": Color.orange()},
    {"latency": 800, "color": Color.red()},
    {"latency": 9999, "color": Color.dark_red()}
]


@bot.tree.command(name='ping', description='Check Latency with the Bot')
async def ping(interaction: Interaction):
    """calculate latency and return time in ms of the response of websocket"""
    start_time = time.time()
    await interaction.response.defer()
    latency = round(bot.latency * 1000)
    measured_time = time.time() - start_time
    end = round(measured_time * 100)

    filtered = [elem for elem in color_cases if elem["latency"] >= latency]
    color = filtered[0]["color"]

    embed = Embed(
      title=":ping_pong: Pong!",
      color=color,
      timestamp=datetime.datetime.now(datetime.timezone.utc)
      )
    embed.add_field(name="Websocket", value=f"```json\n{latency} ms```", inline=False)
    embed.add_field(name="Typing", value=f"```json\n{end} ms```", inline=False)

    await interaction.followup.send(embed=embed)
