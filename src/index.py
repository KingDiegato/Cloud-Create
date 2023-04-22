# -*- coding: utf-8 -*-
"""
Created on Mar 2, 2023

@author: Diegato
"""


import os
import discord
import dotenv

from core import bot

# =======================================================╗
#########################################################║
from commands.ping                  import *           # ║
from commands.av                    import *           # ║
from commands.banner                import *           # ║
from commands.sepia                 import *           # ║
from commands.whitify               import *           # ║
from commands.blackAndWhite         import *           # ║
from commands.highContrast          import *           # ║
from commands.colorful              import *           # ║
from commands.cartoonify            import *           # ║
from commands.colorBurn             import *           # ║
from commands.layout                import *           # ║
from commands.removeBackground      import *           # ║
from commands.oneSilhouette         import *           # ║
from commands.twoSilhouette         import *           # ║
from commands.emoji                 import *           # ║  
from commands.textOverlay           import *           # ║
from commands.texturized            import *           # ║
from commands.helps                 import *           # ║
#########################################################║
# =======================================================╝

# Import the Cloudinary libraries
# ==============================
import cloudinary

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
new = cloudinary.CloudinaryImage(public_id="bot/")

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print("=" * 40)
    print("Online!")
    print("=" * 40)
    await bot.tree.sync()


@bot.command()
async def init(ctx):
    await bot.tree.sync()
    await ctx.reply("Done!")


@bot.tree.command(name="pineado", description="Llama a una persona por su tag")
async def pineado(interaction: Interaction, nombre: Member):
    await interaction.response.send_message(nombre.mention)


bot.run(TOKEN)
