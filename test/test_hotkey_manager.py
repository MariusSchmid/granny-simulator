import granny_simulator as gs

def test_thread_started(mocker):
    mocker.patch('granny_simulator.hotkey_manager.threading.Thread.start',return_value=None)
    gs.listen_to_hotkeys(None)
    gs.hotkey_manager.threading.Thread.start.assert_called_once()

