from discord.app_commands import describe, choices, Choice

from core import bot
from discord import Interaction, message, Embed, Color, ui, ButtonStyle
from modules.module import Link
from classMod.Overlay import TextOverlay

from cloudinary.uploader import upload

#! Text Overlay
@bot.tree.command(name='text_overlay', description="Add a text over the image you upload, choose position.")
@describe()
@choices(font=[
    Choice(name='Roboto', value='Roboto'),
    Choice(name='Verdana', value='Verdana'),
    Choice(name='Pacifico', value='Pacifico'),
])
@choices(position=[
    Choice(name='North', value='north'),
    Choice(name='South', value='south'),
    Choice(name='West', value='west'),
    Choice(name='East', value='east'),
])
@choices(color=[
    Choice(name='Orange', value='Orange'),
    Choice(name='Yellow', value='Yellow'),
    Choice(name='Red', value='Red'),
    Choice(name='Purple', value='Purple'),
    Choice(name='Pink', value='Pink'),
    Choice(name='Green', value='Green'),
    Choice(name='Cyan', value='Cyan'),
    Choice(name='Blue', value='Blue'),
])
@choices(effect=[
    Choice(name='Deg', value='deg'),
    Choice(name='Fade', value='fade'),
    Choice(name='Plain', value='plain')
])
async def text_overlay(interaction: Interaction, drag: message.Attachment,  font: Choice[str], text: str, font_size: int, position: Choice[str], color: Choice[str], effect: Choice[str]):
    try:
        file_name = drag.filename
        view = Link() and TextOverlay(file_name, font.value,
                                    text, font_size, position.value, color.value, effect.value)
        await interaction.response.defer()
        embed = Embed(
            title=f'Picture fetched by: {interaction.user}',
            description=f'Prepare to write {text} over the image',
            color=Color.random(),
        )
        embed.set_image(url='{}'.format(drag))
        embed.set_thumbnail(url=interaction.user.avatar)
        upload(drag.url, public_id=f'Bot/{file_name}')

        view.add_item(ui.Button(label='See on the Browser',
                                        style=ButtonStyle.url, url='{}'.format(drag)))
        await interaction.followup.send(embed=embed, view=view, ephemeral=True)
    except:
        error_embed = Embed(
            title=f'Sorry {interaction.user}',
            description="Command Not Found, please Try Again in a few seconds, type /help_404 to see more info",
            color=Color.random(),
        )
        await interaction.followup.send(embed=error_embed)