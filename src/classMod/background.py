from discord.ui import View, button, Button
from cloudinary import CloudinaryImage

from discord import ButtonStyle, Color, Embed, Interaction
from modules.module import Link, ForceDisabled, Force
import asyncio
from cloudinary.uploader import upload

from datetime import datetime

class BgRemoval(View):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    @button(label='Transform! ✨', style=ButtonStyle.blurple)
    async def bg_removal_model(self, interaction: Interaction, button: Button):
        embed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='''We are Processing the transformation, Please Wait...''',
            color=Color.random(),
        )
        image_tag = CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(transformation=[{'effect': "background_removal"}, {'quality': "auto"}])
        image_blur = CloudinaryImage(
            f"bot/{self.file_name}.png").build_url(transformation=[{'effect': "blur:1500"}, {'quality': "auto"}])
        ephemeral_view = ForceDisabled()
        link_view = Link() and Force(image_tag)
        embed.set_image(url=image_blur)
        new_embed = Embed(
            timestamp=datetime.utcnow(),
            title=f"The image is ready {interaction.user}",
            description="if You cannot see the image here its cause Discord Already cached it and might not render, but you can found the image by clicking in the download button"
        )
        new_embed.set_image(url=image_blur)
        link_view.add_item(Button(label='Download ✨',
                                             style=ButtonStyle.url, url=image_tag, emoji="<a:vibing:747680206734622740>"))
        await asyncio.sleep(1)
        await interaction.response.send_message(embed=embed, view=ephemeral_view)
        button.disabled = True

        await asyncio.sleep(25)
        try:
            uploading_img_no_bg = upload(image_tag, responsive_breakpoints={
                "create_derived": True,
                "bytes_step": 150,
                "min_width": 200,
                "max_width": 4000})
            print('Image uploaded, we are safe')
        except:
            print('image cannot be uploaded')
        await asyncio.sleep(25)
        try:
            new_embed.set_image(url=uploading_img_no_bg['secure_url'])
        except:
            print('keeping the original file and pry for this render')
        await interaction.edit_original_response(embed=new_embed, view=link_view)
        await asyncio.sleep(29)
        await interaction.edit_original_response(embed=new_embed, view=link_view)