from const.constants import TITLE, TEXT, COLOR
import tkinter as tk

#Commentaire
#LOCAL
def main():
    window = tk.Tk()
    window.configure(bg='cyan')
    window.title(TITLE)
    window.configure(bg='green')
    window.geometry("400x400")
    label = tk.Label(text=TITLE, fg=COLOR)
    label.pack()
    window.mainloop()

if __name__ == "__main__":
    main()
