import pyautogui
import time
import pyperclip
from openai import OpenAI

# if the last message in the chat log is from perticuar sender
def isLast_msg_frm_sender(chat_log, sender_name="Aditya Badgotiya"):
    # last message by splitting chatlog and checking the sender name
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True
    return False

# OpenAI client
client = OpenAI(
    api_key="",  # use your API key
)

# Click to focus on the chat application
pyautogui.click(1639, 1412)  # Coordinates should point to the chat window
time.sleep(2)  # Wait for chat to open

# Start loop for responding to chat
while True:
    pyautogui.moveTo(1003, 237)  # Start of chat area
    pyautogui.dragTo(2187, 1258, duration=1.0, button='left')  # Drag to select the chat
    pyautogui.hotkey('ctrl', 'c')  # Copy selected text
    time.sleep(1)

    pyautogui.click(1994, 281)  # Click to deselect

    # copied chat from the clipboard
    chatHistory = pyperclip.paste()
    print(chatHistory)

    # Check if the last message is from the sender
    if isLast_msg_frm_sender(chatHistory):

        # response generation
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Ayush, a coder from India who speaks both Hindi and English. "
                        "You analyze the chat history provided and respond naturally, reflecting your personality. "
                        "Output should be in the tone of Ayush and be limited to a single text message response."
                    ),
                },
                {"role": "user", "content": chatHistory},
            ],
        )

        # Extract the AI response
        response = completion.choices[0].message.content
        pyperclip.copy(response)  # Copy the response to clipboard

        
        pyautogui.click(1088, 1328)  # Click on the chat input box
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')  # Paste the AI response
        time.sleep(1)
        pyautogui.press('enter')  # Press Enter to send the message

    time.sleep(5)
