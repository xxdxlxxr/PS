import heapq

abs_heap = []

for i in range(int(input())):
	num = int(input())

	if num:
		heapq.heappush(abs_heap, (abs(num), num))
	else:
		print(heapq.heappop(abs_heap)[1] if abs_heap else 0)