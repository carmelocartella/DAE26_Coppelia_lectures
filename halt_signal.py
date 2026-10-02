def sysCall_init():
    
    sim = require('sim')
    
    sim.setInt32Signal('general_halt', 0)
    
    self.leftMotor = sim.getObject('../LeftMotor')
    self.rightMotor = sim.getObject('../RightMotor')
    self.proxSensor = sim.getObject('../SensingNose')
    
    self.halt = False

def sysCall_actuation():
    
    if not self.halt:
        sim.setJointTargetVelocity(self.leftMotor, 1.5)
        sim.setJointTargetVelocity(self.rightMotor, 1.5)
    else:
        sim.setJointTargetVelocity(self.leftMotor, 0)
        sim.setJointTargetVelocity(self.rightMotor, 0)

def sysCall_sensing():
    
    proximity_signal = sim.readProximitySensor(self.proxSensor)
    if proximity_signal[0]:
        self.halt = True
        sim.setInt32Signal('general_halt', 1)
    elif sim.getInt32Signal('general_halt'):
        self.halt = True

def sysCall_cleanup():
    # do some clean-up here
    pass

