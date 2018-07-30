def heapsort(data):
    _build_max_heap(data)

    size = len(data)

    while size > 1:
        _swap(data, 0, size - 1)
        size -= 1
        _max_heapify(data, 0, size)


def _build_max_heap(data):
    size = len(data)
    last = size - 1
    start = (last - 1) // 2

    while start >= 0:
        _max_heapify(data, start, size)
        start -= 1


def _max_heapify(data, root, size):
    while 2 * root + 1 < size:
        child = 2 * root + 1

        if child + 1 < size and data[child] < data[child + 1]:
            child = child + 1

        if data[root] < data[child]:
            _swap(data, root, child)
            root = child
        else:
            return



def _swap(data, root, child):
    data[root], data[child] = data[child], data[root]
