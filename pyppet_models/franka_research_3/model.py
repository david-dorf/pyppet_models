from pyppet.format import Link, RigidJoint, RevoluteJoint, SliderJoint, Pose, Model
from math import pi
import os


link0 = Link(name = 'link0', visual = "assets/link0.glb")
link1 = Link(name = 'link1', visual = "assets/link1.glb")
link2 = Link(name = 'link2', visual = "assets/link2.glb")
link3 = Link(name = 'link3', visual = "assets/link3.glb")
link4 = Link(name = 'link4', visual = "assets/link4.glb")
link5 = Link(name = 'link5', visual = "assets/link5.glb")
link6 = Link(name = 'link6', visual = "assets/link6.glb")
link7 = Link(name = 'link7', visual = "assets/link7.glb")
hand = Link(name = 'hand', visual = "assets/hand.glb")
finger1 = Link(name = 'finger1', visual = "assets/finger.glb")
finger2 = Link(name = 'finger2', visual = "assets/finger.glb")

joint0 = RevoluteJoint(
    parent = link0,
    child = link1,
    pose = Pose(translation = (0, 0, 0.333)),
    axis = (0, 0, 1),
    limits = (-2.8973, 2.8973),
)

joint1 = RevoluteJoint(
    parent = link1,
    child = link2,
    pose = Pose(),
    axis = (0, 1, 0),
    limits = (-1.7628, 1.7628),
)

joint2 = RevoluteJoint(
    parent = link2,
    child = link3,
    pose = Pose(translation = (0, 0, 0.316)),
    axis = (0, 0, 1),
    limits = (-2.8973, 2.8973),
)

joint3 = RevoluteJoint(
    parent = link3,
    child = link4,
    pose = Pose(translation = (0.0825, 0, 0)),
    axis = (0, -1, 0),
    limits = (-3.0718, -0.0696),
)

joint4 = RevoluteJoint(
    parent = link4,
    child = link5,
    pose = Pose(translation = (-0.0825, 0, 0.384)),
    axis = (0, 0, 1),
    limits = (-2.8973, 2.8973),
)

joint5 = RevoluteJoint(
    parent = link5,
    child = link6,
    pose = Pose(),
    axis = (0, -1, 0),
    limits = (-0.0175, 3.7525),
)

joint6 = RevoluteJoint(
    parent = link6,
    child = link7,
    pose = Pose(translation = (0.088, 0, 0)),
    axis = (0, 0, 1),
    limits = (-2.8973, 2.8973)
)

joint7 = RigidJoint(
    parent = link7,
    child = hand,
    pose = Pose(translation = (0, 0, -0.107))
)

joint8 = SliderJoint(
    parent = hand,
    child = finger1,
    pose = Pose(translation = (0, 0, -0.0584)),
    axis = (0, 1, 0),
    limits = (0, -0.04)
)

joint9 = SliderJoint(
    parent = hand,
    child = finger2,
    pose = Pose(translation = (0, 0, -0.0584), rotation = (0, 0, pi)),
    axis = (0, 1, 0),
    limits = (0, -0.04)
)

joints = [joint0, joint1, joint2, joint3, joint4, joint5, joint6, joint7, joint8, joint9]

# Model below uses a pixi project root directory, but could be adapted to any path setup
pixi_root = os.getenv("PIXI_PROJECT_ROOT")
if pixi_root is not None:
    path = pixi_root + "/pyppet_models/franka_research_3/"
else:
    raise ValueError("PIXI_PROJECT_ROOT environment variable is not set")
MODEL = Model(name = "franka_research_3", joints = joints, base = link0, path = path)
