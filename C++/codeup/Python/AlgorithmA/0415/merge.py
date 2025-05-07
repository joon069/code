def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    #조건문: n이 1보다 작거나 같으면 a를 반환
    # n이 1보다 작거나 같으면 정렬할 필요가 없음


    mid = n // 2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])
    # 분할
    # a를 반으로 나누어 g1과 g2에 저장
    # g1은 a의 0~mid-1까지, g2는 mid~n-1까지
    # n이 홀수일 경우 g1은 n//2, g2는 n//2+1
    # n이 짝수일 경우 g1과 g2는 n//2

    result=[]
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    #병합
    # g1과 g2를 합치는 과정
    # g1과 g2는 정렬된 상태
    # g1과 g2의 첫 번째 원소를 비교하여 작은 것을 result에 추가

    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result
    # 남은 원소들 처리
    # g1과 g2 중 하나는 비어있음
    # 결과 값 반환

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))

