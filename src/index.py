import asyncio
import os
import discord
import dotenv

import datetime
import time

# Local Imports
# ==============================================================╗
################################################################║
from embeds.helper          import Command_Embeded             #║
from modules.module         import Link, Pagination            #║
from classMod.Avatar        import AvView                      #║
from classMod.BlackWhite    import BlackAndWhite               #║
from classMod.Emoji         import EmojiSizing                 #║
from classMod.Sepia         import SepiaEffect                 #║
from classMod.contrast      import HighContrast                #║
from classMod.Whitify       import WhiteColor                  #║
from classMod.colorful      import ColorFul                    #║
from classMod.Cartoon       import Cartoonify                  #║
from classMod.Burn          import ColorBurn                   #║
from classMod.background    import BgRemoval                   #║
from classMod.Silhouette    import Silhouette, TwoSilhouette   #║
from classMod.Overlay       import TextOverlay                 #║
from classMod.Layout        import LayoutFor                   #║
from classMod.Texture       import Texturized                  #║
################################################################║
# ==============================================================╝
# End Local Imports

# Import Discord Specifications
# ================================
from discord.ext import commands

from discord import Interaction, Member, app_commands

from discord.app_commands import Choice

from core import bot

# ==============================================================╗
################################################################║
from commands.pingCommand import *                             #║
from commands.avCommand   import *                             #║
################################################################║
# ==============================================================╝




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

@bot.event
async def on_ready():
    print('='*40)
    print('Online!')
    print('='*40)
    await bot.tree.sync()


#! init update command
@bot.command()
async def init(ctx):
    await bot.tree.sync()
    await ctx.reply('Done!')


@bot.tree.command(name='pineado', description='Llama a una persona por su tag')
async def pineado(interaction: Interaction, nombre: Member):
    await interaction.response.send_message(nombre.mention)


av_remove_bg_option = discord.SelectOption(label='Remove Background', value='background_removal',
                                           description="remove the background of your pfp, note: doesn't work with no background images.")
av_silhouete_option = discord.SelectOption(label='Color Silhouette', value='color_silhouette',
                                           description='Create a cool and Joyful Color Effect to your pfp')
av_whitify_option = discord.SelectOption(label='Whitify', value='whitify',
                                         description='Clarify your pfp with this Effect')


#! Avatar recover interaction [/av]



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
        upload(f"{member.banner}", public_id=f'Bot/{member.name}qbanner_up')
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


#! Black and White
# Transform the Image with a Black & White filter when you call the interaction.
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


#! High Contrast
#Transform the Image and intensify the contrast but equals the saturation.
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


#! Whitify
# Transform the Image with a Black & White filter when you call the interaction.
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


#! Colorful
# Transform the Image with a Black & White filter when you call the interaction.
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
        upload(drag.url, public_id=f'Bot/cartony_{file_name}')

        view.add_item(discord.ui.Button(label='See on the Browser',
                                        style=discord.ButtonStyle.url, url='{}'.format(drag)))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    except:
        await interaction.response.send_message("Command Not Found, please Try Again in a few seconds, type /help_404 to see more info")


#! ColorBurn
@bot.tree.command(name='color_burn', description='Upload an image and create a Burn effect in a photo')
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
    view = LayoutFor(user_name, pfp_drag.url, banner_drag.url,
                     pfp_drag.size, banner_drag.size)
    embed = discord.Embed(
        title=f'Picture fetched by: {interaction.user}',
        description=f'Prepare for create the layout for a social media and {description}',
        color=discord.Color.random(),
    )
    embed.set_image(url='{}'.format(banner_drag))
    embed.set_thumbnail(url=pfp_drag.url)
    upload(pfp_drag.url,
           public_id=f'UsersLayout/{user_name}_av{pfp_drag.size}')
    upload(banner_drag.url,
           public_id=f'UsersLayout/{user_name}_banner{banner_drag.size}')
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


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


# Silhouette Color Effect! 🧨✨🎉

# Transform the Image with a Black & White filter when you call the interaction.

color_choices = app_commands.choices(choice_color=[
    Choice(name='Red     🟥', value='#CF2C2C'),
    Choice(name='Yellow  🟨', value='#FFF900'),
    Choice(name='Lime    🟩', value='#5EA031'),
    Choice(name='Green   🟢', value='#0B7E29'),
    Choice(name='Cyanade 🟦', value='#1AB4AA'),
    Choice(name='Purple  🟪', value='#7038A1'),
    Choice(name='Pink    💗', value='#D867B4'),
    Choice(name='Wine    🔴', value='#862044'),
    Choice(name='Blue    🔵', value='#09f'),
    Choice(name='Black   ⚫', value='#121212')
])
color_choices_2 = app_commands.choices(choice_color_two=[
    Choice(name='Red     🟥', value='#CF2C2C'),
    Choice(name='Yellow  🟨', value='#FFF900'),
    Choice(name='Lime    🟩', value='#5EA031'),
    Choice(name='Green   🟢', value='#0B7E29'),
    Choice(name='Cyanade 🟦', value='#1AB4AA'),
    Choice(name='Purple  🟪', value='#7038A1'),
    Choice(name='Pink    💗', value='#D867B4'),
    Choice(name='Wine    🔴', value='#862044'),
    Choice(name='Blue    🔵', value='#09f'),
    Choice(name='Black   ⚫', value='#121212')
])


#! Color Silhouette
@bot.tree.command(name='color_silhouette', description='Upload an image to apply a cool Colorized Effect')
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image", choice_color='a color for the effect, Is Required')
@color_choices
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
@color_choices
@color_choices_2
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


#! Texturized
@bot.tree.command(name='texturize', description='Upload an image and create a Layout effect over your file')
@app_commands.describe(drag="drag'n' drop Your desire picture to texturize", strength="Choice how much strength you want your texturize effect", effect='Choice the effect to apply', description="a small description of your uploads")
@app_commands.choices(strength=[
    Choice(name='Weak', value=15),
    Choice(name='Moderate', value=25),
    Choice(name='Strong', value=40)
])
@app_commands.choices(effect=[
    Choice(name='Water', value='water'),
    Choice(name='Pebbles', value='pebbles'),
    Choice(name='Concrete', value='concrete')
])
async def texturize(interaction: Interaction, drag: discord.message.Attachment, strength: Choice[int], effect: Choice[str], description: str | None):
    user_name = interaction.user.name
    view = Texturized(user_name, drag.url, drag.size,
                      strength.value, effect.value)
    embed = discord.Embed(
        title=f'Picture Upload by: {interaction.user}',
        description=f'Prepare for add a texture to this image for a social media' or description,
        color=discord.Color.random(),
    )
    embed.set_image(url='{}'.format(drag))
    upload(drag.url,
           public_id=f'Bot/{user_name}_texturized{drag.size}')
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
