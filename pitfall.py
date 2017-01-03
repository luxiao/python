最让人感到沮丧的错误：
1、迭代list的时候，对list进行pop(i)操作。
比如：for index, item in enumerate(list):
          if item%2 == 0:
              list.pop(index)
改进：list = ［item for item in list if item%2 == 0]
2、同上，迭代dict的时候，不能pop(key)，但是如果里面有元素的话，pop操作依然会触发一次，
然后才引发RuntimeError: dictionary changed size during iteration。要使用copy方法。
比如：d = dict({'a': 1, 'b': 2})
for k in d:
    d.pop(k)
这个迭代的结果就是d.pop()了一次，d为{'b': 2}，引发一个runtime error
改进：for k in d.copy():
          d.pop(k)
copy的操作相当于复制了一个新的dict，基于新的dict的key来pop另外一个dict。

3、函数形参默认值为函数调用
def f(now=datetime.datetime.now()):
          print now
好像很完美的样子，如果不传now就使用系统参数。
在使用一些lib的时候，特别是数据库orm的时候，都支持定义default=now()值，很好用。
导致我们产生了联想，是否python函数也可以这样使用。是的，如果你只是一个运行一次就结束的脚本，是没有太大问题。
但如果你是运行的一个web应用，情形就变的好玩了。你不会每次都拿到now，而是你的python函数加载进web server的那一刻。
也就是说不管后续调用多少次f，now的默认值永远是历史一刻。传入值的不算。也就是说函数加载进python解释器的时候，
所有函数的参数都被固定下来。下面我们来看看一个历史悠久的python问题，now=[]，容器类型参数，也叫可变参数。
def f(n=[]):
    n.append(1)
    print n
    import time
    time.sleep(10)
    f()
结果：
[1]
[1, 1]
[1, 1, 1]
[1, 1, 1, 1]
试着解释一下，函数加载进python解释器的时候，所有参数的默认值必须固定下来，如果是个容器类型变量，则是变量的地址，
所有对该变量的操作，全部是对该地址的操作，因而会保留之前的结果。而函数调用则会进行函数求值。把值固定下来。
知其然，还要知其所以然。
