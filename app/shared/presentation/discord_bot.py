import discord
import discord.ext.commands as commands

class DiscordBotSuite():
    """Discord Botを保持するクラスです"""

    def __init__(
        self,
        command_prefix: str = '!',
    ):
        """Botを初期化します"""
        intents = discord.Intents.default()
        intents.message_content = True

        self.bot = commands.Bot(command_prefix=command_prefix, intents=intents)

    
    def get_bot(self) -> commands.Bot:
        """Botを取得します"""
        return self.bot
    

    def boot(self, token: str) -> None:
        """Botを起動します"""
        self.bot.run(token)
        