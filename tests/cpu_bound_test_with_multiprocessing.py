from multiprocessing import Process


def count(x):
    while x > 0:
        x -= 1


if __name__ == '__main__':
    p1 = Process(target=count, args=(100000000,))
    p1.start()
    p2 = Process(target=count, args=(100000000,))
    p2.start()

    p1.join()
    p2.join()
