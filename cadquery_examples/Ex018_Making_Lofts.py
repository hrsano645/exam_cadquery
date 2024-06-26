import cadquery as cq
from ocp_vscode import show_object

# 長方形と円形のセクション間にロフトを作成します。
# 1. オブジェクトを構築するためのワークプレーンを確立します。
# 1a. ワークプレーンを定義するために名前付きの平面方向「front」を使用します。つまり、
#     正のZ方向が「上」であり、負のZ方向が「下」であることを意味します。
# 2. 未来のジオメトリの基礎となる単純なボックスをbox()関数で作成します。
# 3. ボックスの最も上のZ面を選択します。
# 4. ボックスの最も上の面の中心に2Dの円を描きます。
# 5. 円が描かれた面から3 mm上にワークプレーンを作成します。
# 6. 新しいオフセットワークプレーン上に2Dの円を描きます。
# 7. 円と長方形の間にロフトを作成します。
result = (
    cq.Workplane("front")
    .box(4.0, 4.0, 0.25)
    .faces(">Z")
    .circle(1.5)
    .workplane(offset=3.0)
    .rect(0.75, 0.5)
    .loft(combine=True)
)

# このスクリプトの結果を表示します
show_object(result)
