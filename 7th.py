def circle(moves: str)-> bool:
    x,y=0,0
    for move in moves:
        if move =='U':
            y+=1
        elif move =='D':
            y-=1
        elif move =='L':
            x-=1
        elif move =='R':
            x+=1
    return x==0 and y==0
moves = "UD"
print(circle(moves))
moves = "LL"
print(circle(moves))