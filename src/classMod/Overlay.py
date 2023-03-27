import asyncio

from discord.ui import View, button, Button
from cloudinary import CloudinaryImage

from discord import ButtonStyle, Color, Embed, Interaction
from modules.module import Link

from datetime import datetime

class TextOverlay(View):
    def __init__(self, file_name, font, text, font_size, position, color, effect):
        super().__init__()
        self.file_name = file_name
        self.font = font
        self.text = text
        self.font_size = font_size
        self.position = position
        self.color = color
        self.effect = effect

    @button(label='Transform! ✨', style=ButtonStyle.blurple)
    async def colorful_model(self, interaction: Interaction, button: Button):
        link_view = Link()
        text_overlay = CloudinaryImage(
            f"Colors/Color_{self.color}_{self.effect}").build_url(overlay={'font_family': f'{self.font}', 'font_size': self.font_size, 'font_weight': "bold", 'text': f'{self.text}'.replace(" ", "%20")}, flags="cutter")
        embed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='''Colorful picture Powered by Cloudinary 🎉✨''',
            color=Color.random(),
        )
        print(text_overlay)
        await asyncio.sleep(2)
        image_tag = CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(transformation=[{'overlay': {'url': f'{text_overlay}'}}, {'quality': "auto"}, {'flags': "layer_apply", 'gravity': self.position, 'y': 20, 'x': 10}])
        embed.set_image(url=image_tag)
        link_view.add_item(Button(label='Download ✨',
                                             style=ButtonStyle.url, url=image_tag, emoji="<a:vibing:747680206734622740>"))
        await interaction.response.send_message(embed=embed, view=link_view)