from PIL import Image
import pyautogui

def take_screenshot(save_path="app/utils/screenshot.png"):
    """Takes a screenshot and optionally saves it to a file."""
    try:
        screenshot = pyautogui.screenshot()
        if save_path:
            screenshot.save(save_path)
        return screenshot
    except Exception as e:
        print(f"Screenshot failed: {e}")
        return None