def greeting(name: str) -> str:
    if not name or not name.strip():
        return "Hello, world!"
    return f"Hello, {name}!"
