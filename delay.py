import tkinter as tk
import random
import threading
import time


def create_window():
    root = tk.Toplevel()
    root.title(" ")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
 
    #размер окон
    
    window_width = 100 
    window_height = 100

    x = random.randint(0, screen_width - window_width)
    y = random.randint(0, screen_height - window_height)

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")



def create_windows_loop():
    while True:
        create_window()
        time.sleep(1) # Задержка (сек)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    window_thread = threading.Thread(target=create_windows_loop, daemon=True)
    window_thread.start()

    root.mainloop()
