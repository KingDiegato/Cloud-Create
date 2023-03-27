from discord.ui import View, button, Button
from discord import ButtonStyle, Interaction, Embed
from cloudinary import CloudinaryImage
from datetime import datetime
from modules.module import Link
from classMod.Silhouette import SilhouettePanel

# Todo: Realizar refactor de los transformation = []

class TransformAvView(View):
    def __init__(self, username):
        super().__init__()
        self.username = username

    # ? Row Button = 1
    @button(label='Whitify Avatar', style=ButtonStyle.primary, row=1)
    async def Whitify_av(self, interaction: Interaction, button: Button):
        download_link = Link()
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "contrast:30"}, {'effect': "saturation:-30"}, {'effect': "brightness:30"}])
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
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "contrast:50"}, {'effect': "saturation:-40"}])
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
            f'Bot/{self.username}q:av_up').build_url(effect="sepia")
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
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "grayscale"}])
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
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "contrast:30"}, {'effect': "saturation:30"}, {'effect': "brightness:10"}])
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
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "brightness:30"}, {'effect': "blackwhite:39"}])
        
        silhouette_view = SilhouettePanel(self.username)
        
        embed_transformed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Silhouette black edition: {self.username}',
            description='You can change the color alike the /color_silhouette command, Try it! 🌟'
        )
        embed_transformed.set_image(url=image_transform)
        await interaction.response.send_message(embed=embed_transformed, view=silhouette_view)
        