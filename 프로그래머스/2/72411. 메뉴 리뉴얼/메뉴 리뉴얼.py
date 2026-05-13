def solution(orders, course):
    answer = []
    
    for target_len in course:
        counter = {}
        
        for order in orders:
            order = ''.join(sorted(order))
            
            def dfs(start,path):
                
                if len(path) == target_len:
                    if path not in counter:
                        counter[path] = 0
                    counter[path] += 1
                    return
            
                for i in range(start, len(order)):
                    dfs(i+1,path+order[i])
            dfs(0,"")
        
        if len(counter) == 0:
            continue

        max_count = max(counter.values())
        if max_count < 2:
            continue

        for menu, count in counter.items():
            if count == max_count:
                answer.append(menu)
    
    return sorted(answer)