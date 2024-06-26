import cadquery as cq
from ocp_vscode import show_object

# 1. オブジェクトを構築するためのワークプレーンを確立します。
# 1a. "front"という名前の平面方向を使用してワークプレーンを定義します。これは、
#     正のZ方向が"上"であり、負のZ方向が"下"であることを意味します。
# 2. 後でジオメトリに基づく3Dボックスを作成します。
result = cq.Workplane("front").box(3, 2, 0.5)

# 3. X方向の最も低い面を<Xセレクタで選択します。
# 4. 新しいワークプレーンを作成します。
# 4a. ワークプレーンは、元のボックスに触れないようにオフセットされます。
result = result.faces("<X").workplane(offset=0.75)

# 5. オフセットワークプレーン上に浮いている薄い円盤を作成します。
result = result.circle(1.0).extrude(1.5)

# このスクリプトの結果を表示します。
show_object(result)
