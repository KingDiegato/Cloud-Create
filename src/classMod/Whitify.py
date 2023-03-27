from discord.ui import View, button, Button
from cloudinary import CloudinaryImage

from discord import ButtonStyle, Color, Embed, Interaction
from modules.module import Link

from datetime import datetime

class WhiteColor(View):
  
    transforms = [{'effect': "contrast:30"}, {'effect': "saturation:-30"}, {'effect': "brightness:30"}, {'quality': "auto"}]
    
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        

    @button(label='Transform! ✨', style=ButtonStyle.blurple)
    async def white_color_model(self, interaction: Interaction, button: Button):
        link_view = Link()
        embed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='White Color Effect Powered by Cloudinary 🎉✨',
            color=Color.random(),
        )
        image_tag = CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(transformation=self.transforms)
        embed.set_image(url=image_tag)
        link_view.add_item(Button(label='Download ✨',
                                             style=ButtonStyle.url, url=image_tag, emoji="<a:vibing:747680206734622740>"))
        await interaction.response.send_message(embed=embed, view=link_view)
