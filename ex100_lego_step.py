import cadquery as cq
from ocp_vscode import show_object

# このスクリプトは、任意の正方形のレゴ(TM)ブロックを作成することができます

#####
# 入力
######
lbumps = 1  # ブロックの長さ方向の突起の数
wbumps = 4  # ブロックの幅方向の突起の数
thin = True  # Trueなら薄型、Falseなら厚型

#
# レゴブロックの定数--これによってレゴブロックがレゴブロックになります :)
#
pitch = 8.0
clearance = 0.1
bumpDiam = 4.8
bumpHeight = 1.8
if thin:
    height = 3.2
else:
    height = 9.6

t = (pitch - (2 * clearance) - bumpDiam) / 2.0
postDiam = pitch - t  # 6.5になります
total_length = lbumps * pitch - 2.0 * clearance
total_width = wbumps * pitch - 2.0 * clearance

# ベースを作成する
s = cq.Workplane("XY").box(total_length, total_width, height)
show_object(
    s.translate((0, 0, 0)),
    name="Step 1: Base",
    measure_tools=True,
    axes=True,
    grid=True,
    ortho=True,
    debug=True,
)

# 内側にシェルを作成する
s = s.faces("<Z").shell(-1.0 * t)
show_object(
    s.translate((30, 0, 0)),
    name="Step 2: Shell",
    measure_tools=True,
    axes=True,
    grid=True,
    ortho=True,
    debug=True,
)

# 上部に突起を作成する
s = (
    s.faces(">Z")
    .workplane()
    .rarray(pitch, pitch, lbumps, wbumps, True)
    .circle(bumpDiam / 2.0)
    .extrude(bumpHeight)
)
show_object(
    s.translate((60, 0, 0)),
    name="Step 3: Bumps",
    measure_tools=True,
    axes=True,
    grid=True,
    ortho=True,
    debug=True,
)

# 底部にポストを追加する。ジオメトリによってポストの直径が異なります
# 1つの突起の場合はソリッドスタッド、複数の突起の場合はチューブ、1x1の場合はなし
tmp = s.faces("<Z").workplane(invert=True)

if lbumps > 1 and wbumps > 1:
    tmp = (
        tmp.rarray(pitch, pitch, lbumps - 1, wbumps - 1, center=True)
        .circle(postDiam / 2.0)
        .circle(bumpDiam / 2.0)
        .extrude(height - t)
    )
elif lbumps > 1:
    tmp = (
        tmp.rarray(pitch, pitch, lbumps - 1, 1, center=True)
        .circle(t)
        .extrude(height - t)
    )
elif wbumps > 1:
    tmp = (
        tmp.rarray(pitch, pitch, 1, wbumps - 1, center=True)
        .circle(t)
        .extrude(height - t)
    )
else:
    tmp = s

# ソリッドをレンダリングする
show_object(
    tmp.translate((90, 0, 0)),
    name="Step 4: Posts",
    measure_tools=True,
    axes=True,
    grid=True,
    ortho=True,
    debug=True,
)
