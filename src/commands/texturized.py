from core import bot
from discord import app_commands, Interaction, message, Embed, Color
from classMod.Texture import Texturized
from discord.app_commands import Choice

from cloudinary.uploader import upload


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
async def texturize(interaction: Interaction, drag: message.Attachment, strength: Choice[int], effect: Choice[str], description: str | None):
    try:
        user_name = interaction.user.name
        view = Texturized(user_name, drag.url, drag.size,
                                    strength.value, effect.value)
        await interaction.response.defer()
        embed = Embed(
            title=f'Picture Upload by: {interaction.user}',
            description=f'Prepare for add a texture to this image for a social media' or description,
            color=Color.random(),
        )
        embed.set_image(url='{}'.format(drag))
        upload(drag.url,
            public_id=f'Bot/{user_name}_texturized{drag.size}')
        await interaction.followup.send(embed=embed, view=view, ephemeral=True)
    except:
        error_embed = Embed(
            title=f'Sorry {interaction.user}',
            description="Command Not Found, please Try Again in a few seconds, type /help_404 to see more info",
            color=Color.random(),
        )
        await interaction.followup.send(embed=error_embed)
