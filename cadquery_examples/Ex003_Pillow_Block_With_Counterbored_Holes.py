import cadquery as cq
from ocp_vscode import show_object

# 各寸法の値をハードコーディングする代わりに、これらを変更できます。
length = 80.0  # ブロックの長さ
width = 100.0  # ブロックの幅
thickness = 10.0  # ブロックの厚さ
center_hole_dia = 22.0  # ブロックの中央の穴の直径
cbore_hole_diameter = 2.4  # ボルトのシャンク/スレッドのクリアランス穴の直径
cbore_inset = 12.0  # カウンターボアされた穴がエッジからどれだけ離れているか
cbore_diameter = 4.4  # ボルトヘッドのポケット穴の直径
cbore_depth = 2.1  # ボルトヘッドのポケット穴の深さ

# 上記の寸法に基づいて3Dブロックを作成し、22mmの中央穴と4つのカウンターボアされたボルト穴を追加します。
# 1. オブジェクトを構築できるワークプレーンを確立します。
# 1a. XおよびYの原点を使用してワークプレーンを定義し、正のZ方向が「上」であり、負のZ方向が「下」であることを意味します。
# 2. 最も高い（最大）のZ面が選択され、その上に新しいワークプレーンが作成されます。
# 3. 新しいワークプレーンを使用してブロックを貫通する穴をドリルします。
# 3a. 穴は自動的にワークプレーンの中心に配置されます。
# 4. 最も高い（最大）のZ面が選択され、その上に新しいワークプレーンが作成されます。
# 5. ブロックの全体的な寸法に基づいて、ワークプレーン上に構築用の長方形が作成されます。
# 5a. 構築用オブジェクトは他のジオメトリを配置するためにのみ使用され、最終的に表示されるジオメトリには表示されません。
# 6. 長方形の頂点（コーナー）が選択され、各頂点にカウンターボアされた穴が配置されます（4つすべての頂点に同時に）。
result = (
    cq.Workplane("XY")
    .box(length, width, thickness)
    .faces(">Z")
    .workplane()
    .hole(center_hole_dia)
    .faces(">Z")
    .workplane()
    .rect(length - cbore_inset, width - cbore_inset, forConstruction=True)
    .vertices()
    .cboreHole(cbore_hole_diameter, cbore_diameter, cbore_depth)
    .edges("|Z")
    .fillet(5.0)
)

# Displays the result of this script
show_object(result, measure_tools=True)

# forConstructionがいまいちわかってない: 補助ジオメトリはどこに配置されるのか。配置というよりは見えないけど配置されてるイメージ
# verticesの意味が分かってない: 直訳すると頂点だがで、頂点のコーナーらしい
# cboreHoleは？: カウンターボアされた穴を作成するメソッド。ボルトのシャンク/スレッドのクリアランス穴を作成するために使用される。
