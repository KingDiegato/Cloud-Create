from core import bot
from discord import app_commands, Interaction, message, Embed, Color, ui, ButtonStyle
from classMod.contrast import HighContrast
from modules.module import Link

from cloudinary.uploader import upload

#! High Contrast
#Transform the Image and intensify the contrast but equals the saturation.
@bot.tree.command(name='high_contrast', description='Upload an image to highly contrast it without saturation problem')
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image")
async def high_contrast(interaction: Interaction, drag: message.Attachment, description: str | None):
    try:
        file_name = drag.filename
        view = Link() and HighContrast(file_name)
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
        