import json
import os

def main():
    print(os.environ['TEST'])
    print(os.environ['TEST_JSON_PATH'])

    json_load = json.load(open(os.environ['TEST_JSON_PATH'], 'r'))
    print(json_load)
