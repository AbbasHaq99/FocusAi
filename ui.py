import tkinter as tk
import threading
import pystray
from PIL import Image, ImageDraw
from detector import start_detector, stop_detector

def create_icon():
    image = Image.new("RGB", (64, 64), "#1a1a2e")
    draw = ImageDraw.Draw(image)
    draw.ellipse((8, 8, 56, 56), fill="#00ff88")
    return image

window = tk.Tk()
window.withdraw()

def show_window():
    window.deiconify()
    window.lift()

def hide_window():
    window.withdraw()

window.title("Focus AI")
window.geometry("400x500")
window.configure(bg="#1a1a2e")
window.resizable(False, False)

title_label = tk.Label(
    window,
    text="FOCUS AI",
    font=("Courier", 28, "bold"),
    bg="#1a1a2e",
    fg="#00ff88"
)
title_label.pack(pady=30)

status_label = tk.Label(
    window,
    text="● Not Running",
    font=("Courier", 16),
    bg="#1a1a2e",
    fg="#888888"
)
status_label.pack(pady=10)

score_label = tk.Label(
    window,
    text="Focus Score: --%",
    font=("Courier", 12),
    bg="#1a1a2e",
    fg="#555555"
)
score_label.pack(pady=5)

timer_label = tk.Label(
    window,
    text="Focused for: 0s",
    font=("Courier", 12),
    bg="#1a1a2e",
    fg="#555555"
)
timer_label.pack(pady=5)

is_running = False
focused_seconds = 0

total_seconds = 0

def on_status_change(focused):
    global focused_seconds, total_seconds
    total_seconds += 1
    if focused:
        status_label.config(text="● Focused", fg="#00ff88")
        focused_seconds += 1
        timer_label.config(text=f"Focused for: {focused_seconds}s", fg="#00ff88")
    else:
        status_label.config(text="● Unfocused", fg="#ff4444")
    if total_seconds > 0:
        score = int((focused_seconds / total_seconds) * 100)
        score_label.config(text=f"Focus Score: {score}%", fg="#00ff88")

def setup_tray():
    menu = pystray.Menu(
        pystray.MenuItem("Show", lambda: window.after(0, show_window)),
        pystray.MenuItem("Quit", lambda: window.after(0, window.quit))
    )
    icon = pystray.Icon("FocusAI", create_icon(), "Focus AI", menu)
    icon.run()

def update_timer():
    window.after(1000, update_timer)

def toggle():
    global is_running
    if is_running:
        stop_detector()
        is_running = False
        button.config(text="Start", bg="#00ff88")
        status_label.config(text="● Not Running", fg="#888888")
    else:
        threading.Thread(target=start_detector, args=(on_status_change,), daemon=True).start()
        is_running = True
        button.config(text="Stop", bg="#ff4444")

button = tk.Button(
    window,
    text="Start",
    command=toggle,
    font=("Courier", 14, "bold"),
    bg="#00ff88",
    fg="#1a1a2e",
    activebackground="#00cc66",
    activeforeground="#1a1a2e",
    relief="flat",
    padx=30,
    pady=10,
    cursor="hand2",
    width=15
)
button.pack(pady=30)

update_timer()
threading.Thread(target=setup_tray, daemon=True).start()
window.mainloop()