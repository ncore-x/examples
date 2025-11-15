value = 100


def magic():
    x = value

    def invisible():
        print(x)  # the function remembers the value of x at the time of its creation

    return invisible


run = magic()

value = 200
run()  # res = 100
value = 300
run()  # res = 100
