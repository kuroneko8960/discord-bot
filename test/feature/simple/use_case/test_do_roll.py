from pytest_mock import MockFixture

from app.feature.simple.use_case.do_roll_action import DoRollAction

def test_execute_success(mocker: MockFixture):
    # random.randrange をモック化
    random = mocker.patch('random.randrange')
    random.return_value = 1

    # テスト対象の生成
    sut = DoRollAction()
    response = sut.execute()

    assert response == 1
    assert random.call_count == 1
    assert random.call_args[0][0] == 100
