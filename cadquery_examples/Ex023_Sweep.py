import cadquery as cq
from ocp_vscode import show_object

# スイープするためのスプラインとポリラインパスに使用するポイント
pts = [(0, 1), (1, 2), (2, 4), (4, 16)]

# ポイントのリストから生成されたスプラインパス
path_default = cq.Workplane("XZ").spline(pts)

# 直径1.0の円をスプラインパスに沿ってスイープする
defaultSweep = cq.Workplane("XY").circle(1.0).sweep(path_default)

# スイープはデフォルトでソリッドを作成し、Frenetソリッドを生成しません。FrenetをTrueに設定すると、プロファイルの向きのクリープを防ぐのに役立ちます
frenetShell = (
    cq.Workplane("XY").circle(1.0).sweep(path_default, makeSolid=True, isFrenet=True)
)

# 円以外の形状もスイープできます
defaultRect = cq.Workplane("XY").rect(1.0, 1.0).sweep(path_default)

# ポリラインパスに切り替えますが、スプラインと同じポイントを使用します
path_pline = cq.Workplane("XZ").polyline(pts, includeCurrent=True)

# ポリラインパスを使用すると、結果のソリッドは単一のスイープ外側面ではなく、セグメントを持ちます
plineSweep = cq.Workplane("XY").circle(1.0).sweep(path_pline)

# パスにアークを使用します
path_arc = cq.Workplane("XZ").threePointArc((1.0, 1.5), (0.0, 1.0))

# 外観を少し見栄え良くするために、より小さな円セクションを使用します
arcSweep = cq.Workplane("XY").circle(1.0).sweep(path_arc)

# 結果のソリッドを重ならないように変換し、左から右に表示します
show_object(path_default.translate((0, 0, -1)), name="path_default")
show_object(defaultSweep, name="defaultSweep")
show_object(path_default.translate((5, 0, -1)), name="path_default1")
show_object(frenetShell.translate((5, 0, 0)), name="frenetShell")
show_object(path_default.translate((10, 0, -1)), name="path_default2")
show_object(defaultRect.translate((10, 0, 0)), name="defaultRect")
show_object(path_pline.translate((15, 0, 0)), name="path_pline")
show_object(plineSweep.translate((15, 0, 0)), name="plineSweep")
show_object(path_arc.translate((20, 0, 0)), name="path_arc")
show_object(arcSweep.translate((20, 0, 0)), name="arcSweep")
