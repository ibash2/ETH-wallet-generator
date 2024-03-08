import os

from exceptions import DirectoryIsNotEmpty

def create_dir():
    directory = os.path.join("wallets/")
    # Проверка существования директории
    if not os.path.exists(directory):
        # Создание директории, если она не существует
        os.makedirs(directory)
    else:
        raise DirectoryIsNotEmpty()

def write_to_file(data, filename):
    with open(f"wallets/{filename}.txt", 'a') as f:
        f.write(data+"\n")

