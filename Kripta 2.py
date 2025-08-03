import requests  # сделаем запрос
import json # в формате джейсон
#import pprint
from tkinter import *
from tkinter import messagebox as mb




window = Tk()
window.title("Курс криптовалют")
window.geometry("400x200")

Label(text="Введите название криптовалюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена криптовалюты к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()

result = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd") # выводим данные из сайта
data = json.loads(result.text)
p = pprint.PrettyPrinter(indent=4)

p.pprint(data)