import pyautogui
import pytesseract
from PIL import Image

# Define the region (x, y, width, height)
region = (1879, 1747, 2000, 500)  # Change these values as needed

# Capture the region
screenshot = pyautogui.screenshot(region=region)

# Save (optional)

# Extract text
data = pytesseract.image_to_string(screenshot)

print("Extracted Text:\n", data)


# import time
# for i in range(100):
#     time.sleep(0.5)  # Pause execution for 2 seconds
#     print(pyautogui.position())

words = data.split()
words = [word for word in words if word != "Refresh"]

# Create a list to store the formatted data with line breaks
formatted_data = []

# Process the words in chunks of 4 (for each device: ID, IP, Name, MAC)
for i in range(0, len(words), 4):
    # Join the 4 words and add a line break
    formatted_data.append(" ".join(words[i:i+4]))

# Join the formatted data with a line break after each device
prodata = "\n".join(formatted_data)

# Print the result
print("prodata created")
print(prodata)
# Raw data

# Split the data into lines
lines = prodata.strip().split('\n')

# Create a list to store the devices
devices = []

# Process the data in chunks of 4 (ID, IP, device_name, MAC)
for line in lines:
    # Split each line into components
    parts = line.split()
    if len(parts) == 4:  # Ensure there are exactly 4 components in each line
        devices.append({
            "id": parts[0],  # Device ID
            "ip": parts[1],  # IP address
            "device_name": parts[2],  # Device name
            "mac": parts[3]  # MAC address
        })

# Print the devices list
for device in devices:
    print(f"ID: {device['id']}, IP: {device['ip']}, Name: {device['device_name']}, MAC: {device['mac']}")