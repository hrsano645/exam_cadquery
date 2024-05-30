import cadquery as cq
from ocp_vscode import show_object

box = cq.Solid.makeBox(1, 2, 3)

box2 = cq.Workplane("XY").box(1, 2, 3)

# select top and bottom wires
result = box
# result = box.faces(">Z or <Z").wires()
show_object(result)
