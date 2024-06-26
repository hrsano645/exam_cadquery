import cadquery as cq
from ocp_vscode import show_object

# 薄い壁で両端が開いた空洞のボックスを作成します。
# 1. オブジェクトを構築するためのワークプレーンを確立します。
# 1a. ワークプレーンを定義するために名前付きの平面指向「front」を使用し、
#     正のZ方向が「上」であり、負のZ方向が「下」であることを意味します。
# 2. 未来のジオメトリの基礎となる単純なボックスをbox()関数で作成します。
# 3. +z方向の法線を持つ面を選択します。
# 4. 最も上のZ面を切り抜いてシェルを作成します。
result = cq.Workplane("front").box(2, 2, 2).faces("+Z").shell(-0.05)

# Displays the result of this script
show_object(result, measure_tools=True)

# 元のボックスとの比較をする
result2 = cq.Workplane("front", (4, 0, 0)).box(2, 2, 2)
show_object(result2, measure_tools=True)
