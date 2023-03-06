import discord
import cloudinary
import asyncio
import datetime

from modules.module import Link, Force, ForceDisabled

from discord import Interaction


class SilhouettePanel(discord.ui.View):
    def __init__(self, username):
        super().__init__()
        self.username = username

    @discord.ui.button(label='Purple', style=discord.ButtonStyle.primary, row=1)
    async def purple_sil(self, interaction: discord.Interaction, button: discord.ui.Button):
        image_transform = cloudinary.CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "blackwhite:50"}, {'color': "#7038A1", 'effect': "colorize:50"}, {'effect': "brightness:30"}])
        download_link = Link()
        embed_transformed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Silhouette purple edition! By Cloudinary 🌟',
        )
        download_link.add_item(discord.ui.Button(label='Download Transformed',
                                                 style=discord.ButtonStyle.url, url=image_transform))
        embed_transformed.set_image(url=image_transform)
        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    @discord.ui.button(label='Yellow', style=discord.ButtonStyle.primary, row=1)
    async def yellow_sil(self, interaction: discord.Interaction, button: discord.ui.Button):
        image_transform = cloudinary.CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "blackwhite:50"}, {'color': "#9C9342", 'effect': "colorize:50"}, {'effect': "brightness:30"}])
        download_link = Link()
        embed_transformed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Silhouette purple edition! By Cloudinary 🌟',
        )
        download_link.add_item(discord.ui.Button(label='Download Transformed',
                                                 style=discord.ButtonStyle.url, url=image_transform))
        embed_transformed.set_image(url=image_transform)
        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    @discord.ui.button(label='Red', style=discord.ButtonStyle.primary, row=1)
    async def red_sil(self, interaction: discord.Interaction, button: discord.ui.Button):
        image_transform = cloudinary.CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "blackwhite:50"}, {'color': "#CF2C2C", 'effect': "colorize:50"}, {'effect': "brightness:30"}])
        download_link = Link()
        embed_transformed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Silhouette purple edition! By Cloudinary 🌟',
        )
        download_link.add_item(discord.ui.Button(label='Download Transformed',
                                                 style=discord.ButtonStyle.url, url=image_transform))
        embed_transformed.set_image(url=image_transform)
        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    @discord.ui.button(label='Lime', style=discord.ButtonStyle.primary, row=1)
    async def lime_sil(self, interaction: discord.Interaction, button: discord.ui.Button):
        image_transform = cloudinary.CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "blackwhite:50"}, {'color': "#5EA031", 'effect': "colorize:50"}, {'effect': "brightness:30"}])
        download_link = Link()
        embed_transformed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Silhouette purple edition! By Cloudinary 🌟',
        )
        download_link.add_item(discord.ui.Button(label='Download Transformed',
                                                 style=discord.ButtonStyle.url, url=image_transform))
        embed_transformed.set_image(url=image_transform)
        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    @discord.ui.button(label='Green', style=discord.ButtonStyle.primary, row=2)
    async def green_sil(self, interaction: discord.Interaction, button: discord.ui.Button):
        image_transform = cloudinary.CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "blackwhite:50"}, {'color': "#0B7E29", 'effect': "colorize:50"}, {'effect': "brightness:30"}])
        download_link = Link()
        embed_transformed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Silhouette purple edition! By Cloudinary 🌟',
        )
        download_link.add_item(discord.ui.Button(label='Download Transformed',
                                                 style=discord.ButtonStyle.url, url=image_transform))
        embed_transformed.set_image(url=image_transform)
        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    @discord.ui.button(label='Cyan', style=discord.ButtonStyle.primary, row=2)
    async def cyan_sil(self, interaction: discord.Interaction, button: discord.ui.Button):
        image_transform = cloudinary.CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "blackwhite:50"}, {'color': "#39C0B5", 'effect': "colorize:50"}, {'effect': "brightness:30"}])
        download_link = Link()
        embed_transformed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Silhouette purple edition! By Cloudinary 🌟',
        )
        download_link.add_item(discord.ui.Button(label='Download Transformed',
                                                 style=discord.ButtonStyle.url, url=image_transform))
        embed_transformed.set_image(url=image_transform)
        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    @discord.ui.button(label='Pink', style=discord.ButtonStyle.primary, row=2)
    async def pink_sil(self, interaction: discord.Interaction, button: discord.ui.Button):
        image_transform = cloudinary.CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "blackwhite:50"}, {'color': "#D867B4", 'effect': "colorize:50"}, {'effect': "brightness:30"}])
        download_link = Link()
        embed_transformed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Silhouette purple edition! By Cloudinary 🌟',
        )
        download_link.add_item(discord.ui.Button(label='Download Transformed',
                                                 style=discord.ButtonStyle.url, url=image_transform))
        embed_transformed.set_image(url=image_transform)
        await interaction.response.edit_message(embed=embed_transformed, view=download_link)

    @discord.ui.button(label='Wine', style=discord.ButtonStyle.primary, row=2)
    async def wine_sil(self, interaction: discord.Interaction, button: discord.ui.Button):
        image_transform = cloudinary.CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "blackwhite:50"}, {'color': "#862044", 'effect': "colorize:50"}, {'effect': "brightness:30"}])
        download_link = Link()
        embed_transformed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Silhouette purple edition! By Cloudinary 🌟',
        )
        download_link.add_item(discord.ui.Button(label='Download Transformed',
                                                 style=discord.ButtonStyle.url, url=image_transform))
        embed_transformed.set_image(url=image_transform)
        await interaction.response.edit_message(embed=embed_transformed, view=download_link)


class TransformAvView(discord.ui.View):
    #! Huge Class!!!!!
    def __init__(self, username):
        super().__init__()
        self.username = username

    # ? Row Button = 1
    @discord.ui.button(label='Whitify Avatar', style=discord.ButtonStyle.primary, row=1)
    async def Whitify_av(self, interaction: discord.Interaction, button: discord.ui.Button):
        download_link = Link()
        image_transform = cloudinary.CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "contrast:30"}, {'effect': "saturation:-30"}, {'effect': "brightness:30"}])
        embed_transformed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Here is it {self.username}'
        )
        embed_transformed.set_image(url=image_transform)
        download_link.add_item(discord.ui.Button(label='Download Transformed',
                                                 style=discord.ButtonStyle.url, url=image_transform))
        await interaction.response.send_message(embed=embed_transformed, view=download_link)

    @discord.ui.button(label='High Contrast', style=discord.ButtonStyle.primary, row=1)
    async def High_contrast_av(self, interaction: discord.Interaction, button: discord.ui.Button):
        download_link = Link()
        image_transform = cloudinary.CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "contrast:50"}, {'effect': "saturation:-40"}])
        embed_transformed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Here is it {self.username}'
        )
        embed_transformed.set_image(url=image_transform)
        download_link.add_item(discord.ui.Button(label='Download Transformed',
                                                 style=discord.ButtonStyle.url, url=image_transform))
        await interaction.response.send_message(embed=embed_transformed, view=download_link)

    @discord.ui.button(label='Sepia', style=discord.ButtonStyle.primary, row=1)
    async def Sepia_effect_av(self, interaction: discord.Interaction, button: discord.ui.Button):
        download_link = Link()
        image_transform = cloudinary.CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(effect="sepia")
        embed_transformed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Here is it {self.username}'
        )
        embed_transformed.set_image(url=image_transform)
        download_link.add_item(discord.ui.Button(label='Download Transformed',
                                                 style=discord.ButtonStyle.url, url=image_transform))
        await interaction.response.send_message(embed=embed_transformed, view=download_link)

    # ? Row Button = 2
    @discord.ui.button(label='Black and White', style=discord.ButtonStyle.primary, row=2)
    async def Black_and_white_effect_av(self, interaction: discord.Interaction, button: discord.ui.Button):
        download_link = Link()
        image_transform = cloudinary.CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "grayscale"}])
        embed_transformed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Here is it {self.username}'
        )
        embed_transformed.set_image(url=image_transform)
        download_link.add_item(discord.ui.Button(label='Download Transformed',
                                                 style=discord.ButtonStyle.url, url=image_transform))
        await interaction.response.send_message(embed=embed_transformed, view=download_link)

    @discord.ui.button(label='Colorful Avatar', style=discord.ButtonStyle.primary, row=2)
    async def Colorful_effect_av(self, interaction: discord.Interaction, button: discord.ui.Button):
        download_link = Link()
        image_transform = cloudinary.CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "contrast:30"}, {'effect': "saturation:30"}, {'effect': "brightness:10"}])
        embed_transformed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Here is it {self.username}'
        )
        embed_transformed.set_image(url=image_transform)
        download_link.add_item(discord.ui.Button(label='Download Transformed',
                                                 style=discord.ButtonStyle.url, url=image_transform))
        await interaction.response.send_message(embed=embed_transformed, view=download_link)

    @discord.ui.button(label='Silhouette Avatar', style=discord.ButtonStyle.primary, row=2)
    async def Silhouette_panel(self, interaction: discord.Interaction, button: discord.ui.Button):
        image_transform = cloudinary.CloudinaryImage(
            f'Bot/{self.username}q:av_up').build_url(transformation=[{'effect': "brightness:30"}, {'effect': "blackwhite:50"}])
        silhouette_view = SilhouettePanel(self.username)
        embed_transformed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Silhouette black edition: {self.username}',
            description='You can change the color alike the /color_silhouette command, Try it! 🌟'
        )
        embed_transformed.set_image(url=image_transform)
        await interaction.response.send_message(embed=embed_transformed, view=silhouette_view)


class AvView(discord.ui.View):
    '''
    View Pannel for the Avatar Transformation
    Button Steps Function for create Transformation in the Avatar
    '''

    def __init__(self, name):
        super().__init__()
        self.name = name

    @discord.ui.button(label='Yes! transform it ✨', style=discord.ButtonStyle.primary)
    async def av_select_transform(self, interaction: Interaction, button: discord.ui.Button):
        av_username = self.name
        transformation_view = TransformAvView(av_username)
        try:
            print(av_username)
            embed_prev_img = discord.Embed(
                timestamp=datetime.datetime.utcnow(),
                title=f'Prepare to transform Your Avatar {av_username}',
                description='Select any options and see inmediately results'
            )
            image_transform = cloudinary.CloudinaryImage(
                f'Bot/{av_username}q:av_up').build_url(transformation=[{'effect': "blur:1500"}])
            embed_prev_img.set_image(url=image_transform)

            await interaction.response.send_message(embed=embed_prev_img, view=transformation_view)

        except:
            print("exception error: Command Not Found")
            await interaction.response.send_message(content='Command not Found, Please Try Again in a few seconds')


class BlackAndWhite(discord.ui.View):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    @discord.ui.button(label='Transform! ✨', style=discord.ButtonStyle.blurple)
    async def b_and_w(self, interaction: discord.Interaction, button: discord.ui.Button):
        link_view = Link()
        embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='B&W Effect Powered by Cloudinary 🎉✨',
            color=discord.Color.random(),
        )
        image_tag = cloudinary.CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(effect="grayscale")
        embed.set_image(url=image_tag)
        link_view.add_item(discord.ui.Button(label='Download ✨',
                                             style=discord.ButtonStyle.url, url=image_tag, emoji="<a:vibing:747680206734622740>"))
        await interaction.response.send_message(embed=embed, view=link_view)


class EmojiSizing(discord.ui.View):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    @discord.ui.button(label='Transform! ✨', style=discord.ButtonStyle.blurple)
    async def emoji_sizing(self, interaction: discord.Interaction, button: discord.ui.Button):
        link_view = Link()
        embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='''
                          Improved picture Powered by Cloudinary 🎉✨,
                          Now its can be use perfect for an emoji in discord
                        ''',
            color=discord.Color.random(),
        )
        image_tag = cloudinary.CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(transformation=[{'effect': "improve:indoor:50"}, {'gravity': "auto:face", 'height': 128, 'width': 128, 'crop': "lfill"}])
        embed.set_image(url=image_tag)
        link_view.add_item(discord.ui.Button(label='Download ✨',
                                             style=discord.ButtonStyle.url, url=image_tag, emoji="<a:vibing:747680206734622740>"))
        await interaction.response.send_message(embed=embed, view=link_view)


class SepiaEffect(discord.ui.View):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    @discord.ui.button(label='Transform! ✨', style=discord.ButtonStyle.blurple)
    async def sepia_effect(self, interaction: discord.Interaction, button: discord.ui.Button):
        link_view = Link()
        embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='Sepia Effect Powered by Cloudinary 🎉✨',
            color=discord.Color.random(),
        )
        image_tag = cloudinary.CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(effect="sepia")
        embed.set_image(url=image_tag)
        link_view.add_item(discord.ui.Button(label='Download',
                                             style=discord.ButtonStyle.url, url=image_tag, emoji="<a:vibing:747680206734622740>"))
        await interaction.response.send_message(embed=embed, view=link_view)


class HighContrast(discord.ui.View):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    @discord.ui.button(label='Transform! ✨', style=discord.ButtonStyle.blurple)
    async def high_contrast_model(self, interaction: discord.Interaction, button: discord.ui.Button):
        link_view = Link()
        embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='Contrast Improved Powered by Cloudinary 🎉✨',
            color=discord.Color.random(),
        )
        image_tag = cloudinary.CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(transformation=[{'effect': "contrast:50"}, {'effect': "saturation:-40"}])
        embed.set_image(url=image_tag)
        link_view.add_item(discord.ui.Button(label='Download ✨',
                                             style=discord.ButtonStyle.url, url=image_tag))
        await interaction.response.send_message(embed=embed, view=link_view)


class WhiteColor(discord.ui.View):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    @discord.ui.button(label='Transform! ✨', style=discord.ButtonStyle.blurple)
    async def white_color_model(self, interaction: discord.Interaction, button: discord.ui.Button):
        link_view = Link()
        embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='White Color Effect Powered by Cloudinary 🎉✨',
            color=discord.Color.random(),
        )
        image_tag = cloudinary.CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(transformation=[{'effect': "contrast:30"}, {'effect': "saturation:-30"}, {'effect': "brightness:30"}])
        embed.set_image(url=image_tag)
        link_view.add_item(discord.ui.Button(label='Download ✨',
                                             style=discord.ButtonStyle.url, url=image_tag))
        await interaction.response.send_message(embed=embed, view=link_view)


class ColorFul(discord.ui.View):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    @discord.ui.button(label='Transform! ✨', style=discord.ButtonStyle.blurple)
    async def colorful_model(self, interaction: discord.Interaction, button: discord.ui.Button):
        link_view = Link()
        embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='Colorful picture Powered by Cloudinary 🎉✨',
            color=discord.Color.random(),
        )
        image_tag = cloudinary.CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(transformation=[{'effect': "contrast:30"}, {'effect': "saturation:30"}, {'effect': "brightness:10"}])
        embed.set_image(url=image_tag)
        link_view.add_item(discord.ui.Button(label='Download ✨',
                                             style=discord.ButtonStyle.url, url=image_tag))
        await interaction.response.send_message(embed=embed, view=link_view)


class Cartoonify(discord.ui.View):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    @discord.ui.button(label='Transform! ✨', style=discord.ButtonStyle.blurple)
    async def cartoon_model(self, interaction: discord.Interaction, button: discord.ui.Button):
        link_view = Link()
        embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='Cartonify picture Powered by Cloudinary 🎉✨',
            color=discord.Color.random(),
        )
        image_tag = cloudinary.CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(transformation=[{'effect': "contrast:-30"}, {'effect': "cartoonify"}, {'effect': "saturation:-30"}, {'effect': "brightness:10"}, {'effect': "improve:outdoor:50"}])
        embed.set_image(url=image_tag)
        link_view.add_item(discord.ui.Button(label='Download ✨',
                                             style=discord.ButtonStyle.url, url=image_tag))
        await interaction.response.send_message(embed=embed, view=link_view)


class ColorBurn(discord.ui.View):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    @discord.ui.button(label='Transform! ✨', style=discord.ButtonStyle.blurple)
    async def burn_model(self, interaction: discord.Interaction, button: discord.ui.Button):
        link_view = Link()
        embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='Burning picture Powered by Cloudinary 🎉✨',
            color=discord.Color.random(),
        )
        image_tag = cloudinary.CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(effect="art:zorro")
        embed.set_image(url=image_tag)
        link_view.add_item(discord.ui.Button(label='Download ✨',
                                             style=discord.ButtonStyle.url, url=image_tag))
        await interaction.response.send_message(embed=embed, view=link_view)


class BgRemoval(discord.ui.View):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    @discord.ui.button(label='Transform! ✨', style=discord.ButtonStyle.blurple)
    async def bg_removal_model(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='''We are Processing the transformation, Please Wait...''',
            color=discord.Color.random(),
        )
        image_tag = cloudinary.CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(transformation=[{'effect': "background_removal"}])
        image_blur = cloudinary.CloudinaryImage(
            f"bot/{self.file_name}.png").build_url(transformation=[{'effect': "blur:1500"}])
        ephemeral_view = ForceDisabled()
        link_view = Link() and Force(image_tag)
        embed.set_image(url=image_blur)
        new_embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f"The image is ready {interaction.user}",
            description="if You cannot see the image here its cause Discord Already cached it and might not render, but you can found the image by clicking in the download button"
        )
        new_embed.set_image(url=image_tag)
        link_view.add_item(discord.ui.Button(label='Download ✨',
                                             style=discord.ButtonStyle.url, url=image_tag))
        await interaction.response.send_message(embed=embed, view=ephemeral_view)
        await asyncio.sleep(50)
        await interaction.edit_original_response(embed=new_embed, view=link_view)
        await asyncio.sleep(29)
        await interaction.edit_original_response(embed=new_embed, view=link_view)


class Silhouette(discord.ui.View):
    def __init__(self, file_name, choice_color):
        super().__init__()
        self.file_name = file_name
        self.choice_color = choice_color

    @discord.ui.button(label='Transform! ✨', style=discord.ButtonStyle.blurple)
    async def colorful_model(self, interaction: discord.Interaction, button: discord.ui.Button):
        link_view = Link()
        embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='''Colorful picture Powered by Cloudinary 🎉✨
                           **Note:** Its works Better with a person picture or with a solid color background or transparent background
            ''',
            color=discord.Color.random(),
        )
        image_tag = cloudinary.CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(transformation=[{'effect': "blackwhite:39"}, {'color': self.choice_color, 'effect': "colorize:50"}, {'effect': "brightness:30"}])
        embed.set_image(url=image_tag)
        link_view.add_item(discord.ui.Button(label='Download ✨',
                                             style=discord.ButtonStyle.url, url=image_tag))
        await interaction.response.send_message(embed=embed, view=link_view)


class TwoSilhouette(discord.ui.View):
    def __init__(self, file_name, choice_color, choice_color_2, width):
        super().__init__()
        self.file_name = file_name
        self.choice_color = choice_color
        self.choice_color_2 = choice_color_2
        self.width = width

    @discord.ui.button(label='Transform! ✨', style=discord.ButtonStyle.blurple)
    async def colorful_model(self, interaction: discord.Interaction, button: discord.ui.Button):
        link_view = Link()
        embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='''Colorful picture Powered by Cloudinary 🎉✨
                           **Note:** Its works Better with a person picture or with a solid color background or transparent background
            ''',
            color=discord.Color.random(),
        )
        image_tag = cloudinary.CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(transformation=[
                {'gravity': "west", 'height': "1.0",
                    'width': "0.5", 'crop': "crop"},
                {'effect': "blackwhite:39"},
                {'color': self.choice_color, 'effect': "colorize:50"},
                {'effect': "brightness:30"},
                {'overlay': f"Bot:{self.file_name}.png"},
                {'gravity': "east", 'height': "1.0",
                    'width': "0.5", 'crop': "crop"},
                {'effect': "blackwhite:39"},
                {'color': self.choice_color_2, 'effect': "colorize:30"},
                {'effect': "brightness:29"},
                {'flags': "layer_apply", 'gravity': "east",
                    'x': -(self.width/2)}
            ])
        embed.set_image(url=image_tag)
        link_view.add_item(discord.ui.Button(label='Download ✨',
                                             style=discord.ButtonStyle.url, url=image_tag))
        await interaction.response.send_message(embed=embed, view=link_view)


class TextOverlay(discord.ui.View):
    def __init__(self, file_name, font, text, font_size, position, color, effect):
        super().__init__()
        self.file_name = file_name
        self.font = font
        self.text = text
        self.font_size = font_size
        self.position = position
        self.color = color
        self.effect = effect

    @discord.ui.button(label='Transform! ✨', style=discord.ButtonStyle.blurple)
    async def colorful_model(self, interaction: discord.Interaction, button: discord.ui.Button):
        link_view = Link()
        text_overlay = cloudinary.CloudinaryImage(
            f"Colors/Color_{self.color}_{self.effect}").build_url(overlay={'font_family': f'{self.font}', 'font_size': self.font_size, 'font_weight': "bold", 'text': f'{self.text}'.replace(" ", "%20")}, flags="cutter")
        embed = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='''Colorful picture Powered by Cloudinary 🎉✨''',
            color=discord.Color.random(),
        )
        print(text_overlay)
        await asyncio.sleep(2)
        image_tag = cloudinary.CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(transformation=[{'overlay': {'url': f'{text_overlay}'}}, {'flags': "layer_apply", 'gravity': self.position, 'y': 20, 'x': 10}])
        embed.set_image(url=image_tag)
        link_view.add_item(discord.ui.Button(label='Download ✨',
                                             style=discord.ButtonStyle.url, url=image_tag))
        await interaction.response.send_message(embed=embed, view=link_view)


class LayoutFor(discord.ui.View):
    def __init__(self, user_name, pfp_drag, banner_drag, pfpsize, bannersize):
        super().__init__()
        self.user_name = user_name
        self.pfp_drag = pfp_drag
        self.banner_drag = banner_drag
        self.pfpsize = pfpsize
        self.bannersize = bannersize

    @discord.ui.button(label='Facebook! ✨', style=discord.ButtonStyle.primary, row=1)
    async def facebook_layout(self, interaction: discord.Interaction, button: discord.ui.Button):
        download_view = Link()
        embed_layout = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title='Facebook Layout Powered By Cloudinary ✨',
            description='By clicking in the Download Button, You will see the Image With the size perfectly for the social media, for avatar and for banner individually',
            color=discord.Color.random()
        )
        banner_result = cloudinary.CloudinaryImage(
            f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
                {'gravity': "auto", 'height': 315, 'width': 851, 'crop': "thumb"}]
        )
        av_result = cloudinary.CloudinaryImage(f"UsersLayout/{self.user_name}_av{self.pfpsize}").build_url(transformation=[
            {'gravity': "auto:face", 'height': 360,
                'width': 360, 'zoom': "0.2", 'crop': "thumb"},
            {'radius': "max"}]
        )
        await asyncio.sleep(1)
        layout_shown = cloudinary.CloudinaryImage(
            f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
                {'gravity': "auto", 'height': 315, 'width': 851, 'crop': "thumb"},
                {'overlay': f"UsersLayout:{self.user_name}_av{self.pfpsize}"},
                {'gravity': "auto:face", 'height': 120,
                    'width': 120, 'zoom': "0.2", 'crop': "thumb"},
                {'radius': "max"},
                {'flags': "layer_apply", 'gravity': "south_west", 'x': 20, 'y': 11},
                {'overlay': "Layouts:facebook-layout"},
                {'gravity': "south", 'height': 315, 'width': 851, 'crop': "thumb"},
                {'flags': "layer_apply", 'gravity': "south"},
                {'color': "#F5F5F5", 'overlay': {'font_family': "arial", 'font_size': 36,
                                                 'font_weight': "bold", 'text_align': "left", 'text': f"{self.user_name}"}},
                {'flags': "layer_apply", 'gravity': "south_west", 'x': 160, 'y': 46}
            ])
        print(layout_shown)
        await asyncio.sleep(1)
        embed_layout.set_image(url=layout_shown)
        download_view.add_item(discord.ui.Button(label='Download Banner ✨',
                                                 style=discord.ButtonStyle.url, url=banner_result))
        download_view.add_item(discord.ui.Button(label='Download Avatar ✨',
                                                 style=discord.ButtonStyle.url, url=av_result))
        await interaction.response.send_message(view=download_view, embed=embed_layout)

    @discord.ui.button(label='Linkedin! ✨', style=discord.ButtonStyle.primary, row=1)
    async def linkedin_layout(self, interaction: discord.Interaction, button: discord.ui.Button):
        print(interaction.user.name)
        print(self.user_name)
        download_view = Link()
        embed_layout = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title='Linkedin Layout Powered By Cloudinary ✨',
            description='By clicking in the Download Button, You will see the Image With the size perfectly for the social media, for avatar and for banner individually',
            color=discord.Color.random()
        )
        banner_result = cloudinary.CloudinaryImage(
            f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
                {'gravity': "auto", 'height': 800, 'width': 2000, 'crop': "thumb"}]
        )
        av_result = cloudinary.CloudinaryImage(f"UsersLayout/{self.user_name}_av{self.pfpsize}").build_url(transformation=[
            {'gravity': "auto:face", 'height': 360,
                'width': 360, 'zoom': "0.5", 'crop': "thumb"},
            {'radius': "max"}]
        )
        await asyncio.sleep(1)
        layout_shown = cloudinary.CloudinaryImage(f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
            {'gravity': "auto", 'height': 800, 'width': 2000, 'crop': "thumb"},
            {'overlay': f"UsersLayout:{self.user_name}_av{self.pfpsize}"},
            {'gravity': "auto:face", 'height': 400,
                'width': 400, 'zoom': "0.5", 'crop': "thumb"},
            {'radius': "max"},
            {'flags': "layer_apply", 'gravity': "west", 'x': 62, 'y': 80},
            {'overlay': "Layouts:linkedin-layout"},
            {'gravity': "north", 'height': 800, 'width': 2000, 'crop': "thumb"},
            {'flags': "layer_apply", 'gravity': "south"},
            {'color': "#000000", 'overlay': {'font_family': "arial", 'font_size': 72,
                                             'text_align': "left", 'text': f"{self.user_name}"}},
            {'flags': "layer_apply", 'gravity': "west", 'x': 120, 'y': 320}
        ])
        print(layout_shown)
        await asyncio.sleep(1)
        embed_layout.set_image(url=layout_shown)
        download_view.add_item(discord.ui.Button(label='Download Banner ✨',
                                                 style=discord.ButtonStyle.url, url=banner_result))
        download_view.add_item(discord.ui.Button(label='Download Avatar ✨',
                                                 style=discord.ButtonStyle.url, url=av_result))
        await interaction.response.send_message(view=download_view, embed=embed_layout)

    @discord.ui.button(label='Twitter! ✨', style=discord.ButtonStyle.primary, row=1)
    async def twitter_layout(self, interaction: discord.Interaction, button: discord.ui.Button):
        download_view = Link()
        embed_layout = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title='Twitter Layout Powered By Cloudinary ✨',
            description='By clicking in the Download Button, You will see the Image With the size perfectly for the social media, for avatar and for banner individually',
            color=discord.Color.random()
        )
        banner_result = cloudinary.CloudinaryImage(
            f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
                {'gravity': "auto", 'height': 500, 'width': 1500, 'crop': "thumb"}]
        )
        av_result = cloudinary.CloudinaryImage(f"UsersLayout/{self.user_name}_av{self.pfpsize}").build_url(transformation=[
            {'gravity': "auto:face", 'height': 360,
                'width': 360, 'zoom': "0.5", 'crop': "thumb"},
            {'radius': "max"}]
        )
        await asyncio.sleep(1)
        layout_shown = cloudinary.CloudinaryImage(f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
            {'gravity': "auto:face", 'height': 500,
                'width': 1500, 'crop': "thumb"},
            {'overlay': f"UsersLayout:{self.user_name}_av{self.pfpsize}"},
            {'gravity': "auto:face", 'height': 280,
                'width': 280, 'zoom': "0.5", 'crop': "thumb"},
            {'radius': "max"},
            {'flags': "layer_apply", 'gravity': "west", 'x': 60, 'y': 65},
            {'overlay': "Layouts:twitter-layout"},
            {'gravity': "south", 'height': 500, 'width': 1500, 'crop': "thumb"},
            {'flags': "layer_apply", 'gravity': "south"}
        ])
        print(layout_shown)
        await asyncio.sleep(1)
        embed_layout.set_image(url=layout_shown)
        download_view.add_item(discord.ui.Button(label='Download Banner ✨',
                                                 style=discord.ButtonStyle.url, url=banner_result))
        download_view.add_item(discord.ui.Button(label='Download Avatar ✨',
                                                 style=discord.ButtonStyle.url, url=av_result))
        await interaction.response.send_message(view=download_view, embed=embed_layout)

    @discord.ui.button(label='Discord! ✨', style=discord.ButtonStyle.primary, row=1)
    async def discord_layout(self, interaction: discord.Interaction, button: discord.ui.Button):
        download_view = Link()
        embed_layout = discord.Embed(
            timestamp=datetime.datetime.utcnow(),
            title='Discord Layout Powered By Cloudinary ✨',
            description='By clicking in the Download Button, You will see the Image With the size perfectly for the social media, for avatar and for banner individually',
            color=discord.Color.random()
        )
        banner_result = cloudinary.CloudinaryImage(
            f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
                {'gravity': "auto", 'height': 240, 'width': 680, 'crop': "thumb"}]
        )
        av_result = cloudinary.CloudinaryImage(f"UsersLayout/{self.user_name}_av{self.pfpsize}").build_url(transformation=[
            {'gravity': "auto:face", 'height': 240,
                'width': 240, 'zoom': "0.2", 'crop': "thumb"},
            {'radius': "max"}]
        )
        await asyncio.sleep(1)
        layout_shown = cloudinary.CloudinaryImage(f"UsersLayout/{self.user_name}_banner{self.bannersize}").build_url(transformation=[
            {'gravity': "auto:face", 'height': 226, 'width': 340, 'crop': "thumb"},
            {'overlay': f"UsersLayout:{self.user_name}_av{self.pfpsize}"},
            {'gravity': "auto:face", 'height': 90,
                'width': 90, 'zoom': "0.2", 'crop': "thumb"},
            {'radius': "max"},
            {'flags': "layer_apply", 'gravity': "west", 'x': 13},
            {'overlay': "Layouts:Discord-Layout"},
            {'flags': "layer_apply", 'gravity': "south", 'zoom': "0.5"},
            {'color': "#F5F5F5", 'overlay': {'font_family': "arial", 'font_size': 24,
                                             'font_weight': "bold", 'text_align': "left", 'text': f"{self.user_name}"}},
            {'flags': "layer_apply", 'gravity': "south_west", 'x': 35, 'y': 18}
        ])
        print(layout_shown)
        await asyncio.sleep(1)
        embed_layout.set_image(url=layout_shown)
        download_view.add_item(discord.ui.Button(label='Download Banner ✨',
                                                 style=discord.ButtonStyle.url, url=banner_result))
        download_view.add_item(discord.ui.Button(label='Download Avatar ✨',
                                                 style=discord.ButtonStyle.url, url=av_result))
        await interaction.response.send_message(view=download_view, embed=embed_layout)
