from pyppet_models.franka_research_3.model import MODEL
from pyppet.format import Pose
import rerun as rr


"""Spawns multiple Franka Research 3 robots in a grid layout."""

rr.init("", spawn=True)

cols = 3
rows = 3
spacing = 1.0
for i in range(rows * cols):
    row = i // cols
    col = i % cols
    new_model = MODEL.copy(name = f"franka_{i}", pose = Pose(translation = (row, col, 0)))
    new_model.visualize()
