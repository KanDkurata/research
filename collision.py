import tkinter


def isCollided(a_coords, b_coords):

    # 当たってるかどうかを判断する
    a_x1, a_y1, a_x2, a_y2 = a_coords
    b_x1, b_y1, b_x2, b_y2 = b_coords

    c_x1 = max(a_x1, b_x1)
    c_y1 = max(a_y1, b_y1)
    c_x2 = min(a_x2, b_x2)
    c_y2 = min(a_y2, b_y2)

    if c_x1 < c_x2 and c_y1 < c_y2:
        return True
    else:
        return False


def move(event):

    # マウスの位置からマウス用の矩形の座標計算
    x1 = event.x - mouse_rect_width / 2
    y1 = event.y - mouse_rect_height / 2
    x2 = event.x + mouse_rect_width / 2
    y2 = event.y + mouse_rect_height / 2

    mouse_coords = (x1, y1, x2, y2)

    # マウス用の矩形の座標を変更
    canvas.coords(mouse_rect, mouse_coords)

    if isCollided(mouse_coords, target_coords):
        # 当たってたら相手の矩形の色をオレンジにする
        canvas.itemconfig(target_figure, fill="gray")
    else:
        # 当たってなかったら相手の矩形の色を白に戻す
        canvas.itemconfig(target_figure, fill="white")


app = tkinter.Tk()

canvas = tkinter.Canvas(
    app,
    width=400,
    height=300,
    highlightthickness=0
)
canvas.pack()

# 矩形の座標を設定
target_coords = (95, 130, 250, 200)

# マウス用の矩形の幅と高さを設定
mouse_rect_width = 80
mouse_rect_height = 80

# 矩形を描画
target_figure = canvas.create_rectangle(
    target_coords,
    fill="white"
)

mouse_rect = canvas.create_rectangle(
    0, 0, 0, 0,  # move関数で正しく設定
    fill="white"
)

# マウスが動いたときにmoveを実行するように設定
app.bind("<Motion>", move)

app.mainloop()
