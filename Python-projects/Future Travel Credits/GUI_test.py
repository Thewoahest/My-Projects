import tkinter as tk
from tkinter import *
window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()
frame_c = tk.Frame()
frame_d = tk.Frame()
button = tk.Button

label_a = tk.Label(master=frame_a, text="Username ")
label_a.pack(side = LEFT)
e1 = tk.Entry(master=frame_a)
e1.pack(side = RIGHT)

label_b = tk.Label(master=frame_b, text="Password ")
label_b.pack(side = LEFT)
e2 = tk.Entry(master=frame_b)
e2.pack(side = RIGHT)

label_c = tk.Label(master=frame_c, text="Traveler First name ")
label_c.pack(side = LEFT)
e1 = tk.Entry(master=frame_c)
e1.pack(side = RIGHT)

label_d = tk.Label(master=frame_d, text="Traveler Last name ")
label_d.pack(side = LEFT)
e1 = tk.Entry(master=frame_d)
e1.pack(side = RIGHT)



frame_a.pack()
frame_b.pack()
frame_c.pack()
frame_d.pack()
window.mainloop()

