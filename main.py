import requests
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

ALPHA_VANTAGE_API_KEY = "PQOM599FL73XUAWR"
NEWS_API_KEY = "c0c87be9fe1a4e56ae835a932397d408"

class StockNewsApp:
    def __init__(self, master):
        self.master = master
        master.title("Stock News Alert")
        master.geometry("600x400")

        self.stock_label = ttk.Label(master, text="Enter Stock Symbol:")
        self.stock_label.pack(pady=10)

        self.stock_entry = ttk.Entry(master)
        self.stock_entry.pack()

        self.search_button = ttk.Button(master, text="Search", command=self.get_stock_news)
        self.search_button.pack(pady=10)

        self.result_text = tk.Text(master, height=15, width=70)
        self.result_text.pack(pady=10)

    def get_stock_news(self):
        stock_symbol = self.stock_entry.get().upper()
        if not stock_symbol:
            messagebox.showerror("Error", "Please enter a stock symbol")
            return

        # Get stock data
        stock_params = {
            "function": "GLOBAL_QUOTE",
            "symbol": stock_symbol,
            "apikey": ALPHA_VANTAGE_API_KEY
        }
        stock_url = 'https://www.alphavantage.co/query'
        try:
            stock_response = requests.get(stock_url, params=stock_params)
            stock_response.raise_for_status()
            stock_data = stock_response.json()

            if "Global Quote" not in stock_data or not stock_data["Global Quote"]:
                messagebox.showerror("Error", "Unable to fetch stock data. Please check the stock symbol and try again.")
                return

            current_price = float(stock_data["Global Quote"]["05. price"])
            previous_close = float(stock_data["Global Quote"]["08. previous close"])

            price_change = current_price - previous_close
            price_change_percent = (price_change / previous_close) * 100

            # Get news
            yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
            news_params = {
                "q": stock_symbol,
                "from": yesterday,
                "sortBy": "popularity",
                "apiKey": NEWS_API_KEY
            }
            news_url = 'https://newsapi.org/v2/everything'
            news_response = requests.get(news_url, params=news_params)
            news_response.raise_for_status()
            news_data = news_response.json()

            if news_data["status"] != "ok" or not news_data["articles"]:
                messagebox.showerror("Error", "Unable to fetch news data.")
                return

            # Format and display result
            result = f"{stock_symbol}: {'🔺' if price_change >= 0 else '🔻'}{abs(price_change_percent):.2f}%\n\n"
            for article in news_data["articles"][:3]:
                result += f"Headline: {article['title']}\n"
                result += f"Brief: {article['description']}\n\n"

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result)

        except requests.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockNewsApp(root)
    root.mainloop()