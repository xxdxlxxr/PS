N, S = input().split()
record = dict()

for _ in range(int(N)):
    nickname, chat = input().split()

    if nickname == S:
        print(record[chat] if chat in record else 0)
        break

    if chat not in record:
        record[chat] = 0

    record[chat] += 1