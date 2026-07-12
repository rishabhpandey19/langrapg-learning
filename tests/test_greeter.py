from langraph_youtube.greeter import greet


def test_greeter_default() -> None:
    assert greet() == "Hello, world!"


def test_greeter_custom() -> None:
    assert greet("Ada") == "Hello, Ada!"
