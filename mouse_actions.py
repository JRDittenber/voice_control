import pyautogui
from logger import log_info, log_error

def click_coordinates(x, y):
    try:
        pyautogui.click(x, y)
        log_info(f"Clicked at coordinates ({x}, {y})")
    except Exception as e:
        log_error(f"Failed to click at coordinates ({x}, {y}). Error: {e}")

def skip_video():
    # Replace these coordinates with the actual coordinates of the "skip" button
    click_coordinates(100, 100)

def replay_video():
    # Replace these coordinates with the actual coordinates of the "replay" button
    click_coordinates(200, 200)
