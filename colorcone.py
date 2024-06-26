import cadquery as cq
from ocp_vscode import show_object

# 変数設定
cone_height = 50  # カラーコーンの高さ
cone_radius = 20  # カラーコーンの底面の半径
base_height = 5  # 平たい正方立方体の高さ
base_width = 40  # 平たい正方立方体の幅
base_margin = 10  # 平たい正方立方体のマージン
hemisphere_radius = 5  # 頂点の半球の半径

# 正方立方体のベースを作成
base = cq.Workplane("XY").box(
    base_width + base_margin, base_width + base_margin, base_height
)

# 円錐を作成
cone = (
    cq.Workplane("XY")
    .workplane(offset=base_height / 2)
    .circle(cone_radius)
    .workplane(offset=cone_height)
    .circle(hemisphere_radius)
    .loft()
)

# 半球を作成
hemisphere = (
    cq.Workplane("XY")
    .sphere(hemisphere_radius)
    .translate((0, 0, base_height / 2 + cone_height))
)

# ベースと円錐と半球を結合
cone_model = base.union(cone).union(hemisphere)

# モデルを表示
show_object(cone_model)
