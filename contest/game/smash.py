import random

def smash():
    print "输入4个不一样的数字，根据反馈的正确位置和包含数字的个数来猜出完整的4位数字"
    i = range(1,10)
    random.shuffle(i)
    seed = random.randint(0,5)
    target =''.join([str(t) for t in i[seed:seed+4]])
    #print target
    times = 0
    while(times < 10):
        inp = raw_input('input 4 identity numbers:')
        times += 1
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
            print '%d in right position, and %d in wrong position'%(positive,exists)
    else:
        print 'you lose, secret is %s'%target
        return False
def test():
    pass
    
smash()
    
