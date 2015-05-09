__author__ = 'zuoyun1'

try:
    3<2
except IOError:
    "this is error"
    raise BaseException("xx")