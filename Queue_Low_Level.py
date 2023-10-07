from __future__ import annotations
from typing import Any


EMPTY_NODE_VALUE = '__EMPTY_NODE_VALUE__'

class EmptyQueueError(Exception):
    ...

class Node:
    def __init__(self, value: Any, next: Node = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f'{self.value}'
    
    def __bool__(self) -> bool:
        return bool(self.value != EMPTY_NODE_VALUE)

class Queue:
    def __init__(self) -> None:
        self.first: Node = Node(EMPTY_NODE_VALUE)
        self.last: Node = self.first
        self.count = 0

    def push(self, nodeValue: Any) -> None:
        newNode = Node(nodeValue)
        if self.first.value == EMPTY_NODE_VALUE:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.count += 1

    def pop(self) -> Node:
        if self.first.value == EMPTY_NODE_VALUE:
            raise EmptyQueueError('Queue is empty')
        first = self.first
        if self.first.next is not None:
            self.first = self.first.next
        else: 
            self.first = Node(EMPTY_NODE_VALUE)
        self.count -= 1
        return first

    def peek(self) -> Node:
        return self.first
    
    def __len__(self) -> int:
        return self.count
    
    def __bool__(self) -> bool:
        return bool(self.count)
    
    def __iter__(self) -> Queue:
        return self
    
    def __next__(self) -> Any:
        if self.first.value == EMPTY_NODE_VALUE:
            raise StopIteration
        return self.pop()
        
    def __repr__(self) -> str:
        if not self.first:
            return 'Queue()'
        return f'Queue({self.first}, {self.last})'

if __name__ == "__main__":

    queue = Queue()

    queue.push('A')
    queue.push('B')
    queue.push('C')
    queue.push('D')

    for item in queue:
        print(item)


   