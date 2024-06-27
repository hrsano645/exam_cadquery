import cadquery as cq
from cadquery.selectors import AreaNthSelector
from ocp_vscode import show_object

# ケースの底部を作成する
case_bottom = (
    cq.Workplane("XY")
    .rect(20, 20)  # 20x20の長方形を作成
    .extrude(10)  # 高さ10の立方体に変換
    .edges("|Z or <Z")  # Z軸方向または-Z軸方向のエッジを選択
    .fillet(2)  # 上面以外の全てのエッジを2の半径でフィレット
    .faces(">Z")  # 上面を選択
    .shell(2)  # 厚さ2のシェルを作成（上面は開いたまま）
    .faces(">Z")  # 上面を選択
    .wires(AreaNthSelector(-1))  # 上面の外側のワイヤーを選択
    .toPending()
    .workplane()
    .offset2D(-1)  # ケースのシーム面の中心線ワイヤーを作成
    .extrude(1)  # シェルを一時的な"蓋"で覆う
    .faces(">Z[-2]")  # シーム面を選択
    .wires(AreaNthSelector(0))  # ケースの断面ワイヤーを選択
    .toPending()
    .workplane()
    .cutBlind(2)  # "蓋"を通して切り抜く（シーム面にリップを残す）
)

# 類似のプロセスをトップ部分に繰り返す
# 内部にリップを作る代わりに、ケースのシーム中心線内部の材料を取り除く
case_top = (
    cq.Workplane("XY")
    .move(25)
    .rect(20, 20)  # 20x20の長方形を作成
    .extrude(5)  # 高さ5の立方体に変換
    .edges("|Z or >Z")  # Z軸方向または+Z軸方向のエッジを選択
    .fillet(2)  # 上面以外の全てのエッジを2の半径でフィレット
    .faces("<Z")  # 下面を選択
    .shell(2)  # 厚さ2のシェルを作成（下面は開いたまま）
    .faces("<Z")  # 下面を選択
    .wires(AreaNthSelector(-1))  # 下面の外側のワイヤーを選択
    .toPending()
    .workplane()
    .offset2D(-1)  # ケースのシーム面の中心線ワイヤーを作成
    .cutBlind(-1)  # シーム面の内部を切り抜く
)

show_object(case_bottom)
show_object(case_top, options={"alpha": 0.5})
