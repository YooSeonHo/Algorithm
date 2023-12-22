import sys
import heapq
input = sys.stdin.readline

t = int(input())

def returnRealNum(nums):
    return nums[1]

for _ in range(t) :

    n = int(input())
    max_heap = []
    min_heap = []
    idx = [False] * n

    for i in range(n) :
        cmd,num = input().split()
        # cmd[1] = int화 해야함
        num = int(num)

        if cmd[0] == 'I' :
            heapq.heappush(max_heap,(-num,i))
            heapq.heappush(min_heap,(num,i))
            idx[i] = True
        elif cmd[0] == 'D' :
            # 1 = delete max, -1 = delete min
            if num == 1 :
                while max_heap and not idx[max_heap[0][1]] :
                    heapq.heappop(max_heap)

                if not max_heap :
                    continue
                else :
                    idx[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            elif num == -1 :
                while min_heap and not idx[min_heap[0][1]] :
                    heapq.heappop(min_heap)

                if not min_heap :
                    continue
                else :
                    idx[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    
    #False인 모든 애를 다 지우는게 아니라, True가 나올때 까지 pop하는 이유는
    #맨 앞에 있는 True가 결국 최대값, 최소값이니까 앞에 있는 False만 지우는거 와 진짜 어렵다
    while max_heap and not idx[max_heap[0][1]] :
        heapq.heappop(max_heap)
    while min_heap and not idx[min_heap[0][1]] :
        heapq.heappop(min_heap)

    if not min_heap or not max_heap :
        print("EMPTY")
    else :
        print(-max_heap[0][0], min_heap[0][0])