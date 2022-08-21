from ai import AI


def test_constructor():
    ai = AI([40, 40], 10)
    assert ai.dot_position == [40, 40]
    assert ai.rect_size == 10


def test_get_neighbor():
    ai = AI([40, 40], 10)
    assert ai.get_neighbor([], []) == []


def test_direction():
    ai = AI([10, 10], 1)
    ai.get_neighbor([], [])
    assert ai.direction([5, 5]) == [(6, 5), (4, 5), (5, 4), (5, 6),
                                    (6, 4), (4, 4), (6, 6), (4, 6)]
    assert ai.direction([10, 10]) == [(11, 10), (9, 10), (10, 9), (10, 11),
                                      (11, 9), (9, 9), (11, 11), (9, 11)]


def test_hor_right():
    ai = AI([10, 10], 1)
    ai.get_neighbor([], [])
    assert ai.hor_right([1, 1]) == (2, 1)


def test_hor_left():
    ai = AI([10, 10], 1)
    ai.get_neighbor([], [])
    assert ai.hor_left([1, 1]) == (0, 1)


def test_ver_up():
    ai = AI([10, 10], 1)
    ai.get_neighbor([], [])
    assert ai.ver_up([1, 1]) == (1, 0)


def test_ver_down():
    ai = AI([10, 10], 1)
    ai.get_neighbor([], [])
    assert ai.ver_down([1, 1]) == (1, 2)


def test_diag_up_right():
    ai = AI([10, 10], 1)
    ai.get_neighbor([], [])
    assert ai.diag_up_right([1, 1]) == (2, 0)


def test_diag_up_left():
    ai = AI([10, 10], 1)
    ai.get_neighbor([], [])
    assert ai.diag_up_left([1, 1]) == (0, 0)


def test_diag_down_right():
    ai = AI([10, 10], 1)
    ai.get_neighbor([], [])
    assert ai.diag_down_right([1, 1]) == (2, 2)


def test_diag_down_left():
    ai = AI([10, 10], 1)
    ai.get_neighbor([], [])
    assert ai.diag_down_left([1, 1]) == (0, 2)
