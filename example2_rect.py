import cadquery as cq
from ocp_vscode import show_object

s = cq.Workplane("XY")
sPnts = [
    (2.75, 1.5),
    (2.5, 1.75),
    (2.0, 1.5),
    (1.5, 1.0),
    (1.0, 1.25),
    (0.5, 1.0),
    (0, 1.0),
]
r = s.lineTo(3.0, 0).lineTo(3.0, 1.0).spline(sPnts, includeCurrent=True).close()
result = r.extrude(0.5)

# 上面にフィレットが欠けられるか？
result = result.faces("+Z").fillet(0.05)

# 下面にC面かけられる？
result = result.faces("-Z").chamfer(0.05)

show_object(result, name="boxbody", measure_tools=True)
