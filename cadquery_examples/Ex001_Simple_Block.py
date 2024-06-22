import cadquery as cq
from ocp_vscode import show

# 各寸法の値をハードコーディングする代わりに、これらを変更できます。
length = 80.0  # ブロックの長さ
height = 60.0  # ブロックの高さ
thickness = 10.0  # ブロックの厚さ

# 上記の変数を使用して3Dブロックを作成します。
# 1. オブジェクトを構築するための作業平面を確立します。
# 1a. XとYの原点を使用して作業平面を定義し、正のZ方向が「上」であり、負のZ方向が「下」であることを意味します。
result = cq.Workplane("XY", (5, 5, 5)).box(length, height, thickness)

# オブジェクト生成の位置関係は、何も設定しないと原点を起点に広げることになる。つまり 10の立方体を作ると、5,5,5の位置が原点になる。
# cq.Workplaneでoriginで座標を設定すると座標移動がある。これは世界座標（global coordinate）である。


show(result, measure_tools=True)
