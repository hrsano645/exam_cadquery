import cadquery as cq
from ocp_vscode import show_object

# 四隅に穴のある長方形のブロックを作成します。
# 1. オブジェクトを構築できる作業平面を確立します。
# 1a. 作業平面を定義するために、名前付きの平面方向「front」を使用します。
#     これは、正のZ方向が「上」であり、負のZ方向が「下」であることを意味します。
# 2. 未来のジオメトリの基盤となる単純なボックスをbox()関数で作成します。
# 3. ボックスの最上部のZ面を選択します。
# 4. 新しい作業平面を作成して、新しいジオメトリを構築します。
# 5. 他のジオメトリを配置するために存在するだけの構築用の長方形を作成します。
# 6. 構築用の長方形の頂点を選択します。
# 7. 選択した各頂点の中心に穴を配置します。
result = (
    cq.Workplane("front")
    .box(2, 2, 0.5)
    .faces(">Z")
    .workplane()
    .rect(1.5, 1.5, forConstruction=True)
    .vertices()
    .hole(0.125)
)

# このスクリプトの結果を表示します
show_object(result, measure_tools=True)
