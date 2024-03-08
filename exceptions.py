class DirectoryIsNotEmpty(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args, "Directory is not empty!!! Please move your wallets to another directory")