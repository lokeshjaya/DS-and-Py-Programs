class CircularQueue:
    queue = {}
    max_length = 5
    front = 0
    rear = 0

    '''This function meant for the adding the new element in the queue'''
    def enqueue(self, item):
        if len(self.queue) == self.max_length:
            print("One element should be removed, since the queue is full")
            self.remove_latest_added_element()
        self.queue[self.rear] = item
        self.rear += 1

    '''This function is for remove the latest added element from the queue'''
    def remove_latest_added_element(self):
        print('Removing the latest added element from the Queue and adding the New element')
        self.queue.pop(4)

    '''This function is for displaying the elements from the queue'''
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
            obj.display()
        else:
            break
