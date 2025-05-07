from discord.ui import View, button, Button
from discord import ButtonStyle, Interaction, Embed
from cloudinary import CloudinaryImage
from datetime import datetime
from modules.module import Link, ForceDisabled, Force, Force2
from classMod.silhouette import SilhouettePanel

import asyncio

# Todo: Realizar refactor de los transformation = []


class TransformAvView(View):
    def __init__(self, username, query):
        super().__init__()
        self.username = username
        self.query = query

    # ? Row Button = 1
    @button(label='Whitify Avatar', style=ButtonStyle.primary, row=1)
    async def Whitify_av(self, interaction: Interaction, button: Button):
        download_link = Link()
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up{self.query}').build_url(transformation=[{'effect': "contrast:30"}, {'effect': "saturation:-30"}, {'effect': "brightness:30"}])
        embed_transformed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Here is it {self.username}'
        )
        embed_transformed.set_image(url=image_transform)
        download_link.add_item(Button(label='Download Now',
                                      style=ButtonStyle.url, url=image_transform, emoji="<a:vibing:747680206734622740>"))
        await interaction.response.send_message(embed=embed_transformed, view=download_link)

    @button(label='High Contrast', style=ButtonStyle.primary, row=1)
    async def High_contrast_av(self, interaction: Interaction, button: Button):
        download_link = Link()
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up{self.query}').build_url(transformation=[{'effect': "contrast:50"}, {'effect': "saturation:-40"}])
        embed_transformed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Here is it {self.username}'
        )
        embed_transformed.set_image(url=image_transform)
        download_link.add_item(Button(label='Download Now',
                                      style=ButtonStyle.url, url=image_transform, emoji="<a:vibing:747680206734622740>"))
        await interaction.response.send_message(embed=embed_transformed, view=download_link)

    @button(label='Sepia', style=ButtonStyle.primary, row=1)
    async def Sepia_effect_av(self, interaction: Interaction, button: Button):
        download_link = Link()
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up{self.query}').build_url(effect="sepia")
        embed_transformed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Here is it {self.username}'
        )
        embed_transformed.set_image(url=image_transform)
        download_link.add_item(Button(label='Download Now',
                                      style=ButtonStyle.url, url=image_transform, emoji="<a:vibing:747680206734622740>"))
        await interaction.response.send_message(embed=embed_transformed, view=download_link)

    # ? Row Button = 2
    @button(label='Black and White', style=ButtonStyle.primary, row=2)
    async def Black_and_white_effect_av(self, interaction: Interaction, button: Button):
        download_link = Link()
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up{self.query}').build_url(transformation=[{'effect': "grayscale"}])
        embed_transformed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Here is it {self.username}'
        )
        embed_transformed.set_image(url=image_transform)
        download_link.add_item(Button(label='Download Now',
                                      style=ButtonStyle.url, url=image_transform, emoji="<a:vibing:747680206734622740>"))
        await interaction.response.send_message(embed=embed_transformed, view=download_link)

    @button(label='Colorful Avatar', style=ButtonStyle.primary, row=2)
    async def Colorful_effect_av(self, interaction: Interaction, button: Button):
        download_link = Link()
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up{self.query}').build_url(transformation=[{'effect': "contrast:30"}, {'effect': "saturation:30"}, {'effect': "brightness:10"}])
        embed_transformed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Here is it {self.username}'
        )
        embed_transformed.set_image(url=image_transform)
        download_link.add_item(Button(label='Download Now',
                                      style=ButtonStyle.url, url=image_transform, emoji="<a:vibing:747680206734622740>"))
        await interaction.response.send_message(embed=embed_transformed, view=download_link)

    @button(label='Silhouette Avatar', style=ButtonStyle.primary, row=2)
    async def Silhouette_panel(self, interaction: Interaction, button: Button):
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up{self.query}').build_url(transformation=[{'effect': "brightness:30"}, {'effect': "blackwhite:60"}])

        silhouette_view = SilhouettePanel(self.username)

        embed_transformed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Silhouette black edition: {self.username}',
            description='You can change the color alike the /color_silhouette command, Try it! 🌟'
        )
        embed_transformed.set_image(url=image_transform)
        await interaction.response.send_message(embed=embed_transformed, view=silhouette_view)

    @button(label='Background Remove', style=ButtonStyle.primary, row=2)
    async def Background_remove_av(self, interaction: Interaction, button: Button):
        background_remove_view = ForceDisabled()

        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up{self.query}').build_url(transformation=[{'effect': "background_removal"}, {'quality': "auto"}])
        image_blur = CloudinaryImage(
            f'Bot/{self.username}q:av_up{self.query}').build_url(transformation=[{'effect': "blur:1500"}])

        embed_transformed = Embed(
            timestamp=datetime.utcnow(),
            title=f'PFP without Background is in progress, please wait. {self.username}',
            description='if you cannot see the image, please try to download it in a while'
        )

        embed_transformed.set_image(url=image_blur)

        await interaction.response.send_message(embed=embed_transformed, view=background_remove_view)
        await asyncio.sleep(30)

        transition_embed = Embed(
            timestamp=datetime.utcnow(),
            title=f'PFP with Background Will be here in a moment {self.username}',
            description='if you cannot see the image, please try to download it in a while'
        )
        transition_embed.set_image(url=image_blur)

        await interaction.edit_original_response(embed=transition_embed, view=background_remove_view)

        final_view = Link() and Force2(image_transform)

        final_embed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Background Removed!',
            description='if you cannot see the image, please try to download it in a while'
        )
        final_view.add_item(Button(label='Download Now', style=ButtonStyle.url,
                            url=image_transform, emoji="<a:vibing:747680206734622740>"))
        final_embed.set_image(url=image_transform)

        await asyncio.sleep(30)

        await interaction.edit_original_response(embed=final_embed, view=final_view)
