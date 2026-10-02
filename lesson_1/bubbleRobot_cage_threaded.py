import numpy as np

def sysCall_init():
    sim = require('sim')
    
    # Object handles
    self.left_motor = sim.getObject('../leftMotor')
    self.right_motor = sim.getObject('../rightMotor')
    self.proximity_sensor = sim.getObject('../sensingNose')
    
def sysCall_thread():
    # Run until the simulation stops
    while not sim.getSimulationStopping():
        
        # Read the proximity sensor
        proximity_signal = sim.readProximitySensor(self.proximity_sensor)
        
        # If no obstacles detected move straight
        if proximity_signal[0] == 0:
            sim.setJointTargetVelocity(self.left_motor, 2)
            sim.setJointTargetVelocity(self.right_motor, 2)
        
        # If obstacle detected
        if proximity_signal[0] == 1:
            sim.setJointTargetVelocity(self.left_motor, 0)
            sim.setJointTargetVelocity(self.right_motor, 0)
            
            # Turn left
            if np.random.rand() > 0.5:
                sim.setJointTargetVelocity(self.left_motor, 1)
                sim.setJointTargetVelocity(self.right_motor, -1)
            # Turn right
            else:
                sim.setJointTargetVelocity(self.left_motor, -1)
                sim.setJointTargetVelocity(self.right_motor, 1)
            
            # Wait 3 seconds
            sim.wait(3)