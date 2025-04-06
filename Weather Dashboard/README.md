# 🌤️ Live Weather Dashboard using Streamlit + Selenium

This project is a **live weather data dashboard** built using **Streamlit** and powered by **Selenium-based scraping** to fetch real-time weather updates for any location worldwide.


## 🚀 How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/krishng03/selenium-scraped.git
cd '.\Weather Dashboard\'
```

### 2️⃣ Install Required Packages

Make sure you have Python 3.7+ and install the necessary dependencies:

```bash
pip install -r requirements.txt
```


---

### 3️⃣ Run the App

```bash
streamlit run weather_dashboard.py
```

It will open the app in your browser at `http://localhost:8501/`.

---

## ⚙️ Files Explained

### 🔹 `weather_dashboard.py`

This is the **main Streamlit application**. It takes user input (location), scrapes live weather data, and displays it beautifully using:
- `st.metric` for key stats
- Styled text and markdown
- Tabular data from scraped parameters

### 🔹 `weather_scraper.py`

Contains the **scraping logic** using `Selenium`. It handles:
- Navigating to the weather site
- Extracting current temperature, weather description, min/max temp, and additional data
- Returning all this data in a structured `dict` format


### 🔹 `weather_data.json`

A **non-functional file** that shows the sample output/response structure you get from the scraper. Useful for understanding the data format and fields like:

```json
{
  "current_temp": "29°C",
  "feels_like_temp": "31°C",
  "weather_quickie": "Partly Cloudy",
  "low_temp": "27°C",
  "high_temp": "33°C",
  "cards": [
    {
      "title": "Humidity",
      "body": "70%"
    },
    ...
  ],
  "additional_data": [
    {
      "param": "Visibility",
      "value": "10 km"
    },
    ...
  ]
}
```

---

Feel free to fork and enhance the dashboard. Contributions welcome! 🌍🌤️
