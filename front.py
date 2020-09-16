# - * - coding: utf8 - * -

#tkinterの準備
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from multiprocessing.pool import ThreadPool


#バックを利用するのに使うやつ
import sys
sys.path.append('..')
from craker_back import back



##フレームの作成
root = tk.Tk()

##ウィンドウのサイズを固定
root.resizable(width = False, height = False)

##フレームの名前を設定   
root.title("craker")

##ウィンドウの大きさを設定
canvas = tk.Canvas(root, width = 450, heigh = 620)
canvas.pack()
img = tk.PhotoImage(file = "background.gif")
canvas.create_image(225, 310, image = img)
"""
root.geometry("450x620")
root.configure(bg = "#f1fcfc")
"""

##ラベル作成
"""
label_title = tk.Label(root, text = "虫食い算", font = ("", 17), bg = "#f1fcfc", fg = "#481380")
label_title.place(relx = 0.45, rely = 0.01)

label_diff = tk.Label(root, text = "難易度", bg = "#f1fcfc", fg = "#481380")
label_diff.place(relx = 0.25, rely = 0.1)
"""

label_digits = tk.Label(root, text = "桁数", bg = "#FFFFFF")
label_digits.place(relx = 0.92, rely = 0.134)

##テキストボックスの作成
#txt_diff = tk.Entry(width = 3)
#txt_diff.place(relx = 0.55, rely = 0.05)

txt_digits = tk.Entry(width = 2, bg = "#cff1ef")
txt_digits.place(relx = 0.94, rely = 0.184)

##スケールの作成
label_difficult = tk.Label(root, text = "難", bg = "#FFFFFF")
label_easy = tk.Label(root, text = "易", bg = "#FFFFFF")
label_difficult.place(relx = 0.87, rely = 0.134)
label_easy.place(relx = 0.68, rely = 0.134)
var_input_diff = tk.IntVar(master = root, value = 0)
#var_diff.set(0)
scale_diff = tk.Scale(root, orient = 'h', from_ = 0, to = 9, variable = var_input_diff, showvalue = False, resolution = 1, length = 100)
scale_diff.place(relx = 0.68, rely = 0.186)

##グローバル変数
problem = None
ans = None
diff = None

var_problem = tk.StringVar()
var_problem.set("")
var_diff = tk.StringVar()
var_diff.set("")
var_ans = tk.StringVar()
var_ans.set("")
##問題作成ボタンが押された時に実行される関数
def clicked_1(self):
    global problem, ans, diff
    input_diff = int(var_input_diff.get())
    input_digits = txt_digits.get()
    ###エラーメッセージ
    if not input_digits.isdecimal():
        res_str_error = messagebox.showwarning("エラー", "桁数は数字で入力してください")
        print("showwarning", res_str_error)
        txt_digits.delete(0, tk.END)
        return 1
    if input_digits == "":
        res_null_error = messagebox.showwarning("エラー", "数字を入力してください")
        print("showwarning", res_null_error)
        return 1
    #input_diff = int(input_diff)
    input_digits = int(input_digits)
    """
    if input_diff < 0 or input_diff > 9:
        res_diff_error = messagebox.showwarning("エラー", "難易度は0~9の数字で入力してください")
        print("showwarning", res_diff_error)
        return 1
    """
    if input_digits <= 0 or input_digits >= 6:
        res_digits_error = messagebox.showwarning("エラー", "桁数は1~5の数字で入力してください")
        print("showwarning", res_digits_error)
        txt_digits.delete(0, tk.END)
        return 1
    
    button_problem.config(state = 'disable')
    ###本題
    problem, ans, diff = back.problem_maker(input_diff, input_digits)
    if problem == -1:
        res_error = messagebox.showwarning("エラー", "解が見つかりませんでした\nもう一度試してください")
        print("showwarning, res_error")
        return 1
    strings = back.print_figure(problem)
    var_problem.set(strings)
    var_diff.set("実測難易度\n      " + str(diff))
    button_problem.config(state = 'active')
    var_ans.set("")
label_problem = tk.Label(root, textvariable = var_problem, font = ("Courier", 10), bg = "#D54A43", fg = "#FFFFFF")
label_problem.place(relx = 0.46, rely = 0.35, anchor = "center")
label_real_diff = tk.Label(root, textvariable = var_diff, font = ("Courier", 10), bg = "#5F8247", fg = "#FFFFFF")
label_real_diff.place(relx = 0.72, rely = 0.5)


##問題作成ボタン作成
button_problem = tk.Button(root, text = "問題を\n作成！", bg = "#D54A43", fg = "#FFFFFF", height = 3, width = 7)
button_problem.bind("<Button-1>", clicked_1)
button_problem.place(relx = 0.06, rely = 0.185)

##答えを見るボタンが押された時に実行される関数
def clicked_2(self):
    strings = back.print_figure(ans)
    var_ans.set(strings)
label_ans = tk.Label(root, textvariable = var_ans, font = ("Courier", 10), bg = "#D54A43", fg = "#FFFFFF")
label_ans.place(relx = 0.46, rely = 0.73, anchor = "center")

##答えを見るボタンを作成
button_ans = tk.Button(root, text = "答えを\n見る！", bg = "#D54A43", fg = "#FFFFFF", height = 3, width = 7)
button_ans.bind("<Button-1>", clicked_2)
button_ans.place(relx = 0.06, rely = 0.55)


##使い方ボタンがクリックされた時に実行される関数
def clicked_readme(self):
    res_readme = messagebox.showinfo("使い方", "1.難易度を0~9から選んで入力します\n2.かける数、かけられる数の最大の桁数を\n    1~5の中から選んで入力します\n3.問題作成ボタンを押します\n4.答えを見るには、答えを見るボタンを押します\n\n最高難易度かつ5桁の問題を作成する場合、\nまれにエラーになることがあります\nその場合はもう1度試してください")
    print("showinfo", res_readme)

##使い方ボタン
button_readme = tk.Button(root, text = "使い方を見る", bg = "#FFFFFF", height = 2, width = 10)
button_readme.bind("<Button-1>", clicked_readme)
button_readme.place(relx = 0.037, rely = 0.02)

##イベントループ
root.mainloop()

"""MEMO
apple rgb(235, 60, 60)　235060060
tree  rgb(17, 180, 46)  017180046

"""