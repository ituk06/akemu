"""
Этот модуль реализует приложение Akemu для работы с буфером обмена.
Программа автоматически отслеживает изменения в буфере обмена и позволяет воспроизводить текст,
состоящий в буфере, с помощью виртуальной клавиатуры.
"""
import random
import time
import pyperclip
import keyboard
import customtkinter


class Akemu(customtkinter.CTk):
    """
    Главное окно приложения Akemu, которое отображает таймер,
    буфер обмена и кнопки для запуска действий.
    """
    def __init__(self, *args, **kwargs):
        """
        Инициализация главного окна.
        """
        super().__init__(*args, **kwargs)

        self.title("Akemu")
        self.geometry("355x380")
        self.grid_columnconfigure(0, weight=1)
        self.resizable(width=False, height=False)
        self.attributes('-topmost', 1)

        logo_label = customtkinter.CTkLabel(
            self, text="Буфер обмена", font=customtkinter.CTkFont(size=20, weight="bold")
        )
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 0))

        self.countdown_label = customtkinter.CTkLabel(
            self, text="00:03", font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.countdown_label.grid(row=0, column=1, padx=(95, 20), pady=(20, 0))

        self.textbox = customtkinter.CTkTextbox(self, width=300, height=240)
        self.textbox.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="nsew", columnspan=2)
        self.textbox.insert("0.0", pyperclip.paste())
        self.textbox.configure(state='disabled')

        button = customtkinter.CTkButton(self, text="Начать", command=self.execute_commands)
        button.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        self.clipboard_content = pyperclip.paste()
        self.check_clipboard()

        keyboard.add_hotkey('ctrl + b', self.execute_commands_hotkey)

    def execute_commands_hotkey(self) -> None:
        """
        Запускает выполнение команд с задержкой при нажатии горячей клавиши.
        """
        time.sleep(0.5)
        self.start_typing()

    def execute_commands(self) -> None:
        """
        Запускает выполнение команд после отсчета времени.
        """
        self.start_countdown()
        self.after(4000, self.start_typing)

    def start_countdown(self) -> None:
        """
        Начинает отсчет времени.
        """
        self.countdown(3)

    def countdown(self, count: int) -> None:
        """
        Отсчитывает время и обновляет метку на экране.
        """
        if count >= 0:
            mins, secs = divmod(count, 60)
            timer = f'{mins:02d}:{secs:02d}'
            self.countdown_label.configure(text=timer)
            self.after(1000, self.countdown, count - 1)
        else:
            self.countdown_label.configure(text="00:03")

    @staticmethod
    def type_text(buffer: str) -> None:
        """
        Печатает текст из буфера обмена с задержкой.
        """
        for character in buffer:
            if keyboard.is_pressed('p'):
                break
            keyboard.write(character, delay=random.uniform(0.095, 0.15))

    def start_typing(self) -> None:
        """
        Начинает печатать текст из буфера обмена.
        """
        buffer = pyperclip.paste()
        self.type_text(buffer)

    def check_clipboard(self) -> None:
        """
        Проверяет буфер обмена на изменения.
        """
        new_clipboard_content = pyperclip.paste()
        if new_clipboard_content != self.clipboard_content:
            self.clipboard_content = new_clipboard_content
            self.update_textbox()
        self.after(1000, self.check_clipboard)

    def update_textbox(self) -> None:
        """
        Обновляет текст в поле ввода.
        """
        current_position = self.textbox.index('insert')
        self.textbox.configure(state='normal')
        self.textbox.delete('1.0', 'end')
        self.textbox.insert('1.0', self.clipboard_content)
        self.textbox.configure(state='disabled')
        self.textbox.see(current_position)


if __name__ == "__main__":
    app = Akemu()
    app.mainloop()
