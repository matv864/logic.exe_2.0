import time
import json
from pathlib import Path

PATH_TO_RECORD = Path(Path.cwd() / "assets" / "game_data" / "record.txt")
PATH_TO_SAVING = Path(Path.cwd() / "assets" / "game_data" / "saving.txt")


def save_record(record_score: int) -> None:
    with PATH_TO_RECORD.open("w") as F:
        F.write(str(record_score))


def get_record() -> int:
    with PATH_TO_RECORD.open("r") as F:
        return int(F.read())

# sorry for bad typing (circle of import),
# object is GameConfig from utils/game_config.py


def save_result(config: object) -> None:
    saving = {
        "level": config.level,
        "lifes": config.lifes,
        "time_from_start": int(time.time() - config.start_time)
    }
    with PATH_TO_SAVING.open("w") as F:
        json.dump(saving, F)


def set_saving_result(config: object) -> None:
    with PATH_TO_SAVING.open("r") as F:
        text_of_file = F.read()
        saving = json.loads(text_of_file)
        config.level = saving["level"]
        config.lifes = saving["lifes"]
        config.start_time = time.time() - saving["time_from_start"]
        config.update_score()

# methods to getting and saving game info (record, saving)
