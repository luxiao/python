import operator

from sz import stack
from tree import BinaryTree

def pt(exp):
    explist = exp.split()
    s = stack()
    t = BinaryTree('')
    s.push(t)
    currentTree = t
    for i in explist:
        if i == '(':
            currentTree.insertLeft('')
            s.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            currentTree = s.pop()
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            s.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = s.pop()
        else:
            raise ValueError
    return t

def evaluate(parseTree):
    """这个实现太巧妙了，首先是递归求解子树，其次是四则运算的处理"""
    opers={'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.div}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()

if __name__ == '__main__':
    p = pt('( 3 + 4 )')
    print p.getRootVal()
    print p.getLeftChild().getRootVal()
    print p.getRightChild().getRootVal()
    print evaluate(p)
