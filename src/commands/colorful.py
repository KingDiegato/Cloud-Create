from core import bot
from discord import Embed, Color, Interaction, message, ui, ButtonStyle, app_commands
from modules.module import Link
from cloudinary.uploader import upload

from classMod.colorful import ColorFul

#! Colorful
@bot.tree.command(name='colorful', description='Upload an image and create a colorful effect over your file')
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image")
async def colorful(interaction: Interaction, drag: message.Attachment, description: str | None):
    """
    Uploads an image and creates a colorful effect over the file.

    Args:
        interaction (Interaction): The interaction user.
        drag (message.Attachment): The attachment file.
        description (str | None): A description for the image.

    Returns:
        None
    """
    try:
        file_name = drag.filename
        view = Link() and ColorFul(file_name)
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