from marionette_models.franka_research_3.model import MODEL
import rerun as rr
import time
import math


"""Moves non-rigid joints of a Franka Research 3 robot in a sinusoidal trajectory between limits."""

rr.init("", spawn=True)

i=0
MODEL.visualize()
while True:
    try:
        for joint in MODEL.joints:
            if not hasattr(joint, 'limits'):
                continue
            midline = (joint.limits[0] + joint.limits[1]) / 2
            amplitude = (joint.limits[0] - joint.limits[1]) / 2
            position = midline + amplitude * math.sin(i)
            joint_index = MODEL.joints.index(joint)
            MODEL.move_joint(joint_index, position)
        i+=0.01
        time.sleep(0.01)  # Add a small delay to control the speed of the movement
    except KeyboardInterrupt:
        break
