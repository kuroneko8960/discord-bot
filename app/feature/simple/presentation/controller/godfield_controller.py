from typing import Optional
from discord.ext.commands import Context
from app.feature.simple.use_case.get_godfield_url_action import GetGodfieldUrlAction


class GodfieldController:
    def __init__(self, get_godfield_url_action: GetGodfieldUrlAction):
        self.get_godfield_url_action = get_godfield_url_action


    async def get(self, ctx: Context, passphrase: Optional[str] = None) -> None:
        response = self.get_godfield_url_action.execute(passphrase=passphrase)

        await ctx.send(content=f"{response.url}\n合言葉: {response.passphrase}")
    