import _tkinter
import functions
import init
import turtle

print("PROGRAM REALIZUJĄCY ZADANIE 3 Z MINILOGII 08 - Balony")
try:
    functions.baloons(init.liczba_balonow)
    turtle.done()
except turtle.Terminator:
    turtle.done()
    print("PROGRAM ZOSTAL ZAMKNIETY")
except _tkinter.TclError:
    try:
        turtle.done()
    except turtle.Terminator:
        turtle.done()
        print("PROGRAM ZOSTAL ZAMKNIETY")



