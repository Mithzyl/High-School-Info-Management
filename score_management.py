#!/usr/bin/env python
# coding: utf-8

import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import tkinter.messagebox as messagebox

class StartPage(object):
    def __init__(self, parent_window):
        parent_window.destroy()
        self.window = tk.Tk()
        self.window.title('成绩管理系统')
        self.window.geometry("500x500")
        
        label = Label(self.window, text = "成绩管理系统", font = ("Verdana", 20))
        label.pack(pady = 50)
        
        Button(self.window, text = "学生登录", font = tkFont.Font(size=16),
               command = lambda: StudentLogin(self.window),
               width = 30, height = 2, fg = 'black', bg = 'gray',
               activebackground = 'black', activeforeground = 'white').pack(pady=10)
        
        Button(self.window, text = "教师登录", font = tkFont.Font(size=16),
               command = lambda: TeacherLogin(self.window),
               width = 30, height = 2, fg = 'black', bg = 'gray',
               activebackground = 'black', activeforeground = 'white').pack(pady=10)
        
        Button(self.window, text = "管理员登录", font = tkFont.Font(size=16),
               command = lambda: AdminLogin(self.window),
               width = 30, height = 2, fg = 'black', bg = 'gray',
               activebackground = 'black', activeforeground = 'white').pack(pady=10)

        Button(self.window, text = "权限管理", font = tkFont.Font(size=16),
               command = lambda: PermittionLogin(self.window),
               width = 30, height = 2, fg = 'black', bg = 'gray',
               activebackground = 'black', activeforeground = 'white').pack(pady=10)
        
        Button(self.window, text = "退出", font = tkFont.Font(size=16),
               command = self.window.destroy,
               width = 30, height = 2, fg = 'black', bg = 'gray',
               activebackground = 'black', activeforeground = 'white').pack(pady=10)
        
        self.window.mainloop()


class AdminLogin(object):
    def __init__(self, parent_window):
        parent_window.destroy()
        
        self.window = tk.Tk()
        self.window.title('管理员登录')
        self.window.geometry("500x500")
        
        label = Label(self.window, text = "管理员登录", font = ("Verdana", 20), width = 30, height = 2)
        label.pack()
        
        Label(self.window, text = "用户名", bg = 'white', font = tkFont.Font(size=14)).pack(pady=25)
        self.username = tk.Entry(self.window, width = 30, font=tkFont.Font(size=14), bg='Ivory')
        self.username.pack()
        
        Label(self.window, text = "密码", bg = 'white', font = tkFont.Font(size=14)).pack(pady=25)
        self.password = tk.Entry(self.window, width = 30, font=tkFont.Font(size=14), bg='Ivory')
        self.password.pack()
        
        Button(self.window, text = "登录", width = 8, font = tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text = "返回", width = 8, font = tkFont.Font(size=12), command=self.back).pack()
        
        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()

    def login(self):
        print(str(self.username.get()))
        print(str(self.password.get()))
        password = None
        
        #数据库操作
        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "select * from 用户信息 where User_Id = '%s' and Authorization_level = 2" % (self.username.get())

        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                admin_id = row[0]
                password = row[1]
                print("id = %s, password = %s" % (admin_id, password))
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo("错误", "用户名或密码不正确")
        db.close()

        if self.password.get() == password:
            AdminView(self.window)
        else:
            messagebox.showinfo("错误", "用户名或密码不正确")

    def back(self):
        StartPage(self.window)

class PermittionLogin(object):
    def __init__(self, parent_window):
        parent_window.destroy()
        
        self.window = tk.Tk()
        self.window.title('管理员登录')
        self.window.geometry("500x500")
        
        label = Label(self.window, text = "管理员登录", font = ("Verdana", 20), width = 30, height = 2)
        label.pack()
        
        Label(self.window, text = "用户名", bg = 'white', font = tkFont.Font(size=14)).pack(pady=25)
        self.username = tk.Entry(self.window, width = 30, font=tkFont.Font(size=14), bg='Ivory')
        self.username.pack()
        
        Label(self.window, text = "密码", bg = 'white', font = tkFont.Font(size=14)).pack(pady=25)
        self.password = tk.Entry(self.window, width = 30, font=tkFont.Font(size=14), bg='Ivory')
        self.password.pack()
        
        Button(self.window, text = "登录", width = 8, font = tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text = "返回", width = 8, font = tkFont.Font(size=12), command=self.back).pack()
        
        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()

    def login(self):
        print(str(self.username.get()))
        print(str(self.password.get()))
        password = None
        
        #数据库操作
        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "select * from 用户信息 where User_Id = '%s' and Authorization_level = 2" % (self.username.get())

        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                admin_id = row[0]
                password = row[1]
                print("id = %s, password = %s" % (admin_id, password))
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo("错误", "用户名或密码不正确")
        db.close()

        if self.password.get() == password:
            PermittionManage(self.window)
        else:
            messagebox.showinfo("错误", "用户名或密码不正确")

    def back(self):
        StartPage(self.window)

class StudentLogin(object):
    def __init__(self, parent_window):
        parent_window.destroy()
        
        self.window = tk.Tk()
        self.window.title('学生登录')
        self.window.geometry("500x500")
        
        label = Label(self.window, text = "学生登录", font = ("Verdana", 20), width = 30, height = 2)
        label.pack()
        
        Label(self.window, text = "用户名", bg = 'white', font = tkFont.Font(size=14)).pack(pady=25)
        self.username = tk.Entry(self.window, width = 30, font=tkFont.Font(size=14), bg='Ivory')
        self.username.pack()
        
        Label(self.window, text = "密码", bg = 'white', font = tkFont.Font(size=14)).pack(pady=25)
        self.password = tk.Entry(self.window, width = 30, font=tkFont.Font(size=14), bg='Ivory')
        self.password.pack()
        
        Button(self.window, text = "登录", width = 8, font = tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text = "返回", width = 8, font = tkFont.Font(size=12), command=self.back).pack()
        
        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()

    def login(self):
        print(str(self.username.get()))
        print(str(self.password.get()))
        password = None
        
        #数据库操作
        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "select * from 用户信息 where User_Id = '%s' and Authorization_level = 0" % (self.username.get())

        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                admin_id = row[0]
                password = row[1]
                student_id = row[3]
                print("id = %s, password = %s" % (admin_id, password))
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo("错误", "用户名或密码不正确")
        db.close()

        if self.password.get() == password:
            StudentView(self.window, student_id)
        else:
            messagebox.showinfo("错误", "用户名或密码不正确")

    def back(self):
        StartPage(self.window)

class TeacherLogin(object):
    def __init__(self, parent_window):
        parent_window.destroy()
        
        self.window = tk.Tk()
        self.window.title('教师')
        self.window.geometry("500x500")
        
        label = Label(self.window, text = "教师登录", font = ("Verdana", 20), width = 30, height = 2)
        label.pack()
        
        Label(self.window, text = "用户名", bg = 'white', font = tkFont.Font(size=14)).pack(pady=25)
        self.username = tk.Entry(self.window, width = 30, font=tkFont.Font(size=14), bg='Ivory')
        self.username.pack()
        
        Label(self.window, text = "密码", bg = 'white', font = tkFont.Font(size=14)).pack(pady=25)
        self.password = tk.Entry(self.window, width = 30, font=tkFont.Font(size=14), bg='Ivory')
        self.password.pack()
        
        Button(self.window, text = "登录", width = 8, font = tkFont.Font(size=12), command=self.login).pack(pady=40)
        Button(self.window, text = "返回", width = 8, font = tkFont.Font(size=12), command=self.back).pack()
        
        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()

    def login(self):
        print(str(self.username.get()))
        print(str(self.password.get()))
        password = None
        
        #数据库操作
        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "select * from 用户信息 where User_Id = '%s' and Authorization_level = 1" % (self.username.get())

        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                admin_id = row[0]
                password = row[1]
                teacher_id = row[3]
                print("id = %s, password = %s" % (admin_id, password))
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo("错误", "用户名或密码不正确")
        db.close()

        if self.password.get() == password:
            TeacherView(self.window, teacher_id)
        else:
            messagebox.showinfo("错误", "用户名或密码不正确")

    def back(self):
        StartPage(self.window)

#管理员
#1.添加、修改和删除课程
#2.添加、修改和删除教师和学生信息

class AdminView(object):
    def __init__(self, parent_window):
        parent_window.destroy()
        
        self.window = tk.Tk()
        self.window.title('管理界面')
        self.window.geometry("150x300")

        self.left_top = Frame(width=300, height=200)
        self.right_top = Frame(width=300, height=200)
    
        #个人信息

        self.top_title = Label(self.left_top, text="欢迎", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=W, padx=45, pady=10)

        #功能
        self.function_title = Label(self.right_top, text = "功能", font=('Verdana', 20))
        self.function_title.grid(row = 0, column = 0, columnspan=2, sticky=NSEW)

        self.change_course = Button(self.right_top, text = "修改课程", width = 10, font = tkFont.Font(size=12), command=self.coursePage)
        self.change_course.grid(row = 1, column = 0, columnspan=2, sticky=NSEW, pady=10)

        self.change_teacher_info = Button(self.right_top, text = "修改教师信息", width = 10, font = tkFont.Font(size=12), command=self.teacherPage)
        self.change_teacher_info.grid(row = 2, column = 0, columnspan=2, sticky=NSEW, pady=10)

        self.change_student_info = Button(self.right_top, text = "修改学生信息", width = 10, font = tkFont.Font(size=12), command=self.studentPage)
        self.change_student_info.grid(row = 3, column = 0, columnspan=2, sticky=NSEW, pady=10)

        self.back_button = Button(self.right_top, text = "返回", width = 10, font = tkFont.Font(size=12), command=self.back)
        self.back_button.grid(row = 4, column = 0, columnspan=2, sticky=NSEW, pady=10)

        #显示各个区域
        self.left_top.grid(row=0, column=0, padx=2, pady=5)
        self.right_top.grid(row=1, column=0, padx=2, pady=20)

        
        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()

    def coursePage(self):
        CoursePage(self.window)
        return None
    
    def teacherPage(self):
        TeacherPage(self.window)
        return None

    def studentPage(self):
        StudentPage(self.window)
        return None

    def back(self):
        StartPage(self.window)
        

class PermittionManage(object):
    def __init__(self, parent_window):
        parent_window.destroy()
        
        self.window = Tk()
        self.window.title('权限管理界面')
        self.window.geometry("700x700")
        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=300, height=200)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("用户名", "密码", "权限", "学号或工号")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("用户名", width=100, anchor='center')
        self.tree.column("密码", width=100, anchor='center')
        self.tree.column("权限", width=100, anchor='center')
        self.tree.column("学号或工号", width=100, anchor='center')
        self.tree.heading("用户名", text="用户名")
        self.tree.heading("密码", text="密码")
        self.tree.heading("权限", text="权限")
        self.tree.heading("学号或工号", text="学号或工号")

        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.user = []
        self.password = []
        self.auth = []
        self.id= []

        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "select * from 用户信息"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print("读取用户信息成功")
            #print(results)
            for row in results:
                self.user.append(row[0])
                self.password.append(row[1])
                self.auth.append(row[2])
                self.id.append(row[3])

            for i in range(min(len(self.user), len(self.password), len(self.auth), len(self.id))):
                self.tree.insert('', i, values=(self.user[i],
                self.password[i],
                self.auth[i],
                self.id[i]))
        except:
            print("Error: Unable to fetch data")
        db.close()

        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="账户信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_user = StringVar()
        self.var_pass = StringVar()
        self.var_auth = StringVar()
        self.var_id = StringVar()

        #用户名
        self.right_top_id_label = Label(self.frame_left_top, text="用户名：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_user, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)

        #密码
        self.right_top_name_label = Label(self.frame_left_top, text="密码：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_pass, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)
        self.right_top_name_entry.grid(row=2, column=1)

        #性别
        self.right_top_score_label = Label(self.frame_left_top, text="权限：", font=('Verdana', 15))
        self.right_top_score_entry = Entry(self.frame_left_top, textvariable=self.var_auth, font=('Verdana', 15))
        self.right_top_score_label.grid(row=3, column=0)
        self.right_top_score_entry.grid(row=3, column=1)

        #班级
        self.right_top_teacher_label = Label(self.frame_left_top, text="学号或工号：", font=('Verdana', 15))
        self.right_top_teacher_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_teacher_label.grid(row=4, column=0)
        self.right_top_teacher_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建账户信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中信息', width=20,command=self.update_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中信息', width=20,command=self.del_row)
        self.back_button = Button(self.frame_right_top, text="返回", width=23, command=self.returnLastPage)
        self.back_button.grid(row=5, column=0, columnspan=2, sticky=W, padx=20, pady=5)

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=5)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=5)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=5)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=30, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()
    
    def back(self):
        StartPage(self.window) # 显示主窗口 销毁本窗口

    def returnLastPage(self):
        PermittionLogin(self.window)

    def click(self, event):
        self.col = self.tree.identify_column(event.x)
        self.row = self.tree.identify_row(event.y)

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_user.set(self.row_info[0])
        self.raw_id = self.row_info[0]
        self.var_pass.set(self.row_info[1])
        self.var_auth.set(self.row_info[2])
        self.var_id.set(self.row_info[3])

        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.user, font=('Verdana', 15))

    def new_row(self):
        print('添加新用户')
        print(self.var_user.get())
        print(self.id)
        if self.var_user.get() != '' and self.var_pass.get() != '' and self.var_auth.get() != '' and self.var_id.get() != '':
            db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
            cursor = db.cursor()
            sql = "insert into 用户信息 (User_Id, Password, Authorization_level, Id) \
                   values ('%s', '%s', '%s', '%s')" % \
                    (self.var_user.get(), self.var_pass.get(), self.var_auth.get(), self.var_id.get())
            try:
                cursor.execute(sql)
                db.commit()
                print("录入成功")
                
            except:
                db.rollback()

                messagebox.showinfo("错误", "数据库连接失败")
            db.close()

            self.user.append(self.var_user.get())
            self.password.append(self.var_pass.get())
            self.auth.append(self.var_auth.get())
            self.id.append(self.var_id.get())
            self.tree.insert('', len(self.id) - 1, values=(self.user[len(self.id) - 1],
                             self.password[len(self.id) - 1], 
                             self.auth[len(self.id) - 1],
                             self.id[len(self.id) - 1]))
            self.tree.update()
            messagebox.showinfo('提示！', '插入成功！')
        else:
            messagebox.showinfo('警告！', '请填写用户数据')

    def update_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_user.get() == self.row_info[0]:
                print("修改的用户: ")
                print(self.var_user.get())
                db = pymysql.connect("localhost", "root", "huyuan1649", "course")
                cursor = db.cursor()
                sql = "UPDATE 用户信息 SET Password = '%s', Authorization_level = '%s', Id = '%s' \
                       WHERE User_Id = '%s'" % (self.var_pass.get(), self.var_auth.get(), self.var_id.get(), self.var_user.get())
                try:
                    cursor.execute(sql)
                    db.commit()
                    print("更新成功")
                    messagebox.showinfo('提示！', '更新成功！')
                
                except:
                    db.rollback()

                    messagebox.showinfo("错误", "数据库连接失败")

                id_index = self.user.index(self.row_info[0])
                self.password[id_index] = self.var_pass.get()
                self.auth[id_index] = self.var_auth.get()
                self.id[id_index] = self.var_id.get()

                self.tree.item(self.tree.selection()[0], values=(
                    self.var_user.get(),
                    self.var_pass.get(),
                    self.var_auth.get(),
                    self.var_id.get()))
            else:
                messagebox.showinfo('警告！', '不能修改用户信息！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])
            print(self.tree.get_children())
            db = pymysql.connect("localhost", "root", "huyuan1649", "course")
            cursor = db.cursor()
            sql = "delete from 用户信息 where User_Id = '%s'" % (self.row_info[0])
            try:
                cursor.execute(sql)
                db.commit()
                print("删除成功")
                messagebox.showinfo('提示！', '删除成功！')
            
            except:
                db.rollback()

                messagebox.showinfo("错误", "数据库连接失败")
            db.close()

            id_index = self.user.index(self.row_info[0])
            del self.user[id_index]
            del self.password[id_index]
            del self.auth[id_index]
            del self.id[id_index]
            print(self.user)
            self.tree.delete(self.tree.selection()[0])
            print(self.tree.get_children())


class CoursePage(object):
    def __init__(self, parent_window):
        parent_window.destroy()
        
        self.window = Tk()
        self.window.title('课程管理界面')
        self.window.geometry("700x800")
        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=300, height=250)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        #self.course_id = course_id
        #self.course_name = course_name
        #self.teacher_name = teacher_name

        # 定义下方中心列表区域
        self.columns = ("课程号", "课程名", "学分", "教师姓名")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("课程号", width=150, anchor='center')
        self.tree.column("课程名", width=150, anchor='center')
        self.tree.column("学分", width=100, anchor='center')
        self.tree.column("教师姓名", width=100, anchor='center')
        self.tree.heading("课程号", text="课程号")
        self.tree.heading("课程名", text="课程名")
        self.tree.heading("学分", text="学分")
        self.tree.heading("教师姓名", text="教师姓名")

        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.name = []
        self.credit = []
        self.teacher_name = []

        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "select * from 课程"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print("读取课程成功")
            #print(results)
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.credit.append(row[2])
                self.teacher_name.append(row[3])

            for i in range(min(len(self.id), len(self.name), len(self.credit), len(self.teacher_name))):
                self.tree.insert('', i, values=(self.id[i],
                self.name[i],
                self.credit[i],
                self.teacher_name[i]))
        except:
            print("Error: Unable to fetch data")
        db.close()

        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="课程信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_credit = StringVar()
        self.var_teacher = StringVar()

        #课程号
        self.right_top_id_label = Label(self.frame_left_top, text="课程号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)

        #课程名
        self.right_top_name_label = Label(self.frame_left_top, text="课程名：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)
        self.right_top_name_entry.grid(row=2, column=1)

        #学分
        self.right_top_score_label = Label(self.frame_left_top, text="学分：", font=('Verdana', 15))
        self.right_top_score_entry = Entry(self.frame_left_top, textvariable=self.var_credit, font=('Verdana', 15))
        self.right_top_score_label.grid(row=3, column=0)
        self.right_top_score_entry.grid(row=3, column=1)

        #教师姓名
        self.right_top_teacher_label = Label(self.frame_left_top, text="教师姓名：", font=('Verdana', 15))
        self.right_top_teacher_entry = Entry(self.frame_left_top, textvariable=self.var_teacher, font=('Verdana', 15))
        self.right_top_teacher_label.grid(row=4, column=0)
        self.right_top_teacher_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建课程信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中信息', width=20,command=self.update_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中信息', width=20,command=self.del_row)
        self.back_button = Button(self.frame_right_top, text="返回", width=23, command=self.returnLastPage)
        self.back_button.grid(row=5, column=0, columnspan=2, sticky=W, padx=20, pady=5)
        
        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=30, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=25)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()
    
    def back(self):
        StartPage(self.window) # 显示主窗口 销毁本窗口
    
    def returnLastPage(self):
        AdminView(self.window)

    def click(self, event):
        self.col = self.tree.identify_column(event.x)
        self.row = self.tree.identify_row(event.y)

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.raw_id = self.row_info[0]
        self.var_name.set(self.row_info[1])
        self.var_credit.set(self.row_info[2])
        self.var_teacher.set(self.row_info[3])

        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id, font=('Verdana', 15))

    def new_row(self):
        print('添加新课程')
        print(self.var_id.get())
        print(self.id)
        #print(self.course_name)
        
        #if str(self.var_id.get()) in self.id:
        #    messagebox.showinfo('警告！', '该学生已存在！')
        #else:
        if self.var_id.get() != '' and self.var_name.get() != '' and self.var_credit.get() != '' and self.var_teacher.get() != '':
            db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
            cursor = db.cursor()
            sql = "insert into 课程 (Course_Id, Course_Name, Course_Credit, Teacher_Name) \
                   values ('%s', '%s', '%s', '%s')" % \
                    (self.var_id.get(), self.var_name.get(), self.var_credit.get(), self.var_teacher.get())
            try:
                cursor.execute(sql)
                db.commit()
                print("录入成功")
                
            except:
                db.rollback()

                messagebox.showinfo("错误", "数据库连接失败")
            db.close()

            self.id.append(self.var_id.get())
            self.name.append(self.var_name.get())
            self.credit.append(self.var_credit.get())
            self.teacher_name.append(self.var_teacher.get())
            self.tree.insert('', len(self.id) - 1, values=(self.id[len(self.id) - 1],
                             self.name[len(self.id) - 1], 
                             self.credit[len(self.id) - 1],
                             self.teacher_name[len(self.id) - 1]))
            self.tree.update()
            messagebox.showinfo('提示！', '插入成功！')
        else:
            messagebox.showinfo('警告！', '请填写课程数据')

    def update_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:
                print(self.var_id.get())
                db = pymysql.connect("localhost", "root", "huyuan1649", "course")
                cursor = db.cursor()
                sql = "UPDATE 课程 SET Course_Name = '%s', Course_Credit = '%s', Teacher_Name = '%s' \
                       WHERE Course_Id = '%s'" % (self.var_name.get(), self.var_credit.get(), self.var_teacher.get(), self.var_id.get())
                try:
                    cursor.execute(sql)
                    db.commit()
                    print("更新成功")
                    messagebox.showinfo('提示！', '更新成功！')
                
                except:
                    db.rollback()

                    messagebox.showinfo("错误", "数据库连接失败")

                id_index = self.id.index(self.row_info[0])
                self.name[id_index] = self.var_name.get()
                self.credit[id_index] = self.var_credit.get()
                self.teacher_name[id_index] = self.var_teacher.get()

                self.tree.item(self.tree.selection()[0], values=(
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_credit.get(),
                    self.var_teacher.get()))
            else:
                messagebox.showinfo('警告！', '不能修改课程号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])
            print(self.tree.get_children())
            db = pymysql.connect("localhost", "root", "huyuan1649", "course")
            cursor = db.cursor()
            sql = "delete from 课程 where Course_Id = '%s'" % (self.row_info[0])
            try:
                cursor.execute(sql)
                db.commit()
                print("删除成功")
                messagebox.showinfo('提示！', '删除成功！')
            
            except:
                db.rollback()

                messagebox.showinfo("错误", "数据库连接失败")
            db.close()

            id_index = self.id.index(self.row_info[0])
            del self.id[id_index]
            del self.name[id_index]
            del self.credit[id_index]
            del self.teacher_name[id_index]
            print(self.id)
            self.tree.delete(self.tree.selection()[0])
            print(self.tree.get_children())

class TeacherPage(object):
    def __init__(self, parent_window):
        parent_window.destroy()
        
        self.window = Tk()
        self.window.title('教师管理界面')
        self.window.geometry("700x800")
        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=300, height=300)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("工号", "教师姓名", "性别", "年龄", "科目")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("工号", width=100, anchor='center')
        self.tree.column("教师姓名", width=100, anchor='center')
        self.tree.column("性别", width=100, anchor='center')
        self.tree.column("年龄", width=100, anchor='center')
        self.tree.column("科目", width=100, anchor='center')
        self.tree.heading("工号", text="工号")
        self.tree.heading("教师姓名", text="教师姓名")
        self.tree.heading("性别", text="性别")
        self.tree.heading("年龄", text="年龄")
        self.tree.heading("科目", text="科目")

        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.name = []
        self.sex = []
        self.age = []
        self.subject = []

        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "select * from 教师"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print("读取教师信息成功")
            #print(results)
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.sex.append(row[2])
                self.age.append(row[3])
                self.subject.append(row[4])

            for i in range(min(len(self.id), len(self.name), len(self.sex), len(self.age), len(self.subject))):
                self.tree.insert('', i, values=(self.id[i],
                self.name[i],
                self.sex[i],
                self.age[i],
                self.subject[i]))
        except:
            print("Error: Unable to fetch data")
        db.close()

        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="教师信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=30)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_sex = StringVar()
        self.var_age = StringVar()
        self.var_subject = StringVar()

        #工号
        self.right_top_id_label = Label(self.frame_left_top, text="工号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)

        #姓名
        self.right_top_name_label = Label(self.frame_left_top, text="姓名：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)
        self.right_top_name_entry.grid(row=2, column=1)

        #性别
        self.right_top_score_label = Label(self.frame_left_top, text="性别：", font=('Verdana', 15))
        self.right_top_score_entry = Entry(self.frame_left_top, textvariable=self.var_sex, font=('Verdana', 15))
        self.right_top_score_label.grid(row=3, column=0)
        self.right_top_score_entry.grid(row=3, column=1)

        #年龄
        self.right_top_teacher_label = Label(self.frame_left_top, text="年龄：", font=('Verdana', 15))
        self.right_top_teacher_entry = Entry(self.frame_left_top, textvariable=self.var_age, font=('Verdana', 15))
        self.right_top_teacher_label.grid(row=4, column=0)
        self.right_top_teacher_entry.grid(row=4, column=1)

        #科目
        self.right_top_teacher_label = Label(self.frame_left_top, text="科目：", font=('Verdana', 15))
        self.right_top_teacher_entry = Entry(self.frame_left_top, textvariable=self.var_subject, font=('Verdana', 15))
        self.right_top_teacher_label.grid(row=5, column=0)
        self.right_top_teacher_entry.grid(row=5, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建教师信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中信息', width=20,command=self.update_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中信息', width=20,command=self.del_row)
        self.back_button = Button(self.frame_right_top, text="返回", width=23, command=self.returnLastPage)
        self.back_button.grid(row=5, column=0, columnspan=2, sticky=W, padx=20, pady=5)

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=30, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()
    
    def back(self):
        StartPage(self.window) # 显示主窗口 销毁本窗口
    
    def returnLastPage(self):
        AdminView(self.window)

    def click(self, event):
        self.col = self.tree.identify_column(event.x)
        self.row = self.tree.identify_row(event.y)

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.raw_id = self.row_info[0]
        self.var_name.set(self.row_info[1])
        self.var_sex.set(self.row_info[2])
        self.var_age.set(self.row_info[3])
        self.var_subject.set(self.row_info[4])

        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id, font=('Verdana', 15))

    def new_row(self):
        print('添加新教师')
        print(self.var_id.get())
        print(self.id)
        if self.var_id.get() != '' and self.var_name.get() != '' and self.var_sex.get() != '' and self.var_age.get() != '' and self.var_subject.get() != '':
            db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
            cursor = db.cursor()
            sql = "insert into 教师 (Teacher_Id, Teacher_Name, Teacher_Sex, Teacher_Age, Teacher_Subject) \
                   values ('%s', '%s', '%s', '%s', '%s')" % \
                    (self.var_id.get(), self.var_name.get(), self.var_sex.get(), self.var_age.get(), self.var_subject.get())
            try:
                cursor.execute(sql)
                db.commit()
                print("录入成功")
                
            except:
                db.rollback()

                messagebox.showinfo("错误", "数据库连接失败")
            db.close()

            self.id.append(self.var_id.get())
            self.name.append(self.var_name.get())
            self.sex.append(self.var_sex.get())
            self.age.append(self.var_age.get())
            self.subject.append(self.var_subject.get())
            self.tree.insert('', len(self.id) - 1, values=(self.id[len(self.id) - 1],
                             self.name[len(self.id) - 1], 
                             self.sex[len(self.id) - 1],
                             self.age[len(self.id) - 1],
                             self.subject[len(self.id) - 1]))
            self.tree.update()
            messagebox.showinfo('提示！', '插入成功！')
        else:
            messagebox.showinfo('警告！', '请填写教师数据')

    def update_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:
                print(self.var_id.get())
                db = pymysql.connect("localhost", "root", "huyuan1649", "course")
                cursor = db.cursor()
                sql = "UPDATE 教师 SET Teacher_Name = '%s', Teacher_Sex = '%s', Teacher_Age = '%s', Teacher_Subject = '%s' \
                       WHERE Teacher_Id = '%s'" % (self.var_name.get(), self.var_sex.get(), self.var_age.get(), self.var_subject.get(), self.var_id.get())
                try:
                    cursor.execute(sql)
                    db.commit()
                    print("更新成功")
                    messagebox.showinfo('提示！', '更新成功！')
                
                except:
                    db.rollback()

                    messagebox.showinfo("错误", "数据库连接失败")

                id_index = self.id.index(self.row_info[0])
                self.name[id_index] = self.var_name.get()
                self.sex[id_index] = self.var_sex.get()
                self.age[id_index] = self.var_age.get()
                self.subject[id_index] = self.var_subject.get()

                self.tree.item(self.tree.selection()[0], values=(
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_age.get(),
                    self.var_sex.get(),
                    self.var_subject.get()))
            else:
                messagebox.showinfo('警告！', '不能修改教师数据！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])
            print(self.tree.get_children())
            db = pymysql.connect("localhost", "root", "huyuan1649", "course")
            cursor = db.cursor()
            sql = "delete from 教师 where Teacher_Id = '%s'" % (self.row_info[0])
            try:
                cursor.execute(sql)
                db.commit()
                print("删除成功")
                messagebox.showinfo('提示！', '删除成功！')
            
            except:
                db.rollback()

                messagebox.showinfo("错误", "数据库连接失败")
            db.close()

            id_index = self.id.index(self.row_info[0])
            del self.id[id_index]
            del self.name[id_index]
            del self.sex[id_index]
            del self.age[id_index]
            del self.subject[id_index]
            print(self.id)
            self.tree.delete(self.tree.selection()[0])
            print(self.tree.get_children())

class StudentPage(object):
    def __init__(self, parent_window):
        parent_window.destroy()
        
        self.window = Tk()
        self.window.title('学生管理界面')
        self.window.geometry("700x700")
        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=300, height=250)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        # 定义下方中心列表区域
        self.columns = ("学号", "姓名", "性别", "班级")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("学号", width=100, anchor='center')
        self.tree.column("姓名", width=100, anchor='center')
        self.tree.column("性别", width=100, anchor='center')
        self.tree.column("班级", width=100, anchor='center')
        self.tree.heading("学号", text="学号")
        self.tree.heading("姓名", text="姓名")
        self.tree.heading("性别", text="性别")
        self.tree.heading("班级", text="班级")

        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.name = []
        self.sex = []
        self.classno = []

        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "select * from 学生"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print("读取学生信息成功")
            #print(results)
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.sex.append(row[2])
                self.classno.append(row[3])

            for i in range(min(len(self.id), len(self.name), len(self.sex), len(self.classno))):
                self.tree.insert('', i, values=(self.id[i],
                self.name[i],
                self.sex[i],
                self.classno[i]))
        except:
            print("Error: Unable to fetch data")
        db.close()

        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="学生信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_sex = StringVar()
        self.var_classno = StringVar()

        #学号
        self.right_top_id_label = Label(self.frame_left_top, text="学号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)

        #姓名
        self.right_top_name_label = Label(self.frame_left_top, text="姓名：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)
        self.right_top_name_entry.grid(row=2, column=1)

        #性别
        self.right_top_score_label = Label(self.frame_left_top, text="性别：", font=('Verdana', 15))
        self.right_top_score_entry = Entry(self.frame_left_top, textvariable=self.var_sex, font=('Verdana', 15))
        self.right_top_score_label.grid(row=3, column=0)
        self.right_top_score_entry.grid(row=3, column=1)

        #班级
        self.right_top_teacher_label = Label(self.frame_left_top, text="班级：", font=('Verdana', 15))
        self.right_top_teacher_entry = Entry(self.frame_left_top, textvariable=self.var_classno, font=('Verdana', 15))
        self.right_top_teacher_label.grid(row=4, column=0)
        self.right_top_teacher_entry.grid(row=4, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建学生信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中信息', width=20,command=self.update_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中信息', width=20,command=self.del_row)

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=5)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        self.back_button = Button(self.frame_right_top, text="返回", width=23, command=self.returnLastPage)
        self.back_button.grid(row=5, column=0, columnspan=2, sticky=W, padx=20, pady=5)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=30)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()
    
    def back(self):
        StartPage(self.window) # 显示主窗口 销毁本窗口

    def returnLastPage(self):
        AdminView(self.window)

    def click(self, event):
        self.col = self.tree.identify_column(event.x)
        self.row = self.tree.identify_row(event.y)

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.raw_id = self.row_info[0]
        self.var_name.set(self.row_info[1])
        self.var_sex.set(self.row_info[2])
        self.var_classno.set(self.row_info[3])

        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id, font=('Verdana', 15))

    def new_row(self):
        print('添加新学生')
        print(self.var_id.get())
        print(self.id)
        if self.var_id.get() != '' and self.var_name.get() != '' and self.var_sex.get() != '' and self.var_classno.get() != '':
            db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
            cursor = db.cursor()
            sql = "insert into 学生 (Student_Id, Student_Name, Student_Sex, Student_Class) \
                   values ('%s', '%s', '%s', '%s')" % \
                    (self.var_id.get(), self.var_name.get(), self.var_sex.get(), self.var_classno.get())
            try:
                cursor.execute(sql)
                db.commit()
                print("录入成功")
                
            except:
                db.rollback()

                messagebox.showinfo("错误", "数据库连接失败")
            db.close()

            self.id.append(self.var_id.get())
            self.name.append(self.var_name.get())
            self.sex.append(self.var_sex.get())
            self.classno.append(self.var_classno.get())
            self.tree.insert('', len(self.id) - 1, values=(self.id[len(self.id) - 1],
                             self.name[len(self.id) - 1], 
                             self.sex[len(self.id) - 1],
                             self.classno[len(self.id) - 1]))
            self.tree.update()
            messagebox.showinfo('提示！', '插入成功！')
        else:
            messagebox.showinfo('警告！', '请填写学生数据')

    def update_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:
                print(self.var_id.get())
                db = pymysql.connect("localhost", "root", "huyuan1649", "course")
                cursor = db.cursor()
                sql = "UPDATE 学生 SET Student_Name = '%s', Student_Sex = '%s', Student_Class = '%s' \
                       WHERE Student_Id = '%s'" % (self.var_name.get(), self.var_sex.get(), self.var_classno.get(), self.var_id.get())
                try:
                    cursor.execute(sql)
                    db.commit()
                    print("更新成功")
                    messagebox.showinfo('提示！', '更新成功！')
                
                except:
                    db.rollback()

                    messagebox.showinfo("错误", "数据库连接失败")

                id_index = self.id.index(self.row_info[0])
                self.name[id_index] = self.var_name.get()
                self.sex[id_index] = self.var_sex.get()
                self.classno[id_index] = self.var_classno.get()

                self.tree.item(self.tree.selection()[0], values=(
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_sex.get(),
                    self.var_classno.get()))
            else:
                messagebox.showinfo('警告！', '不能修改学生数据！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])
            print(self.tree.get_children())
            db = pymysql.connect("localhost", "root", "huyuan1649", "course")
            cursor = db.cursor()
            sql = "delete from 学生 where Student_Id = '%s'" % (self.row_info[0])
            try:
                cursor.execute(sql)
                db.commit()
                print("删除成功")
                messagebox.showinfo('提示！', '删除成功！')
            
            except:
                db.rollback()

                messagebox.showinfo("错误", "数据库连接失败")
            db.close()

            id_index = self.id.index(self.row_info[0])
            del self.id[id_index]
            del self.name[id_index]
            del self.sex[id_index]
            del self.classno[id_index]
            print(self.id)
            self.tree.delete(self.tree.selection()[0])
            print(self.tree.get_children())


#学生
class StudentView(object):   
    def __init__(self, parent_window, student_id):    
        parent_window.destroy()
        
        self.window = Tk()
        self.window.title('学生信息')
        self.window.geometry("200x400")
        self.left_top = Frame(width=300, height=200)
        self.right_top = Frame(width=300, height=200)
        self.center = Frame(width=500, height=400)
        self.bottom = Frame(width=650, height=50)

        self.id = StringVar()
        self.name = StringVar()
        self.sex = StringVar()
        self.classno = StringVar()
        self.student_id = student_id

        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "select * from 学生 where Student_Id = %s" %(student_id)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.id = '学号: ' + row[0]
                self.name = '姓名: ' + row[1]
                self.sex = '性别: ' + row[2]
                self.classno = '班级: ' + row[3]
        except:
            print("Error: Unable to fetch data")
            print(student_id)
        db.close()
    
        #个人信息

        self.top_title = Label(self.left_top, text="个人信息", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=W, padx=50, pady=10)

        self.top_id = Label(self.left_top, text=self.id, font=('Verdana', 18))
        self.top_id.grid(row=1, column=0, columnspan=2, sticky=W, padx=50, pady=0)

        self.top_name = Label(self.left_top, text=self.name, font=('Verdana', 18))
        self.top_name.grid(row=2, column=0, columnspan=2, sticky=NSEW, padx=50, pady=0)

        self.top_sex = Label(self.left_top, text=self.sex, font=('Verdana', 18))
        self.top_sex.grid(row=3, column=0, columnspan=2, sticky=NSEW, padx=50, pady=0)

        self.top_classno = Label(self.left_top, text=self.classno, font=('Verdana', 18))
        self.top_classno.grid(row=4, column=0, columnspan=2, sticky=W, padx=50, pady=0)

        #功能
        self.function_title = Label(self.right_top, text = "功能", font=('Verdana', 20))
        self.function_title.grid(row = 0, column = 0, columnspan=2, sticky=NSEW)

        self.select_lesson = Button(self.right_top, text = "选课", width = 10, font = tkFont.Font(size=12), command=self.selectLesson)
        self.select_lesson.grid(row = 1, column = 0, columnspan=2, sticky=NSEW)

        self.get_score = Button(self.right_top, text = "查询成绩", width = 10, font = tkFont.Font(size=12), command=self.showScore)
        self.get_score.grid(row = 2, column = 0, columnspan=2, sticky=NSEW, pady=10)

        #返回按钮
        self.back_button = Button(self.right_top, text="返回", width=10, font=('Verdana', 12), command=self.returnLastPage)
        self.back_button.grid(row=3, column=0, columnspan=2, sticky=NSEW)

        #显示各个区域
        self.left_top.grid(row=0, column=0, padx=2, pady=5)
        self.right_top.grid(row=1, column=0, padx=2, pady=50)

        
        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()

    def selectLesson(self):
        SelectLessonPage(self.window, self.student_id)
        return None
    
    def showScore(self):
        showScorePage(self.window, self.student_id)
        return None

    def returnLastPage(self):
        StudentLogin(self.window)

    def back(self):
        StartPage(self.window)
        return None

class showScorePage(object):
    def __init__(self, parent_window, student_id):    
        parent_window.destroy()
        
        self.window = Tk()
        self.window.title('成绩查询')
        self.window.geometry("500x700")
        self.left_top = Frame(width=300, height=200)
        self.right_top = Frame(width=300, height=200)
        self.center = Frame(width=500, height=400)
        self.bottom = Frame(width=500, height=50)
        self.student_id = student_id

        self.id = StringVar()
        self.name = StringVar()
        self.sex = StringVar()
        self.classno = StringVar()

        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "select * from 学生 where Student_Id = %s" %(student_id)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.id = '学号: ' + row[0]
                self.name = '姓名: ' + row[1]
                self.sex = '性别: ' + row[2]
                self.classno = '班级: ' + row[3]
        except:
            print("Error: Unable to fetch data")
            print(student_id)
        db.close()

        #表格
        self.columns = ("课程号", "课程", "成绩")
        self.tree = ttk.Treeview(self.center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.center, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vbar.set)

        self.tree.column("课程号", width=150, anchor='center')
        self.tree.column("课程", width=150, anchor='center')
        self.tree.column("成绩", width=150, anchor='center')
        self.tree.heading("课程号", text="课程号")
        self.tree.heading("课程", text="课程")
        self.tree.heading("成绩", text="成绩")

        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.course_id = []
        self.course_name = []
        self.score = []
        
        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "select Course_id, Course_name, score from score_query where Student_Id = %s" % (self.student_id)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.course_id.append(row[0])
                self.course_name.append(row[1])
                self.score.append(row[2])
                #print("name: "+row[1])
        except:
            print("Unable to fetch data")
        for i in range(min(len(self.course_id), len(self.course_name), len(self.score))):
            self.tree.insert('', i, values=(self.course_id[i], self.course_name[i], self.score[i]))
        db.close()

        #个人信息
        self.top_title = Label(self.left_top, text="个人信息", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=W, padx=50, pady=10)

        self.top_id = Label(self.left_top, text=self.id, font=('Verdana', 18))
        self.top_id.grid(row=1, column=0, columnspan=2, sticky=W, padx=50, pady=0)

        self.top_name = Label(self.left_top, text=self.name, font=('Verdana', 18))
        self.top_name.grid(row=2, column=0, columnspan=2, sticky=NSEW, padx=50, pady=0)

        self.top_sex = Label(self.left_top, text=self.sex, font=('Verdana', 18))
        self.top_sex.grid(row=3, column=0, columnspan=2, sticky=NSEW, padx=50, pady=0)

        self.top_classno = Label(self.left_top, text=self.classno, font=('Verdana', 18))
        self.top_classno.grid(row=4, column=0, columnspan=2, sticky=W, padx=50, pady=0)

        #返回按钮
        self.back_button = Button(self.bottom, text="返回", width=10, font=('Verdana', 12), command=self.returnLastPage)
        self.back_button.grid(row=0, column=0, columnspan=2, sticky=W, padx=50, pady=20)

        #显示各个区域
        self.left_top.grid(row=0, column=0, padx=150, pady=5)
        self.center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.bottom.grid(row=2, column=0, columnspan=2, padx=4, pady=5)
        
        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()

    def returnLastPage(self):
        StudentView(self.window, self.student_id)

    #返回到首页
    def back(self):
        StartPage(self.window)

class SelectLessonPage(object):
    def __init__(self, parent_window, student_id):
        parent_window.destroy()
        
        self.window = Tk()
        self.window.title('选课界面')
        self.window.geometry("850x650")
        self.left_top = LabelFrame(width=300, height=200, text="个人信息", font=('Verdana', 18))
        self.left_bottom = LabelFrame(width=300, height=200, text="已选课程", font=('Verdana', 18))
        self.right_top = LabelFrame(width=300, height=200, text="操作", font=('Verdana', 18))
        self.right_bottom = LabelFrame(width=300, height=200, text="可选课程", font=('Verdana', 18))
        self.student_id = student_id

        #个人信息变量
        self.id = StringVar()
        self.name = StringVar()
        self.var_name = StringVar()
        self.sex = StringVar()
        self.classno = StringVar()

        #可选课程变量
        self.var_sel_course_id = StringVar()
        self.var_sel_course_name = StringVar()
        self.var_sel_credit = StringVar()
        self.var_sel_teacher_name = StringVar()

        #已选课程变量
        self.var_chosen_course_id = StringVar()
        self.var_chosen_course_name = StringVar()
        self.var_chosen_teacher_name = StringVar()
        self.var_chosen_credit = StringVar()

        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "select * from 学生 where Student_Id = %s" %(student_id)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.id = '学号: ' + row[0]
                self.name = '姓名: ' + row[1]
                self.var_name = row[1]
                self.sex = '性别: ' + row[2]
                self.classno = '班级: ' + row[3]
        except:
            print("Error: Unable to fetch data")
            print(student_id)
        db.close()

        #已选课程
        self.chosen_columns = ("课程号", "课程", "学分", "教师")
        self.chosen_tree = ttk.Treeview(self.left_bottom, show="headings", height=18, columns=self.chosen_columns)
        self.chosen_vbar = ttk.Scrollbar(self.left_bottom, orient=VERTICAL, command=self.chosen_tree.yview)
        self.chosen_tree.configure(yscrollcommand=self.chosen_vbar.set)

        self.chosen_tree.column("课程号", width=75, anchor='center')
        self.chosen_tree.column("课程", width=75, anchor='center')
        self.chosen_tree.column("学分", width=75, anchor='center')
        self.chosen_tree.column("教师", width=75, anchor='center')
        self.chosen_tree.heading("课程号", text="课程号")
        self.chosen_tree.heading("课程", text="课程")
        self.chosen_tree.heading("学分", text="学分")
        self.chosen_tree.heading("教师", text="教师")

        self.chosen_tree.grid(row=0, column=0, sticky=NSEW)
        self.chosen_vbar.grid(row=0, column=1, sticky=NS)

        self.course_id = []
        self.course_name = []
        self.teacher_name = []
        self.credit = []
        
        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "select Course_id, Course_name, Teacher_name, Course_Credit from chosen_lesson where Student_Id = %s" % (self.student_id)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.course_id.append(row[0])
                self.course_name.append(row[1])
                self.teacher_name.append(row[2])
                self.credit.append(row[3])
                print("name: "+row[1])
        except:
            print("Unable to fetch data")
        for i in range(min(len(self.course_id), len(self.course_name), len(self.teacher_name), len(self.credit))):
            self.chosen_tree.insert('', i, values=(self.course_id[i], self.course_name[i], self.credit[i], self.teacher_name[i]))
        db.close()

        #可选课程
        self.sel_columns = ("课程号", "课程", "学分", "教师")
        self.sel_tree = ttk.Treeview(self.right_bottom, show="headings", height=18, columns=self.sel_columns)
        self.sel_vbar = ttk.Scrollbar(self.right_bottom, orient=VERTICAL, command=self.sel_tree.yview)
        self.sel_tree.configure(yscrollcommand=self.sel_vbar.set)

        self.sel_tree.column("课程号", width=100, anchor='center')
        self.sel_tree.column("课程", width=100, anchor='center')
        self.sel_tree.column("学分", width=100, anchor='center')
        self.sel_tree.column("教师", width=100, anchor='center')
        self.sel_tree.heading("课程号", text="课程号")
        self.sel_tree.heading("课程", text="课程")
        self.sel_tree.heading("学分", text="学分")
        self.sel_tree.heading("教师", text="教师")

        self.sel_tree.grid(row=0, column=0, sticky=NSEW)
        self.sel_vbar.grid(row=0, column=1, sticky=NS)

        self.sel_course_id = []
        self.sel_course_name = []
        self.sel_credit = []
        self.sel_teacher_name = []
        
        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "select * from select_lesson"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.sel_course_id.append(row[0])
                self.sel_course_name.append(row[1])
                self.sel_credit.append(row[2])
                self.sel_teacher_name.append(row[3])
                #print("name: "+row[1])
        except:
            print("Unable to fetch data")
        for i in range(min(len(self.sel_course_id), len(self.sel_course_name), len(self.sel_credit), len(self.sel_teacher_name))):
            self.sel_tree.insert('', i, values=(self.sel_course_id[i],
            self.sel_course_name[i], self.sel_credit[i], self.sel_teacher_name[i]))
        db.close()


        #个人信息 左上
        self.top_id = Label(self.left_top, text=self.id, font=('Verdana', 18))
        self.top_id.grid(row=0, column=0, columnspan=2, sticky=W, padx=50, pady=0)

        self.top_name = Label(self.left_top, text=self.name, font=('Verdana', 18))
        self.top_name.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=50, pady=0)

        self.top_sex = Label(self.left_top, text=self.sex, font=('Verdana', 18))
        self.top_sex.grid(row=2, column=0, columnspan=2, sticky=NSEW, padx=50, pady=0)

        self.top_classno = Label(self.left_top, text=self.classno, font=('Verdana', 18))
        self.top_classno.grid(row=3, column=0, columnspan=2, sticky=W, padx=50, pady=0)

        #操作 右上
        self.sel_tree.bind('<ButtonRelease-1>', self.getSelectedLesson)  # 左键获取位置
        self.chosen_tree.bind('<ButtonRelease-1>', self.getChosenLesson)
        self.right_top_button1 = ttk.Button(self.right_top, text="选课", width=20, command=self.chooseLesson)
        self.right_top_button2 = ttk.Button(self.right_top, text="取消选课", width=20, command=self.cancelChosenLesson)
        self.right_top_button3 = ttk.Button(self.right_top, text="返回", width=20, command = self.returnLastPage)

        self.right_top_button1.grid(row=1, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=3, column=0, padx=20, pady=10)

        #显示各个区域
        self.left_top.grid(row=0, column=0, padx=5, pady=5)
        self.left_bottom.grid(row=1, column=0, padx=25, pady=5)
        self.right_top.grid(row=0, column=1, padx=5, pady=5)
        self.right_bottom.grid(row=1, column=1, padx=25, pady=5)
        #self.center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        #self.bottom.grid(row=2, column=0, columnspan=2, padx=4, pady=5)

        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()
    
    #获得点击的可选课程
    def getSelectedLesson(self, event):
        #self.sel_col = self.sel_tree.identify_column(event.x)
        #self.sel_row = self.sel_tree.identify_row(event.y)
        for items in self.sel_tree.selection():
            self.sel_row_info = self.sel_tree.item(items, "values")

        #print("列"+self.sel_col)
        #print("行"+self.sel_row)
        #self.sel_row_info = self.sel_tree.item(self.sel_row, "values")
        print("选择的课程: ")
        print(self.sel_row_info)
        self.var_sel_course_id.set(self.sel_row_info[0])
        self.var_sel_course_name.set(self.sel_row_info[1])
        self.var_sel_credit.set(self.sel_row_info[2])
        self.var_sel_teacher_name.set(self.sel_row_info[3])
        print(self.var_sel_credit.get())
        print(self.var_sel_teacher_name.get())
        #self.right_top_id_entry = Entry(self.right_top, state='disabled', textvariable=self.var_id,
        #                        font=('Verdana', 15))

    def chooseLesson(self):
        #print(self.var_sel_course_id.get())
        #print(self.course_id)
        print("确定选择:")
        
        
        #if str(self.var_sel_course_id.get()) in self.course_id:
            #messagebox.showinfo("警告!", "该课程已经存在")
        #else:
        if self.var_sel_course_id.get() != '' and self.var_sel_course_name.get() != '' and self.var_sel_credit.get() != '' and self.var_sel_teacher_name.get() != '':
            db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
            cursor = db.cursor()
            sql = "insert into 选课 (Student_Id, Student_Name, Course_Id, Course_Name, Teacher_Name, Course_Credit) \
                   values ('%s', '%s', '%s', '%s', '%s', '%s')" % \
                    (self.student_id, self.var_name, self.var_sel_course_id.get(), self.var_sel_course_name.get(), self.var_sel_teacher_name.get(), self.var_sel_credit.get())
            try:
                cursor.execute(sql)
                db.commit()
                print("选课成功")
                
            except:
                db.rollback()

                messagebox.showinfo("错误", "数据库连接失败")
            db.close()

            
            #添加到已选课列表
            self.course_id.append(self.var_sel_course_id.get())
            self.course_name.append(self.var_sel_course_name.get())
            self.teacher_name.append(self.var_sel_teacher_name.get())
            self.credit.append(self.var_sel_credit.get())
            self.chosen_tree.insert('', len(self.course_id)-1, values=(
                self.course_id[len(self.course_id)-1],
                self.course_name[len(self.course_name)-1],
                self.credit[len(self.credit)-1],
                self.teacher_name[len(self.teacher_name)-1]))
            self.chosen_tree.update()

            #删除可选列表中的课程
            course_id_index = self.sel_course_id.index(self.sel_row_info[0])
            #print("删除选课: "+ self.sel_course_name[course_id_index])
            del self.sel_course_id[course_id_index]
            del self.sel_course_name[course_id_index]
            del self.sel_teacher_name[course_id_index]
            del self.sel_credit[course_id_index]
            self.sel_tree.delete(self.sel_tree.selection()[0])
            self.sel_tree.update()

            messagebox.showinfo("提示", "选择成功")

    #获得点击的已选课程
    def getChosenLesson(self, event):
        #self.chosen_col = self.sel_tree.identify_column(event.x)
        #self.chosen_row = self.sel_tree.identify_row(event.y)
        for items in self.chosen_tree.selection():
            self.chosen_row_info = self.chosen_tree.item(items, "values")
            print(self.chosen_row_info)

        #print("列: "+self.chosen_col)
        #print("行: "+self.chosen_row)
        #self.chosen_row_info = self.chosen_tree.item(self.chosen_row, "values")
        self.var_chosen_course_id.set(self.chosen_row_info[0])
        self.var_chosen_course_name.set(self.chosen_row_info[1])
        self.var_chosen_teacher_name.set(self.chosen_row_info[3])  
        self.var_chosen_credit.set(self.chosen_row_info[2])
    
    def cancelChosenLesson(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选课程？')
        if res == True:
            print(self.var_chosen_course_id.get())

            db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
            cursor = db.cursor()
            sql = "delete from 选课 where Course_Id = '%s' and Student_Id = '%s'" % (self.var_chosen_course_id.get(), self.student_id)
            try:
                cursor.execute(sql)
                db.commit()
                print("成功")
                
            except:
                db.rollback()

                messagebox.showinfo("错误", "数据库连接失败")
            db.close()

            #删除表中元素
            course_id_index = self.course_id.index(self.chosen_row_info[0])
            print("删除选课: "+ self.course_name[course_id_index])
            del self.course_id[course_id_index]
            del self.course_name[course_id_index]
            del self.teacher_name[course_id_index]
            del self.credit[course_id_index]
            #print(self.credit)
            #print(self.chosen_tree.selection()[0])
            self.chosen_tree.delete(self.chosen_tree.selection()[0])

            #添加删除的课程到可选列表
            self.sel_course_id.append(self.var_chosen_course_id.get())
            self.sel_course_name.append(self.var_chosen_course_name.get())
            self.sel_teacher_name.append(self.var_chosen_teacher_name.get())
            self.sel_credit.append(self.var_chosen_credit.get())
            self.sel_tree.insert('', len(self.sel_course_id)-1, values=(
                self.sel_course_id[len(self.sel_course_id)-1],
                self.sel_course_name[len(self.sel_course_name)-1],
                self.sel_credit[len(self.sel_credit)-1],
                self.sel_teacher_name[len(self.sel_teacher_name)-1]))
            self.sel_tree.update()

            messagebox.showinfo("提示", "取消选课成功")
            
    #上一页
    def returnLastPage(self):
        StudentView(self.window, self.student_id)

    #返回到首页
    def back(self):
        StartPage(self.window)
        

#教师：录入，修改成绩
class TeacherView(object):
    def __init__(self, parent_window, teacher_id):    
        parent_window.destroy()
        
        self.window = Tk()
        self.window.title('教师界面')
        self.window.geometry("300x700")
        self.left_top = Frame(width=300, height=200)
        self.right_top = Frame(width=300, height=200)
        self.center = Frame(width=500, height=400)
        self.bottom = Frame(width=650, height=50)

        self.id = StringVar()
        self.name = StringVar()
        self.sex = StringVar()
        self.subject = StringVar()
        self.teacher_id = teacher_id
        self.teacher_name = StringVar()
        self.var_course_id = StringVar()
        self.var_course_name = StringVar()

        self.course_id = []
        self.course_name = []

        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "select * from 教师 where Teacher_Id = %s" %(self.teacher_id)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.id = '工号: ' + row[0]
                self.name = '姓名: ' + row[1]
                self.teacher_name = row[1]
                self.sex = '性别: ' + row[2]
                self.subject = '教学科目: ' + row[4]
        except:
            print("Error: Unable to fetch data")
            #print(self.teacher_id)
        db.close()
    
        #个人信息

        self.top_title = Label(self.left_top, text="个人信息", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=W, padx=50, pady=10)

        self.top_id = Label(self.left_top, text=self.id, font=('Verdana', 18))
        self.top_id.grid(row=1, column=0, columnspan=2, sticky=W, padx=50, pady=0)

        self.top_name = Label(self.left_top, text=self.name, font=('Verdana', 18))
        self.top_name.grid(row=2, column=0, columnspan=2, sticky=NSEW, padx=50, pady=0)

        self.top_sex = Label(self.left_top, text=self.sex, font=('Verdana', 18))
        self.top_sex.grid(row=3, column=0, columnspan=2, sticky=W, padx=50, pady=0)

        self.top_classno = Label(self.left_top, text=self.subject, font=('Verdana', 18))
        self.top_classno.grid(row=4, column=0, columnspan=2, sticky=W, padx=50, pady=0)

        #功能
        self.function_title = Label(self.right_top, text = "操作", font=('Verdana', 20))
        self.function_title.grid(row = 0, column = 0, columnspan=2, sticky=NSEW)

        self.select_lesson = Button(self.right_top, text = "录入成绩", width = 10, font = tkFont.Font(size=12), command=self.registerScore)
        self.select_lesson.grid(row = 1, column = 0, columnspan=2, sticky=NSEW)

        #返回按钮
        self.back_button = Button(self.right_top, text="返回", width=10, font=('Verdana', 12), command=self.returnLastPage)
        self.back_button.grid(row = 2, column = 0, columnspan=2, sticky=NSEW, pady=10)

        #self.get_score = Button(self.right_top, text = "查询成绩", width = 10, font = tkFont.Font(size=12), command=self.showScore)
        #self.get_score.grid(row = 2, column = 0, columnspan=2, sticky=NSEW, pady=10)

        #显示教学课程

        self.columns = ("课程号", "课程")
        self.tree = ttk.Treeview(self.center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.center, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vbar.set)

        self.tree.column("课程号", width=100, anchor='center')
        self.tree.column("课程", width=100, anchor='center')
        self.tree.heading("课程号", text="课程号")
        self.tree.heading("课程", text="课程")

        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)
        self.tree.bind('<ButtonRelease-1>', self.getChosenLesson)

        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "SELECT Course_Id, Course_Name from 课程 WHERE Teacher_Name = '%s'" %(self.teacher_name)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print("读取成功")
            print(results)
            for row in results:
                self.course_id.append(row[0])
                self.course_name.append(row[1])

            for i in range(min(len(self.course_id), len(self.course_name))):
                self.tree.insert('', i, values=(self.course_id[i],
                self.course_name[i]))
        except:
            print("Error: Unable to fetch data")
        db.close()
        
        #显示各个区域
        self.left_top.grid(row=0, column=0, padx=30, pady=5)
        self.center.grid(row=1, column=0, padx=40, pady=5)
        self.right_top.grid(row=2, column=0, padx=30, pady=5)

        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()

        #获得点击的已选课程

    def getChosenLesson(self, event):
        #self.chosen_col = self.sel_tree.identify_column(event.x)
        #self.chosen_row = self.sel_tree.identify_row(event.y)
        for items in self.tree.selection():
            self.chosen_row_info = self.tree.item(items, "values")
            #print(self.chosen_row_info)

        self.var_course_id.set(self.chosen_row_info[0])
        self.var_course_name.set(self.chosen_row_info[1])
        #self.var_chosen_course_name.set(self.chosen_row_info[1])

    def returnLastPage(self):
        TeacherLogin(self.window)

    def registerScore(self):
        registerScorePage(self.window, self.var_course_id.get(), self.var_course_name, self.teacher_id)

    def back(self):
        StartPage(self.window)

#录入成绩页面
class registerScorePage(object):
    def __init__(self, parent_window, course_id, course_name, teacher_id):
        parent_window.destroy()
        
        self.window = Tk()
        self.window.title('录入成绩界面')
        self.window.geometry("740x700")
        self.frame_left_top = tk.Frame(width=300, height=200)
        self.frame_right_top = tk.Frame(width=300, height=200)
        self.frame_center = tk.Frame(width=500, height=400)
        self.frame_bottom = tk.Frame(width=650, height=50)

        self.course_id = course_id
        self.course_name = course_name
        self.teacher_id = teacher_id

        # 定义下方中心列表区域
        self.columns = ("学号", "姓名", "成绩")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("学号", width=150, anchor='center')
        self.tree.column("姓名", width=150, anchor='center')
        self.tree.column("成绩", width=100, anchor='center')
        self.tree.heading("学号", text="学号")
        self.tree.heading("姓名", text="姓名")
        self.tree.heading("成绩", text="成绩")

        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        self.id = []
        self.name = []
        self.score = []

        db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
        cursor = db.cursor()
        sql = "SELECT Student_Id, Student_Name, Score from 成绩 where Course_Id = '%s'" %(self.course_id)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            print("读取成绩成功")
            #print(results)
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.score.append(row[2])

            for i in range(min(len(self.id), len(self.name))):
                self.tree.insert('', i, values=(self.id[i],
                self.name[i],
                self.score[i]))
        except:
            print("Error: Unable to fetch data")
        db.close()

        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="成绩信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_score = StringVar()

        #学号
        self.right_top_id_label = Label(self.frame_left_top, text="学号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)

        #姓名
        self.right_top_name_label = Label(self.frame_left_top, text="姓名：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)
        self.right_top_name_entry.grid(row=2, column=1)

        #成绩
        self.right_top_score_label = Label(self.frame_left_top, text="成绩：", font=('Verdana', 15))
        self.right_top_score_entry = Entry(self.frame_left_top, textvariable=self.var_score, font=('Verdana', 15))
        self.right_top_score_label.grid(row=3, column=0)
        self.right_top_score_entry.grid(row=3, column=1)

        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建成绩信息', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中信息', width=20,command=self.update_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中信息', width=20,command=self.del_row)
        self.right_top_button4 = ttk.Button(self.frame_right_top, text="返回", width=20, command = self.returnLastPage)

        # 位置设置
        self.right_top_title.grid(row=1, column=0, pady=10)
        self.right_top_button1.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=4, column=0, padx=20, pady=10)
        self.right_top_button4.grid(row=4, column=0, padx=20, pady=10)

        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=50, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=20, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=150, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.window.protocol("WM_DELETE_WINDOW", self.back)
        self.window.mainloop()
    
    def back(self):
        StartPage(self.window) # 显示主窗口 销毁本窗口

    def returnLastPage(self):
        TeacherView(self.window, self.teacher_id)

    def click(self, event):
        self.col = self.tree.identify_column(event.x)
        self.row = self.tree.identify_row(event.y)

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.raw_id = self.row_info[0]
        self.var_name.set(self.row_info[1])
        self.var_score.set(self.row_info[2])

        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id, font=('Verdana', 15))

    def new_row(self):
        print('123')
        print(self.var_id.get())
        print(self.id)
        print(self.course_name)
        
        #if str(self.var_id.get()) in self.id:
        #    messagebox.showinfo('警告！', '该学生已存在！')
        #else:
        if self.var_id.get() != '' and self.var_name.get() != '' and self.var_score.get() != '':
            db = pymysql.connect('localhost', 'root', 'huyuan1649', 'course')
            cursor = db.cursor()
            sql = "insert into 成绩 (Student_Id, Student_Name, Course_Id, Course_Name, Score) \
                values ('%s', '%s', '%s', '%s', '%s')" % \
                    (self.var_id.get(), self.var_name.get(), self.course_id, self.course_name, self.var_score.get())
            try:
                cursor.execute(sql)
                db.commit()
                print("录入成功")
                
            except:
                db.rollback()

                messagebox.showinfo("错误", "数据库连接失败")
            db.close()

            self.id.append(self.var_id.get())
            self.name.append(self.var_name.get())
            self.score.append(self.var_score.get())
            self.tree.insert('', len(self.id) - 1, values=(self.id[len(self.id) - 1],
                             self.name[len(self.id) - 1], 
                             self.score[len(self.id) - 1]))
            self.tree.update()
            messagebox.showinfo('提示！', '插入成功！')
        else:
            messagebox.showinfo('警告！', '请填写学生数据')

    def update_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row_info[0]:
                print(self.var_id.get())
                db = pymysql.connect("localhost", "root", "huyuan1649", "course")
                cursor = db.cursor()
                #sql = "UPDATE 成绩 SET Score = '%s' \
                #       WHERE Student_Id = '%s'" % (self.var_score.get(), self.var_id.get())
                sql = "UPDATE 成绩 SET Score = '%s', Student_Name = '%s' \
                       WHERE Student_Id = '%s'" % (self.var_score.get(), self.var_name.get(), self.var_id.get())
                try:
                    cursor.execute(sql)
                    db.commit()
                    print("更新成功")
                    messagebox.showinfo('提示！', '更新成功！')
                
                except:
                    db.rollback()

                    messagebox.showinfo("错误", "数据库连接失败")

                id_index = self.id.index(self.row_info[0])
                self.name[id_index] = self.var_name.get()
                self.score[id_index] = self.var_score.get()

                self.tree.item(self.tree.selection()[0], values=(
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_score.get()))
            else:
                messagebox.showinfo('警告！', '不能修改学生学号！')

    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的学号
            print(self.tree.selection()[0])
            print(self.tree.get_children())
            db = pymysql.connect("localhost", "root", "huyuan1649", "course")
            cursor = db.cursor()
            sql = "delete from 成绩 where Student_Id = '%s'" % (self.row_info[0])
            try:
                cursor.execute(sql)
                db.commit()
                print("删除成功")
                messagebox.showinfo('提示！', '删除成功！')
            
            except:
                db.rollback()

                messagebox.showinfo("错误", "数据库连接失败")
            db.close()

            id_index = self.id.index(self.row_info[0])
            del self.id[id_index]
            del self.name[id_index]
            del self.score[id_index]
            print(self.id)
            self.tree.delete(self.tree.selection()[0])
            print(self.tree.get_children())

        
#if __name__ == '__name__':
window = tk.Tk()
StartPage(window)
#AdminLogin(window)
#PermittionLogin(window)
#StudentLogin(window)
#TeacherLogin(window)
#AdminView(window)
#PermittionManage(window)
#CoursePage(window)
#TeacherPage(window)
#StudentPage(window)
#StudentView(window, 1)
#showScorePage(window, 1)
#SelectLessonPage(window, 1)
#TeacherView(window, 1001)
#registerScorePage(window, "101", "计算机", "1001")

