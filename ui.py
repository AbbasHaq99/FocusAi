import tkinter as tk
import threading
from detector import start_detector, stop_detector


window = tk.Tk()
window.title("Focus AI")
window.geometry("350x250")
window.configure(bg="#1a1a2e")
window.resizable(False, False)

is_running = False

def toggle():
    global is_running
    if is_running:
        stop_detector()
        is_running = False
        button.config(text="Start")
    else:
        threading.Thread(target=start_detector, daemon=True).start()
        is_running = True
        button.config(text="Stop")
    
button = tk.Button(window, text="Start", command=toggle)
button.pack(pady=20)

window.mainloop()