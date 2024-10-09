import requests
import pandas as pd
import openpyxl
import schedule
import time
from datetime import datetime

# URL to fetch the data
url = "https://opendata.infrabel.be/explore/dataset/oorzaken-vertraging-per-maand/api/?disjunctive.verantwoordelijk"

# Function to download data and generate Excel report
def download_data():
    response = requests.get(url)
    data = response.json()
    
    # Extract relevant fields into a DataFrame
    records = []
    for item in data['records']:
        fields = item['fields']
        records.append(fields)

    df = pd.DataFrame(records)
    
    # Save the DataFrame to Excel with timestamped filename
    filename = f"delays_report_{datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx"
    df.to_excel(filename, index=False)

    print(f"Report generated: {filename}")

# Schedule the task to run every 4 hours
schedule.every(4).hours.do(download_data)

# Run the scheduling loop
while True:
    schedule.run_pending()
    time.sleep(1)
