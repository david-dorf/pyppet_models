from pyppet_models.franka_research_3.model import MODEL
from pyppet.format import RigidJoint
import rerun as rr
import time
import math


"""Moves non-rigid joints of a Franka Research 3 robot in a sinusoidal trajectory between limits."""


# Initialize sinusoidal trajectory parameters for non-rigid joints
joint_params = []
for joint in MODEL.joints:
    if isinstance(joint, RigidJoint) or joint.limits is None:
        continue  # Skip rigid joints and joints without limits
    midline = (joint.limits[0] + joint.limits[1]) / 2
    amplitude = (joint.limits[0] - joint.limits[1]) / 2
    joint_params.append((joint, midline, amplitude))

t=0
rr.init("", spawn=True)
MODEL.visualize()
while True:
    try:
        for joint, midline, amplitude in joint_params:
            position = midline + amplitude * math.sin(t)
            MODEL.move_joint(joint, position)
        t+=0.01
        time.sleep(0.01)  # Add a small delay to control the speed of the movement
    except KeyboardInterrupt:
        break
