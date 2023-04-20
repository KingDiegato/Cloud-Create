from core import bot
from discord import Embed, Color, Interaction, message, app_commands
from cloudinary.uploader import upload

from classMod.Layout import LayoutFor

#! Layout
@bot.tree.command(name='layout_for', description='Upload an image and create a Layout effect over your file')
@app_commands.describe(pfp_drag="drag'n' drop Your desire profile picture", banner_drag="drag'n' drop Your desire banner image", description="a small description of your uploads")
async def layout_for(interaction: Interaction, pfp_drag: message.Attachment, banner_drag: message.Attachment, description: str | None):
    try:
        user_name = interaction.user.name
        view = LayoutFor(user_name, pfp_drag.url, banner_drag.url,
                        pfp_drag.size, banner_drag.size)
        await interaction.response.defer()
        embed = Embed(
            title=f'Picture fetched by: {interaction.user}',
            description=f'Prepare for create the layout for a social media and {description}',
            color=Color.random(),
        )
        embed.set_image(url='{}'.format(banner_drag))
        embed.set_thumbnail(url=pfp_drag.url)
        upload(pfp_drag.url,
            public_id=f'UsersLayout/{user_name}_av{pfp_drag.size}')
        upload(banner_drag.url,
            public_id=f'UsersLayout/{user_name}_banner{banner_drag.size}')
        await interaction.followup.send(embed=embed, view=view, ephemeral=True)
    except:
        error_embed = Embed(
            title=f'Sorry {interaction.user}',
            description="Command Not Found, please Try Again in a few seconds, type /help_404 to see more info",
            color=Color.random(),
        )
        await interaction.followup.send(embed=error_embed)
