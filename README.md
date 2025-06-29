# ☁️ Weather ETL Pipeline (San Jose)

This project is an end-to-end **ETL (Extract, Transform, Load)** pipeline that fetches live weather data for **San Jose, CA**, stores it in a local SQLite database, and generates a visual plot of temperature and humidity.

---

## 📌 Project Features

- ✅ **Extract**: Connects to the OpenWeatherMap API to get current weather
- ✅ **Transform**: Parses the JSON response to extract key metrics
- ✅ **Load**: Appends the transformed data to a local `SQLite` database
- ✅ **Visualize**: Creates and saves a line plot using `matplotlib`
- ✅ **Schedule-ready**: Designed to run automatically with a cron job

---

## 📊 Sample Output

**Weather Conditions Stored**:
- City Name
- Date & Time (UTC)
- Temperature (°C)
- Humidity (%)
- Weather Description (e.g., "few clouds")

**Example:**

```text
city_name  |     date_time      | temperature_c | humidity_percent | weather_condition
-----------|--------------------|---------------|------------------|-------------------
San Jose   | 2025-06-29 16:15:02|     21.36     |        58        |    few clouds

Technologies Used
- Python 3.9
- OpenWeatherMap API
- SQLite3
- Pandas
- Matplotlib
- Cron (for scheduling)


Setup Instructions:
1. Clone the repository
git clone https://github.com/gwibzzz/weather-etl-project.git
cd weather-etl-project

2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Set your API key
OPENWEATHER_API_KEY=your_actual_key_here

5. Automate with Cron
crontab -e
0 7 * * * /full/path/to/venv/bin/python /full/path/to/weather_etl.py


Directory Structure:
weather-etl-project/
├── weather_etl.py
├── weather_data.db
├── images/
│   └── latest_weather_plot.png
├── .env
├── .gitignore
├── requirements.txt
└── README.md


Next Ideas:
- Multi-city weather ETL
- Export to CSV or Google Sheets
- Cloud deployment (e.g., AWS Lambda, Azure Function)

Author
Erin Gribi
📍 Business + Analytics graduate
🐱 Cat lover, data explorer
🌸 https://www.linkedin.com/in/erin-gribi/

License
This project is open-source and available under the MIT License.