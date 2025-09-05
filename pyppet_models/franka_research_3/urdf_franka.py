from pyppet_models.franka_research_3.model import FRANKA_RESEARCH_3
from pyppet.urdf import pyppet_to_urdf
import xml.etree.ElementTree as ET
from yourdfpy import urdf
import io


urdf_str = pyppet_to_urdf(FRANKA_RESEARCH_3, "franka_research_3.urdf")
root = ET.fromstring(urdf_str)

with io.StringIO(urdf_str) as f:
    urdf_model = urdf.URDF.load(f)
    urdf_model.show()  # Might be difficult to see with yourdfpy viewer background and textures
