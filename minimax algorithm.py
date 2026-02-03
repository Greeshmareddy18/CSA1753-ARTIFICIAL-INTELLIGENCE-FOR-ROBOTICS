b = [' ']*9
H, A = 'X', 'O'
W = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def show():
    print(f"\n {b[0]}|{b[1]}|{b[2]}\n -+-+-\n {b[3]}|{b[4]}|{b[5]}\n -+-+-\n {b[6]}|{b[7]}|{b[8]}\n")

def win(p): return any(all(b[i]==p for i in c) for c in W)
def full(): return ' ' not in b

def minimax(m):
    if win(A): return 1
    if win(H): return -1
    if full(): return 0
    best = -9 if m else 9
    for i in range(9):
        if b[i]==' ':
            b[i]=A if m else H
            best = max(best, minimax(0)) if m else min(best, minimax(1))
            b[i]=' '
    return best

def best():
    return max((minimax(0), i) for i in range(9) if b[i]==' ')[1]

while True:
    show()
    b[int(input("Move (1-9): "))-1] = H
    if win(H) or full(): break
    b[best()] = A
    if win(A) or full(): break

show()
print("Game Over")
