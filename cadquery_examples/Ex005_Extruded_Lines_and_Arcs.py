import cadquery as cq
from ocp_vscode import show_object

# 各次元の値をハードコーディングする代わりに、これらを変更できます。
width = 2.0  # プレートの全体の幅
thickness = 0.25  # プレートの厚さ

# 線と円弧からなるプレートのアウトラインを押し出す
# 1. オブジェクトを構築するためのワークプレーンを確立します。
# 1a. ワークプレーンを定義するために、名前付きの平面指向 "front" を使用します。
#     これにより、正の Z 方向が "上" であり、負の Z 方向が "下" になります。
# 2. 原点からプレートの幅の X 位置までの直線を引きます。
# 2a. このような 2D 描画の開始点は、moveTo() 関数によって開始点が移動しない限り、
#     ワークプレーンの中心 (0, 0) になります。
# 3. 直前の位置から Y 方向に 1.0 ミリメートル上に直線を引きます。
# 4. 直前の点から、(1.0, 1.5) の点を経由して、直前の直線の終点から 0.5 mm 上にある位置に
#     半分戻った X 方向に円弧を引きます。円弧は (0.0, 1.0) で終わり、これは最初の直線の
#     開始点から 1.0 mm 上にある位置です。
# 5. 直前の点から円弧を引きます。この円弧は (-0.5, 1.0) で終わり、曲線のサグは 0.2 で、
#     曲線のベースラインから 0.1 mm 離れた位置に凹んでいます。サグが -0.2 の場合、
#     円弧は凸になります。この規則は、プロファイルが反時計回りに描かれた場合に有効です。
#     時計回り:        +サグ => 凸,  -サグ => 凹
#     反時計回り:    +サグ => 凹,  -サグ => 凸
# 6. 直前の点から円弧を引きます。この円弧は (-0.7, -0.2) で終わり、半径は -1.5 mm で決まります。
#     時計回り:        +半径 => 凸,  -半径 => 凹
#     反時計回り:    +半径 => 凹,  -半径 => 凸
# 7. close() を呼び出して、最後の直線を自動的に引き、スケッチを閉じて押し出し可能にします。
# 7a. close() を使用しない場合、2D スケッチは開いたままになり、押し出し操作の結果は予測できません。
# 8. 2D スケッチを指定した厚さの固体オブジェクトに押し出します。
result = (
    cq.Workplane("front")
    .lineTo(width, 0)
    .lineTo(width, 1.0)
    .threePointArc((1.0, 2.0), (0.0, 1.0))
    .sagittaArc((-0.5, 1.0), 0.2)
    .radiusArc((-1.0, -0.5), -1.5)
    .close()
    .extrude(thickness)
)

# このスクリプトの結果を表示します
show_object(result, measure_tools=True, axes=True, grid=True, ortho=True, debug=True)