import pyautogui
import pytesseract
from PIL import Image
def take_screenshot():
    # Capture the screen
    screenshot = pyautogui.screenshot()
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
    
    print("\n")
    print("\n")
    print("\n")
    
    # Split the data into lines
    lines = prodata.strip().split('\n')
    
    # Process the data and store in a dictionary with device_id as the key
    devices = {}
    
    # Process the data in chunks of 4 (ID, IP, device_name, MAC)
    for line in lines:
        # Split each line into components
        parts = line.split()
        if len(parts) == 4:  # Ensure there are exactly 4 components in each line
            device_id = parts[0]  # Device ID
            devices[device_id] = {
                "ip": parts[1],  # IP address
                "device_name": parts[2],  # Device name
                "mac": parts[3]  # MAC address
            }
    
    # Storing devices in variables named after their ID dynamically using globals()
    for device_id, device_info in devices.items():
        globals()[f"device_{device_id}"] = device_info
    
    # Now, let's pull the information from these dynamically created variables with a single print statement
    
    device_to_pull = "2"  # Let's say we want to pull the information for Device 1
    
    # Single print statement with the old format
    print(f"Device {device_to_pull}:\n"
          f"  IP: {globals()[f'device_{device_to_pull}']['ip']}\n"
          f"  Name: {globals()[f'device_{device_to_pull}']['device_name']}\n"
          f"  MAC: {globals()[f'device_{device_to_pull}']['mac']}")
    
    deviceInfo = (f"Device {device_to_pull}:\n" +
          f"  IP: {globals()[f'device_{device_to_pull}']['ip']}\n" +
          f"  Name: {globals()[f'device_{device_to_pull}']['device_name']}\n" +
          f"  MAC: {globals()[f'device_{device_to_pull}']['mac']}")
    
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    lines = prodata.strip().split('\n')
    
    # Process the data and store in a dictionary with device_id as the key
    devices = {}
    
    # Process the data in chunks of 4 (ID, IP, device_name, MAC)
    for line in lines:
        # Split each line into components
        parts = line.split()
        if len(parts) == 4:  # Ensure there are exactly 4 components in each line
            device_id = parts[0]  # Device ID
            devices[device_id] = {
                "ip": parts[1],  # IP address
                "device_name": parts[2],  # Device name
                "mac": parts[3]  # MAC address
            }
    
    # Storing devices in variables named after their ID dynamically using globals()
    for device_id, device_info in devices.items():
        globals()[f"device_{device_id}"] = device_info
    
    # Construct overallInfo string dynamically
    overallInfo = ""
    
    # Iterate over each device and append its information to overallInfo
    for device_id in devices:
        overallInfo += (f"Device {device_id}:\n"
                        f"  IP: {globals()[f'device_{device_id}']['ip']}\n"
                        f"  Name: {globals()[f'device_{device_id}']['device_name']}\n"
                        f"  MAC: {globals()[f'device_{device_id}']['mac']}\n\n")
    
    # Print the overallInfo
    print(overallInfo)
    
    
    
    
    
    
    
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    
    lines = prodata.strip().split('\n')
    
    # Create a dictionary to store the devices with their ID as the key
    devices = {}
    
    # Process the data in chunks of 4 (ID, IP, device_name, MAC)
    for line in lines:
        # Split each line into components
        parts = line.split()
        if len(parts) == 4:  # Ensure there are exactly 4 components in each line
            device_id = parts[0]  # Device ID
            devices[device_id] = {
                "ip": parts[1],  # IP address
                "device_name": parts[2],  # Device name
                "mac": parts[3]  # MAC address
            }
    
    # Storing devices in separate variables dynamically using globals()
    for device_id, device_info in devices.items():
        globals()[f"device_{device_id}"] = device_info
    
    # Open a file in write mode to store the output
    with open("devices_output.txt", "w") as file:
        # Write the information for all devices to the file
        for device_id in devices:
            file.write(f"Device {device_id}:\n")
            file.write(f"  IP: {globals()[f'device_{device_id}']['ip']}\n")
            file.write(f"  Name: {globals()[f'device_{device_id}']['device_name']}\n")
            file.write(f"  MAC: {globals()[f'device_{device_id}']['mac']}\n")
            file.write("\n")  # Newline for better readability
    
    print("The output has been written to devices_output.txt")