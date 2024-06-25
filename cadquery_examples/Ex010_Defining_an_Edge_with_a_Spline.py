import cadquery as cq
from ocp_vscode import show_object

# 1. スプラインを作成するためのワークプレーンを設定します。
# 1a. XとYの原点を使用してワークプレーンを定義します。つまり、
# 正のZ方向は「上」を意味し、負のZ方向は「下」を意味します。
s = cq.Workplane("XY")

# スプラインが通過するポイント
sPnts = [
    (2.75, 1.5),
    (2.5, 1.75),
    (2.0, 1.5),
    (1.5, 1.0),
    (1.0, 1.25),
    (0.5, 1.0),
    (0, 1.0),
]

# 2. スプラインフィーチャを持つプレートを生成し、閉じたエンティティであることを確認します。
r = s.lineTo(3.0, 0).lineTo(3.0, 1.0).spline(sPnts, includeCurrent=True).close()

# 3. ワイヤをプレートに変換するために押し出します。
result = r.extrude(0.5)

# フィレットを追加します。
result = result.edges().fillet(0.05)

# このスクリプトの結果を表示します。
show_object(result)
