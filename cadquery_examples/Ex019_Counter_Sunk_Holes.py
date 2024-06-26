import cadquery as cq
from ocp_vscode import show_object

# 4つのカウンターシンク穴があるプレートを作成します。
# 1. 名前付きの平面ではなく、XYオブジェクトを使用してワークプレーンを確立します。
# 2. ボックス()関数を使用して、将来のジオメトリの基礎となる単純なボックスを作成します。
# 3. ボックスの一番上の面を選択し、その上にワークプレーンを確立します。
# 4. ワークプレーン上に、他のジオメトリを配置するための構築用の長方形を描画します。
# 5. 長方形の角の頂点を選択し、cskHole()関数を使用して、各頂点を穴の中心としてカウンターシンク穴を配置します。
# 5a. カウンターシンク穴の深さをNoneに設定すると、穴が完全に切り抜かれます。
result = (
    cq.Workplane(cq.Plane.XY())
    .box(4, 2, 0.5)
    .faces(">Z")
    .workplane()
    .rect(3.5, 1.5, forConstruction=True)
    .vertices()
    .cskHole(0.125, 0.25, 82.0, depth=None)
)

# このスクリプトの結果を表示します
show_object(result)
