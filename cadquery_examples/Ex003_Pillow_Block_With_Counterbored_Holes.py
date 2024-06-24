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
result = (
    cq.Workplane("XY")
    .box(length, width, thickness)
    # .edges("|Z")  # Z軸に平行なエッジを選択
    # .fillet(8.0)  # フィレットの半径を5.0に設定
    # .edges("|X")  # Z軸に平行なエッジを選択
    # .fillet(2.0)  # フィレットの半径を5.0に設定
    .edges()  # Z軸に平行なエッジを選択
    .fillet(2.0)  # フィレットの半径を5.0に設定
    .faces(">Z")
    .workplane()
    .hole(center_hole_dia)
    .faces(">Z")
    .workplane()
    .rect(length - cbore_inset, width - cbore_inset, forConstruction=True)
    .vertices()
    .cboreHole(cbore_hole_diameter, cbore_diameter, cbore_depth)
)

# 結果を表示します
show_object(result, measure_tools=True)

# --- Claude 3.5 Sonnet からいろいろ変更したもの ---

# フィレットを適用
result2 = (
    cq.Workplane("XY", (length + 10, 0, 0))
    .box(length, width, thickness)
    .edges("|Z")  # Z軸に平行なエッジを選択
    .fillet(5.0)  # フィレットの半径を5.0に設定
    .edges("|X")  # X軸またはY軸に平行なエッジを選択
    .fillet(2.0)  # フィレットの半径を2.0に設定
    # 中央の穴を開ける
    .faces(">Z")
    .workplane()
    .hole(center_hole_dia)
    # カウンターボア穴を追加
    .faces(">Z")
    .workplane()
    .rect(length - cbore_inset, width - cbore_inset, forConstruction=True)
    .vertices()
    .cboreHole(cbore_hole_diameter, cbore_diameter, cbore_depth)
)

# 結果の表示
show_object(result2, measure_tools=True)
