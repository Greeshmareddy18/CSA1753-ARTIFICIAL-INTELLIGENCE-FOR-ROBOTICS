b = [' '] * 9

def show():
    print(f"\n {b[0]}|{b[1]}|{b[2]}\n -+-+-\n {b[3]}|{b[4]}|{b[5]}\n -+-+-\n {b[6]}|{b[7]}|{b[8]}\n")

def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(all(b[i]==p for i in c) for c in w)

def play():
    p = 'X'
    while True:
        show()
        m = int(input(f"{p} (1-9): ")) - 1
        if b[m] == ' ':
            b[m] = p
            if win(p): show(); print(p,"wins"); break
            if ' ' not in b: show(); print("Draw"); break
            p = 'O' if p=='X' else 'X'

play()
