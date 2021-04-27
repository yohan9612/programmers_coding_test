def solution(numbers, target):
    answer = 0
    len_numbers = len(numbers)

    def dfs(i=0):
        if i < len_numbers:
            numbers[i] *= 1
            dfs(i + 1)

            numbers[i] *= -1
            dfs(i + 1)

        elif sum(numbers) == target:
            nonlocal answer
            answer += 1

    dfs()

    return answer


print(solution([1, 1, 1, 1, 1], 3))
