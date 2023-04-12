from discord.ext import commands
from discord import Status, Activity, Intents, ActivityType

intents = Intents.default()


bot = commands.Bot(command_prefix='$', intents=intents, status=Status.online,activity=Activity(
                                                        type=ActivityType.watching, name='Art Attack', details='About to create a new colorful world, and bring a big experience to your images'))
