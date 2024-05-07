import keyboard
a = keyboard.read_key()
#每当按下空格时
while True:
    if keyboard.is_pressed('space'):
        keyboard.press('a')
        break
    else:
        continue