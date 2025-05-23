from core import bot

from discord import Interaction, Member, Embed, Color
from cloudinary.uploader import upload

from utils.randomString import get_random_string

from classMod.avatar import AvView


@bot.tree.command(name="banner", description="Obtener el Banner")
async def av(interaction: Interaction, member: Member):
    try:
        query = get_random_string(len(member.name))
        av_view = AvView(member.name, query)
        await interaction.response.defer()
        show_banner = Embed(
            title=f"Avatar de {member.name}",
            description="🌟☁ Lets Transform it ☁🌟",
            color=Color.random(),
        )
        show_banner.set_image(url=member.banner)
        upload(f"{member.banner}",
               public_id=f"Bot/{member.name}qbanner_up{query}")
        await interaction.followup.send(
            embed=show_banner,
            view=av_view,
        )
    except:
        error_embed = Embed(
            title=f"Sorry {member.name}",
            description="Banner not found, try again in a few moments",
            color=Color.random(),
        )
        await interaction.followup.send(embed=error_embed)
