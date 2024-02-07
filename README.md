# Akemu-Python-A-keystroke-emulator-
Программа, которая эмулирует процесс ввода текста, скопированного в буфер обмена, с задержкой между нажатиями клавиш.

Эта программа на Python выполняет следующие действия:
1) Импортирует необходимые модули:
  pyperclip для работы с буфером обмена,
  keyboard для эмуляции нажатий клавиш,
  time для работы со временем
  random для генерации случайных чисел.

2) Определяет функцию type_text, которая принимает строку buffer в качестве аргумента. Эта функция перебирает каждый символ в buffer и, если не нажата клавиша ‘p’, эмулирует нажатие этого символа с задержкой от 0.095 до 0.15 секунды. Если нажата клавиша ‘p’, функция выводит сообщение “Программа остановлена” и прекращает ввод.

3) Считывает текст из буфера обмена и сохраняет его в переменную text.

4) Выводит на экран сообщение “Ваш скопированный текст:” и затем сам скопированный текст.

5) Ждет 5 секунд.

6) Снова считывает текст из буфера обмена и сохраняет его в переменную buffer.

7) Вызывает функцию type_text с buffer в качестве аргумента.

В общем, эта программа эмулирует процесс ввода текста, скопированного в буфер обмена, с задержкой между нажатиями клавиш. Это может быть полезно, например, для автоматизации ввода текста в приложениях, которые не поддерживают вставку из буфера обмена.

Чтобы запустить эту программу, выполните следующие шаги:

1) Установите Python, если он еще не установлен. Вы можете скачать его с официального сайта Python.
	https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe

2) Установите необходимые библиотеки. Откройте командную строку или терминал и введите следующие команды:
   pip install pyperclip
   pip install keyboard

Важно: Использование этого кода может нарушать политику безопасности некоторых систем или приложений. Пожалуйста, используйте его ответственно и только в тех случаях, когда у вас есть явное разрешение на эмуляцию ввода с клавиатуры.

A program that emulates the process of typing text copied to the clipboard with a delay between keystrokes.

This Python program performs the following actions:

1) Imports the necessary modules: pyperclip to work with the clipboard, keyboard to emulate keystrokes, time to work with time, random to generate random numbers.

2) Defines the type_text function, which takes the buffer string as an argument. This function iterates through each character in buffer and, if the ‘p’ key is not pressed, emulates pressing this character with a delay of 0.095 to 0.15 seconds. If the ‘p’ key is pressed, the function displays the message “The program is stopped" and stops typing.

3) Reads text from the clipboard and saves it to the text variable.

4) Displays the message “Your copied text:” and then the copied text itself.

5) It waits for 5 seconds.

6) Reads the text from the clipboard again and saves it to the buffer variable.

7) Calls the type_text function with buffer as an argument.

8) In general, this program emulates the process of typing text copied to the clipboard, with a delay between keystrokes. This can be useful, for example, to automate text input in applications that do not support pasting from the clipboard.

To run this program, follow these steps:

1) Install Python if it is not already installed. You can download it from the official Python website.
   https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe

3) Install the necessary libraries. Open a command prompt or terminal and type the following commands:
   pip install pyperclip
   pip install keyboard
Important: Using this code may violate the security policy of some systems or applications. Please use it responsibly and only in cases where you have explicit permission to emulate keyboard input.
