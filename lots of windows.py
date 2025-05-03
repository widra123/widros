import tkinter as tk
import random
import threading

def create_window():
    root = tk.Toplevel()
    root.title(" ") #название окон

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    #размер окон
    
    window_width = 100
    window_height = 100

    x = random.randint(0, screen_width - window_width)
    y = random.randint(0, screen_height - window_height)

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

def create_multiple_windows(num_windows):
    threads = []
    for _ in range(num_windows):
        thread = threading.Thread(target=create_window)
        threads.append(thread)
        thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    num_windows = 10 #нужное количество окон
    create_multiple_windows(num_windows)
    root.mainloop()


