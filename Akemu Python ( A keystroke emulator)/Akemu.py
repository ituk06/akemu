import pyperclip #pyperclip для работы с буфером обмена 
import keyboard #keyboard для эмуляции нажатий клавиш
import time #time для работы со временем 
import random #random для генерации случайных чисел.
def type_text(buffer): 
    for character in buffer: 
        if keyboard.is_pressed('p'): 
            print('Программа остановлена') 
            break 
        keyboard.write(character, delay = random.uniform(0.095, 0.15)) #
text = pyperclip.paste() 
print('Ваш скопированный текст:') 
print(text) 
time.sleep(5) 
buffer = pyperclip.paste() 
type_text(buffer) 
