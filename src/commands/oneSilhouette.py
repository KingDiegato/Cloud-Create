from core import bot
from discord import Embed, Color, Interaction, message, ui, ButtonStyle, app_commands
from modules.module import Link
from cloudinary.uploader import upload
from commands.silhouetteConstants import color_choices, strength

from classMod.silhouette import Silhouette

#! Color Silhouette


@bot.tree.command(name='color_silhouette', description='Upload an image to apply a cool Colorized Effect')
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image", choice_color='a color for the effect, Is Required')
@color_choices
@strength
async def color_silhouette(interaction: Interaction, drag: message.Attachment, choice_color: app_commands.Choice[str], strength: app_commands.Choice[str], description: str | None):
    try:
        file_name = drag.filename
        view = Link() and Silhouette(file_name, choice_color.value, strength.value)
        await interaction.response.defer()
        embed = Embed(
            title=f'Picture fetched by: {interaction.user}',
            description=description or 'Prepare for edit the next Image:',
            color=Color.random(),
        )
        print(drag.content_type)
        print(drag.size)
        print(drag.width)
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
