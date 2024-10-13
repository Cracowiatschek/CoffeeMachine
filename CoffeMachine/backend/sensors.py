import requests as r


def temperature():
    try:
        req = r.get("")
        return f"{req} °C"
    except Exception as e:
        print(e)
        return "Err"


def milk():
    try:
        req = r.get("")
        return f"{req} %"
    except Exception as e:
        print(e)
        return "Err"


def grind():
    try:
        req = r.get("")
        return f"{req}"
    except Exception as e:
        print(e)
        return "Err"

