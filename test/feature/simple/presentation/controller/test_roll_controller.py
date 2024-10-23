import pytest
from pytest_mock import MockerFixture

from app.feature.simple.presentation.controller.roll_controller import RollController

@pytest.mark.asyncio
async def test_roll(mocker: MockerFixture):
    # context をモック化
    ctx = mocker.Mock()

    ctx.send = mocker.AsyncMock()
    
    ctx.author = mocker.Mock()
    ctx.author.mention = "<@:1234567890>"

    ctx.message = mocker.Mock()
    ctx.message.channel = mocker.Mock()
    ctx.message.channel.typing = mocker.MagicMock(lambda _: _)

    # asyncio.sleep をモック化
    mocker.patch('asyncio.sleep')

    # DoRollAction をモック化
    action = mocker.Mock()
    action.execute = mocker.Mock()
    action.execute.return_value = 99

    # テスト対象の生成
    sut = RollController(action)
    await sut.roll(ctx=ctx)

    # 検証
    assert action.execute.call_count == 1
    assert ctx.send.call_count == 1
    assert ctx.send.call_args.kwargs["content"] == "<@:1234567890>のダイスロール！ >>> **99**"