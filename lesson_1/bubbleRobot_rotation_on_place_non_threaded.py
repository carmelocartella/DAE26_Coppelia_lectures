def sysCall_init():
    sim = require('sim')
    
    # need to get all the handles of the robot I want to control
    self.robot = sim.getObject('..')
    self.left_motor = sim.getObject('../LeftMotor')
    self.right_motor = sim.getObject('../RightMotor')
    
def sysCall_sensing():
    pass
    
def sysCall_actuation():
    
    # Once for a sim cycle we will use setTargetJointVelocity to set a cinematic input to the motors 
    sim.setJointTargetVelocity(self.left_motor, -1.0)
    sim.setJointTargetVelocity(self.right_motor, 1.0)