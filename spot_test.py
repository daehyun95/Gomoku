from spot import Spot


def test_constructor():
    spot = Spot(100, 100, 255, 20)
    assert spot.x == 100
    assert spot.y == 100
    assert spot.stone_color == 255
    assert spot.stone_size == 20
