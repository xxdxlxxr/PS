N, song = int(input()) - 1, ["baby", "sukhwan", "tururu", "turu", "very", "cute", "tururu",  "turu", "in", "bed", "tururu", "turu", "baby", "sukhwan"]
tmp = N // 14

if N % 14 in [3, 7, 11]:
    print(f"tu+ru*{tmp + 1}" if tmp > 3 else "turu" + tmp * "ru")
elif N % 14 in [2, 6, 10]:
    print(f"tu+ru*{tmp + 2}" if tmp > 2 else "tururu" + tmp * "ru")
else:
    print(song[N % 14])