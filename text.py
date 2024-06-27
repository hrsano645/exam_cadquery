import cadquery as cq
from ocp_vscode import show_object

# テキストを2Dプロファイルとして作成し、それを押し出して3Dオブジェクトに変換
text_3d = cq.Workplane("XY").text(
    "こんにちはこんにちは！",
    10,
    1,
    font="BIZ UDGothic",
)

# 結果を表示
show_object(text_3d, measure_tools=True, axes=True, grid=True)