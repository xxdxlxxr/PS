import heapq

q = []

for i in range(int(input())):
	num_list = list(map(int, input().split()))

	if not q:
		for num in num_list:
			heapq.heappush(q, num)
	else:
		for num in num_list:
			if q[0] < num:
				heapq.heappush(q, num)
				heapq.heappop(q)

print(q[0])