import sqlite3
import requests
from datetime import datetime
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# VirusTotal API key
API_KEY = os.getenv('API_KEY')

# Path to the Firefox profile directory containing places.sqlite
firefox_profile_path = 'C:\\Users\\ARYAN KUMAR\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\q72qvwky.default-release-1713718247832'

# Connect to the Firefox places.sqlite database
try:
    conn = sqlite3.connect(f'{firefox_profile_path}\\places.sqlite')
    cursor = conn.cursor()

    # SQL query to retrieve URL visit information
    query = """
    SELECT moz_places.url, moz_places.title, moz_historyvisits.visit_date
    FROM moz_places
    INNER JOIN moz_historyvisits ON moz_places.id = moz_historyvisits.place_id
    ORDER BY moz_historyvisits.visit_date DESC
    """

    # Execute the query
    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Print the URLs, visit dates, and check for maliciousness using VirusTotal API
    for row in rows:
        url = row[0]
        title = row[1]
        visit_date = datetime.fromtimestamp(row[2] / 1000000).strftime('%Y-%m-%d %H:%M:%S')
        print(f"Title: {title}")
        print(f"URL: {url}")
        print(f"Visit Date: {visit_date}")
        
        # VirusTotal API request
        params = {'apikey': API_KEY, 'resource': url}
        response = requests.get('https://www.virustotal.com/vtapi/v2/url/report', params=params)
        
        try:
            result = response.json()
            if result['response_code'] == 1:
                if result['positives'] > 0:
                    print("This URL is malicious!")
                else:
                    print("This URL is not malicious.")
            else:
                print("Scan result not available.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON response for URL: {url}")
        except KeyError:
            print(f"Error: Unexpected response from VirusTotal API for URL: {url}")
            
        print("-" * 50)

    # Close the database connection
    conn.close()

except sqlite3.Error as e:
    print(f"Error connecting to Firefox database: {e}")
