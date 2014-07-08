import time
import thread
def timer(no, interval):
    cnt = 0
    while cnt<10:
        print 'Thread:(%d) Time:%s\n'%(no, time.ctime())
        time.sleep(interval)
        cnt+=1
    thread.exit_thread()
def repeat(s,no,times):
    """Returns the string s repeat times.
    and test its performance
    """
    print 'Thread start:(%d) Time:%s\n'%(no, time.ctime())
    for i in range(0,times):
        result=s+s
    print 'Thread end:(%d) Time:%s\n'%(no, time.ctime())
    return result
def repeatplus(s,no,times):
    """Returns the string s repeat times.
    and test its performance
    """
    print 'Thread start:(%d) Time:%s\n'%(no, time.ctime())
    for i in range(0,times):
        result=s*2
    print 'Thread end:(%d) Time:%s\n'%(no, time.ctime())
    return result   
 
def test(): #Use thread.start_new_thread() to create 2 new threads
    thread.start_new_thread(repeat, ('repeat',1,10000000))
    thread.start_new_thread(repeatplus, ('repeat',2,10000000))
 
if __name__=='__main__':
    test()

