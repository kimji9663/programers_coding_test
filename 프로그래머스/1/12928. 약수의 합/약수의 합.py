def solution(n):
    dividers = []
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dividers.append(i)
    for i in range(len(dividers)):
        answer += dividers[i]
    return answer