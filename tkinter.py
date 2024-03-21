import tkinter as tk

def draw_flower(canvas):
    # Dibujar el tallo de la flor
    canvas.create_line(150, 350, 150, 250, fill="green", width=5)

    # Dibujar los pétalos de la flor
    canvas.create_oval(100, 200, 200, 300, fill="yellow", outline="")
    canvas.create_oval(200, 200, 300, 300, fill="yellow", outline="")
    canvas.create_oval(150, 150, 250, 250, fill="yellow", outline="")
    canvas.create_oval(150, 250, 250, 350, fill="yellow", outline="")

    # Dibujar el centro de la flor
    canvas.create_oval(150, 200, 250, 300, fill="red", outline="")

def main():
    root = tk.Tk()
    root.title("Flor Amarilla")

    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    draw_flower(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
