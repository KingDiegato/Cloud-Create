"""middleware for before invocation onf any command"""

from src.core import bot

@bot.before_invoke
async def invoke_middleware():
    """middleware for before invocation onf any command"""
