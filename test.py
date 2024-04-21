import sqlite3
from datetime import datetime

# Path to the Firefox profile directory containing places.sqlite
firefox_profile_path = 'C:\\Users\\User\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\uqrlemz1.default-release'

# Connect to the Firefox places.sqlite database
try:
    conn = sqlite3.connect(f'{firefox_profile_path}/places.sqlite')
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

    # Print the URLs and visit dates
    for row in rows:
        url = row[0]
        title = row[1]
        visit_date = datetime.fromtimestamp(row[2] / 1000000).strftime('%Y-%m-%d %H:%M:%S')
        print(f"Title: {title}")
        print(f"URL: {url}")
        print(f"Visit Date: {visit_date}")
        print("-" * 50)

    # Close the database connection
    conn.close()

except sqlite3.Error as e:
    print(f"Error connecting to Firefox database: {e}")