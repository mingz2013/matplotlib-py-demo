# -*- coding:utf-8 -*-
"""
"""
__date__ = "2019/6/13"
__author__ = "zhaojm"

import numpy as np
from matplotlib import pyplot as plt


def get_list(fname, skiprows=2):
    arr = np.loadtxt(fname, skiprows=skiprows, dtype=np.int)
    print(arr.itemsize)
    return arr


def draw(l):
    x = np.arange(0, len(l))
    y = l[x]
    plt.title("Matplotlib demo")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    plt.plot(x, y)
    plt.show()


def test_draw():
    arr = np.array([1, 21, 3, 14, 5, 16, 7, 81, 9, 101, 11, 112, 13, 114, 15, 116, 17, 118, 19, 20])
    draw(arr)


def test_get_list():
    fname = "test_lines.log"
    arr = get_list(fname)
    print(arr)
    pass


def test_main():
    fname = "test_lines.log"
    draw(get_list(fname))


def main():
    draw(get_list("1_3.log"))

    # draw(get_list("insert_1yi_sort.log", skiprows=14))
    pass


if __name__ == "__main__":
    main()
    # test_draw()
    # test_get_list()
    # test_main()
