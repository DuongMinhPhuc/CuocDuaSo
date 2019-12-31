import sys,tty,termios
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                print("up")
                return "up"
        elif k=='\x1b[B':
                print("down")
                return "down"
        elif k=='\x1b[C':
                print("right")
                return "right"
        elif k=='\x1b[D':
                print("left")
                return "left"
        elif k == "a":
            print("cua trai")
            return "a"
        elif k == "d":
            print("cua phai")
            return "d"
        # else:
        #         print("not an arrow key!")

while True:
    inkey = _Getch()
    while True:
        k = inkey()
        print(k)