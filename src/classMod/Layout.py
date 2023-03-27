import asyncio

from discord.ui import View, button, Button
from cloudinary import CloudinaryImage

from discord import ButtonStyle, Color, Embed, Interaction
from modules.module import Link

from datetime import datetime

class LayoutFor(View):
    def __init__(self, user_name, pfp_drag, banner_drag, pfpsize, bannersize):
        super().__init__()
        self.user_name = user_name
        self.pfp_drag = pfp_drag
        self.banner_drag = banner_drag
        self.pfpsize = pfpsize
        self.bannersize = bannersize

    @button(label='Facebook! ✨', style=ButtonStyle.primary, row=1)
    async def facebook_layout(self, interaction: Interaction, button: Button):
        download_view = Link()
        embed_layout = Embed(
            timestamp=datetime.utcnow(),
            title='Facebook Layout Powered By Cloudinary ✨',
            description='By clicking in the Download Button, You will see the Image With the size perfectly for the social media, for avatar and for banner individually',
            color=Color.random()
        )
        banner_result = CloudinaryImage(
            f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
                {'gravity': "auto", 'height': 315, 'width': 851, 'crop': "thumb"}]
        )
        av_result = CloudinaryImage(f"UsersLayout/{self.user_name}_av{self.pfpsize}").build_url(transformation=[
            {'gravity': "auto:face", 'height': 360,
                'width': 360, 'zoom': "0.2", 'crop': "thumb"},
            {'radius': "max"}]
        )
        await asyncio.sleep(1)
        layout_shown = CloudinaryImage(
            f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
                {'gravity': "auto", 'height': 315, 'width': 851, 'crop': "thumb"},
                {'quality': "auto"},
                {'overlay': f"UsersLayout:{self.user_name}_av{self.pfpsize}"},
                {'gravity': "auto:face", 'height': 120,
                    'width': 120, 'zoom': "0.2", 'crop': "thumb"},
                {'radius': "max"}, {'quality': "auto"},
                {'flags': "layer_apply", 'gravity': "south_west", 'x': 20, 'y': 11},
                {'overlay': "Layouts:facebook-layout"},
                {'gravity': "south", 'height': 315, 'width': 851, 'crop': "thumb"},
                {'quality': "auto"},
                {'flags': "layer_apply", 'gravity': "south"},
                {'color': "#F5F5F5", 'overlay': {'font_family': "arial", 'font_size': 36,
                                                 'font_weight': "bold", 'text_align': "left", 'text': f"{self.user_name}"}}, {'quality': "auto"},
                {'flags': "layer_apply", 'gravity': "south_west", 'x': 160, 'y': 46}
            ])
        print(layout_shown)
        await asyncio.sleep(1)
        embed_layout.set_image(url=layout_shown)
        download_view.add_item(Button(label='Download Banner ✨',
                                                 style=ButtonStyle.url, url=banner_result))
        download_view.add_item(Button(label='Download Avatar ✨',
                                                 style=ButtonStyle.url, url=av_result))
        await interaction.response.send_message(view=download_view, embed=embed_layout)

    @button(label='Linkedin! ✨', style=ButtonStyle.primary, row=1)
    async def linkedin_layout(self, interaction: Interaction, button: Button):
        print(interaction.user.name)
        print(self.user_name)
        download_view = Link()
        embed_layout = Embed(
            timestamp=datetime.utcnow(),
            title='Linkedin Layout Powered By Cloudinary ✨',
            description='By clicking in the Download Button, You will see the Image With the size perfectly for the social media, for avatar and for banner individually',
            color=Color.random()
        )
        banner_result = CloudinaryImage(
            f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
                {'gravity': "auto", 'height': 800, 'width': 2000, 'crop': "thumb"}]
        )
        av_result = CloudinaryImage(f"UsersLayout/{self.user_name}_av{self.pfpsize}").build_url(transformation=[
            {'gravity': "auto:face", 'height': 360,
                'width': 360, 'zoom': "0.5", 'crop': "thumb"},
            {'radius': "max"}]
        )
        await asyncio.sleep(1)
        layout_shown = CloudinaryImage(f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
            {'gravity': "auto", 'height': 800, 'width': 2000,
                'crop': "thumb"}, {'quality': "auto"},
            {'overlay': f"UsersLayout:{self.user_name}_av{self.pfpsize}"},
            {'gravity': "auto:face", 'height': 400,
                'width': 400, 'zoom': "0.5", 'crop': "thumb"},
            {'radius': "max"}, {'quality': "auto"},
            {'flags': "layer_apply", 'gravity': "west", 'x': 62, 'y': 80},
            {'overlay': "Layouts:linkedin-layout"},
            {'gravity': "north", 'height': 800, 'width': 2000, 'crop': "thumb"},
            {'quality': "auto"},
            {'flags': "layer_apply", 'gravity': "south"},
            {'color': "#000000", 'overlay': {'font_family': "arial", 'font_size': 72,
                                             'text_align': "left", 'text': f"{self.user_name}"}}, {'quality': "auto"},
            {'flags': "layer_apply", 'gravity': "west", 'x': 120, 'y': 320}
        ])
        print(layout_shown)
        await asyncio.sleep(1)
        embed_layout.set_image(url=layout_shown)
        download_view.add_item(Button(label='Download Banner ✨',
                                                 style=ButtonStyle.url, url=banner_result))
        download_view.add_item(Button(label='Download Avatar ✨',
                                                 style=ButtonStyle.url, url=av_result))
        await interaction.response.send_message(view=download_view, embed=embed_layout)

    @button(label='Twitter! ✨', style=ButtonStyle.primary, row=1)
    async def twitter_layout(self, interaction: Interaction, button: Button):
        download_view = Link()
        embed_layout = Embed(
            timestamp=datetime.utcnow(),
            title='Twitter Layout Powered By Cloudinary ✨',
            description='By clicking in the Download Button, You will see the Image With the size perfectly for the social media, for avatar and for banner individually',
            color=Color.random()
        )
        banner_result = CloudinaryImage(
            f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
                {'gravity': "auto", 'height': 500, 'width': 1500, 'crop': "thumb"}]
        )
        av_result = CloudinaryImage(f"UsersLayout/{self.user_name}_av{self.pfpsize}").build_url(transformation=[
            {'gravity': "auto:face", 'height': 360,
                'width': 360, 'zoom': "0.5", 'crop': "thumb"},
            {'radius': "max"}]
        )
        await asyncio.sleep(1)
        layout_shown = CloudinaryImage(f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
            {'gravity': "auto:face", 'height': 500,
                'width': 1500, 'crop': "thumb"}, {'quality': "auto"},
            {'overlay': f"UsersLayout:{self.user_name}_av{self.pfpsize}"},
            {'gravity': "auto:face", 'height': 280,
                'width': 280, 'zoom': "0.5", 'crop': "thumb"},
            {'radius': "max"},
            {'flags': "layer_apply", 'gravity': "west", 'x': 60, 'y': 65},
            {'quality': "auto"},
            {'overlay': "Layouts:twitter-layout"},
            {'gravity': "south", 'height': 500, 'width': 1500, 'crop': "thumb"},
            {'quality': "auto"},
            {'flags': "layer_apply", 'gravity': "south"}
        ])
        print(layout_shown)
        await asyncio.sleep(1)
        embed_layout.set_image(url=layout_shown)
        download_view.add_item(Button(label='Download Banner ✨',
                                                 style=ButtonStyle.url, url=banner_result))
        download_view.add_item(Button(label='Download Avatar ✨',
                                                 style=ButtonStyle.url, url=av_result))
        await interaction.response.send_message(view=download_view, embed=embed_layout)

    @button(label='Discord! ✨', style=ButtonStyle.primary, row=1)
    async def discord_layout(self, interaction: Interaction, button: Button):
        download_view = Link()
        embed_layout = Embed(
            timestamp=datetime.utcnow(),
            title='Discord Layout Powered By Cloudinary ✨',
            description='By clicking in the Download Button, You will see the Image With the size perfectly for the social media, for avatar and for banner individually',
            color=Color.random()
        )
        banner_result = CloudinaryImage(
            f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
                {'gravity': "auto", 'height': 240, 'width': 680, 'crop': "thumb"}]
        )
        av_result = CloudinaryImage(f"UsersLayout/{self.user_name}_av{self.pfpsize}").build_url(transformation=[
            {'gravity': "auto:face", 'height': 240,
                'width': 240, 'zoom': "0.2", 'crop': "thumb"},
            {'radius': "max"}]
        )
        await asyncio.sleep(1)
        layout_shown = CloudinaryImage(f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
            {'gravity': "auto:face", 'height': 226, 'width': 340,
                'crop': "thumb"}, {'quality': "auto"},
            {'overlay': f"UsersLayout:{self.user_name}_av{self.pfpsize}"},
            {'gravity': "auto:face", 'height': 90,
                'width': 90, 'zoom': "0.2", 'crop': "thumb"},
            {'radius': "max"}, {'quality': "auto"},
            {'flags': "layer_apply", 'gravity': "west", 'x': 13},
            {'overlay': "Layouts:Discord-Layout"}, {'quality': "auto"},
            {'flags': "layer_apply", 'gravity': "south", 'zoom': "0.5"},
            {'color': "#F5F5F5", 'overlay': {'font_family': "arial", 'font_size': 24,
                                             'font_weight': "bold", 'text_align': "left", 'text': f"{self.user_name}"}}, {'quality': "auto"},
            {'flags': "layer_apply", 'gravity': "south_west", 'x': 35, 'y': 18}
        ])
        print(layout_shown)
        await asyncio.sleep(1)
        embed_layout.set_image(url=layout_shown)
        download_view.add_item(Button(label='Download Banner ✨',
                                                 style=ButtonStyle.url, url=banner_result))
        download_view.add_item(Button(label='Download Avatar ✨',
                                                 style=ButtonStyle.url, url=av_result))
        await interaction.response.send_message(view=download_view, embed=embed_layout)