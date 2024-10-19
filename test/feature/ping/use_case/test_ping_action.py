from app.feature.ping.use_case.ping_action import PingAction


def test_ping_action():
    action = PingAction()

    assert action.execute() == "にゃ！"