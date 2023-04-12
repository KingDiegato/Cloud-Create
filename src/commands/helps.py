from core import bot
from discord import  Interaction,  Embed, Color

from embeds.helper import Command_Embeded
from modules.module import Pagination

#! Help Global Helps
@bot.tree.command(name='help', description='Help About The usage of the bot')
async def help(interaction: Interaction):
    embed_help = Embed(
        title=f"General Help for bot interaction, (for command help type /help_command)",
        description=f'''About the Cloud Create Bot: 
                          
                        This bot is made with Cloudinary Api and offer many interactive options to edit images on the fly.
                        
                        The **interactions** are step by step to transform an image from the command to the result
                        
                        There is only 2 Available archive for now: **[image/png, image/jpeg(jpg) & image/webp]**
                        
                        Discord Cloud Create offer an option to edit your Avatar and your Banner[must be Discord Premium user]
                        
                        All the files uploaded with this bot is save for 7 days in Cloudinary and auto erased.
                        
                        **Disclaimer:** all the files you upload may be respectful with the terms and condition of Discord©
                        The use of this bot for load content nsfw might be consider for **Ban your Discord Account Permanently**
                        
                        You can contact me on Discord for any issue here: https://discord.gg/dncv6DajDX
                        or DM 𝕯𝖎𝖊𝖌𝖆𝖙𝖔(#)4880
                      ''',
        color=Color.red(),
    )
    embed_help.set_thumbnail(url=interaction.user.avatar)
    embed_help.set_footer(
        text='In case of getting a 404 Not Found, consult /help_404')
    await interaction.edit_original_response(embed=embed_help, content='')


#! Help Commands
@bot.tree.command(name='help_commands', description='Command usage, Prefix, Returns and Interaction')
async def help_commands(interaction: Interaction):
    help_view = Pagination()
    await interaction.response.send_message(embed=Command_Embeded(), view=help_view)


#! Help Error 404
@bot.tree.command(name='help_404', description='Help About Error 404 aplication dont response')
async def help_404(interaction: Interaction):
    embed_404 = Embed(
        title=f"Error 404 The Aplication don't response",
        description='''This could be for many reason: 
                          
                        **1.- Connection error with the platform**
                        **2.- Discord TimeOut (tried more than 3 seconds to call the command)**
                        **3.- Internet too Slow**
                        **4.- I Hate You (jk)**
                        **5.- Cloudinary Service Might be Down for a while**
                      ''',
        color=Color.red()
    )
    embed_404.set_thumbnail(url=interaction.user.avatar)
    embed_404.set_footer(
        text='In case of getting a 404 Not Found, try again in a few seconds')
    await interaction.response.send_message(embed=embed_404)
