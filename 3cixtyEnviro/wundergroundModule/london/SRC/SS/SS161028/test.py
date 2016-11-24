from Tkinter import Tk

def foo():
    print("timer went off!")

def countdown(n, bps, root):
    if n == 0:
        root.destroy() # exit mainloop
    else:
        print(n)
        root.after(1000 / bps, countdown, n - 1, bps, root)  # repeat the call

root = Tk()
#root.withdraw() # don't show the GUI window
root.after(4000, foo) # call foo() in 4 seconds
root.after(0, countdown, 10, 2, root)  # show that we are alive
root.mainloop()
print("done")


import time, threading
def foo():
    print(time.ctime())
    threading.Timer(10, foo).start()

foo()