from core import bot
from discord import Interaction, Member, Embed, Color
from cloudinary.uploader import upload

from classMod.Avatar        import AvView                      

@bot.tree.command(name='av', description='Obtener el Avatar')
async def av(interaction: Interaction, member: Member):
    try:
        av_view = AvView(member.name)
        await interaction.response.defer()
        show_avatar = Embed(
            title=f'Avatar de {member.name}',
            description='🌟☁ Lets Transform it ☁🌟',
            color=Color.random(),
        )
        show_avatar.set_image(url=member.avatar)
        upload(f"{member.avatar}", public_id=f'Bot/{member.name}q:av_up')
        await interaction.followup.send(embed=show_avatar, view=av_view)
    except:
        error_embed = Embed(
            title=f'Sorry {member.name}',
            description='Avatar not found, try again in a few moments',
            color=Color.random(),
        )
        await interaction.followup.send(embed=error_embed)
        