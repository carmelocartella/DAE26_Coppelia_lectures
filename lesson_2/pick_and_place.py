import math as m

def sysCall_init():
    sim = require('sim')
    
    self.robot = sim.getObject('..')
    self.robot_joints = [sim.getObject('..' + '/joint'*(i+1))for i in range(6)]
    self.ee_connection = sim.getObject('..' + '/joint'*6 + '/ROBOTIQ85/attachPoint')
    self.ee_sensor = sim.getObject('..' + '/joint'*6 + '/ROBOTIQ85/EEProximity')
    
    self.MAX_V = 1
    self.MAX_A = 1
    self.MAX_J = 1

# Convert specifics to parameters to be provided to the move function
def buildMoveParams(joints, targetConfig, maxV, maxA, maxJ):
    params = {
            'joints' : joints,
            'targetPos' : targetConfig,
            'maxVel' : [maxV]*6,
            'maxAccel' : [maxA]*6,
            'maxJerk' : [maxJ]*6}
    
    return params

def checkMoveToConfig(joints, target, threshold):
    '''Target position must be specified in degrees, returns whether joints are close enough
    'delta' to the target position at current time'''

    current_pos = [math.degrees(sim.getJointPosition(j)) for j in joints]  # radians to degrees
    errors = [curr - targ for curr, targ in zip(current_pos, target)]
    return all(abs(e) < threshold for e in errors)

def from_deg2rad(angles):
    return [m.radians(angle) for angle in angles]

def sysCall_thread():
    obj_handle = -1
    
    # Set a position goal for joints in the joint space
    goalJ = [m.radians(0), m.radians(90), m.radians(0), m.radians(0), m.radians(0), m.radians(0)]
    # Convert params and move to the desired configuration
    params = buildMoveParams(self.robot_joints, goalJ, self.MAX_V, self.MAX_A, self.MAX_J)
    sim.moveToConfig(params)
    sim.wait(1)
    
    # Set a new position goal
    goalJ = [0, 30, -120, 0, 0, 0]
    
    params = buildMoveParams(self.robot_joints, from_deg2rad(goalJ), self.MAX_V, self.MAX_A, self.MAX_J)
    # to be sure that the robot gets there until an error is minimized
    while not checkMoveToConfig(self.robot_joints, goalJ, 0.1):
        sim.moveToConfig(params)
    
    while True:
        # Read the sensor
        detection_signal = sim.readProximitySensor(self.ee_sensor)
        # If obstacle is detected
        if detection_signal[0]:
            print(detection_signal)
            # Retreive the handle of the object
            obj_handle = detection_signal[3]
            break
            
    print(sim.getObjectParent(obj_handle))
    
    # Set the object parent to the object detected 'glued' to the end effector
    sim.setObjectParent(obj_handle, self.ee_connection, 1)
    
    goalJ = [0, -30, 120, 0, 0, 0]
    params = buildMoveParams(self.robot_joints, from_deg2rad(goalJ), self.MAX_V, self.MAX_A, self.MAX_J)
    while not checkMoveToConfig(self.robot_joints, goalJ, 0.1):
        sim.moveToConfig(params)
    
    sim.setObjectParent(obj_handle, -1, 1)
    
# See the user manual or the available code snippets for additional callback functions and details
