import numpy as np 

def sysCall_init():
    sim = require('sim')
    
    # Take the object handles
    self.robot = sim.getObject('..')
    self.proximity_sensor = sim.getObject('../sensingNose')
    self.right_motor = sim.getObject('../rightMotor')
    self.left_motor = sim.getObject('../leftMotor')
    
    # Draw the robot trajectory
    self.robot_trajectory = sim.addDrawingObject(sim.drawing_linestrip + sim.drawing_cyclic, 2, 0, -1, 200, [2, 2, 0])
    
    # Define if the robot is driving back
    self.drive_back_time = 0
    
    # Define if an obstacle is detected
    self.proximity_signal = -1

def sysCall_actuation():
    # The robot is turning
    if self.drive_back_time > 0:
        self.drive_back_time -= sim.getSimulationTimeStep()
        
    # Obstacle detected and not turning
    if self.proximity_signal == 1 and self.drive_back_time <= 0:
        self.drive_back_time = 3
        
        # Turn right
        if np.random.rand() > 0.5:
            sim.setJointTargetVelocity(self.right_motor, 1)
            sim.setJointTargetVelocity(self.left_motor, -1)
        # Turn left
        else:
            sim.setJointTargetVelocity(self.right_motor, -1)
            sim.setJointTargetVelocity(self.left_motor, 1)
    if self.drive_back_time <= 0:
        # Default behaviour is to drive straight:
        sim.setJointTargetVelocity(self.left_motor, 3)
        sim.setJointTargetVelocity(self.right_motor, 3)

def sysCall_sensing():
    # Retreive the robot position and fill the trajectory object
    position = sim.getObjectPosition(self.robot)
    sim.addDrawingObjectItem(self.robot_trajectory, position)
    
    # Read the sensor
    self.proximity_signal = sim.readProximitySensor(self.proximity_sensor)[0]

def sysCall_cleanup():
    # do some clean-up here
    pass

# See the user manual or the available code snippets for additional callback functions and details
