print '\n'.join([(lambda x: 'fuzzbuzz' if x%3 ==0 and x%5 ==0 else 'fuzz' if x%3 ==0 else 'buzz' if x%5 == 0 else 'None')(i) for i in range(1, 100)])
