__author__ = 'zuoyun1'
import os
import shutil

def open_io():
    fo = open("io_test", "wb")
    print "Name of the file: ", fo.name
    print "Closed or not : ", fo.closed
    print "Opening mode : ", fo.mode
    print "Softspace flag : ", fo.softspace

    fo.write("Python is a great language.\nYeah its great!!\n");
    fo.close();

    fo = open("io_test", "r+")

    print fo.read(10)

    position = fo.tell()
    print "current position", position

    fo.seek(0, 0)


# os.remove("io_test")
shutil.rmtree("path")
os.mkdir("path")
os.chdir("path")
open_io()
print os.getcwd()

