from pathlib import Path
import yaml

config_path = Path("configs/paths.yaml")

with open(config_path, "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

cfosat_data = Path(config["cfosat_data"])

print("CFOSAT data path:")
print(cfosat_data)

print("Path exists:")
print(cfosat_data.exists())
