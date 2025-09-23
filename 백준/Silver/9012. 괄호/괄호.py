# 9012 괄호
T = int(input())
L = '('
R = ')'
for i in range(T):
    vps_list = []
    vps = input()
    for j in vps:
        if j == L:
            vps_list.append(L)
        elif j == R:
            if len(vps_list) != 0:
                vps_list.pop()
            else:
                print("NO")
                break
    else:
        if len(vps_list) != 0:
            print("NO")
        else:
            print("YES")