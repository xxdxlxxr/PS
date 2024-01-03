scores = [1, 2, 3, 3, 4, 10, 1, 2, 2, 2, 3, 5, 10]

for T in range(int(input())):
    Gandalf = list(map(int, input().split()))
    Sauron = list(map(int, input().split()))
    answer = sum(Gandalf[i] * scores[i] for i in range(6)) - sum(Sauron[i] * scores[i + 6] for i in range(7))

    print(f'Battle {T + 1}: ', end='')
    print('No victor on this battle field' if answer == 0 else 'Good triumphs over Evil' if answer > 0 else 'Evil eradicates all trace of Good')