def solution(time):
    pairs = 0
    count = [0] * 60
    for m in [t % 60 for t in time]:
        other = 60 - m if m > 0 else 0
        pairs += count[other]
        count[m] += 1
        
    return pairs

if __name__ == '__main__':
    
    time = [30,20,150,100,40]
    print(solution(time))               # 3