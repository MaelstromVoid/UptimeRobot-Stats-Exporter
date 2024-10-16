# UptimeRobot Stats Exporter


## Overview

The **UptimeRobot Stats Exporter** is a Python script designed to fetch uptime statistics from UptimeRobot's public stats page and export the collected data to an Excel file. This tool allows users to analyze the performance of their monitored services easily.

## Features

- Fetch uptime data for specific monitor codes.
- Support for retrieving data from multiple pages.
- Export data into a user-friendly Excel format.

## Requirements

- Python 3.x
- Required libraries:
  - `requests`
  - `pandas`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/MaelstromVoid/UptimeRobot-Stats-Exporter.git
   cd UptimeRobot-Stats-Exporter
   ```

2. Install the required libraries:
   ```bash
   pip3 install libraries_name
   ```

## Usage

To run the script, use the following command structure:

```bash
python3 uptime_exporter.py <monitor_code> [--max_pages <number_of_pages>]
```

### Parameters

- `<monitor_code>`: The unique monitor code from the UptimeRobot stats URL (e.g., `aAAaaaAAA0`).
- `--max_pages <number_of_pages>` (optional): Specify the number of pages to fetch (default is 1).

### Examples

1. Fetch uptime data for a specific monitor (e.g., `aAAaaaAAA0` from https://stats.uptimerobot.com/aAAaaaAAA0) and save it to an Excel file:
   ```bash
   python3 uptime_exporter.py aAAaaaAAA0
   ```

2. Fetch uptime data for the same monitor but for multiple pages (e.g., 10 pages):
   ```bash
   python3 uptime_exporter.py aAAaaaAAA0 --max_pages 10
   ```

## Output

The script will generate an Excel file named `uptime_report.xlsx` in the same directory, containing the uptime data organized by application names and days.

## License

This project is licensed under the Creative Commons Zero v1.0 Universal.

## Acknowledgments

- UptimeRobot for providing the monitoring service.
- Pandas and Requests libraries for making data manipulation and HTTP requests easier.
