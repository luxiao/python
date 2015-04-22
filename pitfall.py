最让人感到沮丧的错误：
1、迭代list的时候，对list进行pop(i)操作。dict的pop则无影响。
比如：for index, item in enumerate(list):
          if item%2 == 0:
              list.pop(index)
改进：list = ［item for item in list if item%2 == 0]
