import time
import winsound

unfocused_since = None
UNFOCUSED_LIMIT = 10

def check_focus(is_focused, on_status_change=None):
    global unfocused_since
    
    if is_focused:
        unfocused_since = None
        if on_status_change:
            on_status_change(True)
    else:
        if unfocused_since is None:
            unfocused_since = time.time()
        seconds_unfocused = time.time() - unfocused_since
        if on_status_change:
            on_status_change(False)
        if seconds_unfocused >= 10:
            winsound.Beep(1000, 500)
            unfocused_since = None