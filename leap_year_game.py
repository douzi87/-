import tkinter as tk
from tkinter import messagebox
import random

def is_leap_year(year):
    """判断是否为闰年"""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def generate_year():
    """随机生成一个年份"""
    return random.randint(1582, 3000)

def check_answer(user_answer):
    """检查用户答案"""
    global total_correct, total_questions, year
    total_questions += 1

    if (user_answer == "闰年" and is_leap_year(year)) or (user_answer == "平年" and not is_leap_year(year)):
        total_correct += 1
        messagebox.showinfo("结果", "正确！")
    else:
        messagebox.showinfo("结果", f"错误！{year}年是{'闰年' if is_leap_year(year) else '平年'}。")

    next_question()

def next_question():
    """生成下一题"""
    global year, total_questions, total_correct
    if total_questions < 5:
        year = generate_year()
        question_label.config(text=f"{year}年是平年还是闰年？")
    else:
        if total_correct == 5:
            messagebox.showinfo("挑战成功", f"恭喜你！全部答对！\n总答题数：{total_questions}，正确数：{total_correct}")
        else:
            messagebox.showinfo("挑战失败", f"再接再厉！\n总答题数：{total_questions}，正确数：{total_correct}")
        window.destroy()

# 初始化
total_correct = 0
total_questions = 0
year = generate_year()

# 创建主窗口
window = tk.Tk()
window.title("平年与闰年挑战")
window.geometry("300x200")

# 添加组件
question_label = tk.Label(window, text=f"{year}年是平年还是闰年？", font=("Arial", 14))
question_label.pack(pady=20)

button_leap = tk.Button(window, text="闰年", command=lambda: check_answer("闰年"), width=10, font=("Arial", 12))
button_leap.pack(pady=5)

button_common = tk.Button(window, text="平年", command=lambda: check_answer("平年"), width=10, font=("Arial", 12))
button_common.pack(pady=5)

# 运行主循环
window.mainloop()