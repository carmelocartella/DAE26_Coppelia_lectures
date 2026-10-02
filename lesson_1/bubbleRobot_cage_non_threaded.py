import numpy as np

def sysCall_init():
    sim = require('sim')
    
    # Object handles
    self.right_motor = sim.getObject('../rightMotor')
    self.left_motor = sim.getObject('../leftMotor')
    self.proximity_sensor = sim.getObject('../sensingNose')
    
    # Utilities
    self.proximity_signal = 0
    self.turning_time = 0 # This "state" defines if we are still turning or not
    

def sysCall_actuation():
    
    if self.turning_time > 0:
        self.turning_time -= sim.getSimulationTimeStep()
    
    if self.proximity_signal > 0 and self.turning_time <= 0:
        self.turning_time = 3
        if np.random.rand() > 0.5:
            # Turn right
            sim.setJointTargetVelocity(self.left_motor, -1)
            sim.setJointTargetVelocity(self.right_motor, 1)
        else:
            # Turn left
            sim.setJointTargetVelocity(self.left_motor, 1)
            sim.setJointTargetVelocity(self.right_motor, -1)
            
    if self.proximity_signal == 0 and self.turning_time <= 0:
        # Default behaviour move straight
        sim.setJointTargetVelocity(self.left_motor, 2)
        sim.setJointTargetVelocity(self.right_motor, 2)
            
    
            
    
def sysCall_sensing():
    sensor_reading = sim.readProximitySensor(self.proximity_sensor)
    self.proximity_signal = sensor_reading[0]
    

def sysCall_cleanup():
    # do some clean-up here
    pass

# See the user manual or the available code snippets for additional callback functions and details
