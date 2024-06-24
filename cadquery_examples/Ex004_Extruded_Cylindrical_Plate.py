import cadquery as cq
from ocp_vscode import show_object

# 各寸法の値をハードコーディングする代わりに、これらを変更できます。
circle_radius = 50.0  # プレートの半径
thickness = 13.0  # プレートの厚さ
rectangle_width = 13.0  # 円柱状プレートの中央の長方形の幅
rectangle_length = 19.0  # 円柱状プレートの中央の長方形の長さ

# 中央に長方形の穴がある円柱状プレートを押し出します。
# 1. オブジェクトを構築できる作業平面を確立します。
# 1a. "front" という名前の平面方向を使用して作業平面を定義します。
#     これにより、正の Z 方向が "上" であり、負の Z 方向が "下" になります。
# 2. 外側の円の2Dジオメトリは、中央の穴を作成する長方形と同時に作成されます。
# 2a. 円と長方形は自動的に作業平面の中心に配置されます。
# 2b. hole() のような他の関数とは異なり、circle() は直径ではなく半径を取ります。
# 3. 円と長方形は一緒に押し出され、中央に長方形の穴がある円柱状プレートが作成されます。
# 3a. circle() と rect() を他の形状に変更することで、プレートやその中の穴を完全に変更できます。
result = (
    cq.Workplane("front")
    .circle(circle_radius + 20)
    .rect(rectangle_width, rectangle_length)
    .extrude(thickness + 5)
)

# extrudeは押し出しの意味。認識できる外周の形状を押し出すことで、3Dオブジェクトを作成します。

# このスクリプトの結果を表示します
show_object(result, measure_tools=True)
