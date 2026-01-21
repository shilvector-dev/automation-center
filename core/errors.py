from enum import Enum

class EngineError(Enum):
    INVALID_MODE = "E001"
    MODE_ALREADY_ACTIVE = "E002"
    FILE_NOT_FOUND = "E003"
    OBS_CONECTION_FALED = "E004"
    