from const.constants import TITLE, TEXT, COLOR
import tkinter as tk

def main():
    window = tk.Tk()
    window.title(TITLE)
    window.geometry("200x200")
    label = tk.Label(text=TITLE, fg=COLOR)
    label.pack()
    window.mainloop()

if __name__ == "__main__":
    main()
