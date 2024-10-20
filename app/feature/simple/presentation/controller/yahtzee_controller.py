from typing import Optional
from discord.ext.commands import Context

from app.feature.simple.use_case.get_yahtzee_url_action import GetYahtzeeUrlAction

class YahtzeeController:
    def __init__(self, get_action: GetYahtzeeUrlAction):
        self.get_action = get_action


    async def get(self, ctx: Context, room_name: Optional[str] = None) -> None:
        url = self.get_action.execute(room_name=room_name)

        await ctx.send(content=url)
        