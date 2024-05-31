import cadquery as cq
from ocp_vscode import show_object

# パラメータ定義
p_outerWidth = 100.0  # 箱の外側の幅
p_outerLength = 150.0  # 箱の外側の長さ
p_outerHeight = 50.0  # 箱の外側の高さ

p_thickness = 3.0  # 箱の壁の厚さ
p_sideRadius = 10.0  # 箱の側面の曲線の半径
p_topAndBottomRadius = 2.0  # 箱の上部および下部の曲線の半径

p_screwpostInset = 12.0  # ねじポストが縁からどれだけ内側に配置されるか
p_screwpostID = 4.0  # ねじポスト穴の内径（ねじの直径に近い値）
p_screwpostOD = 10.0  # ねじポストの外径（ポスト全体の厚さを決定する）

p_boreDiameter = 8.0  # 座ぐり穴の直径（ある場合）
p_boreDepth = 1.0  # 座ぐり穴の深さ
p_countersinkDiameter = 0.0  # 皿穴の外径（ねじ頭の外径に近い値）
p_countersinkAngle = (
    90.0  # 皿穴の角度（中心から片側までの角度ではなく、対向する面間の角度）
)
p_flipLid = True  # 蓋を上下逆さまに配置するかどうか
p_lipHeight = 1.0  # 蓋の裏側の突起の高さ（箱本体にぴったり嵌る）

# 外側シェルの作成
oshell = (
    cq.Workplane("XY")
    .rect(p_outerWidth, p_outerLength)
    .extrude(p_outerHeight + p_lipHeight)
)

# フィレットを適用する順序を間違えるとおかしな形状になる
if p_sideRadius > p_topAndBottomRadius:
    oshell = oshell.edges("|Z").fillet(p_sideRadius)
    oshell = oshell.edges("#Z").fillet(p_topAndBottomRadius)
else:
    oshell = oshell.edges("#Z").fillet(p_topAndBottomRadius)
    oshell = oshell.edges("|Z").fillet(p_sideRadius)

# show_object(oshell)

# 内側シェルの作成
ishell = (
    oshell.faces("<Z")
    .workplane(p_thickness, True)
    .rect((p_outerWidth - 2.0 * p_thickness), (p_outerLength - 2.0 * p_thickness))
    .extrude(
        (p_outerHeight - 2.0 * p_thickness), False
    )  # 結合をfalseに設定して新しいボスだけを生成
)
ishell = ishell.edges("|Z").fillet(p_sideRadius - p_thickness)

# show_object(ishell)

# # 外側シェルから内側シェルを切り取って箱を作成
box = oshell.cut(ishell)

# # ねじポストを作成
# POSTWIDTH = p_outerWidth - 2.0 * p_screwpostInset
# POSTLENGTH = p_outerLength - 2.0 * p_screwpostInset

# box = (
#     box.faces(">Z")
#     .workplane(-p_thickness)
#     .rect(POSTWIDTH, POSTLENGTH, forConstruction=True)
#     .vertices()
#     .circle(p_screwpostOD / 2.0)
#     .circle(p_screwpostID / 2.0)
#     .extrude(-1.0 * (p_outerHeight + p_lipHeight - p_thickness), True)
# )

# show_object(box)

# exit()

# 蓋を上部と下部に分割
(lid, bottom) = (
    box.faces(">Z")
    .workplane(-p_thickness - p_lipHeight)
    .split(keepTop=True, keepBottom=True)
    .all()
)  # 二つのソリッドに分割

result = lid.translate((0, 0, 10)).union(bottom)
show_object(result, measure_tools=True)

# exit()

# 蓋を移動し、蓋の内側から下部を差し引いて嵌り部分を作成
lowerLid = lid.translate((0, 0, -p_lipHeight))

show_object(lowerLid, measure_tools=True)

cutlip = lowerLid.cut(bottom).translate(
    (p_outerWidth + p_thickness, 0, p_thickness - p_outerHeight + p_lipHeight)
)
# memo なるほど。bottomに少し入れこんで差分を作ることで、bottomのサイズをそのまま嵌り部分にできるのか。
# ただその時に高さをきれいに合わせるために、最初のbox作成で高さをp_outerHeight + p_lipHeightにしているのか。

# result = lid.translate((0, 0, 10)).union(bottom)
show_object(cutlip, measure_tools=True)

exit()

# ねじ穴の中心を計算
topOfLidCenters = (
    cutlip.faces(">Z")
    .workplane(centerOption="CenterOfMass")
    .rect(POSTWIDTH, POSTLENGTH, forConstruction=True)
    .vertices()
)

# 目的に応じた穴を追加
if p_boreDiameter > 0 and p_boreDepth > 0:
    topOfLid = topOfLidCenters.cboreHole(
        p_screwpostID, p_boreDiameter, p_boreDepth, 2.0 * p_thickness
    )
elif p_countersinkDiameter > 0 and p_countersinkAngle > 0:
    topOfLid = topOfLidCenters.cskHole(
        p_screwpostID, p_countersinkDiameter, p_countersinkAngle, 2.0 * p_thickness
    )
else:
    topOfLid = topOfLidCenters.hole(p_screwpostID, 2.0 * p_thickness)

# 蓋を上下逆さまにする場合
if p_flipLid:
    topOfLid = topOfLid.rotateAboutCenter((1, 0, 0), 180)

# 結果を結合して返す
result = topOfLid.union(bottom)

show_object(result, name="boxbody", measure_tools=True)
