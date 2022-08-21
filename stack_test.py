from stack import Stack
from spot import Spot


def test_constructor():
    user = Stack("User", 10)
    computer = Stack("Computer", 10)
    assert user.content == []
    assert user.position == []
    assert user.sequence == [0, 0, 0, 0]
    assert user.player == "User"
    assert user.rect_size == 10
    assert user.three_sequence is False
    assert user.four_sequence is False


def test_push():
    user = Stack("User", 10)
    computer = Stack("Computer", 10)
    user.push(Spot(10, 10, 255, 10))
    assert user.content
    assert user.position == [(10, 10)]
    computer.push(Spot(10, 10, 255, 10))
    assert computer.content
    assert computer.position == [(10, 10)]


def test_decision_win():
    user = Stack("User", 10)
    computer = Stack("Computer", 10)
    assert user.decision_win() is False
    assert computer.decision_win() is False


def test_check_horizontally():
    user = Stack("User", 10)
    computer = Stack("Computer", 10)
    user.push(Spot(10, 10, 255, 10))
    computer.push(Spot(10, 10, 255, 10))
    user.decision_win()
    computer.decision_win()
    assert user.position == [(10, 10)]
    assert computer.position == [(10, 10)]
    assert user.check_horizontally() is False
    assert computer.check_horizontally() is False


def test_check_vertically():
    user = Stack("User", 10)
    computer = Stack("Computer", 10)
    user.push(Spot(10, 10, 255, 10))
    computer.push(Spot(10, 10, 255, 10))
    user.decision_win()
    computer.decision_win()
    assert user.position == [(10, 10)]
    assert computer.position == [(10, 10)]
    assert user.check_vertically() is False
    assert computer.check_vertically() is False


def test_check_diagonally_up():
    user = Stack("User", 10)
    computer = Stack("Computer", 10)
    user.push(Spot(10, 10, 255, 10))
    computer.push(Spot(10, 10, 255, 10))
    user.decision_win()
    computer.decision_win()
    assert user.position == [(10, 10)]
    assert computer.position == [(10, 10)]
    assert user.check_diagonally_up() is False
    assert computer.check_diagonally_up() is False


def test_check_diagonally_down():
    user = Stack("User", 10)
    computer = Stack("Computer", 10)
    user.push(Spot(10, 10, 255, 10))
    computer.push(Spot(10, 10, 255, 10))
    user.decision_win()
    computer.decision_win()
    assert user.position == [(10, 10)]
    assert computer.position == [(10, 10)]
    assert user.check_diagonally_down() is False
    assert computer.check_diagonally_down() is False


def test_check_num_sequence():
    user = Stack("User", 10)
    computer = Stack("Computer", 10)
    user.push(Spot(10, 10, 255, 10))
    computer.push(Spot(10, 10, 255, 10))
    user.decision_win()
    computer.decision_win()
    assert user.position == [(10, 10)]
    assert computer.position == [(10, 10)]
    assert user.four_sequence is False
    assert computer.four_sequence is False
    assert user.three_sequence is False
    assert computer.three_sequence is False
