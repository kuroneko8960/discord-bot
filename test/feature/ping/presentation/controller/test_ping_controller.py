import pytest
from pytest_mock import MockerFixture

from app.feature.ping.presentation.controller.ping_controller import PingController

@pytest.mark.asyncio
async def test_ping_controller_execute(mocker: MockerFixture) -> None:
    # Setup
    ping_action = mocker.Mock()
    ping_action.execute = mocker.AsyncMock()
    ping_action.execute.return_value = "Ping"

    ping_controller = PingController(ping_action=ping_action)

    context = mocker.Mock()
    context.send = mocker.AsyncMock()

    # Exercise
    await ping_controller.execute(ctx=context)

    # Verify
    assert ping_action.execute.call_count == 1
    assert context.send.call_count == 1
    assert await context.send.call_args.kwargs["content"] == "Ping"