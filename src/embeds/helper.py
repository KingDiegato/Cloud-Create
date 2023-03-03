import discord


def Command_Embeded():
    '''
    Create an Embed for the Help Command Interaction
    '''
    embed_commands = discord.Embed(
        title="Commands Help (1/2)",
        description="""
                      The command interaction with the bot is step by step for editing images,
                      **Prefix:** Slash command (/) & use cash symbol for init new updates ($init),
                      **List of commands:**
                      """,
        color=discord.Color.blurple()
    )
    embed_commands.add_field(name="Background Remove", value="""☑**Command:** /background_remove
                                                                    🎶**Return:** The image with png format and backgroundless
                                                                    💨**Steps:** Upload Image (drag) -> processing transform (btn) -> Result (Download & Choice)
                                                                """, inline=False)
    embed_commands.add_field(name="Avatar Transform", value="""☑**Command:** /av
                                                                    🎶**Return:** From your pfp, any transformation you choose
                                                                    💨**Steps:** Recover image (member interact) -> Transform panel (btn) -> Result (btn)
                                                                """, inline=False)
    embed_commands.add_field(name="Color Silhouette", value="""☑**Command:** /color_silhouette
                                                                    🎶**Return:** From Uploaded Image, **return** Silhouette with the choosen color
                                                                    💨**Steps:** Upload image (drag) & Choice Color (options) -> Transform panel (btn) -> Result (btn)
                                                                """, inline=False)
    embed_commands.add_field(name="Whitify Image", value="""☑**Command:** /whitify
                                                                    🎶**Return:** From Uploaded Image, **return** White improve Image
                                                                    💨**Steps:** Upload image (drag) -> Transform panel (btn) -> Result (btn)
                                                                """, inline=False)
    embed_commands.add_field(name="Colorful Image", value="""☑**Command:** /colorful
                                                                    🎶**Return:** From Uploaded Image, **return** Color Intensify Image
                                                                    💨**Steps:** Upload image (drag) -> Transform panel (btn) -> Result (btn)
                                                                """, inline=False)
    embed_commands.add_field(name="High Contrast Image", value="""☑**Command:** /high_contrast
                                                                    🎶**Return:** From Uploaded Image, **return** Color Intensify Image
                                                                    💨**Steps:** Upload image (drag) -> Transform panel (btn) -> Result (btn)
                                                                """, inline=False)
    embed_commands.set_footer(
        text="Command /help for regular and terms helps, Command /help_404 for not found or response errors")
    embed_commands.set_thumbnail(
        url="https://res.cloudinary.com/diegato/image/upload/e_contrast:50/e_saturation:-40/v1/Bot/Testing-1q:av_up")

    return embed_commands


def Commands_Page2():
    '''
    Create an Embed for the Help Command Interaction
    '''
    embed_commands_page2 = discord.Embed(
        title="Commands Help (2/2)",
        description="""
                      The command interaction with the bot is step by step for editing images,
                      **Prefix:** Slash command (/) & use cash symbol for init new updates ($init),
                      **List of commands:**
                      """,
        color=discord.Color.blurple()
    )
    embed_commands_page2.add_field(name="Background Remove", value="""☑**Command:** /dsicord_emoji_resize
                                                                    🎶**Return:** The image Resize for fit in the emoji ideal config
                                                                    💨**Steps:** Upload Image (drag) -> Apply resize (btn) -> Result (btn)
                                                                """, inline=False)
    embed_commands_page2.add_field(name="Avatar Transform", value="""☑**Command:** /black_and_white
                                                                    🎶**Return:** From Uploaded Image, **return** Grayscale Transformation
                                                                    💨**Steps:** Upload image (drag) -> Apply effect (btn) -> Result (btn)
                                                                """, inline=False)
    embed_commands_page2.add_field(name="Color Silhouette", value="""☑**Command:** /sepia_effect
                                                                    🎶**Return:** From Uploaded Image, **return** Sepia Transformation
                                                                    💨**Steps:** Upload image (drag) -> Apply effect (btn) -> Result (btn)
                                                                """, inline=False)
    embed_commands_page2.add_field(name="Whitify Image", value="""☑**Command:** /ping
                                                                    🎶**Return:** **Pong!**
                                                                    💨**Steps:** Call to action
                                                                """, inline=False)
    embed_commands_page2.add_field(name="Colorful Image", value="""☑**Command:** /banner
                                                                    🎶**Return:** From The Banner, **return** any transformation you choose (must be Nitro User)
                                                                    💨**Steps:** Recover image (member interact) -> Transform panel (btn) -> Result (btn)
                                                                """, inline=False)
    embed_commands_page2.add_field(name="High Contrast Image", value="""☑**Command:** /help*
                                                                    🎶**Return:** Summary of the help
                                                                    💨**Steps:** Call to action
                                                                """, inline=False)
    embed_commands_page2.set_footer(
        text="Command /help for regular and terms helps, Command /help_404 for not found or response errors")
    embed_commands_page2.set_thumbnail(
        url="https://res.cloudinary.com/diegato/image/upload/e_contrast:50/e_saturation:-40/v1/Bot/Testing-1q:av_up")

    return embed_commands_page2
