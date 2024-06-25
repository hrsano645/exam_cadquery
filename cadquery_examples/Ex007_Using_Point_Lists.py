import cadquery as cq
from ocp_vscode import show_object

# これらは各寸法の値をハードコーディングする代わりに変更できます。
plate_radius = 2.0  # 押し出されるプレートの半径
hole_pattern_radius = 0.25  # 穴が配置される円の半径
thickness = 0.125  # 押し出されるプレートの厚さ
# ワークプレーンの中心から極座標配置でプレートに4つの穴を持つプレートを作成します。
# 1. オブジェクトを構築できるワークプレーンを確立します。
# 1a. ワークプレーンを定義するために名前付きの平面方向「front」を使用します。つまり、
#     正のZ方向が「上」であり、負のZ方向が「下」であることを意味します。
r = cq.Workplane("front").circle(plate_radius)

# 3. 穴の中心点として使用される4つのポイントをスタックにプッシュします。
r = r.pushPoints([(1.5, 0), (0, 1.5), (-1.5, 0), (0, -1.5)])

# 4. このcircle()呼び出しは、すべての4つのポイントに対して動作し、それぞれに円を配置します。
r = r.circle(hole_pattern_radius)


# ポイントをさらに追加して穴を開けることもできる
r = r.pushPoints([(1, 1), (1, -1), (-1, 1), (-1, -1)])
r = r.circle(hole_pattern_radius)


# 5. すべての2Dジオメトリはプレートの指定された厚さに押し出されます。
# 5a. 小さな穴の円はプレートの外側の円に含まれているため、プレートから切り抜かれることを想定しています。別個の切り抜き操作は必要ありません。
result = r.extrude(thickness)

# このスクリプトの結果を表示します
show_object(result)
