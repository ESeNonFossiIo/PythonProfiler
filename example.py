from sys import path as syspath
syspath.append("./PP/")

from PP import PP

profiler = PP.PP()

profiler.add("for")
profiler.add("sleep")

profiler.start("sleep")
for i in range(3):
    sleep(i)
profiler.end("sleep")

profiler.start("for")
for i in range(1000):
    print(i*i, end='\r', flush=True)
profiler.end("for")

profiler.start("sleep")
for i in range(3):
    sleep(i)
profiler.end("sleep")

profiler.print()
