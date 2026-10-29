def solution(n):
    answer = []
    n = str(n)
    for i in range(len(n)):
        answer.insert(0, int(n[i]))
        print(answer)
    return answer