import requests 
import tkinter as tk

def conver_currency():
    MainCurrency = entry_from_currency.get().strip().upper()
    Currency_Need_Convert = entry_to_currency.get().strip().upper()
    user_amount = int(entry_amout_currency.get())
    api_url = f"https://v6.exchangerate-api.com/v6/8b728582c2ec153eaa5dae44/latest/{MainCurrency}"
    respone = requests.get(api_url)
    if respone.status_code == 200:
        data = respone.json()
        datakey = data["conversion_rates"]
        money_rate_value = datakey[Currency_Need_Convert]
        convert_Currency = user_amount * money_rate_value
        result_label.config(text=f"The {user_amount} {MainCurrency} = {convert_Currency:.3} {Currency_Need_Convert}")
    else:
        result_label.config(text="Sorry You Have Problem In Your Internet Try Again Later")


root = tk.Tk()
root.title("Money Convert")
root.geometry("500x400")

label_from = tk.Label(root , text="Please Enter The Currency You Want To Convert From:")
label_from.pack()

entry_from_currency = tk.Entry(root)
entry_from_currency.pack()


label_to = tk.Label(root , text="Please Enter The Currency You want To Convert To: ")
label_to.pack()

entry_to_currency = tk.Entry(root)
entry_to_currency.pack()

label_amount = tk.Label(root , text="Please Enter The Amount You Want To Convert: ")
label_amount.pack()

entry_amout_currency = tk.Entry(root)
entry_amout_currency.pack()

convert_button = tk.Button(root , text="Convert" , command=conver_currency)
convert_button.pack()

result_label = tk.Label(root , text="Converted Amount will be shown here")
result_label.pack()

root.mainloop()


