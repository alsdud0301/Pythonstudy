# 100까지 소수
for i in range(2, 101):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
    if is_prime:
        print(i)