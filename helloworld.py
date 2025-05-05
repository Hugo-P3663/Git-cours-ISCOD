from const.constants import TITLE, TEXT, COLOR
import tkinter as tk

#Commentaire
#LOCAL
def main():
    window = tk.Tk()
    window.configure(bg='cyan')
    window.title(TITLE)
    window.configure(bg='green')
    window.geometry("500x500")
    label = tk.Label(text=TITLE, fg=COLOR)
    label_date = tk.Label(text=datetime.now())
    label.pack()
    window.mainloop()

if __name__ == "__main__":
    main()
