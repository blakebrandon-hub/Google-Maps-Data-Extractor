# 🗺️ Google Maps Data Extractor

![gmaps_github](https://github.com/blakebrandon-hub/Google-Maps-Data-Extractor/assets/50201165/dfb9c5de-43d3-44c7-b2dc-0b5ae34d2b4d)

A Python script that automates the extraction of data from Google Maps search results and exports it to a CSV file.

## 🌟 Features

- **Automated Data Extraction:** Input any search query (e.g., "breweries in Austin, Texas") and retrieve relevant data from Google Maps.
- **CSV Export:** Extracted data is neatly organized and exported to a CSV file for easy analysis and reference.

## 🛠️ Technologies Used

- **Python:** Core programming language.
- **Requests:** For sending HTTP requests to retrieve web pages.
- **BeautifulSoup:** For parsing HTML content and extracting information.

## 🔧 Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/blakebrandon-hub/Google-Maps-Data-Extractor.git
    cd Google-Maps-Data-Extractor
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Script:**

    ```bash
    python lead_generator.py
    ```

5. **Provide Input:**
   - Enter a search query (e.g., ```search_query = "breweries in Austin, Texas"```).
   - The script will process the search results and export the data to a CSV file named `results.csv`.
  
## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for details.

## ⚠️ Important Notes

- **Ethical Use:** Ensure you have the right to scrape the data and that your actions comply with Google's Terms of Service.
- **Rate Limiting:** To avoid being blocked, consider implementing delays between requests.
- **Data Accuracy:** The accuracy of the extracted data depends on the structure of the Google Maps pages and may vary if the structure changes.
