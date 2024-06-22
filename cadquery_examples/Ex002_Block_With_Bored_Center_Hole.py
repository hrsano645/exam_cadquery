import cadquery as cq
from ocp_vscode import show_object

# 各寸法の値をハードコーディングする代わりに、これらを変更できます。
length = 80.0  # ブロックの長さ
height = 60.0  # ブロックの高さ
thickness = 10.0  # ブロックの厚さ
center_hole_dia = 22.0  # ブロックの中央の穴の直径

# 上記の寸法に基づいてブロックを作成し、中央に直径22mmの穴を追加します。
# 1. オブジェクトを構築するためのワークプレーンを確立します。
# 1a. XとYの原点を使用してワークプレーンを定義し、正のZ方向が「上」であり、負のZ方向が「下」であることを意味します。
# 2. 最も高い（最大）Z面が選択され、その上に新しいワークプレーンが作成されます。
# 3. 新しいワークプレーンを使用してブロックに穴を掘ります。
# 3a. 穴は自動的にワークプレーンの中央に配置されます。
result = (
    cq.Workplane("XY")
    .box(length, height, thickness)
    .faces(">Z")
    .workplane()
    .hole(center_hole_dia)
)
show_object(result, measure_tools=True)
