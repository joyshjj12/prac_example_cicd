from app import add

def test_app():
    assert add(2,3) == 5
    assert add(0,0) == 0