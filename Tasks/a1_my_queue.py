"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        # для очереди можно использовать python list
        self.data = []
        self.ind = 0

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """

        self.data.append(elem)
        self.ind += 1

        print(elem)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """

        try:
            return self.data.pop(0)

        except:
            return None


    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        print(ind)
        return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        return None


if __name__ == "__main__":

    s = Queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)

    print(s.data)

    s.dequeue()
    print(s.data)
    s.dequeue()
    print(s.data)