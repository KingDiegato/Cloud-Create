# -*- coding: utf-8 -*-
"""
Created on Mar 2, 2023

@author: Diegato

Recovering the PROJECT

TODO: apply pylint and conventions for python 3.10 ...
TODO: create a .pyi (interface directory) for each class
"""

import os
import importlib
import discord
import dotenv
import cloudinary

from core import bot

for filename in os.listdir("./src/commands"):
    if filename.endswith(".py") and not filename.startswith("__"):
        importlib.import_module(f"commands.{filename[:-3]}")

dotenv.load_dotenv()

CLOUD_NAME = os.getenv("CLOUD_NAME")
CLOUD_API_KEY = os.getenv("CLOUD_API_KEY")
CLOUD_API_SECRET = os.getenv("CLOUD_API_SECRET")
CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")

config = cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=CLOUD_API_KEY,
    api_secret=CLOUD_API_SECRET,
    secure=True,
)

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@bot.event
async def on_ready():
    """
      when system is on ready, execute the next line:
    """
    print("=" * 40)
    print("Online!")
    print("=" * 40)
    await bot.wait_until_ready()
    await bot.tree.sync()
    print("bot tree synced")


@bot.command()
async def init(ctx):
    """
      force tree command to init
    """
    print("forcing syncing")
    await bot.tree.sync()
    await ctx.reply("Done!")


@bot.tree.command(name="pineado", description="Llama a una persona por su tag")
async def pineado(interaction: discord.Interaction, nombre: discord.Member):
    """
      pin the user mentioned
    """
    await interaction.response.send_message(nombre.mention)

if __name__ == "__main__":
    bot.run(TOKEN)
