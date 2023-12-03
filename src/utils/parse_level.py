from pathlib import Path
import json

def get_level_config(level_id):
    assets = Path(Path.cwd() / "assets" / "levels")
    levels = sorted(assets.iterdir())
    if level_id < len(levels):
        level_filename = levels[level_id]
        with level_filename.open() as F:
            level_config = json.load(F)
            return level_config
        
