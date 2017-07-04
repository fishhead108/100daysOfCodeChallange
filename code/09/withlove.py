

class TCBlock:

    def __init__(self, block_name):
        self.block_name = block_name

    def __enter__(self):
        print(f"##Beginning of {self.block_name} block")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"##Ending of {self.block_name} block")


with TCBlock("docker build"):
    print("First level")
    print("First level")

    with TCBlock("Inner"):
        print("Second level")
        print("Second level")
