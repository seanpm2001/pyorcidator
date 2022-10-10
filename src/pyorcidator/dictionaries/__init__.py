""" Loads all JSON files into a single mother dict"""

import json
import logging
from pathlib import Path
from typing import Dict, Mapping

__all__ = [
    "dicts",
    "stem_to_path",
]

logger = logging.getLogger(__name__)

HERE = Path(__file__).parent.resolve()
DEGREE_PATH = HERE.joinpath("degree.json")

JSON_PATHS = sorted(HERE.glob("*.json"))
print(JSON_PATHS)
for path in JSON_PATHS:
    logger.info("loading PyORCIDator data from %", path)

dicts: Mapping[str, Dict[str, str]] = {path.stem: json.loads(path.read_text()) for path in JSON_PATHS}
stem_to_path: Mapping[str, Path] = {path.stem: path for path in JSON_PATHS}
