class CircularQueue:
    queue = {}
    max_length = 5
    front = 0
    rear = 0

    def enqueue(self, item):
        if len(self.queue) == self.max_length:
            print("One element should be removed, since the queue is full")
            self.remove_latest_added_element()
        self.queue[self.rear] = item
        self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            oldest_element = self.queue[self.front]
            self.queue.pop(self.front)
            self.front += 1
            return oldest_element

    def remove_latest_added_element(self):
        print(self.rear)
        print('Removing the latest added element from the Queue and adding the New element')
        self.queue.pop(4)

    def display(self):
        for i in self.queue:
            print(self.queue[i], end=' ')


if __name__ == "__main__":
    obj = CircularQueue()
    while True:
        choice = int(input())
        if choice == 1:
            obj.enqueue(int(input()))
        elif choice == 2:
            obj.dequeue()
        elif choice == 3:
            obj.display()
        else:
            break