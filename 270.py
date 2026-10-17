n1 = int(input())
n2 = int(input())

for n in [n1, n2]:
    sq = n * n
    temp_n = n
    temp_sq = sq
    is_automorphic = True

    while temp_n > 0:
        if temp_n % 10 != temp_sq % 10:
            is_automorphic = False
            break
        temp_n //= 10
        temp_sq //= 10

    if is_automorphic:
        print("True")
    else:
        print("False")

