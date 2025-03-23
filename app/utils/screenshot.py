
import os
from typing import Optional
import base64
from io import BytesIO
from datetime import datetime

class ScreenshotManager:
    def __init__(self):
        self._screenshot_func = None
        try:
            import pyautogui
            self._screenshot_func = pyautogui.screenshot
        except ImportError:
            print("Warning: pyautogui not available - screenshots disabled")

    def take_screenshot(self, save_path: Optional[str] = None) -> Optional[str]:
        """Takes a screenshot and optionally saves it to a file.
        Returns: Base64 encoded image string if successful, None otherwise"""
        
        if not self._screenshot_func:
            return None
            
        try:
            screenshot = self._screenshot_func()
            
            if save_path:
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                screenshot.save(save_path)
                
            # Convert to base64 for API response
            buffered = BytesIO()
            screenshot.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            return img_str
            
        except Exception as e:
            print(f"Screenshot failed: {e}")
            return None
