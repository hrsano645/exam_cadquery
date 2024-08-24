import cadquery as cq
from ocp_vscode import show_object

# モデルを作成する
result = cq.Workplane("XY").box(3, 3, 0.5).edges("|Z").fillet(0.125)
show_object(result, name="Box", axes=True, grid=True)

# モデルをShapeオブジェクトとして取得する
shape = result.val()

print(dir(shape))

# バウンディングボックスを作成する
bounding_box = shape.BoundingBox()

print(dir(bounding_box))
print(bounding_box.__dict__)

# バウンディングボックスの情報を取得して表示
print(f"Min: {bounding_box.xmin=}, {bounding_box.ymin=}, {bounding_box.zmin=}")
print(f"Max: {bounding_box.xmax=}, {bounding_box.ymax=}, {bounding_box.zmax=}")
print(f"Center: {bounding_box.center}")
print(f"DiagonalLength: {bounding_box.DiagonalLength}")
