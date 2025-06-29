import os
import requests
import pandas as pd
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# === CONFIG ===
load_dotenv()
API_KEY = os.getenv("API_KEY")
CITY = "San Jose"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
DB_NAME = "weather_data.db"

# === STEP 1: EXTRACT ===
response = requests.get(URL)
print(response.status_code)
data = response.json()

if response.status_code != 200 or 'name' not in data:
    print("❌ API error:", data)
    exit()

# === STEP 2: TRANSFORM ===
weather = {
    "city_name": data["name"],
    "date_time": datetime.utcfromtimestamp(data["dt"]),
    "temperature_c": data["main"]["temp"],
    "humidity_percent": data["main"]["humidity"],
    "weather_condition": data["weather"][0]["description"]
}

df = pd.DataFrame([weather])
print(df)

# === STEP 3: LOAD ===
conn = sqlite3.connect(DB_NAME)
df.to_sql("weather", conn, if_exists="append", index=False)

# === STEP 4: VISUALIZE ===
history_df = pd.read_sql_query("SELECT * FROM weather", conn)
conn.close()

history_df["date_time"] = pd.to_datetime(history_df["date_time"])

plt.figure(figsize=(10, 5))
plt.plot(history_df["date_time"], history_df["temperature_c"], marker='o', label="Temperature (°C)")
plt.plot(history_df["date_time"], history_df["humidity_percent"], marker='s', label="Humidity (%)")
plt.xlabel("Datetime")
plt.ylabel("Values")
plt.title(f"Weather Trends in {CITY}")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("images/latest_weather_plot.png")
plt.close()

print("✅ Data loaded and chart saved: images/latest_weather_plot.png")
