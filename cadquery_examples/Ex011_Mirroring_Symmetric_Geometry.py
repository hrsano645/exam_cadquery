import cadquery as cq
from ocp_vscode import show_object

# 1.  オブジェクトを構築するための作業平面を確立します。
# 1a. "front"という名前の平面方向を使用して作業平面を定義します。
#     これは、正のZ方向が"上"であり、負のZ方向が"下"であることを意味します。
# 2.  hLine関数を使用して作業平面上に水平線を引きます。
# 2a. 1.0は距離ではなく座標です。hLineToを使用すると、x座標を使用できます。
r = cq.Workplane("front").hLine(1.0)

# 3.  vLineとhLine関数を使用して、垂直線と水平線のシリーズを描画します。
r = r.vLine(0.5).hLine(-0.25).vLine(-0.25).hLineTo(0.0)

# 4.  Y軸を中心にジオメトリをミラーリングし、3Dオブジェクトに押し出します。
result = r.mirrorY().extrude(0.25)

# このスクリプトの結果を表示します
show_object(result)
