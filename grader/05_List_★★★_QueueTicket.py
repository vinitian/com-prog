n = int(input())
queue = []
call = []
current = 0
qtime = []
k = -1

for i in range(n):
    s = input().split() # command
    if s[0] == 'reset':
        queue = [int(s[1])]
        # current = queue[0]
        # call = queue[0]
        order = queue[0]
        startTime = []
        times = []
        
    elif s[0] == 'new': 
        print("ticket {}".format(queue[-1]))
        queue.append(int(queue[-1])+1)
        startTime.append(int(s[1]))
        
    elif s[0] == 'next': 
        print('call {}'.format(queue[0]))
        order = queue[0]
        queue.pop(0)
        time = startTime[0]
        startTime.pop(0)
        
    elif s[0] == 'order': 
        
        dt = int(s[1]) - time
        print('qtime {} {}'.format(order, dt))
        times.append(dt)
        
    elif s[0] == 'avg_qtime':
        avg = round(sum(times)/len(times),4)
        print('avg_qtime {}'.format(avg))