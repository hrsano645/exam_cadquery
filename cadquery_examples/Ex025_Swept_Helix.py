import cadquery as cq
from ocp_vscode import show_object

r = 0.5  # ヘリックスの半径
p = 0.4  # ヘリックスのピッチ - ループ間の垂直距離
h = 2.4  # ヘリックスの高さ - 総高さ

# ヘリックス
wire = cq.Wire.makeHelix(pitch=p, height=h, radius=r)
show_object(wire)
helix = cq.Workplane(obj=wire)

# 最終結果：ヘリックスに沿ってスイープされた2D形状。
result = (
    cq.Workplane("XZ")  # ヘリックスはZ軸方向に移動する
    .center(r, 0)  # 等脚台形のオフセット
    .polyline(((-0.15, 0.1), (0.0, 0.05), (0, 0.35), (-0.15, 0.3)))
    .close()  # エッジをワイヤにする
    .sweep(helix, isFrenet=True)  # Frenetは期待どおりの向きを保つ
)

show_object(result)

# スイープした2D図形を表示する

result2 = (
    cq.Workplane("XZ")  # ヘリックスはZ軸方向に移動する
    .center(r, 0)  # 等脚台形のオフセット
    .polyline(((-0.15, 0.1), (0.0, 0.05), (0, 0.35), (-0.15, 0.3)))
    .close()  # エッジをワイヤにする
    .extrude(0.5)  # ワイヤを3D形状にする
)

show_object(result2)
