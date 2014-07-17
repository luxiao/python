class Singleton(object):   
    _instance = None   
    def __new__(cls, *args, **kwargs):   
        if not cls._instance:   
            cls._instance = super(Singleton, cls).__new__(   
                                cls, *args, **kwargs)   
        return cls._instance   

if __name__ == '__main__':   
    s1=S()   
    s2=S()   
    if(id(s1)==id(s2)):   
        print "Same",id(s1),id(s2)   
    else:   
        print "Different"
    if(id(s1._instance)==id(s2._instance)):   
        print "Same",id(s1._instance),id(s2._instance)   
    else:   
        print "Different" 
