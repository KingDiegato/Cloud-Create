from discord.ui import View, Button, button
from discord import ButtonStyle, Interaction, Embed, Color
from modules.module import Link
from datetime import datetime
from cloudinary import CloudinaryImage

class SepiaEffect(View):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    @button(label='Transform! ✨', style=ButtonStyle.blurple)
    async def sepia_effect(self, interaction: Interaction, button: Button):
        link_view = Link()
        embed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='Sepia Effect Powered by Cloudinary 🎉✨',
            color=Color.random(),
        )
        image_tag = CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(effect="sepia")
        embed.set_image(url=image_tag)
        link_view.add_item(Button(label='Download',
                                             style=ButtonStyle.url, url=image_tag, emoji="<a:vibing:747680206734622740>"))
        await interaction.response.send_message(embed=embed, view=link_view)