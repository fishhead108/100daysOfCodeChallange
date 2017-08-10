# genqueue.py
#
# Generate a sequence of items that put onto a queue
import queue, threading


def consume_queue(thequeue):
    while True:
        item = thequeue.get()
        if item is StopIteration:
            break
        yield item


# Example
if __name__ == '__main__':

    def consumer(q):
        for item in consume_queue(q):
            print("Consumed", item)
        print("done")


    in_q = queue.Queue()
    con_thr = threading.Thread(target=consumer, args=(in_q,))
    con_thr.start()

    # Now, pipe a bunch of data into the queue
    for i in range(100):
        in_q.put(i)
    in_q.put(StopIteration)
