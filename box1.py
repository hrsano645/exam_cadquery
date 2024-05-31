# 単純な箱を作るexample
# 要件: 上蓋と本体を作る。かみ合わせ式の箱を作る。
# 大きさは全体で 縦横 6cm、高さ 3cm。 上側は 1cm、下側は 2cm とする。
# 板厚は 3mm, はめあいのため、でっぱりは1.5mm

import cadquery as cq
from ocp_vscode import show_object

# 全体の数値設定
width = 60
height = 60
upper_depth = 10
lower_depth = 20
wall_thickness = 3
tab_thickness = 1.5
tab_height = 1.5

# 下側の箱を作る

bottom_box = cq.Workplane("XY").box(width, height, lower_depth)
# 内側をくりぬく
bottom_box = bottom_box.faces(">Z").shell(-wall_thickness)

# z底面とx側面の角を丸める
# bottom_box = bottom_box.edges("<Z or |Z").fillet(wall_thickness)

show_object(bottom_box, name="boxbody", measure_tools=True)


# 下側箱の上蓋のかみ合わせ部分を作る
# 高さ1.5mmのでっぱり部分を用意する
tabs = (
    cq.Workplane("XY")
    .workplane(offset=lower_depth / 2 + tab_height / 2)
    # .rect(width - tab_thickness, height - tab_thickness)
    # .extrude(tab_thickness)
    .box(width - tab_thickness, height - tab_thickness, tab_thickness)
    # .faces(">Z")
    # .shell(-wall_thickness)
)

tabs_shell = tabs.faces(">Z").shell(-wall_thickness)

# 突起を作成
# # 下側本体と凸部分を結合
# bottom_box = bottom_box.union(tabs)


show_object(tabs, name="Tabs", measure_tools=True)

# 上側の箱を作る
