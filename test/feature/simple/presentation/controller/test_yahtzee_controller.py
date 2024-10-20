import pytest
from pytest_mock import MockerFixture

from app.feature.simple.presentation.controller.yahtzee_controller import YahtzeeController

@pytest.mark.asyncio
async def test_get_with_no_parameter(mocker: MockerFixture):
    ctx = mocker.Mock()
    ctx.send = mocker.AsyncMock()

    get_action = mocker.Mock()
    get_action.execute = mocker.Mock()
    get_action.execute.return_value = 'url'

    sut = YahtzeeController(
        get_action=get_action
    )
    await sut.get(ctx)

    assert get_action.execute.call_count == 1
    assert get_action.execute.call_args.kwargs['room_name'] == None
    assert ctx.send.call_count == 1
    assert ctx.send.call_args.kwargs['content'] == 'url'


@pytest.mark.asyncio
async def test_get_with_parameter(mocker: MockerFixture):
    ctx = mocker.Mock()
    ctx.send = mocker.AsyncMock()

    get_action = mocker.Mock()
    get_action.execute = mocker.Mock()
    get_action.execute.return_value = 'url'

    sut = YahtzeeController(
        get_action=get_action
    )
    await sut.get(ctx, 'room')

    assert get_action.execute.call_count == 1
    assert get_action.execute.call_args.kwargs['room_name'] == 'room'
    assert ctx.send.call_count == 1
    assert ctx.send.call_args.kwargs['content'] == 'url'