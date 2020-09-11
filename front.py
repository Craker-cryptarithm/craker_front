# - * - coding: utf8 - * -

#tkinterの準備
import tkinter as tk
from tkinter import messagebox

#バックを利用するのに使うやつ
import sys
sys.path.append('..')
from craker_back import back



##フレームの作成
root = tk.Tk()

##フレームの名前を設定
root.title("craker")

##ウィンドウの大きさを設定
root.geometry("700x1000")

##ラベル作成
label_title = tk.Label(root, text = "虫食い算")
label_title.place(relx = 0.45, rely = 0.01)

label_diff = tk.Label(root, text = "難易度(0~9)")
label_diff.place(relx = 0.35, rely = 0.05)

label_digits = tk.Label(root, text = "桁数の最大値(1~5)")
label_digits.place(relx = 0.35, rely = 0.1)

##テキストボックスの作成
txt_diff = tk.Entry(width = 3)
txt_diff.place(relx = 0.55, rely = 0.05)

txt_digits = tk.Entry(width = 3)
txt_digits.place(relx = 0.55, rely = 0.1)

##グローバル変数
problem = None
ans = None
diff = None

##問題作成ボタンが押された時に実行される関数
var_problem = tk.StringVar()
var_problem.set("")
def clicked_1(self):
    global problem, ans, diff
    input_diff = txt_diff.get()
    input_digits = txt_digits.get()
    ###エラーメッセージ
    if input_diff == "" or input_digits == "":
        res_null_error = messagebox.showwarning("エラー", "数字を入力してください")
        print("showwarning", res_null_error)
        return 1
    input_diff = int(input_diff)
    input_digits = int(input_digits)
    if input_diff < 0 or input_diff > 9:
        res_diff_error = messagebox.showwarning("エラー", "難易度は0~9の数字で答えてください")
        print("showwarning", res_diff_error)
        return 1
    if input_digits <= 0 or input_digits >= 6:
        res_digits_error = messagebox.showwarning("エラー", "桁数は1~6の数字で答えてください")
        print("showwarning", res_digits_error)
        return 1
    
    ###本題
    problem, ans, diff = back.problem_maker(input_diff, input_digits)
    
    strings = back.print_figure(problem)
    var_problem.set(strings)
label_problem = tk.Label(root, textvariable = var_problem, font = "VLゴシック")
label_problem.place(relx = 0.45, rely = 0.3)

##問題作成ボタン作成
button_problem = tk.Button(root, text = "問題を作成！")
button_problem.bind("<Button-1>", clicked_1)
button_problem.place(relx = 0.6, rely = 0.15)

##答えを見るボタンが押された時に実行される関数
var_ans = tk.StringVar()
var_ans.set("")
def clicked_2(self):
    strings = back.print_figure(ans)
    var_ans.set(strings)
label_ans = tk.Label(root, textvariable = var_ans, font = "VLゴシック")
label_ans.place(relx = 0.45, rely = 0.6)

##答えを見るボタンを作成
button_ans = tk.Button(root, text = "答えを見る！")
button_ans.bind("<Button-1>", clicked_2)
button_ans.place(relx = 0.6, rely = 0.58)

"""
var_2 = tk.StringVar()
var_2.set(" ")
##ボタンが押された時に実行される関数
def clicked(self):
    input_num = txt.get()
    if input_num == '':
        res = messagebox.showwarning("エラー", "数字が入力されていません")
        print("showwarning", res)
    else:
        #label_ans.place_forget()
        #var_2 = tk.StringVar()
        #var_2.set(divisor(int(input_num)))
    #txt.delete(0, tk.END)
    return var_2
label_ans = tk.Label(root, textvariable = var_2, justify = 'left', font = "VLゴシック")
label_ans.place(x = 10, y = 60)
"""

##イベントループ
root.mainloop()
