from datetime import datetime
from discord.ui import View, Button
from discord import ButtonStyle, Color, Embed, Interaction
from cloudinary import CloudinaryImage
from modules.module import Link


class Cartoonify(View):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    async def cartoon_model(self, interaction: Interaction, button: Button):
        button = {**button, 'label': 'Transform! ✨',
                  'style': ButtonStyle.blurple}
        link_view = Link()
        embed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='Cartonify picture Powered by Cloudinary 🎉✨',
            color=Color.random(),
        )
        image_tag = CloudinaryImage(
            f"Bot/cartony_{self.file_name}.png"
        ).build_url(
            transformation=[
                {'effect': "contrast:-50"},
                {'effect': "cartoonify"},
                {'effect': "saturation:-10"},
                {'effect': "improve:outdoor:50"},
                {'quality': "auto"}
            ]
        )

        embed.set_image(url=image_tag)
        link_view.add_item(
            Button(
                label='Download ✨',
                style=ButtonStyle.url,
                url=image_tag,
                emoji="<a:vibing:747680206734622740>"
            )
        )
        await interaction.response.send_message(embed=embed, view=link_view)
