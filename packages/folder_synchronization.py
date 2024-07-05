import os
import shutil
import time
import sched
import logging
from calculator import MD5Calculator

class FolderSynchronizer:
    # Initialize the FolderSynchronizer with source and replica directories and synchronization interval
    def __init__(self, source, replica, interval):
        self.source = source # Source directory to synchronize from
        self.replica = replica # Replica directory to synchronize to
        self.interval = interval # Time interval for synchronization
        self.scheduler = sched.scheduler(time.time, time.sleep) # Scheduler for periodic sync

    def sync(self):
        for root, dirs, files in os.walk(self.source): # Walk through all files in source directory
            replica_root = root.replace(self.source, self.replica, 1) # Determine corresponding path in replica
            if not os.path.exists(replica_root): # If replica directory does not exist
                os.makedirs(replica_root) # Create it
                logging.info(f"Directory created: {replica_root}")
            for file in files: # Iterate over files in current directory
                source_file = os.path.join(root, file) # Full path to source file
                replica_file = os.path.join(replica_root, file) # Full path to replica file
                # If replica file does not exist or its MD5 hash differs from source file
                if not os.path.exists(replica_file) or MD5Calculator.calculate(source_file) != MD5Calculator.calculate(replica_file):
                    shutil.copy2(source_file, replica_file) # Copy file from source to replica
                    logging.info(f"File copied: {source_file} to {replica_file}") # Log file copy
            for file in os.listdir(replica_root): # Check for files in replica that are not in source
                replica_file = os.path.join(replica_root, file) # Full path to replica file
                source_file = replica_file.replace(self.replica, self.source, 1) # Determine corresponding source file path
                if not os.path.exists(source_file): # If source file does not exist
                    # Logic to handle deletion or notification for the replica file
                    if os.path.isdir(replica_file):
                        shutil.rmtree(replica_file)
                        logging.info(f"Directory removed: {replica_file}")
                    else:
                        os.remove(replica_file)
                        logging.info(f"File removed: {replica_file}")

    def scheduled_sync(self):
        self.sync()
        # Schedule the next call
        self.scheduler.enter(self.interval, 1, self.scheduled_sync)

    def start(self):
        # Start the scheduled synchronization
        self.scheduled_sync()
        self.scheduler.run()
        logging.info("Synchronization scheduled.")