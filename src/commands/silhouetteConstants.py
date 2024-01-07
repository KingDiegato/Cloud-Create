from discord import app_commands
from discord.app_commands import Choice

color_choices = app_commands.choices(choice_color=[
    Choice(name='Red     🟥', value='#CF2C2C'),
    Choice(name='Yellow  🟨', value='#FFF900'),
    Choice(name='Lime    🟩', value='#5EA031'),
    Choice(name='Green   🟢', value='#0B7E29'),
    Choice(name='Cyanade 🟦', value='#1AB4AA'),
    Choice(name='Purple  🟪', value='#7038A1'),
    Choice(name='Pink    💗', value='#D867B4'),
    Choice(name='Wine    🔴', value='#862044'),
    Choice(name='Blue    🔵', value='#09f'),
    Choice(name='Black   ⚫', value='#121212')
])
color_choices_2 = app_commands.choices(choice_color_two=[
    Choice(name='Red     🟥', value='#CF2C2C'),
    Choice(name='Yellow  🟨', value='#FFF900'),
    Choice(name='Lime    🟩', value='#5EA031'),
    Choice(name='Green   🟢', value='#0B7E29'),
    Choice(name='Cyanade 🟦', value='#1AB4AA'),
    Choice(name='Purple  🟪', value='#7038A1'),
    Choice(name='Pink    💗', value='#D867B4'),
    Choice(name='Wine    🔴', value='#862044'),
    Choice(name='Blue    🔵', value='#09f'),
    Choice(name='Black   ⚫', value='#121212')
])

strength = app_commands.choices(strength=[
    Choice(name='Weak', value='15'),
    Choice(name='Moderate', value='25'),
    Choice(name='Strong', value='40')
])
