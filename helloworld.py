from const.constants import TITLE, TEXT, COLOR
import tkinter as tk

#Commentaire
def main():
    window = tk.Tk()
    window.configure(bg='yellow')
    window.title(TITLE)
    window.configure(bg='green')
    window.geometry("300x300")
    label = tk.Label(text=TITLE, fg=COLOR)
    label.pack()
    window.mainloop()

if __name__ == "__main__":
    main()
