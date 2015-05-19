"""
Test program for SimpleTS. 

Author :        John Markus Bjorndalen <johnm@cs.uit.no>
Version:        1.1
"""
import SimpleTS
import threading
import time

TSNAME = "tst"

SimpleTS.provideTS(TSNAME)
time.sleep(1)

def test():
    print "**** test function, 'computing' for a while"
    time.sleep(3)
    print "**** test function ready to return"
    return "this is a test"

ts = SimpleTS.getNamedTS(TSNAME)

# Add something to the tuple space using eval
ts.Eval((1,2), test, (), (3,4))

# Wait for it, first with rd
print "--- Client trying to read returned value"
ret = ts.Rd()
print "--- Rd returned", ret
ret = ts.In((1,2,SimpleTS.MatchAny(), 3))
print "--- In returned", ret
