import json
def load_assets() -> dict:
    """Returns key-value pairs from the json configuration file"""
    try:
        with open("cfg/assets.json", "r") as f:
            return f.json()
    except Exception as e:
        print(f"An error has been encountered while loading a file of type {type(e)}")
        exit()
def test():
    print("foo")