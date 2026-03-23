import yfinance as yf
import os

# Set your target buy price here
BUY_THRESHOLD = 23.00 

def check_silver():
    # SI=F is the ticker for Silver Futures
    data = yf.Ticker("SI=F")
    current_price = data.history(period="1d")['Close'].iloc[-1]
    
    print(f"Current Silver Price: ${current_price:.2f}")
    
    if current_price <= BUY_THRESHOLD:
        print("🚨 BUY ALERT: Silver is cheap!")
        # If you set up a Telegram bot later, add the send logic here
    else:
        print("Status: Above buy price. Standing by.")

if __name__ == "__main__":
    check_silver()
