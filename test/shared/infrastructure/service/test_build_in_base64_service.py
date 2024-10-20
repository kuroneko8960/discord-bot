from pytest_mock import MockerFixture

from app.shared.infrastructure.service.build_in_base64_service import BuildInBase64Service

def test_encode():
    sut = BuildInBase64Service()
    result = sut.encode('hoge-fuga')

    assert result == 'aG9nZS1mdWdh' # base64 encoded str