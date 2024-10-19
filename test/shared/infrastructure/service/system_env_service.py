import sys

from pytest_mock import MockFixture

from app.shared.infrastructure.service.system_env_service import SystemEnvService


def test_get_env(mocker: MockFixture) -> None:
    mocker.patch('os.environ.get', return_value='hoge')

    sut = SystemEnvService()
    result = sut.get_env('key')

    assert result == 'hoge'