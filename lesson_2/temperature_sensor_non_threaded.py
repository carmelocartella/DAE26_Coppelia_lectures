def sysCall_init():
    sim = require('sim')

    self.temperature_list = [22.0, 24.0, 26.0, 28.0, 30.0]
    self.timer = 0
    sim.setFloatSignal('room_temperature', 0.0)
    
    self.temperature_counter = 0

def sysCall_actuation():
    if self.timer > 0:
        self.timer -= sim.getSimulationTimeStep()
    
    if self.timer <= 0:
        # The temperature is maintained for 30s before changing
        self.timer = 30
        self.temperature_counter += 1
        
        # Retreive the temperature to be displayed in a cyclic manner
        temp_idx = self.temperature_counter % len(self.temperature_list)
        # Set the signal
        sim.setFloatSignal('room_temperature', self.temperature_list[temp_idx])
        print(f'Room temperature: {self.temperature_list[temp_idx]}')

def sysCall_sensing():
    # put your sensing code here
    pass

def sysCall_cleanup():
    # do some clean-up here
    pass

# See the user manual or the available code snippets for additional callback functions and details
