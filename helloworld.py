import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Hello world")
    window.geometry("200x200")
    label = tk.Label(text="Hello world", fg="yellow")
    label.pack()
    window.mainloop()

if __name__ == "__main__":
    main()
