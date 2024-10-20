import base64
from pytest_mock import MockerFixture

from app.feature.simple.use_case.get_yahtzee_url_action import GetYahtzeeUrlAction


def test_execute_no_parameter(mocker: MockerFixture):
    env_service = mocker.Mock()
    env_service.get_env = mocker.Mock()
    env_service.get_env.return_value = "default-room"

    base64_service = mocker.Mock()
    base64_service.encode = mocker.Mock()
    base64_service.encode.return_value = "ZGVmYXVsdC1yb29t"

    sut = GetYahtzeeUrlAction(
        env_service=env_service,
        base64_service=base64_service
    )
    result = sut.execute()

    assert result == 'https://buddyboardgames.com/yahtzee?room=ZGVmYXVsdC1yb29t'
    assert env_service.get_env.call_count == 1
    assert env_service.get_env.call_args[0][0] == 'YAHTZEE_ROOM_NAME'
    assert base64_service.encode.call_count == 1
    assert base64_service.encode.call_args[0][0] == 'default-room'


def test_execute_with_parameter(mocker: MockerFixture):
    env_service = mocker.Mock()
    env_service.get_env = mocker.Mock()

    base64_service = mocker.Mock()
    base64_service.encode = mocker.Mock()
    base64_service.encode.return_value = "d2FuLXJvb20%3D"

    sut = GetYahtzeeUrlAction(
        env_service=env_service,
        base64_service=base64_service
    )
    result = sut.execute('wan-room')

    assert result == 'https://buddyboardgames.com/yahtzee?room=d2FuLXJvb20%3D'
    assert env_service.get_env.call_count == 0
    assert base64_service.encode.call_count == 1
    assert base64_service.encode.call_args[0][0] == 'wan-room'