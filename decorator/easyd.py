def enhanced(meth):
    def new(self, y):
        print "I am enhanced"
        return meth(self, y)
    return new
"""
class C:
    def bar(self, x):
        print "some method says:", x
    bar = enhanced(bar)"""
    
class C:
    @classmethod
    def foo(cls, y):
        print "classmethod", cls, y
    @enhanced
    def bar(self, x):
        print "some method says:", x
