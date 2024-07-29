import cadquery as cq
from ocp_vscode import show_object

src_text = "夏日\n真夏日\n猛暑日\n酷暑日"

# テキストを2Dプロファイルとして作成し、それを押し出して3Dオブジェクトに変換
text_3d = cq.Workplane("XY").text(
    src_text,
    10,
    1,
    font="BIZ UDGothic",
    kind="bold",
)


# 結果を表示
show_object(text_3d, measure_tools=True, axes=True, grid=True)

cq.exporters.export(text_3d, "text_3d.stl")
