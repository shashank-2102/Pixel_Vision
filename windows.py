import win32gui

def list_window_names():
    window_list = []

    def win_enum_handler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            window_text = win32gui.GetWindowText(hwnd)
            if window_text:
                window_list.append((hwnd, window_text))

    win32gui.EnumWindows(win_enum_handler, None)

    return window_list

# Call the function to list window names and their handles
window_list = list_window_names()

# Print the list of window names and handles
for hwnd, window_text in window_list:
    print(f"Window Handle: {hwnd}, Window Text: {window_text}")
