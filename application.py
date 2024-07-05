import argparse
import sys

sys.path.append('./packages')

from logger import LoggerSetup
from folder_synchronization import FolderSynchronizer

class Application:
    def parse_args(self):
        # Create an argument parser for command line options
        parser = argparse.ArgumentParser(description="Synchronize two folders.")
        parser.add_argument("--source", required=True, help="Source folder path")
        parser.add_argument("--replica", required=True, help="Replica folder path")
        parser.add_argument("--interval", type=int, required=True, help="Synchronization interval in seconds")
        parser.add_argument("--log", required=True, help="Log file path")
        return parser.parse_args()
    
    def run(self):
        # Parse command line arguments
        args = self.parse_args()
        # Setup logging based on the provided log file path
        LoggerSetup.setup(args.log)
        # Initialize the FolderSynchronizer with the provided arguments and start the synchronization process
        FolderSynchronizer(args.source, args.replica, args.interval).start()

if __name__ == "__main__":
    Application().run()