# 연결리스트를 이용한 스택 ADT 구현

```py
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None
    
    def push(self, item)
```