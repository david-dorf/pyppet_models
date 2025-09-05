import pyppet.format as pf
from math import pi


asset_path = "pyppet_models/franka_research_3/assets/"

color_orange = (1.0, 0.5, 0.0)

mesh_0 = pf.Mesh(filename = asset_path + "link0.glb")
mesh_1 = pf.Mesh(filename = asset_path + "link1.glb")
mesh_2 = pf.Mesh(filename = asset_path + "link2.glb")
mesh_3 = pf.Mesh(filename = asset_path + "link3.glb")
mesh_4 = pf.Mesh(filename = asset_path + "link4.glb")
mesh_5 = pf.Mesh(filename = asset_path + "link5.glb")
mesh_6 = pf.Mesh(filename = asset_path + "link6.glb")
mesh_7 = pf.Mesh(filename = asset_path + "link7.glb")
mesh_hand = pf.Mesh(filename = asset_path + "hand.glb")
mesh_finger = pf.Mesh(filename = asset_path + "finger.glb")

base = pf.BaseLink()
link0 = pf.Link(name = 'link0', visual = pf.Visual(mesh_0))
link1 = pf.Link(name = 'link1', visual = pf.Visual(mesh_1))
link2 = pf.Link(name = 'link2', visual = pf.Visual(mesh_2))
link3 = pf.Link(name = 'link3', visual = pf.Visual(mesh_3))
link4 = pf.Link(name = 'link4', visual = pf.Visual(mesh_4))
link5 = pf.Link(name = 'link5', visual = pf.Visual(mesh_5))
link6 = pf.Link(name = 'link6', visual = pf.Visual(mesh_6))
link7 = pf.Link(name = 'link7', visual = pf.Visual(mesh_7))
hand = pf.Link(name = 'hand', visual = pf.Visual(mesh_hand))
finger1 = pf.Link(name = 'finger1', visual = pf.Visual(mesh_finger))
finger2 = pf.Link(name = 'finger2', visual = pf.Visual(mesh_finger))

basejoint = pf.RigidJoint(
    parent = base,
    child = link0,
)

joint0 = pf.RevoluteJoint(
    parent = link0,
    child = link1,
    pose = pf.Pose(translation = (0, 0, 0.333)),
    axis = (0, 0, 1),
    limits = pf.Limits(position_range = (-2.8973, 2.8973)),
)

joint1 = pf.RevoluteJoint(
    parent = link1,
    child = link2,
    pose = pf.Pose(),
    axis = (0, 1, 0),
    limits = pf.Limits(position_range = (-1.7628, 1.7628)),
)

joint2 = pf.RevoluteJoint(
    parent = link2,
    child = link3,
    pose = pf.Pose(translation = (0, 0, 0.316)),
    axis = (0, 0, 1),
    limits = pf.Limits(position_range = (-2.8973, 2.8973)),
)

joint3 = pf.RevoluteJoint(
    parent = link3,
    child = link4,
    pose = pf.Pose(translation = (0.0825, 0, 0)),
    axis = (0, -1, 0),
    limits = pf.Limits(position_range = (-3.0718, -0.0696)),
)

joint4 = pf.RevoluteJoint(
    parent = link4,
    child = link5,
    pose = pf.Pose(translation = (-0.0825, 0, 0.384)),
    axis = (0, 0, 1),
    limits = pf.Limits(position_range = (-2.8973, 2.8973)),
)

joint5 = pf.RevoluteJoint(
    parent = link5,
    child = link6,
    pose = pf.Pose(),
    axis = (0, -1, 0),
    limits = pf.Limits(position_range = (-0.0175, 3.7525)),
)

joint6 = pf.RevoluteJoint(
    parent = link6,
    child = link7,
    pose = pf.Pose(translation = (0.088, 0, 0)),
    axis = (0, 0, 1),
    limits = pf.Limits(position_range = (-2.8973, 2.8973)),
)

joint7 = pf.RigidJoint(
    parent = link7,
    child = hand,
    pose = pf.Pose(translation = (0, 0, -0.107))
)

joint8 = pf.SliderJoint(
    parent = hand,
    child = finger1,
    pose = pf.Pose(translation = (0, 0, -0.0584)),
    axis = (0, 1, 0),
    limits = pf.Limits(position_range = (0, -0.04)),
)

joint9 = pf.SliderJoint(
    parent = hand,
    child = finger2,
    pose = pf.Pose(translation = (0, 0, -0.0584), rotation = (0, 0, pi)),
    axis = (0, 1, 0),
    limits = pf.Limits(position_range = (0, -0.04)),
)

joints = [basejoint, joint0, joint1, joint2, joint3, joint4, joint5, joint6, joint7, joint8, joint9]

FRANKA_RESEARCH_3 = pf.Model(name = "franka_research_3", joints = joints)
