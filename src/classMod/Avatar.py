from discord.ui import View, button, Button
from discord import Interaction, ButtonStyle, Embed
from datetime import datetime
from cloudinary import CloudinaryImage
from classMod.TransformView import TransformAvView

class AvView(View):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @button(label='Yes! transform it ✨', style=ButtonStyle.primary)
    async def av_select_transform(self, interaction: Interaction, button: Button):
        av_username = self.name
        transformation_view = TransformAvView(av_username)
       
        print(av_username)
        embed_prev_img = Embed(
            timestamp=datetime.utcnow(),
            title=f'Prepare to transform Your Avatar {av_username}',
            description='Select any options and see inmediately results'
        )
        image_transform = CloudinaryImage(
            f'Bot/{av_username}q:av_up').build_url(transformation=[{'effect': "blur:1500"}])
        embed_prev_img.set_image(url=image_transform)

        await interaction.response.send_message(embed=embed_prev_img, view=transformation_view)

        