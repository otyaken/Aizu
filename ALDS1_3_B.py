# -*- coding utf-8 -*-
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B

class Queue:
    head = 0
    tail = 0
    max_queue_length = 100000
    queue = [i for i in range(0, max_queue_length)]

    def enqueue(self, process_time):
        self.queue[self.head % self.max_queue_length] = process_time
        self.head += 1
    def dequeue(self):
        return_val = self.queue[self.tail % self.max_queue_length]
        self.tail += 1
        return return_val
    def length(self):
        return self.head - self.tail

[num_process, quantum] = list(map(int, input().split()))
queue = Queue()
for i in range(0, num_process):
    _input = input().split()
    process_id = _input[0]
    time = int(_input[1])
    queue.enqueue([process_id, time])

now_time = 0

while True:
    process = queue.dequeue()
    if process[1] - quantum > 0:
        process[1] = process[1] - quantum
        queue.enqueue(process)
        now_time += quantum
    else:
        now_time += process[1]
        print(process[0], now_time)
    if queue.length() == 0:
        break
