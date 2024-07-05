import hashlib

class MD5Calculator:
    @staticmethod
    def calculate(file_path):
        # Initialize MD5 hash object
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            # Read the file in chunks to handle large files
            for chunk in iter(lambda: f.read(4096), b""):
                # Update the hash with the chunk
                hash_md5.update(chunk)
        # Return the hexadecimal digest of the hash
        return hash_md5.hexdigest()