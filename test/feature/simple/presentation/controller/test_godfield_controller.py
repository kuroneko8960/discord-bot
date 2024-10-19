from app.feature.simple.use_case.get_godfield_url_action import GetGodfieldUrlResponse
import pytest
from pytest_mock import MockerFixture

from app.feature.simple.presentation.controller.godfield_controller import GodfieldController

@pytest.mark.asyncio
async def test_get_with_no_parameter(mocker: MockerFixture):    
    ctx = mocker.Mock()
    ctx.send = mocker.AsyncMock()

    action = mocker.Mock()
    action.execute = mocker.Mock()
    action.execute.return_value = GetGodfieldUrlResponse(
        url='url',
        passphrase='passphrase'
    )

    sut = GodfieldController(
        get_godfield_url_action=action
    )
    await sut.get(ctx=ctx)

    assert action.execute.call_count == 1
    assert action.execute.call_args.kwargs["passphrase"] == None
    assert ctx.send.call_count == 1
    assert ctx.send.call_args.kwargs["content"] == "url\n合言葉: passphrase"


@pytest.mark.asyncio
async def test_get_with_parameter(mocker: MockerFixture):
    ctx = mocker.Mock()
    ctx.send = mocker.AsyncMock()

    action = mocker.Mock()
    action.execute = mocker.Mock()
    action.execute.return_value = GetGodfieldUrlResponse(
        url='url',
        passphrase='passphrase'
    )

    sut = GodfieldController(
        get_godfield_url_action=action
    )
    await sut.get(ctx=ctx, passphrase='passphrase')

    assert action.execute.call_count == 1
    assert action.execute.call_args.kwargs["passphrase"] == 'passphrase'
    assert ctx.send.call_count == 1
    assert ctx.send.call_args.kwargs["content"] == "url\n合言葉: passphrase"