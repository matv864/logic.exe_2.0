# keep levels here and return config of one level by "click" from upper floor of program


class Level:
    def __init__(self):
        # we get name of files with levels from constants in "list levels"
        #  we need make handle last level how winning level
        #   we need return counter levels
        self._now_level = -1
        self._list_levels = []
        self.counter_levels = len(self._list_levels)


    def get_next_level_config(self):
        # we get filename from "list levels" by index "now_level"
        self._now_level += 1



