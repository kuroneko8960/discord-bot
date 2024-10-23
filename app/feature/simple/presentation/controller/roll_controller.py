import asyncio
from discord.ext.commands import Context

from app.feature.simple.use_case.do_roll_action import DoRollAction

class RollController:
    def __init__(self, do_roll_action: DoRollAction):
        self.do_roll_action = do_roll_action

    async def roll(self, ctx: Context):
        # タイピング中を表示
        async with ctx.message.channel.typing():
            # 3秒ウェイト
            await asyncio.sleep(1)

            # ロール実行
            result = self.do_roll_action.execute()

            # 結果を送信
            await ctx.send(content=f"{ctx.author.mention}のダイスロール！ >>> **{result}**")