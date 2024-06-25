import cadquery as cq
from ocp_vscode import show_object

# 1. オブジェクトを構築するためのワークプレーンを設定します。
# 1a. "front" という名前の平面方向を使用してワークプレーンを定義します。
#     これは、正のZ方向が "上" であり、負のZ方向が "下" であることを意味します。
# 2. 後で穴が配置される3Dボックスを作成します。
result = cq.Workplane("front").box(2, 3, 0.5)

# 3. >Z max セレクターを使用して最も上の面を見つけます。
# 3a. 新しいワークプレーンを設定してジオメトリを構築します。
# 3b. ボックスに穴を作成します。
result = result.faces(">Z").workplane().hole(0.5)

# このスクリプトの結果を表示します。
show_object(result)
