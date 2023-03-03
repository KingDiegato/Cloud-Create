import discord
from discord import Interaction
import asyncio

from embeds.helper import Command_Embeded, Commands_Page2


class Link(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None


class Close(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='Close', style=discord.ButtonStyle.red)
    async def close(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Good Bye!')
        self.value = False
        self.stop()


class Force(discord.ui.View):
    def __init__(self, image_tag):
        super().__init__()
        self.image_tag = image_tag
        self.value = None

    @discord.ui.button(label='Load Image', style=discord.ButtonStyle.danger)
    async def force_image_load(self, interaction: Interaction, button: discord.ui.Button):
        watching = Link()
        force_embed = discord.Embed(
            title=f'''
            Forced image render, if the image dont load, You can find the image in this url in a few seconds:
            ''',
            description=f'''
            {self.image_tag}
            This action cloud take any longer, Discord provide a timeout of 3 seconds in any interaction, then the image might not render inmediately\n
            if it's dont render inmediately try to pulse Load Image Btn again.
            ''',
            color=discord.Color.random()
        )
        watching.add_item(discord.ui.Button(label='Download Transformed',
                                            style=discord.ButtonStyle.url, url=self.image_tag))

        force_embed.set_image(url=self.image_tag)
        button.disabled = True
        await interaction.response.send_message(embed=force_embed, view=watching)
        await interaction.message.edit(view=self)
        await asyncio.sleep(30)
        button.disabled = False
        await interaction.message.edit(view=self)


class Pagination(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='Page 1', style=discord.ButtonStyle.secondary)
    async def page_1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(embed=Command_Embeded(), view=self)

    @discord.ui.button(label='Page 2', style=discord.ButtonStyle.secondary)
    async def page_2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(embed=Commands_Page2(), view=self)
