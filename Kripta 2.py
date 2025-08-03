import requests  # сделаем запрос
import json # в формате джейсон
#import pprint
from tkinter import *
from tkinter import messagebox as mb


def exchange():
    code = entry.get()

    if code:
        try:
            response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd")
            response.raise_for_status()
            data = response.json()
            if code in data["rates"]:
                exchange_rate = data["rates"][code]
                mb.showinfo("Курс обмена криптовалюты", f"Курс:{exchange_rate} {code} за 1 доллар")
            else:
                mb.showerror("Ошибка!", f"Криптовалюта {code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите название криптовалюты")


window = Tk()
window.title("Курс криптовалют")
window.geometry("400x200")

Label(text="Введите название криптовалюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена криптовалюты к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()



