from core import bot
from discord import Embed, Color, Interaction, message, ui, ButtonStyle, app_commands
from modules.module import Link
from cloudinary.uploader import upload

from classMod.Emoji import EmojiSizing

#! Discord emoji Resize
@bot.tree.command(name='discord_emoji_resize', description="Resize an image to fit in the Discord emoji perfect configuration, it's focus in face")
@app_commands.describe(drag="drag'n' drop a file or upload from directory", description="a description for the image")
async def discord_emoji_resize(interaction: Interaction, drag: message.Attachment, description: str | None):
    try:
        file_name = drag.filename
        view = Link() and EmojiSizing(file_name)
        embed = Embed(
            title=f'Picture fetched by: {interaction.user}',
            description=description or 'Prepare for edit the next Image:',
            color=Color.random(),
        )
        print(drag.content_type)
        print(drag.size)
        embed.set_image(url='{}'.format(drag))
        embed.set_thumbnail(url=interaction.user.avatar)
        upload(drag.url, public_id=f'Bot/{file_name}')

        view.add_item(ui.Button(label='See on the Browser',
                                        style=ButtonStyle.url, url='{}'.format(drag)))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    except:
        await interaction.response.send_message("Command Not Found, please Try Again in a few seconds, type /help_404 to see more info")
