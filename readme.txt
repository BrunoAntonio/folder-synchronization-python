Description
This project consists of two main scripts: calculator.py and folder_synchronization.py. The calculator.py script is used to calculate the MD5 hash of files, ensuring data integrity during the synchronization process. The folder_synchronization.py script synchronizes files between a source and a replica directory, using the MD5 hash to detect changes. Another script is used to log the changes.

Installation
To use this project ensure you have Python 3.7 installed on your system. No additional libraries are required beyond the Python Standard Library.

1. Clone the repository or download the scripts to your local machine.
2. Ensure the scripts are in the same directory or adjust the import path accordingly.

Usage
To start the folder synchronization, run the following command in your terminal:
python folder_synchronization.py <source_directory> <replica_directory> <sync_interval_in_seconds>

Replace <source_directory>, <replica_directory>, and <sync_interval_in_seconds> with your desired values.
Example: python application.py --source source_folder --replica replica_folder --interval 6 --log logs\sync_log.txt

To start the unit tests, run the following command in your terminal (from the project_root): python -m unittest discover

Folder Structure:

project_root/
|application.py # Script to run the application
|readme.txt # Description of the project
│
├── packages/ # Source files
│   ├── calculator.py # MD5 hash calculator script
│   └── folder_synchronization.py # Folder synchronization script
|   └── logger.py # Logger script
│
├── tests/ # Unit tests
│   ├── test_calculator.py # Tests for calculator.py
    └── test_folder_synchronization.py # Tests for folder_synchronization.py

