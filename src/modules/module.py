import discord
from discord import Interaction, ButtonStyle
from discord.ui import View, button, Button
import asyncio

from embeds.helper import Command_Embeded, Commands_Page2, Commands_Page3


class Link(View):
    def __init__(self):
        super().__init__()
        self.value = None


class Close(View):
    def __init__(self):
        super().__init__()
        self.value = None

    @button(label='Close', style=ButtonStyle.red)
    async def close(self, interaction: Interaction, button: Button):
        await interaction.response.send_message('Good Bye!')
        self.value = False
        self.stop()


class ForceDisabled(View):
    def __init__(self):
        super().__init__()
        self.value = None

    @button(label='Loading...', style=ButtonStyle.danger, emoji='<a:typing:597589448607399949>' or ':typing:',  disabled=True)
    async def ephemeral_button(self, interaction: Interaction, button: Button):
        pass


class Force(View):
    def __init__(self, image_tag):
        super().__init__()
        self.image_tag = image_tag
        self.value = None

    @button(label='Load Image', style=ButtonStyle.success)
    async def force_image_load(self, interaction: Interaction, button: Button):
        watching = Link()
        force_embed = discord.Embed(
            title=f'''
            Forced image render, if the image dont load, You can find the image in this url in a few seconds:
            ''',
            description=f'''
            {self.image_tag}
            This action cloud take any longer, Discord provide a timeout of 3 seconds in any interaction, then the image might not render inmediately\n
            if it's dont render inmediately try to pulse Load Image Btn again in 30 seconds....
            ''',
            color=discord.Color.random()
        )
        watching.add_item(Button(label='Download Transformed',
                                            style=ButtonStyle.url, url=self.image_tag))

        force_embed.set_image(url=self.image_tag)
        button.disabled = True
        await interaction.response.send_message(embed=force_embed, view=watching, ephemeral=False)
        await asyncio.sleep(30)
        button.disabled = False

class Force2(View):
    def __init__(self, image_tag):
        super().__init__()
        self.image_tag = image_tag
        self.value = None
        
    @button(label='Load Image', style=ButtonStyle.success)
    async def force_image_load(self, interaction: Interaction, button: Button):
        button.disabled = True        
        watching = Link()
        watching.add_item(Button(label='Download Transformed',
                                            style=ButtonStyle.url, url=self.image_tag))
        await interaction.response.send_message(view=watching, ephemeral=False, content=self.image_tag)


class Pagination(View):
    def __init__(self):
        super().__init__()

    @button(label='Page 1', style=ButtonStyle.secondary)
    async def page_1(self, interaction: Interaction, button: Button):
        await interaction.response.edit_message(embed=Command_Embeded(), view=self)

    @button(label='Page 2', style=ButtonStyle.secondary)
    async def page_2(self, interaction: Interaction, button: Button):
        await interaction.response.edit_message(embed=Commands_Page2(), view=self)

    @button(label='Page 3', style=ButtonStyle.secondary)
    async def page_3(self, interaction: Interaction, button: Button):
        await interaction.response.edit_message(embed=Commands_Page3(), view=self)
