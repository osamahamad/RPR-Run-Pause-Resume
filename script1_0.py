import time

# Parameters to configure
triedWords=20
timeMins=0
timeSecs=5
throttleMillisecs=200

# Find more example scripts at https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/default.py
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           pipeline=False,
                           engine=Engine.BURP
                           )
    engine.start() 

    for i in range(3, 8):
        engine.queue(target.req, randstr(i), learn=1)
        engine.queue(target.req, target.baseInput, learn=2)

    secs=timeMins*60+timeSecs
    n=0
    for word in open('words.txt'):
        time.sleep(throttleMillisecs/1000)
        engine.queue(target.req, word.rstrip())
        n+=1
        if(n==triedWords):
         time.sleep(secs)
         n=0

def handleResponse(req, interesting):
    if interesting:
        table.add(req)