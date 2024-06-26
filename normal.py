import cadquery as cq

# 簡単なボックスを作成
box = cq.Workplane("XY").box(1, 2, 3)

# ボックスの面の一つを取得し、その法線を表示
face = box.faces(">Z").val()
normal = face.normalAt()
print(f"法線ベクトル: {normal}")
