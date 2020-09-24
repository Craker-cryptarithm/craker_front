# - * - coding: utf8 - * -
"""
Craker Frontend
Copyright 2020 bamboo
"""

#tkinterの準備
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#バックを利用する
import sys
sys.path.append('..')
from craker_back import back


##ウィンドウの作成
root = tk.Tk()
root.resizable(width = False, height = False)
root.title("craker")
canvas = tk.Canvas(root, width = 1280, heigh = 720)
canvas.pack()
img = tk.PhotoImage(file = "background.gif")
canvas.create_image(640, 360, image = img)

##アイコン設定
root.iconbitmap("icon.ico")

##ラベル表示
txt_menu = tk.StringVar()
txt_menu.set("モードを\n選んでね↓")
label_menu = tk.Label(root, textvariable = txt_menu, bg = "#FFFFFF", font = ("", 20))
label_menu.place(relx = 0.79, rely = 0.02)

whitchCalculatuion = -1

##新しいウィンドウの作成
def createNewWindow():
    global label_menu
    label_menu.destroy()
    global whitchCalculatuion
    newWindow = tk.Toplevel(root)
    newWindow.geometry("150x130")
    newWindow.resizable(width = False, height = False)
    newWindow.title("モード選択")

    txt_mode = tk.StringVar()

    def clicked_addition():
        global whitchCalculatuion
        whitchCalculatuion = 0
        txt_mode.set("たし算モード")
        newWindow.destroy()
    def clicked_subtraction():
        global whitchCalculatuion
        whitchCalculatuion = 1
        txt_mode.set("ひき算モード")
        newWindow.destroy()
    def clicked_multiplication():
        global whitchCalculatuion
        whitchCalculatuion = 2
        txt_mode.set("かけ算モード")
        newWindow.destroy()
    def clicked_division():
        global whitchCalculatuion
        whitchCalculatuion = 3
        txt_mode.set("わり算モード")
        newWindow.destroy()
    
    button_addition = tk.Button(newWindow, text = "たし算", bg = "#FFFFFF", fg = "#000000", command = clicked_addition, font = ("", 12))
    button_addition.pack()

    button_subtraction = tk.Button(newWindow, text = "ひき算", bg = "#FFFFFF", fg = "#000000", command = clicked_subtraction, font = ("", 12))
    button_subtraction.pack()

    button_multiplication = tk.Button(newWindow, text = "かけ算", bg = "#FFFFFF", fg = "#000000", command = clicked_multiplication, font = ("", 12))
    button_multiplication.pack()

    button_division = tk.Button(newWindow, text = "わり算", bg = "#FFFFFF", fg = "#000000", command = clicked_division, font = ("", 12))
    button_division.pack()

    label_mode = tk.Label(root, textvariable = txt_mode, bg = "#FFFFFF", font = ("", 20))
    label_mode.place(relx = 0.79, rely = 0.05)


button_NewWindow = tk.Button(root, text = "モードを選ぶ", command = createNewWindow, font = ("", 12), bg = "#FFFFFF")
button_NewWindow.place(relx = 0.8, rely = 0.1)


##ラベル作成
label_digits = tk.Label(root, text = "桁数", bg = "#FFFFFF", font = ("", 13))
label_digits.place(relx = 0.018, rely = 0.23)

##テキストボックスの作成
txt_digits = tk.Entry(width = 2, bg = "#cff1ef", font = ("", 18))
txt_digits.place(relx = 0.02, rely = 0.3)

##スケールの作成
label_difficult = tk.Label(root, text = "難", bg = "#FFFFFF", font = ("", 13))
label_easy = tk.Label(root, text = "易", bg = "#FFFFFF", font = ("", 13))
label_difficult.place(relx = 0.19, rely = 0.23)
label_easy.place(relx = 0.05, rely = 0.23)
var_input_diff = tk.IntVar(master = root, value = 0)
scale_diff = tk.Scale(root, orient = 'h', from_ = 0, to = 9, variable = var_input_diff, showvalue = False, resolution = 1, length = 200)
scale_diff.place(relx = 0.05, rely = 0.305)

##グローバル変数の宣言
problem = None
ans = None
diff = None

##変数の初期化
var_problem = tk.StringVar()
var_problem.set("")
var_diff = tk.StringVar()
var_diff.set("")
var_ans = tk.StringVar()
var_ans.set("")


##問題作成ボタンが押された時に実行される関数
def clicked_problem(self):
    global problem, ans0, ans1, ans2, ans3, diff
    input_diff = int(var_input_diff.get())
    input_digits = txt_digits.get()

    ###エラーメッセージ
    if whitchCalculatuion == -1:
        res_mode_error + messagebox.showwarning("エラー", "モードを選んでください")
        print("showwarning", res_mode_error)
        return 1
    if input_digits == "":  #入力されていないとき
        res_null_error = messagebox.showwarning("エラー", "桁数を入力してください")
        print("showwarning", res_null_error)
        return 1
    if not input_digits.isdecimal():    #入力が数字じゃないとき
        res_str_error = messagebox.showwarning("エラー", "数字を入力してください")
        print("showwarning", res_str_error)
        txt_digits.delete(0, tk.END)
        return 1
    input_digits = int(input_digits)
    if input_digits <= 0 or input_digits >= 6:  #入力の数字が 0~5 じゃないとき
        res_digits_error = messagebox.showwarning("エラー", "桁数は1~5の数字で入力してください")
        print("showwarning", res_digits_error)
        txt_digits.delete(0, tk.END)
        return 1
    
    if whitchCalculatuion == 0:
        button_problem.config(state = 'disable')
        problem, ans0, diff = back.problem_maker_addition(input_diff, input_digits)
    if whitchCalculatuion == 1:
        button_problem.config(state = 'disable')
        problem, ans1, diff = back.problem_maker_subtraction(input_diff, input_digits)
    if whitchCalculatuion == 2:
        button_problem.config(state = 'disable')
        problem, ans2, diff = back.problem_maker_multiplication(input_diff, input_digits)
    if whitchCalculatuion == 3:
        button_problem.config(state = 'disable')
        problem, ans3, diff = back.problem_maker_division(input_diff, input_digits)

    if problem == -1:   #タイムアウトが発生したとき
        res_error = messagebox.showwarning("エラー", "解が見つかりませんでした\nもう一度試してください")
        print("showwarning, res_error")
        return 1
    var_problem.set(problem)
    var_diff.set("実測難易度\n      " + str(diff))
    button_problem.config(state = 'active')
    var_ans.set("")

##clicked_problem実行時のラベル
label_problem = tk.Label(root, textvariable = var_problem, font = ("Courier", 12), bg = "#D54A43", fg = "#FFFFFF")
label_problem.place(relx = 0.32, rely = 0.62, anchor = "center")
label_real_diff = tk.Label(root, textvariable = var_diff, font = ("Courier", 14), bg = "#FFFFFF", fg = "#000000")
label_real_diff.place(relx = 0.03, rely = 0.8)

##問題作成ボタン作成
button_problem = tk.Button(root, text = "問題を\n作成！", bg = "#D54A43", fg = "#FFFFFF", height = 3, width = 7, font = ("", 15))
button_problem.bind("<Button-1>", clicked_problem)
button_problem.place(relx = 0.475, rely = 0.295)


##答えを見るボタンが押された時に実行される関数
def clicked_ans(self):
    if whitchCalculatuion == 0:
        var_ans.set(ans0)
    if whitchCalculatuion == 1:
        var_ans.set(ans1)
    if whitchCalculatuion == 2:
        var_ans.set(ans2)
    if whitchCalculatuion == 3:
        var_ans.set(ans3)

#clicked_ans実行時のラベル
label_ans = tk.Label(root, textvariable = var_ans, font = ("Courier", 12  ), bg = "#D54A43", fg = "#FFFFFF")
label_ans.place(relx = 0.75, rely = 0.62, anchor = "center")

##答えを見るボタンを作成
button_ans = tk.Button(root, text = "答えを\n見る！", bg = "#D54A43", fg = "#FFFFFF", height = 3, width = 7, font = ("", 15))
button_ans.bind("<Button-1>", clicked_ans)
button_ans.place(relx = 0.898, rely = 0.3)


##使い方ボタンがクリックされた時に実行される関数
def clicked_readme(self):
    res_readme = messagebox.showinfo("使い方", "1.モードを、たし算、ひき算、\n    かけ算、わり算の中から選択します。\n2.難易度をスケールバーで調整します\n3.筆算の問題中の最大の桁数を\n    1~5の中から選んで入力します\n4.問題作成ボタンを押します\n5.答えを見るには、答えを見るボタンを押します\n\n最高難易度かつ5桁の問題を作成する場合、\nまれにエラーになることがあります\nその場合はもう1度試してください")
    print("showinfo", res_readme)

##使い方ボタン
button_readme = tk.Button(root, text = "使い方を見る", bg = "#FFFFFF", font = ("", 19))
button_readme.bind("<Button-1>", clicked_readme)
button_readme.place(relx = 0.096, rely = 0.065)


##イベントループ
root.mainloop()
