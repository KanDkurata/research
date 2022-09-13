#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter

root = tkinter.Tk()


# キャンバスの生成
c0 = tkinter.Canvas(root, width=150, height=150)
oval_id = c0.create_oval(10, 10, 140, 140, tags='o')
c0.itemconfigure(oval_id, fill='#ffb6c1', outline='red')


# 図形の位置を取得
oval_pos = c0.coords(oval_id)

# テキストをとりあえず描写
text_id = c0.create_text(10, 10, text=u"文字表示される所ですね")

# テキストのサイズを取得
text_size = c0.bbox(text_id)


# 図形の中央を取得
oc_x = oval_pos[2] / 2
oc_y = oval_pos[3] / 2


# テキストの中央を取得
tc_x = text_size[2] / 2
tc_y = text_size[3] / 2


# テキストを図形のセンターに移動
c0.move(text_id, oc_x - (oval_pos[0]/2), oc_y - tc_y)


c0.pack()

root.mainloop()
