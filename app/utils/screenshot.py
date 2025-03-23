import pyautogui
import pytesseract
from PIL import Image
import base64
import re
from openai import OpenAI
client = OpenAI(api_key="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")  # Replace with your API key
overallInfo = ""

def take_screenshot():
    # Capture the region
    screenshot = pyautogui.screenshot()

    # Save (optional)
    screenshot.save("screenshot_region.png")
    # Extract text
    # import openai
    # import base64
    # from openai import OpenAI
    # import csv


    # client = OpenAI(api_key="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")  # Pass key here or set it as env var



    # # Load and encode the image
    # with open("/home/shaun/Desktop/intersection/screenshot_region.png", "rb") as img_file:
    #     base64_image = base64.b64encode(img_file.read()).decode("utf-8")

    # # Call GPT-4 Vision model with image input
    # response = client.chat.completions.create(
    #     model="gpt-4o",
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": [
    #                 # {"type": "text","text": "Only extract clean CSV-style data from the table in this image. Remove slashes, dashes, extra formatting, and ignore any unrelated or surrounding text."},
    #                 {"type": "text", "text": "Extract only the raw table data from this image, no explanation or description."},
    #                 # {"type": "text", "text": "list the index number, IP address, Device Name, and Mac address in a single line per Index always split them with a comma and space"},
    #                 {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
    #             ],
    #         }
    #     ],
    #     max_tokens=500,
    # )

    # data = response.choices[0].message.content

    # print(response.choices[0].message.content)

    # overallInfo = data.replace('```', '')

    # print(overallInfo)




    # === OpenAI client setup ===


    # === Load and encode the image ===
    with open("app/utils/screenshot_region.png", "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode("utf-8")

    # === Send image to GPT-4 Vision ===
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Extract only the raw table data from this image, no explanation. "
                            "Format as: index, IP address, Device Name, MAC Address. "
                            "Ignore slashes and unrelated text."
                        ),
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                    }
                ],
            }
        ],
        max_tokens=1000,
    )

    # === Step 1: Raw GPT Output ===
    raw_data = response.choices[0].message.content
    print("\n--- Raw GPT Output ---\n")
    print(raw_data)

    # === Step 2: Clean up triple backticks and whitespace ===
    cleaned_data = raw_data.replace("```", "").strip()
    lines = cleaned_data.split('\n')

    # === Step 3: Format table with aligned columns and store in variable ===
    col_widths = [4, 18, 22, 20]
    header = ["#", "IP Address", "Device Name", "MAC Address"]

    # Build final_output as a string
    overallInfo = ""
    overallInfo += "".join(word.ljust(width) for word, width in zip(header, col_widths)) + "\n"

    # Add each cleaned data row
    for line in lines:
        if re.match(r'^\d+\s*,', line.strip()):
            parts = [part.strip() for part in line.split(",")]
            if len(parts) == 4:
                formatted_row = "".join(part.ljust(width) for part, width in zip(parts, col_widths))
                overallInfo += formatted_row + "\n"

    # === Step 4: Print the final cleaned output ===
    print("\n--- Final Aligned Output ---\n")
    print(overallInfo)