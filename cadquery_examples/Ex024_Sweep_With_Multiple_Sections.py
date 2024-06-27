import cadquery as cq
from ocp_vscode import show_object

# X軸に長さ20.0の直線を作成
path = cq.Workplane("XZ").moveTo(-10, 0).lineTo(10, 0)
show_object(path, name="パス")

# 直径2.0から直径1.0まで直径2.0の円をX軸に沿って長さ10.0 + 10.0スイープする
defaultSweep = (
    cq.Workplane("YZ")
    .workplane(offset=-10.0)
    .circle(2.0)
    .workplane(offset=10.0)
    .circle(1.0)
    .workplane(offset=10.0)
    .circle(2.0)
    .sweep(path, multisection=True)
)

# 異なる形状でスイープすることもできます
recttocircleSweep = (
    cq.Workplane("YZ")
    .workplane(offset=-10.0)
    .rect(2.0, 2.0)
    .workplane(offset=8.0)
    .circle(1.0)
    .workplane(offset=4.0)
    .circle(1.0)
    .workplane(offset=8.0)
    .rect(2.0, 2.0)
    .sweep(path, multisection=True)
)

circletorectSweep = (
    cq.Workplane("YZ")
    .workplane(offset=-10.0)
    .circle(1.0)
    .workplane(offset=7.0)
    .rect(2.0, 2.0)
    .workplane(offset=6.0)
    .rect(2.0, 2.0)
    .workplane(offset=7.0)
    .circle(1.0)
    .sweep(path, multisection=True)
)


# 形状の配置は重要です。予期しない形状が生成される可能性があります
specialSweep = (
    cq.Workplane("YZ")
    .circle(3.0)
    .workplane(offset=10.0)
    .rect(2.0, 2.0)
    .sweep(path, multisection=True)
)

# パスを円弧に切り替える：線の長さl=5.0、半円の半径r=4.0、線の長さl=5.0
path = (
    cq.Workplane("XZ")
    .moveTo(-5, 4)
    .lineTo(0, 4)
    .threePointArc((4, 0), (0, -4))
    .lineTo(-5, -4)
)

# 異なる形状の配置はパスに従う必要があります
# 最初の線に沿って半径1.5の円柱をスイープ
# 次に半径1.5から半径1.0までの円弧に沿ってスイープ
# 最後の線に沿って半径1.0の円柱をスイープ
arcSweep = (
    cq.Workplane("YZ")
    .workplane(offset=-5)
    .moveTo(0, 4)
    .circle(1.5)
    .workplane(offset=5, centerOption="CenterOfMass")
    .circle(1.5)
    .moveTo(0, -8)
    .circle(1.0)
    .workplane(offset=-5, centerOption="CenterOfMass")
    .circle(1.0)
    .sweep(path, multisection=True)
)


# 重ならないように結果の固体を移動し、左から右に表示する
show_object(defaultSweep)
show_object(circletorectSweep.translate((0, 5, 0)))
show_object(recttocircleSweep.translate((0, 10, 0)))
show_object(specialSweep.translate((0, 15, 0)))
show_object(arcSweep.translate((0, -5, 0)))
