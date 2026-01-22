from core.errors import EngineError
import datetime as dt
import os
import json

class Engine:
    def __init__(self, default_mode="off", log_path="logs/engine.log"):
        try:
            with open ("ia_core/commands.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            raise RuntimeError("Arquivo de comandos não encontrado")
        
        self.mode = default_mode
        self.log_path = log_path
        self.commands = data
        
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
    
    def set_mode(self, new_mode):
        if new_mode not in self.commands["modes"]:
            self._log(f"Incorrect mode atemptive: {new_mode}")
            return EngineError.INVALID_MODE
        elif new_mode == self.mode:
            self._log(f"Mode already active: {new_mode}")
            return EngineError.MODE_ALREADY_ACTIVE 
        else:
            self._log(f"Mode changed from {self.mode} to {new_mode}")
            self.mode = new_mode
    
    def get_mode(self):
        return self.mode
    
    def get_avaiable_modes(self):
        return self.commands["modes"]

    def _log(self, message):
        timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")