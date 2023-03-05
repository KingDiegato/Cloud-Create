import asyncio
import os
import discord
import dotenv

import datetime
import time

# Local Imports
# ==========================================================================================================================
from classes import AvView, BlackAndWhite, EmojiSizing, SepiaEffect, HighContrast, WhiteColor
from classes import ColorFul, BgRemoval, Silhouette, TextOverlay, LayoutFor, Cartoonify, ColorBurn, TwoSilhouette
from embeds.helper import Command_Embeded
from modules.module import Link, Pagination
# ==========================================================================================================================
# End Local Imports

# Import Discord Specifications
# ================================
from discord.ext import commands

from discord import Interaction

from discord import Member

from discord import *

from discord.app_commands import Choice

# Import the Cloudinary libraries
# ==============================
import cloudinary
from cloudinary.uploader import upload

dotenv.load_dotenv()

CLOUD_NAME = os.getenv('CLOUD_NAME')
CLOUD_API_KEY = os.getenv('CLOUD_API_KEY')
CLOUD_API_SECRET = os.getenv('CLOUD_API_SECRET')
CLOUDINARY_URL = os.getenv('CLOUDINARY_URL')

config = cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=CLOUD_API_KEY,
    api_secret=CLOUD_API_SECRET,
    secure=True
)
new = cloudinary.CloudinaryImage(
    public_id='bot/'
)

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='$', intents=intents)  # Prefijo del bot


@bot.event
async def on_ready():
    print('='*40)
    print('Online!')
    print('='*40)
    await bot.tree.sync()
    await bot.change_presence(activity=discord.Game('Crear Imagenes muy Geniales'))


#! init update command
@bot.command()
async def init(ctx):
    await bot.tree.sync()
    await ctx.reply('Done!')


@bot.tree.command(name='pineado', description='Llama a una persona por su tag')
async def pineado(interaccion: Interaction, nombre: Member):
    await interaccion.response.send_message(nombre.mention)


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

av_remove_bg_option = discord.SelectOption(label='Remove Background', value='background_removal',
                                           description="remove the background of your pfp, note: doesn't work with no background images.")
av_silhouete_option = discord.SelectOption(label='Color Silhouette', value='color_silhouette',
                                           description='Create a cool and Joyful Color Effect to your pfp')
av_whitify_option = discord.SelectOption(label='Whitify', value='whitify',
                                         description='Clarify your pfp with this Effect')


#! Avatar recover interaction [/av]
@bot.tree.command(name='av', description='Obtener el Avatar')
async def av(interaction: Interaction, member: Member):
    '''
    Command Avatar View
    '''
    try:
        av_view = AvView(member.name)
        show_avatar = discord.Embed(
            title=f'Avatar de {member.name}',
            description='🌟☁ Lets Transform it ☁🌟',
            color=discord.Color.random(),
        )
        show_avatar.set_image(url=member.avatar)
        upload(f"{member.avatar}", public_id=f'Bot/{member.name}q:av_up')
        await interaction.response.send_message(embed=show_avatar, view=av_view)
    except:
        await interaction.response.send_message("Command Not Found, please Try Again in a few seconds, type /help_404 to see more info")


#! Banner
@bot.tree.command(name='banner', description='Obtener el Banner')
async def av(interaction: Interaction, member: Member):
    '''
    Recover Banner
    '''
    try:
        av_view = AvView(member.name)
        show_banner = discord.Embed(
            title=f'Avatar de {member.name}',
            description='🌟☁ Lets Transform it ☁🌟',
            color=discord.Color.random(),
        )
        show_banner.set_image(url=member.banner)
        upload(f"{member.banner}", public_id=f'Bot/{member.name}q:banner_up')
        await interaction.response.send_message(embed=show_banner, view=av_view,)
    except FileNotFoundError:
        await interaction.response.send_message('Your Banner is not available for edits')
    except:
        await interaction.response.send_message("Command Not Found, please Try Again in a few seconds, type /help_404 to see more info")


#! Sepia
@bot.tree.command(name='sepia_effect', description='Upload an image for Edit content')
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image")
async def sepia_effect(interaction: Interaction, drag: discord.message.Attachment, description: str | None):
    '''
    Sepia Effect

    Transform the Image with a Sepia filter when you call the interaction.
    '''
    try:
        file_name = drag.filename
        view = Link() and SepiaEffect(file_name)
        embed = discord.Embed(
            title=f'Picture fetched by: {interaction.user}',
            description=description or 'Prepare for edit the next Image:',
            color=discord.Color.random(),
        )
        embed.set_image(url='{}'.format(drag))
        embed.set_thumbnail(url=interaction.user.avatar)
        upload(drag.url, public_id=f'Bot/{file_name}')

        view.add_item(discord.ui.Button(label='See on the Browser',
                                        style=discord.ButtonStyle.url, url='{}'.format(drag)))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    except:
        await interaction.response.send_message("Command Not Found, please Try Again in a few seconds, type /help_404 to see more info")

# End of Sepia Effect Command

'''
B&W Effect

Transform the Image with a Black & White filter when you call the interaction.
'''


#! Black and White
@bot.tree.command(name='black_and_white', description='Upload an image and transform to Black and White')
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image")
async def black_and_white(interaction: Interaction, drag: discord.message.Attachment, description: str | None):
    '''
    Convert Your image to an Black And White effect with GrayScale

    @params interaction: Interaction, drag: discord.message.Attachment, description: sty | None
    '''
    try:
        file_name = drag.filename
        view = Link() and BlackAndWhite(file_name)
        embed = discord.Embed(
            title=f'Picture fetched by: {interaction.user}',
            description=description or 'Prepare for edit the next Image:',
            color=discord.Color.random(),
        )
        embed.set_image(url='{}'.format(drag))
        embed.set_thumbnail(url=interaction.user.avatar)
        upload(drag.url, public_id=f'Bot/{file_name}')

        view.add_item(discord.ui.Button(label='See on the Browser',
                                        style=discord.ButtonStyle.url, url='{}'.format(drag)))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    except:
        await interaction.response.send_message("Command Not Found, please Try Again in a few seconds, type /help_404 to see more info")

# End of B&W Effect Command

'''
High Contrast Effect 

Transform the Image and intensify the contrast but equals the saturation.
'''


#! High Contrast
@bot.tree.command(name='high_contrast', description='Upload an image to highly contrast it without saturation problem')
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image")
async def high_contrast(interaction: Interaction, drag: discord.message.Attachment, description: str | None):
    try:
        file_name = drag.filename
        view = Link() and HighContrast(file_name)
        embed = discord.Embed(
            title=f'Picture fetched by: {interaction.user}',
            description=description or 'Prepare for edit the next Image:',
            color=discord.Color.random(),
        )
        embed.set_image(url='{}'.format(drag))
        embed.set_thumbnail(url=interaction.user.avatar)
        upload(drag.url, public_id=f'Bot/{file_name}')

        view.add_item(discord.ui.Button(label='See on the Browser',
                                        style=discord.ButtonStyle.url, url='{}'.format(drag)))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    except:
        await interaction.response.send_message("Command Not Found, please Try Again in a few seconds, type /help_404 to see more info")

# End of HighContrast Effect Command

'''
Whitify Effect 

Transform the Image with a Black & White filter when you call the interaction.
'''


#! Whitify
@bot.tree.command(name='whitify', description='Upload an image and Scale this to become More Clear')
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image")
async def whitify(interaction: Interaction, drag: discord.message.Attachment, description: str | None):
    try:
        file_name = drag.filename
        view = Link() and WhiteColor(file_name)
        embed = discord.Embed(
            title=f'Picture fetched by: {interaction.user}',
            description=description or 'Prepare for edit the next Image:',
            color=discord.Color.random(),
        )
        embed.set_image(url='{}'.format(drag))
        embed.set_thumbnail(url=interaction.user.avatar)
        upload(drag.url, public_id=f'Bot/{file_name}')

        view.add_item(discord.ui.Button(label='See on the Browser',
                                        style=discord.ButtonStyle.url, url='{}'.format(drag)))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    except:
        await interaction.response.send_message("Command Not Found, please Try Again in a few seconds, type /help_404 to see more info")

# End of Whitify Effect Command

'''
ColorFul Effect 

Transform the Image with a Black & White filter when you call the interaction.
'''


#! Colorful
@bot.tree.command(name='colorful', description='Upload an image and create a colorful effect over your file')
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image")
async def colorful(interaction: Interaction, drag: discord.message.Attachment, description: str | None):
    try:
        file_name = drag.filename
        view = Link() and ColorFul(file_name)
        embed = discord.Embed(
            title=f'Picture fetched by: {interaction.user}',
            description=description or 'Prepare for edit the next Image:',
            color=discord.Color.random(),
        )
        embed.set_image(url='{}'.format(drag))
        embed.set_thumbnail(url=interaction.user.avatar)
        upload(drag.url, public_id=f'Bot/{file_name}')

        view.add_item(discord.ui.Button(label='See on the Browser',
                                        style=discord.ButtonStyle.url, url='{}'.format(drag)))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    except:
        await interaction.response.send_message("Command Not Found, please Try Again in a few seconds, type /help_404 to see more info")

# End of Colorful Effect Command


#! Cartoonify
@bot.tree.command(name='cartoonify', description='Upload an image and create a Cartonify effect in a photo')
@app_commands.describe(drag="drag 'n' drop a file or upload from directory", description="a description for the image")
async def cartoonify(interaction: Interaction, drag: discord.message.Attachment, description: str | None):
    try:
        file_name = drag.filename
        view = Link() and Cartoonify(file_name)
        embed = discord.Embed(
            title=f'Picture fetched by: {interaction.user}',
            description=description or 'Prepare for edit the next Image:',
            color=discord.Color.random(),
        )
        embed.set_image(url='{}'.format(drag))
        embed.set_thumbnail(url=interaction.user.avatar)
        upload(drag.url, public_id=f'Bot/{file_name}')

        view.add_item(discord.ui.Button(label='See on the Browser',
                                        style=discord.ButtonStyle.url, url='{}'.format(drag)))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    except:
        await interaction.response.send_message("Command Not Found, please Try Again in a few seconds, type /help_404 to see more info")


#! ColorBurn
@bot.tree.command(name='color_burn', description='Upload an image and create a Cartonify effect in a photo')
@app_commands.describe(drag="drag 'n' drop a file or upload from directory", description="a description for the image")
async def color_burn(interaction: Interaction, drag: discord.message.Attachment, description: str | None):
    try:
        file_name = drag.filename
        view = Link() and ColorBurn(file_name)
        embed = discord.Embed(
            title=f'Picture fetched by: {interaction.user}',
            description=description or 'Prepare for edit the next Image:',
            color=discord.Color.random(),
        )
        embed.set_image(url='{}'.format(drag))
        embed.set_thumbnail(url=interaction.user.avatar)
        upload(drag.url, public_id=f'Bot/{file_name}')

        view.add_item(discord.ui.Button(label='See on the Browser',
                                        style=discord.ButtonStyle.url, url='{}'.format(drag)))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    except:
        await interaction.response.send_message("Command Not Found, please Try Again in a few seconds, type /help_404 to see more info")


#! Layout
@bot.tree.command(name='layout_for', description='Upload an image and create a Layout effect over your file')
@app_commands.describe(pfp_drag="drag'n' drop Your desire profile picture", banner_drag="drag'n' drop Your desire banner image", description="a small description of your uploads")
async def layout_for(interaction: Interaction, pfp_drag: discord.message.Attachment, banner_drag: discord.message.Attachment, description: str | None):

    user_name = interaction.user.name
    view = LayoutFor(user_name, pfp_drag.url, banner_drag.url)
    embed = discord.Embed(
        title=f'Picture fetched by: {interaction.user}',
        description=f'Prepare for create the layout for a social media and {description}',
        color=discord.Color.random(),
    )
    embed.set_image(url='{}'.format(banner_drag))
    embed.set_thumbnail(url=pfp_drag.url)
    upload(pfp_drag.url, public_id=f'UsersLayout/{user_name}_av')
    upload(banner_drag.url, public_id=f'UsersLayout/{user_name}_banner')
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


'''
Background Removal Effect! 🧨✨🎉

Transform the Image with a Black & White filter when you call the interaction.

This is an unnestable service cause The image is pretty slow to load and the interaction with discord timeout the function
when 3.5 segs passes and the image usually load in 20-30 seconds
'''


#! Remove Background
@bot.tree.command(name='background_remove', description='Upload an image and Remove the Background')
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image")
async def background_remove(interaction: Interaction, drag: discord.message.Attachment, description: str | None):
    try:
        file_name = drag.filename
        view = Link() and BgRemoval(file_name)
        embed = discord.Embed(
            title=f'Picture fetched by: {interaction.user}',
            description=description or 'Prepare for remove the background to the next Image:',
            color=discord.Color.random(),
        )
        embed.set_image(url='{}'.format(drag))
        embed.set_thumbnail(url=interaction.user.avatar)
        upload(drag.url, public_id=f'Bot/{file_name}')

        view.add_item(discord.ui.Button(label='See on the Browser',
                                        style=discord.ButtonStyle.url, url='{}'.format(drag)))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    except:
        await interaction.response.send_message("Command Not Found, please Try Again in a few seconds, type /help_404 to see more info")

# End of Bg Removal Effect Command

'''
Silhouette Color Effect! 🧨✨🎉

Transform the Image with a Black & White filter when you call the interaction.
'''
ColorChoices = app_commands.choices(choice_color=[
    Choice(name='Red', value='#CF2C2C'),
    Choice(name='Yellow', value='#9C9342'),
    Choice(name='Lime', value='#5EA031'),
    Choice(name='Green', value='#0B7E29'),
    Choice(name='Cyanade', value='#1AB4AA'),
    Choice(name='Purple', value='#7038A1'),
    Choice(name='Pink', value='#D867B4'),
    Choice(name='Wine', value='#862044'),
    Choice(name='Blue', value='#09f'),
    Choice(name='Black', value='#121212')
])
ColorChoices_2 = app_commands.choices(choice_color_two=[
    Choice(name='Red', value='#CF2C2C'),
    Choice(name='Yellow', value='#9C9342'),
    Choice(name='Lime', value='#5EA031'),
    Choice(name='Green', value='#0B7E29'),
    Choice(name='Cyanade', value='#1AB4AA'),
    Choice(name='Purple', value='#7038A1'),
    Choice(name='Pink', value='#D867B4'),
    Choice(name='Wine', value='#862044'),
    Choice(name='Blue', value='#09f'),
    Choice(name='Black', value='#121212')
])


#! Color Silhouette
@bot.tree.command(name='color_silhouette', description='Upload an image to apply a cool Colorized Effect')
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image", choice_color='a color for the effect, Is Required')
@ColorChoices
async def color_silhouette(interaction: Interaction, drag: discord.message.Attachment, choice_color: Choice[str], description: str | None):
    file_name = drag.filename
    view = Link() and Silhouette(file_name, choice_color.value)
    embed = discord.Embed(
        title=f'Picture fetched by: {interaction.user}',
        description=description or 'Prepare for edit the next Image:',
        color=discord.Color.random(),
    )
    print(drag.content_type)
    print(drag.size)
    print(drag.width)
    embed.set_image(url='{}'.format(drag))
    embed.set_thumbnail(url=interaction.user.avatar)
    upload(drag.url, public_id=f'Bot/{file_name}')

    view.add_item(discord.ui.Button(label='See on the Browser',
                                    style=discord.ButtonStyle.url, url='{}'.format(drag)))
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


#! Two Color Silhouette
@bot.tree.command(name='two_color_silhouette', description='Upload an image to apply a cool Colorized Effect')
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image", choice_color='a color for the effect, Is Required')
@ColorChoices
@ColorChoices_2
async def two_color_silhouette(interaction: Interaction, drag: discord.message.Attachment, choice_color: Choice[str], choice_color_two: Choice[str], description: str | None):
    file_name = drag.filename
    view = Link() and TwoSilhouette(file_name, choice_color.value,
                                    choice_color_two.value, drag.width)
    embed = discord.Embed(
        title=f'Picture fetched by: {interaction.user}',
        description=description or 'Prepare for edit the next Image:',
        color=discord.Color.random(),
    )
    print(drag.content_type)
    print(drag.size)
    print(drag.width)
    embed.set_image(url='{}'.format(drag))
    embed.set_thumbnail(url=interaction.user.avatar)
    upload(drag.url, public_id=f'Bot/{file_name}')

    view.add_item(discord.ui.Button(label='See on the Browser',
                                    style=discord.ButtonStyle.url, url='{}'.format(drag)))
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


#! Discord emoji Resize
@bot.tree.command(name='discord_emoji_resize', description="Resize an image to fit in the Discord emoji perfect configuration, it's focus in face")
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image")
async def discord_emoji_resize(interaction: Interaction, drag: discord.message.Attachment, description: str | None):
    try:
        file_name = drag.filename
        view = Link() and EmojiSizing(file_name)
        embed = discord.Embed(
            title=f'Picture fetched by: {interaction.user}',
            description=description or 'Prepare for edit the next Image:',
            color=discord.Color.random(),
        )
        print(drag.content_type)
        print(drag.size)
        embed.set_image(url='{}'.format(drag))
        embed.set_thumbnail(url=interaction.user.avatar)
        upload(drag.url, public_id=f'Bot/{file_name}')

        view.add_item(discord.ui.Button(label='See on the Browser',
                                        style=discord.ButtonStyle.url, url='{}'.format(drag)))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    except:
        await interaction.response.send_message("Command Not Found, please Try Again in a few seconds, type /help_404 to see more info")


#! Text Overlay
@bot.tree.command(name='text_overlay', description="Add a text over the image you upload, choose position.")
@app_commands.describe()
@app_commands.choices(font=[
    Choice(name='Roboto', value='Roboto'),
    Choice(name='Verdana', value='Verdana'),
    Choice(name='Pacifico', value='Pacifico'),
])
@app_commands.choices(position=[
    Choice(name='North', value='north'),
    Choice(name='South', value='south'),
    Choice(name='West', value='west'),
    Choice(name='East', value='east'),
])
@app_commands.choices(color=[
    Choice(name='Orange', value='Orange'),
    Choice(name='Yellow', value='Yellow'),
    Choice(name='Red', value='Red'),
    Choice(name='Purple', value='Purple'),
    Choice(name='Pink', value='Pink'),
    Choice(name='Green', value='Green'),
    Choice(name='Cyan', value='Cyan'),
    Choice(name='Blue', value='Blue'),
])
@app_commands.choices(effect=[
    Choice(name='Deg', value='deg'),
    Choice(name='Fade', value='fade'),
    Choice(name='Plain', value='plain')
])
async def text_overlay(interaction: Interaction, drag: discord.message.Attachment,  font: Choice[str], text: str, font_size: int, position: Choice[str], color: Choice[str], effect: Choice[str]):
    file_name = drag.filename
    view = Link() and TextOverlay(file_name, font.value,
                                  text, font_size, position.value, color.value, effect.value)
    embed = discord.Embed(
        title=f'Picture fetched by: {interaction.user}',
        description=f'Prepare to write {text} over the image',
        color=discord.Color.random(),
    )
    embed.set_image(url='{}'.format(drag))
    embed.set_thumbnail(url=interaction.user.avatar)
    upload(drag.url, public_id=f'Bot/{file_name}')

    view.add_item(discord.ui.Button(label='See on the Browser',
                                    style=discord.ButtonStyle.url, url='{}'.format(drag)))
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


#! Help Global Helps
@bot.tree.command(name='help', description='Help About The usage of the bot')
async def help(interaction: Interaction):
    embed_help = discord.Embed(
        title=f"General Help for bot interaction, (for command help type /help_command)",
        description=f'''About the Cloud Create Bot: 
                          
                        This bot is made with Cloudinary Api and offer many interactive options to edit images on the fly.
                        
                        The **interactions** are step by step to transform an image from the command to the result
                        
                        There is only 2 Available archive for now: **[image/png, image/jpeg(jpg) & image/webp]**
                        
                        Discord Cloud Create offer an option to edit your Avatar and your Banner[must be Discord Premium user]
                        
                        All the files uploaded with this bot is save for 7 days in Cloudinary and auto erased.
                        
                        **Disclaimer:** all the files you upload may be respectful with the terms and condition of Discord©
                        The use of this bot for load content nsfw might be consider for **Ban your Discord Account Permanently**
                        
                        You can contact me on Discord for any issue here: https://discord.gg/dncv6DajDX
                        or DM 𝕯𝖎𝖊𝖌𝖆𝖙𝖔(#)4880
                      ''',
        color=discord.Color.red(),
    )
    embed_help.set_thumbnail(url=interaction.user.avatar)
    embed_help.set_footer(
        text='In case of getting a 404 Not Found, consult /help_404')
    await interaction.response.send_message(content="Typing...")
    await asyncio.sleep(5)
    await interaction.edit_original_response(embed=embed_help, content='')


#! Help Commands
@bot.tree.command(name='help_commands', description='Command usage, Prefix, Returns and Interaction')
async def help_commands(interaction: Interaction):
    help_view = Pagination()
    await interaction.response.send_message(embed=Command_Embeded(), view=help_view)


#! Help Error 404
@bot.tree.command(name='help_404', description='Help About Error 404 aplication dont response')
async def help_404(interaction: Interaction):
    embed_404 = discord.Embed(
        title=f"Error 404 The Aplication don't response",
        description='''This could be for many reason: 
                          
                        **1.- Connection error with the platform**
                        **2.- Discord TimeOut (tried more than 3 seconds to call the command)**
                        **3.- Internet too Slow**
                        **4.- I Hate You (jk)**
                        **5.- Cloudinary Service Might be Down for a while**
                      ''',
        color=discord.Color.red()
    )
    embed_404.set_thumbnail(url=interaction.user.avatar)
    embed_404.set_footer(
        text='In case of getting a 404 Not Found, try again in a few seconds')
    await interaction.response.send_message(embed=embed_404)

bot.run(TOKEN)
