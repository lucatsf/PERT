import tkinter as tk
from tkinter import ttk

def calculate():
  o = int(optimistic.get())
  n = int(likely.get())
  p = int(pessimistic.get())
  result = (o + (4 * n) + p) / 6
  result = round(result, 2)
  output_label.configure(text=f"Time estimate: {result} hours")

#window
windown = tk.Tk()
windown.title("Program Evaluation and Review Technique")
windown.geometry("400x300")

#title
title_label = ttk.Label(windown, text="Pert", font=("Arial 22 bold"))
title_label.pack()

#input field
input_frame = ttk.Frame(windown)
optimistic = ttk.Entry(input_frame)
optimistic_label = ttk.Label(input_frame, text="Optimistic value")
likely = ttk.Entry(input_frame)
likely_label = ttk.Label(input_frame, text="Likely value")
pessimistic = ttk.Entry(input_frame)
pessimistic_label = ttk.Label(input_frame, text="Pessimistic value")
button = ttk.Button(input_frame, text="Calculate", command=calculate)
optimistic_label.pack(padx=5, pady=5)
optimistic.pack()
likely_label.pack(padx=5, pady=5)
likely.pack()
pessimistic_label.pack(padx=5, pady=5)
pessimistic.pack()

button.pack(padx=10, pady=10)
input_frame.pack(pady=10)

#output field
output_label = ttk.Label(windown, font=("Arial 18"))
output_label.pack()

#run
windown.mainloop()
