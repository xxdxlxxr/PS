S, A, B = int(input()), int(input()), int(input())

print(250 + (S > A) * (100 * ((S - A) // B + ((S - A) % B != 0))))