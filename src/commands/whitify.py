from core import bot
from discord import Interaction, message, app_commands, Color, ui, ButtonStyle, Embed
from classMod.Whitify import WhiteColor
from modules.module import Link

from cloudinary.uploader import upload

#! Whitify
# Transform the Image with a Black & White filter when you call the interaction.
@bot.tree.command(name='whitify', description='Upload an image and Scale this to become More Clear')
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image")
async def whitify(interaction: Interaction, drag: message.Attachment, description: str | None):
    try:
        file_name = drag.filename
        view = Link() and WhiteColor(file_name)
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
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    except:
        await interaction.response.send_message("Command Not Found, please Try Again in a few seconds, type /help_404 to see more info")

# End of Whitify Effect Command