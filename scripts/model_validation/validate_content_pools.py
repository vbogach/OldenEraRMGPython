import json
from pathlib import Path

from loguru import logger

from olden_era.models.content_pool import ContentPool


def main():
    data_root = Path(r"C:\Users\vbogach\Documents\olden_era\data\content_pools")
    json_paths = list(data_root.rglob("*.json"))

    for json_path in json_paths:
        with open(json_path, "r") as f:
            data = json.load(f)

        # logger.info(f"Validating {json_path}...")
        for entry in data:
            try:
                validated = ContentPool.model_validate(entry)
                # logger.info(f"Validated {validated.name}")
            except Exception as e:
                logger.error(e)


if __name__ == "__main__":
    main()
