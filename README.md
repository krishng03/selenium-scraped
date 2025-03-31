# 🕸️ Selenium & BeautifulSoup Web Scraping Projects

This repository contains multiple projects that use **Selenium** and **BeautifulSoup** for web scraping. Each project scrapes data from various websites and stores the results in **CSV** and **JSON** files. Some projects may also include visualizations.

## 🚀 Setup Instructions

### 1️⃣ **Create a Virtual Environment**
Before running any project, it's recommended to create a **Python virtual environment** to manage dependencies:
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 2️⃣ **Install Dependencies**
After activating the virtual environment, install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3️⃣ **Navigate to the Project Folder**
Each project has its own folder. Navigate to the desired project before running it:
```bash
cd path/to/project_folder
```
Read the README.md inside the project folder for specific details.

### 4️⃣ **Run the Python Script**
Execute the script using Python:
```bash
python file_name.py
```
The script will scrape data from the web and save the output.

## 📁 Output Files
Each project generates data in the following formats:
- **CSV File**: `csv_file_name.csv`
- **JSON File**: `json_file_name.json`
- **Visuals** (if applicable): `img_name.png` or `charts/` directory

## 📚 Libraries Used
- **Selenium**: For browser automation and scraping dynamic content
- **BeautifulSoup**: For parsing HTML and extracting data
- **Pandas**: For data manipulation and analysis
- **Matplotlib**: For data visualization
- **Requests**: For making HTTP requests
