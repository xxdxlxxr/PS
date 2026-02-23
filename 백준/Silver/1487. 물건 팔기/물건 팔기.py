N, c_list, d_list = int(input()), [], []

for i in range(N):
	c, d = map(int,input().split())
	c_list.append(c)
	d_list.append(d)

tmp, answer = 0, 0

for i in sorted(set(c_list)):
	money = 0
	
	for j in range(N):
		if i <= c_list[j] and i > d_list[j]:
			money += i - d_list[j]
	
	if tmp < money:
		tmp = money
		answer = i
	
print(answer)