from game_controller import GameController


def test_constructor():
    dot_position = get_dot_position()
    gc = GameController((200, 200), dot_position,
                        ((200//20) - 4), ((200//20) - 2))
    assert gc.continue_game is True
    assert gc.playing is True
    assert gc.check_user_sequence is False
    assert gc.check_computer_sequence is False
    assert gc._pix_w == 200
    assert gc._pix_h == 200
    assert gc.stone_size == ((200//20) - 4)
    assert gc.count == 0


def test_user_put_stone():
    dot_position = get_dot_position()
    gc = GameController((200, 200), dot_position,
                        ((200//20) - 4), ((200//20) - 2))
    gc.user_put_stone(20, 20)
    assert gc.to_draw_user
    assert gc.dot_position == [(60, 60), (60, 140), (140, 60), (140, 140)]
    assert gc.check_user_sequence is False


def test_com_put_stone():
    dot_position = get_dot_position()
    gc = GameController((200, 200), dot_position,
                        ((200//20) - 4), ((200//20) - 2))
    gc.user_put_stone(20, 20)
    assert gc.count == 0
    # Nothing will happen, since stone was put in user's turn
    assert gc.put_stone
    assert gc.ai_move
    assert gc.to_draw_computer


def test_put_stone():
    dot_position = get_dot_position()
    gc = GameController((200, 200), dot_position,
                        ((200//20) - 4), ((200//20) - 2))
    gc.user_put_stone(20, 20)
    assert gc.dot_position == [(60, 60), (60, 140), (140, 60), (140, 140)]


def test_update():
    dot_position = get_dot_position()
    gc = GameController((200, 200), dot_position,
                        ((200//20) - 4), ((200//20) - 2))
    gc.user_put_stone(20, 20)
    gc.update()
    assert len(gc.dot_position) == 4
    assert gc.check_computer_sequence is False
    assert gc.check_user_sequence is False


def get_dot_position():
    dot_position = set()
    for i in range(60, 200, 80):
        for j in range(60, 200, 80):
            dot_position.add((i, j))
    return sorted(dot_position)
