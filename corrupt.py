import os
import random
import shutil
import logging

path = "./toCorrupt"
corruptedPath = "./Corrupted"
backupPath = "./Backup"

# if backup directory does not exist, create it
if not os.path.exists(backupPath):
    os.makedirs(backupPath)

# Set up logging
logging.basicConfig(filename="file_corruption.log", level=logging.INFO)

files = os.listdir(path)

for file in files:
    if os.path.exists(corruptedPath + "/" + file):
        continue
    try:
        with open(path + "/" + file, "rb") as f:
            data = bytearray(f.read())
        # Backup the file before corrupting it
        shutil.copy(path + "/" + file, backupPath + "/" + file)
        # Corrupt the file by replacing all bytes with random bytes
        for i in range(len(data)):
            data[i] = random.randint(0, 255)
        with open(corruptedPath + "/" + file, "wb") as f:
            f.write(data)
        os.remove(path + "/" + file)
        print("Corrupted:", file)
        logging.info(f"Corrupted: {file}")
    except Exception as e:
        print(f"Error corrupting {file}: {e}")
        logging.error(f"Error corrupting {file}: {e}")

print("Done")
