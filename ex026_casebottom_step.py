import cadquery as cq
from cadquery.selectors import AreaNthSelector
from ocp_vscode import show_object

# ステップ1: 長方形を作成して押し出し
step1 = cq.Workplane("XY").rect(20, 20).extrude(10)

# ステップ2: フィレットを適用
step2 = step1.edges("|Z or <Z").fillet(2)

# ステップ3: 上面を選択してシェルを作成
step3 = step2.faces(">Z").shell(2)

# ステップ4: 上面の外側のワイヤーを選択して中央にオフセット
step4 = (
    step3.faces(">Z")
    .wires(AreaNthSelector(-1))
    .toPending()
    .workplane()
    .offset2D(-1)
    .extrude(1)
)

# ステップ5: シーム面の断面ワイヤーを選択して切り抜き
step5 = (
    step4.faces(">Z[-2]").wires(AreaNthSelector(0)).toPending().workplane().cutBlind(2)
)

# 各ステップの結果を表示
show_object(
    step1.translate((0, 0, 0)),
    name="Step 1: Extrude",
    measure_tools=True,
    axes=True,
    grid=True,
    ortho=True,
    debug=True,
)
show_object(
    step2.translate((25, 0, 0)),
    name="Step 2: Fillet",
    measure_tools=True,
    axes=True,
    grid=True,
    ortho=True,
    debug=True,
)
show_object(
    step3.translate((50, 0, 0)),
    name="Step 3: Shell",
    measure_tools=True,
    axes=True,
    grid=True,
    ortho=True,
    debug=True,
)
show_object(
    step4.translate((75, 0, 0)),
    name="Step 4: Offset and Extrude",
    measure_tools=True,
    axes=True,
    grid=True,
    ortho=True,
    debug=True,
)
show_object(
    step5.translate((100, 0, 0)),
    name="Step 5: Cut",
    measure_tools=True,
    axes=True,
    grid=True,
    ortho=True,
    debug=True,
)
