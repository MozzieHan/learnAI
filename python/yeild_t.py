#!/usr/bin/env python
# coding=utf-8
import time

def fib(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, a+b
        n -= 1

def consumer():
    while True:
        val = yield
        print("custoum: ", val)


def productor():
    for i in range(30):
        print("begin pro: ", i)
        cus.send(i)
        print("end pro: ", i)
        time.sleep(0.2)



if __name__ == "__main__":
    f = fib(10)
    # for i in f:
    #    print(i)
    cus = consumer()
    cus.send(None)
    productor()

