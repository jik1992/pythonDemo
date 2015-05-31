# coding=utf-8
import gc
import objgraph

gc.collect()

y = [1, 2, 3, 4]
x = [1]

objgraph.show_refs([y], filename='sample-graph.png')  # 把[y]里面所有对象的引用画出来
objgraph.show_backrefs([x], filename='sample-backref-graph.png')  # 把对x对象的引用全部画出来

objgraph.show_most_common_types(limit=50)
