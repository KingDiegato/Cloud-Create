from core import bot
from discord import Embed, Color, Interaction, message, ui, ButtonStyle, app_commands
from modules.module import Link
from cloudinary.uploader import upload
from commands.silhouetteConstants import *

from classMod.Silhouette import TwoSilhouette

#! Two Color Silhouette
@bot.tree.command(name='two_color_silhouette', description='Upload an image to apply a cool Colorized Effect')
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image", choice_color='a color for the effect, Is Required')
@color_choices
@color_choices_2
@strength
async def two_color_silhouette(interaction: Interaction, drag: message.Attachment, choice_color: Choice[str], choice_color_two: Choice[str],  strength: Choice[str], description: str | None):
    try:
        file_name = drag.filename
        view = Link() and TwoSilhouette(file_name, choice_color.value,
                                        choice_color_two.value, drag.width, strength.value)
        await interaction.response.defer()
        embed = Embed(
            title=f'Picture fetched by: {interaction.user}',
            description=description or 'Prepare for edit the next Image:',
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
