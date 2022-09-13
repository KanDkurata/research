import tkinter


def click(event):
    global figure
    global before_x, before_y

    x = event.x
    y = event.y

    # クリックされた位置に一番近い図形のID取得
    figure = canvas.find_closest(x, y)

    # マウスの座標を記憶
    before_x = x
    before_y = y


def drag(event):
    global before_x, before_y

    x = event.x
    y = event.y

    # 前回からのマウスの移動量の分だけ図形も移動
    canvas.move(
        figure,
        x - before_x, y - before_y
    )

    # マウスの座標を記憶
    before_x = x
    before_y = y


def main():
    global canvas

    app = tkinter.Tk()

    # キャンバス作成
    canvas = tkinter.Canvas(
        app,
        width=1000, height=600,
        highlightthickness=0,
        bg="white"
    )

    canvas.grid(row=0, column=0)

    app.update()
    canvas.create_line(
        canvas.winfo_width()/2, 0, canvas.winfo_width() /
        2, canvas.winfo_height()  # x1,y1,x2,y2
    )

    # 色を用意
    color = (
        "red"
    )

    # テキストを用意
    texts = (
        "注文は終了？", "値段の表示", "野菜名の入力", "合計金額の表示", "入力値の保存", "値段の入力", "合計金額の増加", "空の注文票の作成", "野菜名の表示", "終了",
    )

    # テキストの数だけ適当に位置をずらしながら長方形（正方形）を描画
    for i, text_one in enumerate(texts):
        x = 100
        y = i * 50 + 250
        if i > 6:
            x += 120
            y -= 350
        if i > 12:
            x += 240
            y -= 700
        textlist = canvas.create_text(
            x, y,  # x,y
            text=text_one,
            fill=color,
        )

        # 描画した図形にイベント処理設定
        canvas.tag_bind(textlist, "<ButtonPress-1>", click)
        canvas.tag_bind(textlist, "<Button1-Motion>", drag)

    app.mainloop()


if __name__ == "__main__":
    main()
