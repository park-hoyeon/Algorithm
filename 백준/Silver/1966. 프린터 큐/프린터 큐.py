case = int(input())
value = []
for _ in range(case):
    N,M = map(int,input().split())
    value = list(map(int, input().split()))

    index = [i for i in range(N)]   # N개 문서의 기존 순서 저장
    count = 0   # 몇 번째로 인쇄할지 카운트하는 변수

    while True:
        # 현재 문서가 중요도가 가장 높다면
        if value[0] == max(value):
            count+=1
            if index[0] == M:   # 궁금한 문서인지 확인
                print(count)
                break
            #궁금한 문서가 아니라면 리스트에서 탈출
            else:
                del value[0]
                del index[0]
        # 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있으면
        else:
            value.append(value[0])
            del value[0]
            index.append(index[0])
            del index[0]



