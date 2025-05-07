"""
  Silhouete styling for images
"""

import asyncio

from datetime import datetime
from discord import Embed, ButtonStyle, Interaction, Color
from discord.ui import View, button as discord_button, Button
from cloudinary import CloudinaryImage
from modules.module import Link


def colorify(color: str, strength: int = 39) -> list:
    '''
    Return a list with the transformation Parameters
    * {color: str} in Hexadecimal
    '''
    return [
        {
            'effect': f"blackwhite:{strength}"
        },
        {
            'color': f"{color}", 'effect': "colorize:50"
        },
        {
            'effect': "brightness:30"
        }
    ]


embed_transformed = Embed(timestamp=datetime.utcnow())
embed_transformed.title = 'Silhouette {color} edition! By Cloudinary 🌟'


class SilhouettePanel(View):
    """
      Main class for panel of silhouette intereactions
    """

    def __init__(self, username):
        super().__init__()
        self.username = username

    @discord_button(label='Purple', row=1)
    async def purple_sil(self, interaction: Interaction, button: Button):
        button.style = ButtonStyle.primary
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=colorify("#7038A1"))
        download_link = Link()
        embed_transformed.title.format(color='Purple')

        download_link.add_item(Button(label='Download Now',
                                      style=ButtonStyle.url,
                                      url=image_transform,
                                      emoji="<a:vibing:747680206734622740>"))
        embed_transformed.set_image(url=image_transform)
        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    @discord_button(label='Yellow', row=1)
    async def yellow_sil(self, interaction: Interaction, button: Button):
        button.style = ButtonStyle.primary
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=colorify("#FFF900"))
        download_link = Link()

        embed_transformed.title = 'Silhouette Yellow edition! By Cloudinary 🌟'

        download_link.add_item(Button(label='Download Now',
                                      style=ButtonStyle.url,
                                      url=image_transform,
                                      emoji="<a:vibing:747680206734622740>"))
        embed_transformed.set_image(url=image_transform)
        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    @discord_button(label='Red', row=1)
    async def red_sil(self, interaction: Interaction, button: Button):
        button.style = ButtonStyle.primary
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=colorify("#CF2C2C"))
        download_link = Link()

        embed_transformed.title = 'Silhouette Red edition! By Cloudinary 🌟'

        download_link.add_item(Button(label='Download Now', style=ButtonStyle.url,
                               url=image_transform, emoji="<a:vibing:747680206734622740>"))
        embed_transformed.set_image(url=image_transform)
        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    @discord_button(label='Lime', row=1)
    async def lime_sil(self, interaction: Interaction, button: Button):
        button.style = ButtonStyle.primary
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=colorify("#5EA031"))
        download_link = Link()

        embed_transformed.title = 'Silhouette Lime edition! By Cloudinary 🌟'

        download_link.add_item(Button(label='Download Now', style=ButtonStyle.url,
                               url=image_transform, emoji="<a:vibing:747680206734622740>"))
        embed_transformed.set_image(url=image_transform)
        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    @discord_button(label='Green', row=2)
    async def green_sil(self, interaction: Interaction, button: Button):
        button.style = ButtonStyle.primary
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=colorify('#0B7E30'))
        download_link = Link()

        embed_transformed.title = 'Silhouette Green edition! By Cloudinary 🌟'

        embed_transformed.set_image(url=image_transform)

        download_link.add_item(Button(label='Download Now', style=ButtonStyle.url,
                               url=image_transform, emoji="<a:vibing:747680206734622740>"))

        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    @discord_button(label='Cyan', row=2)
    async def cyan_sil(self, interaction: Interaction, button: Button):
        button.style = ButtonStyle.primary
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=colorify('#39C0B5'))
        download_link = Link()

        embed_transformed.title = 'Silhouette Cyan edition! By Cloudinary 🌟'

        download_link.add_item(Button(label='Download Now', style=ButtonStyle.url,
                               url=image_transform, emoji="<a:vibing:747680206734622740>"))

        embed_transformed.set_image(url=image_transform)

        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    @discord_button(label='Pink', row=2)
    async def pink_sil(self, interaction: Interaction, button: Button):
        button.style = ButtonStyle.primary
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=colorify('#D867B4'))
        download_link = Link()

        embed_transformed.title = 'Silhouette Pink edition! By Cloudinary 🌟'

        download_link.add_item(Button(label='Download Now', style=ButtonStyle.url,
                               url=image_transform, emoji="<a:vibing:747680206734622740>"))

        embed_transformed.set_image(url=image_transform)

        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    @discord_button(label='Wine', row=2)
    async def wine_sil(self, interaction: Interaction, button: Button):
        button.style = ButtonStyle.primary
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=colorify('#862044'))
        download_link = Link()

        embed_transformed.title = 'Silhouette Wine edition! By Cloudinary 🌟'

        download_link.add_item(Button(label='Download Now', style=ButtonStyle.url,
                               url=image_transform, emoji="<a:vibing:747680206734622740>"))

        embed_transformed.set_image(url=image_transform)

        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    async def blue_sil(self, interaction: Interaction, button: Button):
        """Blue silhouette"""
        button.label = 'Blue'
        button.style = ButtonStyle.primary
        button.row = 3
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=colorify('#09f'))
        download_link = Link()

        embed_transformed.title = 'Silhouette Blue edition! By Cloudinary 🌟'

        download_link.add_item(Button(label='Download Now', style=ButtonStyle.url,
                               url=image_transform, emoji="<a:vibing:747680206734622740>"))

        embed_transformed.set_image(url=image_transform)

        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    @discord_button(label='Azure', row=3)
    async def azure_sil(self, interaction: Interaction, button: Button):
        button.style = ButtonStyle.primary
        image_transform = CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=colorify('#888'))
        download_link = Link()

        embed_transformed.title = 'Silhouette Azure edition! By Cloudinary 🌟'

        download_link.add_item(Button(label='Download Now', style=ButtonStyle.url,
                               url=image_transform, emoji="<a:vibing:747680206734622740>"))

        embed_transformed.set_image(url=image_transform)

        await interaction.response.edit_message(embed=embed_transformed, view=download_link)


class Silhouette(View):
    """
      Panel for silhouette transform
    """

    def __init__(self, file_name, choice_color, strength):
        super().__init__()
        self.file_name = file_name
        self.choice_color = choice_color
        self.strength = strength

    @discord_button(label='Transform! ✨', style=ButtonStyle.blurple)
    async def colorful_model(self, interaction: Interaction, button: Button):
        button.style = ButtonStyle.blurple
        link_view = Link()
        embed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='''Colorful picture Powered by Cloudinary 🎉✨
                           **Note:** Its works Better with a person picture 
                           or with a solid color background or transparent background
            ''',
            color=Color.random(),
        )
        image_tag = CloudinaryImage(
            f"Bot/{self.file_name}.png"
        ).build_url(transformation=[
            {'effect': f"blackwhite:{self.strength}"},
            {'color': self.choice_color, 'effect': "colorize:50"},
            {'effect': "brightness:30"}, {'quality': "auto"}])
        embed.set_image(url=image_tag)
        link_view.add_item(Button(label='Download ✨',
                                  style=ButtonStyle.url,
                                  url=image_tag,
                                  emoji="<a:vibing:747680206734622740>"))
        await interaction.response.send_message(embed=embed, view=link_view)


class TwoSilhouette(View):
    """
      Panel for silhouette transform
    """

    def __init__(self, file_name, choice_color, choice_color_2, width, strength):
        super().__init__()
        self.file_name = file_name
        self.choice_color = choice_color
        self.choice_color_2 = choice_color_2
        self.width = width
        self.strength = strength

    @discord_button(label='Transform! ✨', style=ButtonStyle.blurple)
    async def colorful_model(self, interaction: Interaction, button: Button):
        button.style = ButtonStyle.blurple
        link_view = Link()
        embed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='''Colorful picture Powered by Cloudinary 🎉✨
                           **Note:** Its works Better with a person picture 
                           or with a solid color background or transparent background
            ''',
            color=Color.random(),
        )
        image_tag = CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(transformation=[
                {'gravity': "west", 'height': "1.0",
                    'width': "0.5", 'crop': "crop"},
                {'effect': f"blackwhite:{self.strength}"},
                {'color': self.choice_color, 'effect': "colorize:50"},
                {'effect': "brightness:30"},
                {'overlay': f"Bot:{self.file_name}.png"},
                {'gravity': "east", 'height': "1.0",
                    'width': "0.5", 'crop': "crop"},
                {'effect': f"blackwhite:{self.strength}"},
                {'color': self.choice_color_2, 'effect': "colorize:30"},
                {'effect': "brightness:30"},
                {'flags': "layer_apply", 'gravity': "east",
                    'x': f'-{(self.width/2)}'}
            ])
        await asyncio.sleep(0.8)
        embed.set_image(url=image_tag)
        link_view.add_item(Button(label='Download ✨',
                                  style=ButtonStyle.url,
                                  url=image_tag,
                                  emoji="<a:vibing:747680206734622740>"))
        await interaction.response.send_message(embed=embed, view=link_view)
