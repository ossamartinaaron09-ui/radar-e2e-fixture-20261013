from src.greeting import greeting


def test_greeting_for_named_person():
    assert greeting("Radar") == "Hello, Radar!"


def test_greeting_for_blank_name_uses_world_default():
    assert greeting("") == "Hello, world!"
