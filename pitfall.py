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
copy的操作相当于复制了一个新的dict，基于新的dict的key来pop另外一个dict

