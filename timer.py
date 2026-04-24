import time
import winsound

unfocused_since = None
UNFOCUSED_LIMIT = 10

def check_focus(is_focused):
    global unfocused_since
    
    if is_focused:
        unfocused_since = None
    else:
        if unfocused_since is None:
            unfocused_since = time.time()
        seconds_unfocused = time.time() - unfocused_since
        print(f"Unfocused for {seconds_unfocused:.1f} seconds")
        if seconds_unfocused >= 10:
            winsound.Beep(1000, 500)
            unfocused_since = None