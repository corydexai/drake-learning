#taking notes on all the things i'll need to get the increments here working.
#the goal is to grab 3d coords from a urdf to plot position of the spoon tip in a 3d plane in matplotlib
#and commpare measured

import numpy as np
import math
from pydrake.common import FindResourceOrThrow
from pydrake.multibody.rigid_body_tree import RigidBodyTree, RigidBodyFrame
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# load rigid body tree
tree = RigidBodyTree("/home/dexai/catkin_ws/src/ice_cream_parlor_description/urdf/Dexai_parlor-drake.urdf")

# set robot configuration
q = np.zeros(7) #following comment was syler's:# arm position doesn't matter here so just use zeros

#prep for 3d graphing
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# look up indices of camera frames
cam_idx = tree.FindBody("kinect1_rgb_optical_frame").get_body_index()
depth_idx = tree.FindBody("kinect1_depth_optical_frame").get_body_index()

# do kinematics with iiwa joint configuration
kinsol = tree.doKinematics(q)
# find relative transform between rgb and depth optical frame
T = tree.relativeTransform(kinsol, cam_idx, depth_idx)
T_rgb_d = T
# print T
X = T[:3,3] # extract position from transformation matrix
X_rgb_d = X
print (X)



ax.plot(???)
ax.show()
