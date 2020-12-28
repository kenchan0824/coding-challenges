def solution(number):
    number = number.replace(' ', ''). replace('-', '')
    ans, i, n = [], 0, len(number)
    while i < n:
        if n - i in [2, 4]:
            ans.append(number[i:i+2])
            i += 2
        else:
            ans.append(number[i:i+3])
            i += 3

    return '-'.join(ans)


if __name__ == "__main__":
    
    number = "1-23-45 6"
    solution(number)
    number = "123 4-567"
    solution(number)
    number = "123 4-5678"
    solution(number)
    number = "12"
    solution(number)
    number = "--17-5 229 35-39475 "
    solution(number)
    