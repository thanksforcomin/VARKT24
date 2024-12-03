from multiprocessing import Process
from Launch import *
from Functions import *

if __name__ == "__main__":

    l = Process(
        target=calculate_best,
        args=(angle_linear, 10_000, 30_000, 90_000, 5000, "linear.txt"),
    )
    p = Process(
        target=calculate_best,
        args=(angle_parabolic, 10_000, 30_000, 90_000, 5000, "parabolic.txt"),
    )
    e = Process(
        target=calculate_best,
        args=(angle_elliptic, 10_000, 30_000, 90_000, 5000, "elliptic.txt"),
    )

    l1 = Process(
        target=calculate_best,
        args=(angle_linear, 30_000, 50_000, 90_000, 5000, "linear_1.txt"),
    )
    p1 = Process(
        target=calculate_best,
        args=(angle_parabolic, 30_000, 50_000, 90_000, 5000, "parabolic_1.txt"),
    )
    e1 = Process(
        target=calculate_best,
        args=(angle_elliptic, 30_000, 50_000, 90_000, 5000, "elliptic_1.txt"),
    )

    l.start()
    p.start()
    e.start()
    l1.start()
    p1.start()
    e1.start()

    l.join()
    p.join()
    e.join()
    l1.join()
    p1.join()
    e1.join()
