from dino_runner.utils.constants import GODZHELP, GODZHELP_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Godzhelp(PowerUp):
    def __init__(self):
        self.image = GODZHELP
        self.type = GODZHELP_TYPE
        super().__init__(self.image, self.type)