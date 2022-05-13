import heapq

while True:
    num = int(input())
    if num == 0 :
        break
    
    heap = list(map(int,input().split()))
    heapq.heapify(heap)
    
    ans = 0
    for i in range(len(heap)-1):
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        cost = n1 + n2
        ans += cost
        heapq.heappush(heap, cost)
        
    print(ans)