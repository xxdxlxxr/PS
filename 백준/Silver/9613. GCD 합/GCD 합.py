def get_gcd(a, b):
	while b:
		a, b = b, a % b

	return a

for i in range(int(input())):
	case = list(map(int, input().split()))
	print(sum(get_gcd(case[j], case[k]) for j in range(1, case[0]) for k in range(j + 1, case[0] + 1)))