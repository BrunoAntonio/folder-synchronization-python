import logging
import os

# Define a class to encapsulate the setup of the application's logging system
class LoggerSetup:
    @staticmethod
    def setup(log_file_path):
        """
        Configures the logging system to write logs to both a file and the console (static method).
        :param log_file_path: The path to the file where logs should be written.
        """
        # Ensure the directory for the log file exists, create it if necessary
        log_dir = os.path.dirname(log_file_path)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        # Initialize the logging system with a specific configuration
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler()
        ])