from discord.ui import View, Button, button
from discord import ButtonStyle, Interaction, Embed, Color
from modules.module import Link
from datetime import datetime
from cloudinary import CloudinaryImage

class EmojiSizing(View):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    @button(label='Transform! ✨', style=ButtonStyle.blurple)
    async def emoji_sizing(self, interaction: Interaction, button: Button):
        link_view = Link()
        embed = Embed(
            timestamp=datetime.utcnow(),
            title=f'Picture fetched by: {interaction.user}',
            description='''
                          Improved picture Powered by Cloudinary 🎉✨,
                          Now its can be use perfect for an emoji in discord
                        ''',
            color=Color.random(),
        )
        image_tag = CloudinaryImage(
            f"Bot/{self.file_name}.png").build_url(transformation=[{'effect': "improve:indoor:50"}, {'gravity': "auto:face", 'height': 128, 'width': 128, 'crop': "lfill"}, {'quality': "auto"}])
        embed.set_image(url=image_tag)
        link_view.add_item(Button(label='Download ✨',
                                             style=ButtonStyle.url, url=image_tag, emoji="<a:vibing:747680206734622740>"))
        await interaction.response.send_message(embed=embed, view=link_view)