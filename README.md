# BulkTracker

BulkTracker is a command-line interface (CLI) application designed to help users track their caloric intake and food costs during a "bulking" phase. It allows users to manage a database of food products and log their daily consumption to monitor both nutrition and budget.

## Features
* **Product Management:** Add food items with their nutritional value (kcal) and price.
* **Daily Logging:** Track what you eat and when.
* **Database:** Uses SQLite for persistent data storage.
* **Privacy:** Database configuration is separated from the code via a settings file.

## Project Structure
* `src/`: Contains the source code (database logic, models, main script).
* `data/`: Stores the SQLite database file (not included in Git).
* `settings_example.json`: A template for the configuration file.

## Installation & Setup (How to run)

To run this project locally, follow these steps:

### 1. Clone the repository

`git clone <URL_TO_YOUR_REPO>`
`cd BulkTracker`

### 2. Create a Virtual Environment
It is recommended to use a virtual environment.

`python -m venv venv`
`venv\Scripts\activate`



### 3. Install Requirements
Install the necessary Python packages.

`pip install -r requirements.txt`