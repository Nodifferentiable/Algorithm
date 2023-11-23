import heapq

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heapq.heapify(heap)
print(heapq.nsmallest(2,heap))