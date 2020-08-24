import argparse
import json

ap = argparse.ArgumentParser()
ap.add_argument('-cf', '--config_path', help = 'config file path')
args = ap.parse_args()
CONFIG_FILE_PATH = "./config/config.json" if args.config_path == None else args.config_path
with open(CONFIG_FILE_PATH) as f:
    data = json.load(f)

WEBCAMS = data['webcam']
