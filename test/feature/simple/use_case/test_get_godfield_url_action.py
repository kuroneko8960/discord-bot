from pytest_mock import MockFixture

from app.feature.simple.use_case.get_godfield_url_action import GetGodfieldUrlAction


def test_success_execute_no_parameter(mocker: MockFixture):
    env_service = mocker.Mock()
    env_service.get_env.return_value = 'passphrase'

    sut = GetGodfieldUrlAction(env_service)
    response = sut.execute()

    assert response.url == 'https://godfield.net'
    assert response.passphrase == 'passphrase'


def test_success_execute_with_parameter(mocker: MockFixture):
    env_service = mocker.Mock()

    sut = GetGodfieldUrlAction(env_service)
    response = sut.execute('passphrase')

    assert response.url == 'https://godfield.net'
    assert response.passphrase == 'passphrase'