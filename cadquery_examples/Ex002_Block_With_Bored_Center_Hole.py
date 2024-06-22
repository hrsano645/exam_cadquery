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
# result = (
#     cq.Workplane("XY")
#     .box(length, height, thickness)
#     .faces(">Z")
#     .workplane()
#     .hole(center_hole_dia)
# )

# cutThruAllは何をしているか？
# これは、指定されたオブジェクトのすべての面を通過する切断を作成します。


# このスクリプトの結果を表示します
# show_object(result)

result = (
    cq.Workplane("XY")
    .box(10, 10, 10)
    # -----
    .faces(">X")  # 右側面
    .workplane()
    .hole(1.5)
    # -----
    .faces("<X")  # 左側面
    .workplane()
    .rect(
        3,
        1,
    )  # 3x3の長方形
    .cutThruAll()
    # -----
    .faces(">Y")  # 前面
    .workplane()
    .circle(1)  # 半径1の円
    .cutThruAll()
    # -----
    .faces("<Y")  # 背面
    .workplane()
    .slot2D(5, 2, 90)  # 5x2のスロット
    .cutThruAll()
    # -----
    .faces(">Z")  # 上面
    .workplane()
    .polygon(6, 4)  # 6角形
    .cutThruAll()
    # -----
    .faces("<Z")  # 下面
    .workplane()
    .polygon(3, 4)  # 3角形
    .cutThruAll()
)

# cq.Workplaneでまずは座標面を設定する。その後、facesで面を指定し、workplaneでその面に座標面を設定する。
# holeはショートカット的なもので、穴をあけるという意味、円柱を作成して、その中に穴をあけるという意味。
# cutThruAllは、指定されたオブジェクトのすべての面を通過する切断を作成します。適当な形状を作ったときに、その形状を切断するという意味。
show_object(result, measure_tools=True)


# では、形状を切り取るときに、その形状元のオブジェクトの座標をずらしたらどうなるか？
result2 = (
    cq.Workplane("XY", (20, 0, 0))
    .box(10, 10, 10)
    # -----
    .faces(">X")  # 右側面
    .workplane()
    .hole(1.5)  # ホールはそのまま
    # -----
    .faces("<X")  # 左側面
    # ここでオフセットをずらす=X軸方向に左に2mmずらす
    .workplane(offset=5)
    .rect(
        3,
        1,
    )
    .cutThruAll()
)

show_object(result2, name="ずらした場合", measure_tools=True)

# 今の計上を抜いたものとしては、全部2Dの平面を使ってるかな？
