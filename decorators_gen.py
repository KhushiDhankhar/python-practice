def demo():
    print("Start")
    yield 10

    print("Middle")
    yield 20

    print("End")

g=demo()
next(g)
next(g)
#next(g)