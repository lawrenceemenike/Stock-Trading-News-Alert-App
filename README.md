# Stock-Trading-News-Alert-App
A Python app that fetches real-time stock data and relevant news articles using API endpoints.

# What It Does
- The app retrieves current stock prices from Alpha Vantage API
- It also fetches related news articles from News API
- It calculates price changes and percentages, displays stock info and top 3 news headlines in a GUI

# Why I Built This
To learn:
- How to interact with multiple APIs in a single application
- Handling JSON responses from different sources
- Building a GUI that integrates live data
- Proper structuring of API requests with parameters

# How to Use
- Clone the repository
- Install requirements: pip install requests tkinter
- Replace ALPHA_VANTAGE_API_KEY and NEWS_API_KEY with your own API keys
- Run python main.py
- Enter a stock symbol (e.g., TSLA) and click "Search"

# What I Learned
- Most importanlty i learnt how to structure API requests with proper parameters
- Error handling for API calls
_ This is my first app using two API's. I learnt Parsing and integrating data from multiple sources
- Creating a responsive GUI with Tkinter
- Working with financial and news data APIs, something I am passionate about and looking to build more apps around

# Next Steps
Add more detailed stock information (e.g., volume, market cap)
Implement caching to reduce API calls
Create alerts for significant price changes
Add charts or graphs for visual representation of data

This project serves as a practical example of building a data-driven application using public APIs. Feel free to use it as a starting point for your own API-based projects!
