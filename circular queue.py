class CircularQueue:
    def __init__(self,max_size):
        self.queue = [None]*max_size
        self.front = -1
        self.rear = -1
        self.size = 0
        self.max_size = max_size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def enqueue(self,song_title):
        if self.is_full():
            print("Queue is Full")
        else:
            if self.front ==-1:
                self.front = 0
            self.rear =(self.rear +1) % self.max_size
            self.queue[self.rear] = song_title
            self.size += 1
            print(f"{song_title} added to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            song_title = self.queue[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front +1) % self.max_size
            self.size -= 1
            print(f"{song_title} is removed from the queue")

if __name__=="__main__":
    num_operations = int(input())
    song_queue = CircularQueue(1000)

    for _ in range(num_operations):
        operation = input().split()
        if operation[0] == "ENQUEUE":
            song_title = " ".join(operation[1:])
            song_queue.enqueue(song_title)
        elif operation[0] == "DEQUEUE":
            song_queue.dequeue()
