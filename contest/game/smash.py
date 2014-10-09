# -*- coding: cp936 -*-
import random
from itertools import permutations as perm, combinations as comb

T = range(1,10)
L = 4

def splitList(ls, step):
    """将目标数组，按L的步长拆分成几个子数组"""
    print [ls[step*t:step*(t+1)] for t in range(len(ls)/step+(0 if len(ls)%step == 0 else 1))]
    

def smash():
    
    i = T
    random.shuffle(i)
    seed = random.randint(0,L+1)
    target =''.join([str(t) for t in i[seed:seed+4]])
    #print target
    times = 0
    while(times < 10):
        times += 1
        inp = raw_input('input 4 identity numbers:')
        assert(len(inp) == 4)
        for i in inp:
            assert(49 <= ord(i) <=57)
        exists = 0
        positive = 0
        if inp == target:
            print 'you win in %d times'%times
            return True
        else:
            for i in inp:
                if i in target and inp.index(i) == target.index(i):
                    positive += 1
                elif i in target:
                    exists += 1
            print '%s%s'%(positive*'#',exists*'?')
    else:
        print 'you lose, secret is %s'%target
        return False
def decode():
    pass

if __name__ == '__main__':
    splitList(T,L)
    """
    print "输入4个不一样的数字，根据反馈的正确位置(#标记)和包含数字的个数（?标记）来猜出完整的4位数字"
    play = True 
    while(play):
        smash()
        play = (raw_input('play it again?(y): ') != 'n')"""
    
        
    
