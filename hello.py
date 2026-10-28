from datetime import datetime, timezone


def greeting(name: str = "coisini") -> str:
    return f"Hello from {name}!"


if __name__ == "__main__":
    print(greeting())
    print(f"generated at {datetime.now(timezone.utc).isoformat(timespec='seconds')}")
