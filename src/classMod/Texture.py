import asyncio

from discord.ui import View, button, Button
from discord import Interaction, ButtonStyle, Embed, Color
from datetime import datetime
from cloudinary import CloudinaryImage
from modules.module import Link
from classMod.TransformView import TransformAvView

class Texturized(View):
    def __init__(self, user_name, url, size, strength, effect):
        super().__init__()
        self.user_name = user_name
        self.url = url
        self.size = size
        self.strength = strength
        self.effect = effect

    @button(label='Texturize! ✨', style=ButtonStyle.primary, row=1)
    async def texturized_frame(self, interaction: Interaction, button: Button):
        download_view = Link()
        embed_layout = Embed(
            timestamp=datetime.utcnow(),
            title='Texture applied Powered By Cloudinary ✨',
            description='By clicking in the Download Button, You will see the Image With the size perfectly for the social media, for avatar and for banner individually',
            color=Color.random()
        )
        result = CloudinaryImage(
            f"Bot/{self.user_name}_texturized{self.size}").build_url(transformation=[
                {'overlay': f"Effects:{self.effect}"},
                {'effect': "displace", 'flags': "layer_apply",
                    'x': self.strength, 'y': self.strength}, {'quality': "auto"}
            ]
        )
        await asyncio.sleep(1)
        print(result)
        embed_layout.set_image(url=result)
        download_view.add_item(Button(label='Download ✨',
                                                 style=ButtonStyle.url, url=result, emoji="<a:vibing:747680206734622740>"))
        await interaction.response.send_message(view=download_view, embed=embed_layout)
