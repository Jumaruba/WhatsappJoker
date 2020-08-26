import pyautogui, time



print("Type the name who you wanna send the message") 
name = input() 
print("Type the message")
message = input()
print("How many times you wanna send the message")
times = int(input())

try: 
    left, top, width, height = pyautogui.locateOnScreen('search_icon.png') 
except: 
    try: 
        left, top, width, height = pyautogui.locateOnScreen('back_icon.png')
        pyautogui.click(left + 20,top + 20, left) 
        left, top, width, height = pyautogui.locateOnScreen('search_icon.png')
    except: 
        print("Search icon not found, make sure that whatsapp is opened in full screen")



# Find the person to send the message 
margin_left = 200
margin_top = 20
pyautogui.click(left + margin_left, top + margin_top); 
pyautogui.hotkey('alt', 'a', 'backspace')
pyautogui.typewrite(name) 
time.sleep(1)
pyautogui.click(left + margin_left, top + margin_top + 150);






# Send the message 
try: 
    left, top, width, height = pyautogui.locateOnScreen('emoji_icon.png') 
except: 
    print("Emoji icon not found") 

pyautogui.click(left + margin_left, top+ margin_top)


for i in range(times): 
    pyautogui.typewrite(message) 
    pyautogui.typewrite('\n')


left, top, width, height = pyautogui.locateOnScreen('back_icon.png')
pyautogui.click(left, top, left) 