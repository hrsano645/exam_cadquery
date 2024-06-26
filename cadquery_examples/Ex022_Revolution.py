import cadquery as cq
from ocp_vscode import show_object

# モデルの寸法。これらは、形状のコードを直接変更する代わりに変更できます。
rectangle_width = 10.0
rectangle_length = 10.0
angle_degrees = 360.0

# 長方形から円柱を回転させる
# 異なるパラメータで回転操作を試すために、このセクションのコメントを切り替えてください
# result = cq.Workplane("XY").rect(rectangle_width, rectangle_length, False).revolve()
# result = (
#     cq.Workplane("XY")
#     .rect(rectangle_width, rectangle_length, False)
#     .revolve(angle_degrees)
# )
# result = (
#     cq.Workplane("XY")
#     .rect(rectangle_width, rectangle_length)
#     .revolve(angle_degrees, (-5, -5))
# )
# result = (
#     cq.Workplane("XY")
#     .rect(rectangle_width, rectangle_length)
#     .revolve(angle_degrees, (-5, -5), (-5, 5))
# )
result = (
    cq.Workplane("XY")
    .rect(rectangle_width, rectangle_length)
    .revolve(angle_degrees, (-5, -5), (-5, 5), False)
)

# 四角い壁のドーナツを回転させる
# result = (
#     cq.Workplane("XY")
#     .rect(rectangle_width, rectangle_length, True)
#     .revolve(angle_degrees, (20, 0), (20, 10))
# )

# スクリプトの結果を表示する
show_object(result)
