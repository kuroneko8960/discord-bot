from discord.ext import commands

def register_ping_command(bot: commands.Bot) -> None:
    """Pingコマンドを登録します"""

    @bot.command(name="ping")
    async def ping(ctx):
        await ctx.send('にゃ')