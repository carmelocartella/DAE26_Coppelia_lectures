def sysCall_init():
    sim = require('sim')
    
    print("into init")
    
def sysCall_thread():
    
    print("into threading")
    
    left_motor = sim.getObject('../leftMotor')
    right_motor = sim.getObject('../rightMotor')
    prox_sensor = sim.getObject('../sensingNose')
    
    while True:
    
        prox_sign = sim.readProximitySensor(prox_sensor)
        
        print(prox_sign[0])
        
        if prox_sign[0] == 0:
            sim.setJointTargetVelocity(left_motor, 2)
            sim.setJointTargetVelocity(right_motor, 1.2)
            
        if prox_sign[0] == 1:
            sim.setJointTargetVelocity(left_motor, -1)
            sim.setJointTargetVelocity(right_motor, -1)
            
            sim.wait(3)