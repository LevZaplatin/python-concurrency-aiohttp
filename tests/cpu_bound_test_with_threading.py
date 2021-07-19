from threading import Thread


def count(x):
    while x > 0:
        x -= 1


t1 = Thread(target=count, args=(100000000,))
t1.start()
t2 = Thread(target=count, args=(100000000,))
t2.start()

t1.join()
t2.join()
