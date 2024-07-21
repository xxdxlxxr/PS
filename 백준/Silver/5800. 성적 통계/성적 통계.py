for i in range(int(input())):
    scores = list(map(int, input().split()))
    N, scores = scores[0], sorted(scores[1:])
    diff = [scores[j + 1] - scores[j] for j in range(N - 1)]
    print('Class', i + 1)
    print(f'Max {scores[-1]}, Min {scores[0]}, Largest gap {max(diff)}')