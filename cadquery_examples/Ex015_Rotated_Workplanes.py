import cadquery as cq
from ocp_vscode import show_object

# 1.  オブジェクトを構築するためのワークプレーンを確立します。
# 1a. 名前付きの平面方向 "front" を使用してワークプレーンを定義します。これは、
#     正のZ方向が "上" であり、負のZ方向が "下" であることを意味します。
# 2.  未来のジオメトリの基礎となる単純なボックスをbox()関数で作成します。
# 3.  ボックスの最上部のZ面を選択します。
# 4.  新しいワークプレーンを作成し、transformed関数で移動および回転します。
# 5.  他のジオメトリを配置するために存在するだけの構築用の長方形を作成します。
# 6.  構築用長方形の頂点を選択します。
# 7.  選択した各頂点の中心に穴を配置します。
# 7a. ワークプレーンが回転しているため、面には角度のついた穴ができます。
rotate_angle = 45

result = (
    cq.Workplane("front")
    .box(4.0, 4.0, 0.25)
    .faces(">Z")
    .workplane()
    .transformed(offset=(0, -1.5, 1.0), rotate=(rotate_angle, 0, 0))
    .rect(1.5, 1.5, forConstruction=True)
    .vertices()
    .hole(0.25)
)

# このスクリプトの結果を表示します
show_object(result, measure_tools=True)

# 以下は穴をあけるホールの元のモデルがどこの位置に生成しているかを見た結果。長方形を作って角度をつける、面に対しての法線方向に穴をあける。

result2 = (
    cq.Workplane("front", (10, 0, 0))
    .box(4.0, 4.0, 0.25)
    .faces(">Z")
    .workplane()
    .transformed(offset=(0, -1.5, 1.0), rotate=(rotate_angle, 0, 0))
    .rect(1.5, 1.5)
    .extrude(0.5)
)

show_object(result2, measure_tools=True)
