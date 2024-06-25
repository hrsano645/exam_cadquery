import cadquery as cq
from ocp_vscode import show_object

# 1.  オブジェクトを構築するためのワークプレーンを設定します。
# 1a. "front"という名前の平面方向を使用してワークプレーンを定義します。
#     これは、正のZ方向が"上"であり、負のZ方向が"下"であることを意味します。
# 2.  後で穴が配置される3Dボックスを作成します。
result = cq.Workplane("front").box(3, 2, 0.5)

# 3.  左下の頂点を選択してワークプレーンを作成します。
# 3a. >Zセレクタを使用して最も上のZ面を選択します。
# 3b. <XYセレクタを使用して面の左下の頂点を選択します。
# 3c. 頂点上に新しいワークプレーンを作成して将来のジオメトリを構築します。
result = result.faces(">Z").vertices("<XY").workplane(centerOption="CenterOfMass")

# 4.  選択した頂点を中心とする円を描きます。
# 4a. 円はボックスを通して切り抜かれ、角が取り除かれます。
result = result.circle(1.0)

# このスクリプトの結果を表示します
show_object(result)

result = result.cutThruAll()
# このスクリプトの結果を表示します
show_object(result)
