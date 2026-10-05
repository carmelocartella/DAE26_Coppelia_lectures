def sysCall_init():
    sim = require('sim')
    
    self.motor = sim.getObject('../fanMotor')
    self.threshold_temp = 24.5
    
    self.sensor_temp = sim.getFloatSignal('room_temperature')
    
    # Set some fan properties
    self.fan_power = 1
    self.fan_speed = 10

def sysCall_actuation():
    
    if self.sensor_temp > self.threshold_temp and self.fan_power:
        sim.setJointTargetVelocity(self.motor, self.fan_speed)
    else:
        sim.setJointTargetVelocity(self.motor, 0)

def sysCall_sensing():

    self.sensor_temp = sim.getFloatSignal('room_temperature')

def sysCall_cleanup():
    # do some clean-up here
    pass

# See the user manual or the available code snippets for additional callback functions and details
