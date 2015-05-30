# coding=utf-8
#
# ncalls表示函数调用的次数
# tottime表示指定函数消耗的时间
# percall表示函数每次调用的平均耗时,tottime/ncalls
# cumtime表示该函数及其所有子函数的调用耗时,就是从函数开始调用到返回的时间
# 第二个percall为cumtime/primitive calls的值
# filename:lineno(function)表示每个函数所在的位置

# console: python -m cProfile caption_5_io.py

import cProfile


def func():
    print("")


cProfile.run('func()')
