from deque_1 import Deque


def is_palindrome(word):
    d = Deque()
    for c in word:
        d.addFront(c)

    while d.size() > 1:
        if d.removeFront() != d.removeTail():
            return False

    return True
