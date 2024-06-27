import cadquery as cq
from ocp_vscode import show_object

# スプラインパス
path = cq.Workplane("XZ").spline([(0, 0), (2, 5), (10, 0)])
# プロファイルとしての円
profile = cq.Workplane("XY").circle(1)
# スイープ実行
result = profile.sweep(path)

# 結果を表示
print(f"spline length [path]:{path.val().Length():.3f}")
show_object(path, name="path")
show_object(
    result,
    name="result",
    axes=True,
    grid=True,
    ortho=True,
    # debug=True,
)


# ポイントのリストから生成されたスプラインパス
# 最初のスイープの原点指示がないとだめ。もしくはスプライン線を敷くときに、includeCurrent=Trueを指定する（同じ原点になるはず
path_default = cq.Workplane("XZ").spline(
    [(0, 1), (1, 2), (2, 4), (4, 16)], includeCurrent=True
)

# 直径1.0の円をスプラインパスに沿ってスイープする
defaultSweep = cq.Workplane("XY").circle(1.0).sweep(path_default)

print(f"spline length [path_default]:{path_default.val().Length():.3f}")
show_object(path_default.translate((0, 10, 0)), name="path_default")
show_object(
    defaultSweep.translate((0, 10, 0)),
    name="defaultSweep",
    axes=True,
    grid=True,
    ortho=True,
    # debug=True,
)
