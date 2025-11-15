def main(x):
    try:
        return 100 / x
    except Exception:
        return 0
    finally:
        return 100


print(main(0))  # res = 100
