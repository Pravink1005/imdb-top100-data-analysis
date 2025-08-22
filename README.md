# 🎬 IMDb Top 100 Movies Analysis (from Top 250)

## 📌 Project Overview
This project scrapes data from IMDb's **Top 250 Movies list**, but focuses only on the **Top 100 movies** for analysis.  
The dataset is enriched with the OMDb API, cleaned, and analyzed using Python.  
The results are also exported to Excel and can be connected to **Power BI** for interactive dashboards.

---

## ⚙️ Project Workflow
1. **Scraping IMDb**  
   - `scripts/get_top100.py` → Collects the **Top 100 movies** (title + IMDb ID) from IMDb's Top 250 list.  
   - `scripts/scraper.py` → Fetches detailed movie data (ratings, genre, runtime, box office, etc.) via the OMDb API.  

2. **Exploratory Data Analysis (EDA)**  
   - `scripts/analyze_in_python.py` → Cleans and analyzes the dataset with **Pandas, Seaborn, Matplotlib**.  
   - Generates:  
     - Rating distribution  
     - Genre popularity  
     - Box office vs rating  
     - Runtime distribution  
     - Ratings by decade  
     - Correlation heatmap  

3. **Reporting**  
   - Exports analysis results to:  
     - `data/omdb_top100.csv` → Raw scraped dataset (Top 100 movies).  
     - `reports/imdb_analysis_summary.xlsx` → Excel report with raw data, summary stats, and key insights.  

---

## 📊 Example Insights
- **Average IMDb Rating**: ~8.5  
- **Highest Rated Movie**: *The Shawshank Redemption* (9.3)  
- **Lowest Rated Movie**: *Toy Story* (8.3)  
- **Most Common Genre**: Drama  
- **Average Runtime**: ~137 minutes  
- **Average Box Office**: ~$129M  

---

## 🛠️ Tech Stack
- **Python**: Pandas, Seaborn, Matplotlib, Requests  
- **APIs**: IMDb, OMDb  
- **Power BI** (for dashboard visualization)  
- **Excel Reports** via `openpyxl`  

---

## 🚀 How to Run

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt

2️⃣ Scrape IMDb Data
python scripts/get_top100.py
python scripts/scraper.py

3️⃣ Run Analysis (EDA + Export to Excel)
python scripts/analyze_in_python.py


📂 Project Structure
imdb_movie_analysis/
│
├── data/
│   ├── omdb_top100.csv              # Scraped dataset (Top 100 from IMDb Top 250)
│
├── reports/
│   └── imdb_analysis_summary.xlsx   # Excel report with insights
│
├── scripts/
│   ├── get_top100.py                # Fetch Top 100 from IMDb Top 250
│   ├── scraper.py                   # Scrape details via OMDb
│   └── analyze_in_python.py         # EDA + Excel export
│
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation

Developed by Pravin Kumar A
MSc Data Science & Business Analysis 🎓