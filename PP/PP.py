from time import time

def get_time():
    return int(round(time() * 1000))

class Profiler(object):

    def __init__(self, name=""):
        self.total_time = 0
        self.name       = name

        self.time = 0.0

    def reset(selt):
        self.total_time = 0

    def start(self):
        self.time = get_time()

    def end(self):
        assert self.time > 0.0,\
            " Call start function before end"
        self.total_time += get_time() - self.time
        self.time = 0.0

class PP(object):

    def __init__(self):
        self.profilers = dict()

    def add(self, name=""):
        self.profilers[name] = Profiler()

    def start(self, name=""):
        assert name in self.profilers.keys()
        self.profilers[name].start()

    def end(self, name=""):
        assert name in self.profilers.keys()
        self.profilers[name].end()

    def print(self):
        print ("="*60)
        for name in self.profilers:
            print (" %15s ................ %.3f secs"%(name, self.profilers[name].total_time/1000.0))
        print ("="*60)
