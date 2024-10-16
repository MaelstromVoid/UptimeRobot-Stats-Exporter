import requests
import pandas as pd
import argparse

def fetch_uptime_data(monitor_code, max_pages=1):
    """
    Fetch uptime data from the UptimeRobot stats page API for a specific monitor.

    :param monitor_code: The unique code from the UptimeRobot stats page URL.
    :param max_pages: The number of pages to fetch (default is 1).
    :return: A Pandas DataFrame with all the collected data.
    """

    data_dict = {}
    base_url = f'https://stats.uptimerobot.com/api/getMonitorList/{monitor_code}'

    for page in range(1, max_pages + 1):
        url = f'{base_url}?page={page}'
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01'
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            monitors = data['psp']['monitors']

            if not data_dict:
                days = data['days']

            for monitor in monitors:
                name = monitor['name']
                daily_ratios = monitor['dailyRatios']
                ratios = [ratio['ratio'] for ratio in daily_ratios]
                data_dict[name] = ratios
        else:
            print(f"Error fetching data from page {page}: {response.status_code}")
            break
    df = pd.DataFrame.from_dict(data_dict, orient='index', columns=days)
    return df

def export_to_excel(df, file_name='uptime_report.xlsx'):
    """
    Export the DataFrame to an Excel file.

    :param df: The Pandas DataFrame to export.
    :param file_name: The name of the output Excel file (default is 'uptime_report.xlsx').
    """

    df.to_excel(file_name, index=True, index_label="Application")
    print(f"Export complete: {file_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to fetch UptimeRobot stats and export them to Excel.")
    parser.add_argument("monitor_code", type=str, help="The unique monitor code from the UptimeRobot stats URL.")
    parser.add_argument("--max_pages", type=int, default=1, help="The number of pages to fetch (default: 1).")
    args = parser.parse_args()
    df = fetch_uptime_data(monitor_code=args.monitor_code, max_pages=args.max_pages)
    export_to_excel(df)
