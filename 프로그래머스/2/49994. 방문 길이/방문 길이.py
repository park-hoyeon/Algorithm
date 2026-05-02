def solution(dirs):
    answer = 0
    visited = set()

    x,y = 0,0
    
    for i in range(len(dirs)):
        before_x, before_y = x,y
        
        if dirs[i] == 'U':
            x -= 1
        elif dirs[i] == 'D':
            x += 1
        elif dirs[i] == 'R':
            y += 1
        elif dirs[i] == 'L':
            y -= 1
        
        # 범위 밖이면 해당x
        if x > 5 or x < -5 or y > 5 or y < -5:
            x = before_x
            y = before_y
            continue
        
        road = (before_x,before_y,x,y)
        reverse_road = (x,y,before_x,before_y)
        
        # 방문처리하기
        if road not in visited:
            visited.add(road)
            visited.add(reverse_road)
            answer+=1
    
    return answer