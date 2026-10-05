import os
import subprocess

def sysCall_init():
    sim = require('sim')
    
    # Retreive the json file to be read
    self.working_dir = '/home/carmelo/coppelia_ws/coppelia_lectures_2026/lesson_2'
    self.gui_file = os.path.join(self.working_dir, "gui_state.json")
    
    # Start the GUI
    self.gui_process = subprocess.Popen(['python3', os.path.join(self.working_dir, 'fan_interface.py')])
    
def sysCall_thread():
    
    # GUI communication rountine to read from a JSON file the state of the GUI
    import json
    
    fan_speed = 0
    power_state = False
    
    while True:
        if os.path.exists(self.gui_file):
            try:
                with open(self.gui_file, "r") as f:
                    state = json.load(f)
                    fan_speed = state.get("fan_speed", 0)
                    sim.setInt32Signal('fan_speed', fan_speed)
                    power_state = state.get("power_state", False)
            except Exception:
                print(Exception)
        else:
            print("GUI file not found ...")
            
        if power_state:
            sim.setInt32Signal('fan_power', 1)
        else:
            sim.setInt32Signal('fan_power', 0)
        
                
        sim.wait(0.5)     # GUI is read twice a second