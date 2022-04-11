def scroll(q, n):
    for i in range(n):
        q.enqueue(q.dequeue())
    return q
