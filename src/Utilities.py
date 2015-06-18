
from time import time

class Timer:
    
    def start(self):
        self.start_time = time()
    def etime(self):
        return time() - self.start_time


def timewrap2(func):
    def new_func(*args, **kwargs):
        print "starting %s" % func.__name__
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time() - start_time
        print "elapsed time: %f" % end_time
        print
        return result
    return new_func

def timewrap(switch='off'):
    def decorator(func):
        def new_func(*args, **kwargs):
            if switch == 'on':
                print "starting %s" % func.__name__
                start_time = time()
            result = func(*args, **kwargs)
            if switch == 'on':
                end_time = time() - start_time
                print "elapsed time: %f" % end_time
                print
            return result
        return new_func
    return decorator
