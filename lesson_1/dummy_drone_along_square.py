import numpy as np

def sysCall_init():
    sim = require('sim')
    
    # Utils
    points_per_side = 50
    self.z = 1

    # Drone handle
    self.drone = sim.getObject('..')
    
    # Define the trajectory
    corners = np.array([
        [0, 0],  # Bottom-left
        [1, 0],  # Bottom-right
        [1, 1],  # Top-right
        [0, 1],  # Top-left
        [0, 0]   # Close the square back to start
    ])
    
    self.trajectory = []
    for i in range(len(corners) - 1):
        p1 = corners[i]
        p2 = corners[i+1]
        # Linear interpolation between p1 and p2
        x = np.linspace(p1[0], p2[0], points_per_side, endpoint=False)
        y = np.linspace(p1[1], p2[1], points_per_side, endpoint=False)
        segment = np.column_stack((x, y))
        self.trajectory.append(segment)
        
    self.trajectory.append(np.array([corners[-1]]))
    self.trajectory = np.vstack(self.trajectory) #Nx2 matrix
    
def sysCall_thread():
    
    sim.setObjectPosition(
        self.drone,
        [self.trajectory[0, 0],
         self.trajectory[0, 1],
         self.z]
    )
        
    for coordinates in self.trajectory:
        sim.setObjectPosition(self.drone, [coordinates[0], coordinates[1], self.z])
        sim.wait(0.08)
            

# See the user manual or the available code snippets for additional callback functions and details
