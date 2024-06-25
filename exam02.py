import cadquery as cq
from ocp_vscode import show_object

result = (
    cq.Workplane("XY")
    .rect(10, 10)  # 四角形のスケッチ
    .extrude(5)  # 押し出し
    .faces(">Z")
    .workplane()  # 新しいワークプレーンの作成
    .circle(5)  # 円のスケッチ
    .extrude(5)  # 押し出し
)

show_object(result)
