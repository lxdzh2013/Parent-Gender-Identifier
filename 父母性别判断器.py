import tkinter as tk

root = tk.Tk()
root.title("父母性别判断器")
root.geometry("420x280")
root.resizable(False, False)

lang_dict = {
    "cn": {
        "win_title": "父母性别判断器",
        "top_title": "父母性别判断器",
        "tip": "请点击下方按钮",
        "btn_father": "爸爸",
        "btn_mother": "妈妈",
        "btn_switch": "Switch to English",
        "res_father": "判断结果：爸爸 → 男性",
        "res_mother": "判断结果：妈妈 → 女性"
    },
    "en": {
        "win_title": "Parent Gender Detector",
        "top_title": "Parent Gender Detector",
        "tip": "Please click the button below",
        "btn_father": "Father",
        "btn_mother": "Mother",
        "btn_switch": "切换至中文",
        "res_father": "Result: Father → Male",
        "res_mother": "Result: Mother → Female"
    }
}

now_lang = "cn"

lab_title = tk.Label(root, font=("微软雅黑", 18, "bold"))
lab_title.pack(pady=15)

lab_result = tk.Label(root, font=("微软雅黑", 14))
lab_result.pack(pady=10)

frame_btn = tk.Frame(root)
frame_btn.pack(pady=15)

btn_father = tk.Button(frame_btn, width=10, height=2, font=("微软雅黑", 12), bg="#409eff", fg="white")
btn_father.grid(row=0, column=0, padx=12)

btn_mother = tk.Button(frame_btn, width=10, height=2, font=("微软雅黑", 12), bg="#f87171", fg="white")
btn_mother.grid(row=0, column=1, padx=12)

btn_switch = tk.Button(root, font=("微软雅黑", 11), bg="#722ed1", fg="white")
btn_switch.pack(pady=8)

def show_father():
    lab_result.config(text=lang_dict[now_lang]["res_father"], fg="#0066cc")

def show_mother():
    lab_result.config(text=lang_dict[now_lang]["res_mother"], fg="#e63946")

def refresh_ui():
    root.title(lang_dict[now_lang]["win_title"])
    lab_title.config(text=lang_dict[now_lang]["top_title"])
    lab_result.config(text=lang_dict[now_lang]["tip"], fg="#333333")
    btn_father.config(text=lang_dict[now_lang]["btn_father"])
    btn_mother.config(text=lang_dict[now_lang]["btn_mother"])
    btn_switch.config(text=lang_dict[now_lang]["btn_switch"])

def switch_lang():
    global now_lang
    now_lang = "en" if now_lang == "cn" else "cn"
    refresh_ui()

btn_father.config(command=show_father)
btn_mother.config(command=show_mother)
btn_switch.config(command=switch_lang)

refresh_ui()
root.mainloop()