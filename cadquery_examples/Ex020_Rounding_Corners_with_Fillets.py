import cadquery as cq
from ocp_vscode import show_object

# Z軸に4つの角を丸めたプレートを作成します。
# 1. オブジェクトを構築するためのワークプレーンを確立します。
# 1a. XとYの原点を使用してワークプレーンを定義し、正のZ方向が「上」であり、負のZ方向が「下」であることを意味します。
# 2. 未来のジオメトリの基盤となる単純なボックスをbox()関数で作成します。
# 3. Z軸に平行なすべてのエッジを選択します。
# 4. 指定された半径で選択された各エッジにフィレットを作成します。
result = cq.Workplane("XY").box(3, 3, 0.5).edges("|Z").fillet(0.125)

# Displays the result of this script
show_object(result)
