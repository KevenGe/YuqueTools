from functools import partial


def func1(a: int, b: int) -> int:
    pass


def main():
    f1 = func1
    f2 = partial(func1, a=1)
    f3 = partial(func1, a=2)
    f4 = partial(func1, a=1)
    print(str(f1))
    print(str(f2))
    print(str(f3))
    print(str(f4))
    print(id(f1))
    print(id(f2))
    print(id(f3))
    print(id(f4))
    
    print(f2.func.__name__)
    print(f2.args)
    print(f2.keywords)

    print(f"{f2.func.__name__}_{f2.args}_{f2.keywords}")

if __name__ == "__main__":
    main()
