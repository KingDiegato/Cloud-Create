from core import bot

from discord import Interaction, Member, Embed, Color
from cloudinary.uploader import upload

# ==============================================================╗
from classMod.Avatar        import AvView                      #║
# ==============================================================╝

@bot.tree.command(name='banner', description='Obtener el Banner')
async def av(interaction: Interaction, member: Member):
    '''
    Recover Banner
    '''
    try:
        av_view = AvView(member.name)
        show_banner = Embed(
            title=f'Avatar de {member.name}',
            description='🌟☁ Lets Transform it ☁🌟',
            color=Color.random(),
        )
        show_banner.set_image(url=member.banner)
        upload(f"{member.banner}", public_id=f'Bot/{member.name}qbanner_up')
        await interaction.response.send_message(embed=show_banner, view=av_view,)
    except FileNotFoundError:
        await interaction.response.send_message('Your Banner is not available for edits')
    except:
        await interaction.response.send_message("Command Not Found, please Try Again in a few seconds, type /help_404 to see more info")