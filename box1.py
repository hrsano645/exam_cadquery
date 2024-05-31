# 単純な箱を作るexample
# 要件: 上蓋と本体を作る。はめ込み式の箱を作る。
# 大きさは全体で 縦横 6cm、高さ 3cm。 上側は 1cm、下側は 2cm とする。
# 板厚は 3mm, はめあいのため、でっぱりは1.5mm

import cadquery as cq
from ocp_vscode import show_object

# 全体の数値設定
width = 60
height = 60
upper_depth = 30
lower_depth = 30
tichkness = 3
projection = 1.5

# 下側の箱を作る

lower_box = cq.Workplane("XY").box(width, height, lower_depth)
# 内側をくりぬく
lower_box = lower_box.faces(">Z").shell(-tichkness)

# z底面とx側面の角を丸める
lower_box = lower_box.edges("<Z or |Z").fillet(projection)

show_object(lower_box, measure_tools=True)

# 上側の箱を作る
