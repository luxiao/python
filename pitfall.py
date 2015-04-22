最让我感动沮丧的错误：
1、迭代list的时候，对list进行pop(i)操作。dict的pop则无影响。
改进：list = ［item for item in list if item%2 == 0]
