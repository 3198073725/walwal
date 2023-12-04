# -*- coding:utf-8 -*-\
import os,csv,os.path
#增删改查
"""
增：add、insert
删：del、delete、remoue
改：update
查：select、find、search
"""

#学生信息管理系统
#学生信息类
class Student:
    def __init__(self,no,name,math,chinese,english):
        self.no = int(no)
        self.name = name

        # #方法一
        # self.math = math
        # self.chinese = chinese
        # self.ehglish = english

        #方法二
        self.math = int(math)
        self.chinese = int(chinese)
        self.english = int(english)

#学生管理类
class Student_list:
    def __init__(self):
        self.stulist = []

    #判断输入成绩是否正确
    def __enterScore(self,msg):

        # 方法一
        # while True:
        #     #异常处理
        #     try:
        #         score =msg
        #         if 0 <= int(score) <= 150:
        #             break
        #         else:
        #             print("输入错误，成绩应在0到150之间")
        #             break
        #     except:
        #         print("输入错误，成绩应在0到150之间")


        #方法二
        #成绩属于
        while True:
            score = input(msg)
            # 异常处理
            try:
                if 0 <= int(score) <= 150:
                    break
                else:
                    print(f"输入错误，{msg}应在0到150之间")
            except:
                print(f"输入错误,请重新输入正确的{msg}")
        return score
    #判断stulist中是否存在相同学号
    def __exists(self, no):
        # print(self.stulist.no)
        # 判断学号是否存在
        #for  else:全部遍历完在进行判断，if else:遍历一次判断一次，无法查找全部的学号。
        for stu in self.stulist:
            if stu.no == no:
                return True
        else:
            return False


    #添加学生信息方法
    def insertStu(self):
        while True:
            #int()：可加可不加，加上更严谨
            try:
                no = int(input("请输入学号："))
                # print(self.__exists(no))
                if self.__exists(no) == True:
                    print('该学号已存在')
                    print(''.center(30, '-'))

                else:
                    name = input("请输入姓名：")
                # 方法一：用数学成绩测试
                # math = int(input("请输入数学成绩："))
                # chinese = int(input("请输入语文成绩："))
                # english = int(input("请输入英语成绩："))
                # self.__enterScore(math)
                    # 方法二
                    math = self.__enterScore("数学成绩：")
                    chinese = self.__enterScore("语文成绩：")
                    english = self.__enterScore("英语成绩：")

                    stu = Student(no, name, math, chinese, english)
                    self.stulist.append(stu)
                    # print(self.stulist)
                    break
            except:
                print("您输入的格式错误，请重新输入")

        #方便用户继续添加
        print(''.center(24,'<'))
        choice = input('是否继续添加(y/n)?\n').lower()
        if choice == 'n':
            self.showStu()
        elif choice=='y':
            self.insertStu()
        else:
            print("输入错误，退出系统")
            self.info()


    #显示学生基本信息
    def showStu(self):
        print(''.center(52, '-'))
        print('{:8}\t{:8}\t{:8}\t{:8}\t{:8}'.format('学号','姓名','数学','语文','英语'))
        for stu in self.stulist:
            print('{:<8}\t{:8}\t{:<8}\t{:<8}\t{:<8}'.format(stu.no,stu.name,stu.math,stu.chinese,stu.english))
        print(''.center(52,'-'))

    # delStu(self):删除学生信息
    def delStu(self):

        while True:
            #展示学生信息
            self.showStu()
            try:
                #接收学号
                #int()可加可不加，加上更严谨
                no = int(input("请输入要删除的学号："))
                #遍历找相同学号
                for item in self.stulist[::]:
                    if item.no == no:
                        self.stulist.remove(item) #item：包含某一个学生所有的数据（学号，姓名，成绩）
                        print('删除成功')
                        break
                else:
                    print('该学号不存在')
                self.showStu()
                # 继续删除
                choice = input('是否继续删除(y/n)?\n').lower()
                if choice == 'y':
                    self.delStu()
                elif choice == 'n':
                    self.info()
                else:
                    print('输入错误，退出系统')
                break
            except :
                print("您输入的格式错误，请重新输入")
                self.delStu()

    #修改全部数据
    def update_Stu(self):
        while True:
            try:
                self.showStu()
                no = int(input("请输入要修改信息的学生学号："))
                if self.__exists(no):
                    #修改对应学号的其他信息
                    for item in self.stulist[::]:
                        if item.no == no:
                            print(''.center(52, '+'))
                            item.name = input("请输入姓名：")
                            item.math = int(self.__enterScore("请输入数学成绩："))
                            item.chinese = int(self.__enterScore("请输入语文成绩："))
                            item.english = int(self.__enterScore("请输入英语成绩："))
                            break
                    print("修改成功")
                    self.showStu()
                else:
                    print('该学号不存在,请重新输入')
            except:
                print("输入格式错误，退出系统")
                self.update()
            choice = input('是否继续修改(y/n)?\n').lower()
            if choice == 'y':
                self.update_Stu()
            elif choice == 'n':
                self.info()
            else:
                print('输入错误，退出系统')
                self.info()

    #修改单个数据信息
    def updateStu(self):

        """
        1、接收学号
        2、遍历
        3、判断学号是否存在
        4、接收其他数据（姓名，成绩）
        5、重新写入self.stulist
        :return:
        """
        while True:
            try:
                self.showStu()
                no = int(input("请输入要修改信息的学生学号："))
                if self.__exists(no):
                    try:
                        print("1.姓名")
                        print("2.数学")
                        print("3.语文")
                        print("4.英语")
                        studen = int(input("请选择修改那项数据:"))
                        #修改对应学号的其他信息
                        for item in self.stulist[::]:
                            if item.no == no:
                                print(''.center(52, '+'))
                                if int(studen) == 1:
                                    item.name = input("请输入姓名：")
                                elif int(studen) == 2:
                                    item.math = int(self.__enterScore("请输入数学成绩："))
                                elif int(studen) == 3:
                                    item.chinese = int(self.__enterScore("请输入语文成绩："))
                                elif int(studen) == 4:
                                    item.english = int(self.__enterScore("请输入英语成绩："))
                                elif int(studen) != (1,2,3,4):
                                    print("抱歉没有该数据可供修改")
                                    break
                                print("修改成功")
                                self.showStu()
                    except:
                            print("输入的格式错误，请重新输入")
                            self.updateStu()

                else:
                    print('该学号不存在,请重新输入')
            except:
                print("抱歉您输入的格式有误，请重新输入")
                self.updateStu()
            choice = input('是否继续修改(y/n)?\n').lower()
            if choice == 'y':
                self.updateStu()
            elif choice == 'n':
                self.info()
            else:
                print('输入错误，退出系统')
                self.info()
    def update(self):
        while True:
            self.showStu()
            try:
                print("1.修改单个数据")
                print("2.修改全部数据")
                print("3.退回上级目录")
                up = int(input("请选择修改方式:"))
                if up == 1:
                    self.updateStu()
                elif up == 2:
                    self.update_Stu()
                elif up == 3:
                    self.info()
                else:
                    print("请按指定数字进行修改")

            except:
                print("格式输入错误请重新输入")

    #导入学生信息
    def loadStu(self):
        print("在导入前请把目标.csv文件放在同文件夹内")
        print("注意当前系统只支持.csv文件")
        print("导入学生信息".center(52, "*"))
        while True:
            try:
                str = input("请输入要导入的.csv文件:")+(".csv")
                value = os.path.exists(r"E:\pythonProject\学生信息管理")
                if value == True:
                    with open(str,'r', encoding='UTF-8') as fp:
                        fs = fp.readline().strip('\n')
                        while True:
                            fs = fp.readline().strip('\n')
                            if not fs:
                                break
                            else:
                                stu = Student(*fs.split(','))
                                if self.__exists(stu.no):
                                    print(f'学号:{stu.no}已存在')
                                else:
                                    self.stulist.append(stu)
                        print("导入完成")



                elif value == False:
                    print("您的目录下没有该文件")
                else:
                    print("输入错误，请重新输入")
            except:
                print("您输入的格式错误")
                # self.info()
            choice = input('是否继续导入(y/n)?\n').lower()
            if choice == 'y':
                self.loadStu()
            elif choice == 'n':
                self.showStu()
                self.info()
            else:
                print('输入错误，退出系统')
                self.info()
    #按学号查找学生
    def find_no(self):
        try:
            no = int(input("请输入要查看的学号："))
            if self.__exists(no):
                for str in self.stulist[::]:
                    if str.no == no:
                        print(f"学号：{str.no}，姓名：{str.name}，数学成绩：{str.math}，语文成绩：{str.chinese}，英语成绩：{str.english}")
                        break
            else:
                print("没有该学号的信息")
            choice = input('是否继续查看(y/n)?\n').lower()
            if choice == 'y':
                self.find_no()
            elif choice == 'n':
                self.findStu()
            else:
                print('输入错误，退出系统')
                self.info()

        except:
            print("您输入的格式有误，退出系统")
            self.findStu()
    #按姓名查找学生
    def find_name(self):
            name = input("请输入要查找的姓名：")
            for stu in self.stulist:
                if name == stu.name:
                    print('学号:{}，姓名:{}、数学成绩:{}、语文成绩:{}、英语成绩:{}'.format(stu.no, stu.name, stu.math, stu.chinese,stu.english))
            choice = input('是否继续查看(y/n)?\n').lower()
            if choice == 'y':
                self.find_name()
            elif choice == 'n':
                self.findStu()
            else:
                print('输入错误，退出系统')
                self.info()
    #查看总人数
    def find_sum(self):
            str = len(self.stulist)
            print(f"总人数为{str}人")
    #查看学生信息
    def findStu(self):
        try:
            print("1.按学号查找")
            print("2.按姓名查找")
            print("3.查看总人数")
            print("4.退回到上级")
            s = int(input("请选择你要查找学生方式："))
            if s == 1:
                self.find_no()
            elif s == 2:
                self.find_name()
            elif s == 3:
                self.find_sum()
            elif s == 4:
                self.info()
            else:
                print("输入错误请重新输入")
        except:
            print("您输入的格式错误，退出系统")
    #导出学生信息
    def saveStu(self):
        #上下文管理器：with
        print("请注意在输入导出名字时不用加后缀")
        str = input("请输入想导出的名字：")+(".csv")
        print("导出学生信息".center(52, "*"))
        if os.path.exists(str) == False:

            with open (str,"w+",newline="",encoding='utf-8') as f:
                w = csv.writer(f, delimiter=',')
                w.writerow(['学号', '姓名', '数学', '语文', '英语'])
                for stu in self.stulist:
                   w.writerow([stu.no,stu.name,stu.math,stu.chinese,stu.english])
                print('输出成功，请到源文件夹内查看')
                print('退出系统')
                exit()
        else:
            print("该目录已有同名文件，请更换导出名字")
            exit()

    #个人课程平均分
    def avg(self):

        self.showStu()
        while True:
            try:
                no = int(input("请输入你想查看课程平均分的学号："))
                if self.__exists(no):
                    for item in self.stulist[::]:
                        if item.no == no:
                            avg = (item.math + item.chinese + item.english )/3
                            print("{}的课程平均分为{:.2f}".format(item.name,avg))
                            break
                else:
                    print("该学号不存在，请重新输入")
            except:
                print("您输入的格式有问题，请重新输入")

            choice = input('是否继续查看(y/n)?\n').lower()
            if choice == 'y':
                self.avg()
            elif choice == 'n':
                self.score()
            else:
                print('输入错误，退出系统')
                self.score()
    #整体课程平均分
    def avg_zt(self):
        if len(self.stulist) > 0:
            avg_math = sum([stu.math for stu in self.stulist])/len([stu.math for stu in self.stulist])
            avg_chinese = sum([stu.chinese for stu in self.stulist])/len([stu.chinese for stu in self.stulist])
            avg_english = sum([stu.english for stu in self.stulist])/len([stu.english for stu in self.stulist])
            print(f"数学平均分：{avg_math}，语文平均分：{avg_chinese}，英语平均分：{avg_english}")
            self.score()
    #平均分菜单
    def avg_main(self):
        while True:
            try:
                print("平均分查看菜单")
                print("1.查看个人平均分")
                print("2.查看整体平均分")
                s = int(input("请进行选择查看方式："))
                if s == 1:
                    self.avg()
                elif s == 2:
                    self.avg_zt()
                else:
                    print("请输入正确的查看方式")
            except:
                print("您输入的有误，退出系统")
                self.score()
    #课程最高分
    def max(self):
               if len(self.stulist) > 0:
                   math_max = max([stu.math for stu in self.stulist ])
                   chinese_max = max([stu.chinese for stu in self.stulist])
                   english_max = max([stu.english for stu in self.stulist])
                   print(f"数学成绩最高分是:{math_max}")
                   print(f'语文成绩最高分是:{chinese_max}')
                   print(f'英语成绩最高分是:{english_max}')
               else:
                   print('还没有学生成绩...')
    #课程最低分
    def min(self):
        if len(self.stulist) > 0:
            math_min = min([stu.math for stu in self.stulist])
            chinese_min = min([stu.chinese for stu in self.stulist])
            english_min = min([stu.english for stu in self.stulist])
            print(f"数学成绩最底分是:{math_min}")
            print(f'语文成绩最底分是:{chinese_min}')
            print(f'英语成绩最底分是:{english_min}')

    #
    #排序菜单
    def sortStu(self):
        self.showStu()
        try:
            print("排序".center(52, "*"))
            print("1.按学号排序")
            print("2.按姓名排序")
            print("3.按数学成绩排序")
            print("4.按语文成绩排序")
            print("5.按英语成绩排序")
            s = int(input("请输入您想进行的排序方式："))
            while True:
                if s == 1:
                    print("学号")
                    # self.noStu()
                elif s == 2:
                    print("姓名")
                elif s == 3:
                    print("数学")
                elif s == 4:
                    print("yuwen")
                elif s == 5:
                    print("英语")
                else:
                    print("请输入指定数字")
                break
        except:
            print("您输入的格式错误，请重新输入")
    #学生成绩管理菜单
    def score(self):
        print("学生成绩管理菜单".center(52, "*"))
        print("avg-->课程平均分")
        print("max-->课程最高分")
        print("sort----->排序")
        print("return---->返回")
        while True:
            s = input("score>").strip().lower()
            if s == 'avg':
                self.avg_main()
            elif s == 'max':
                self.max()
            elif s == 'min':
                self.min()
            elif s == 'sort':
                self.sortStu()
            elif s == 'return':
                self.main()
            else:
                print("输入错误，请重新输入")

    #学生基本信息管理菜单
    def info(self):
        print('学生基本信息管理菜单'.center(52, "*"))
        print("load-->导入学生信息")
        print("insert->添加学生信息")
        print("delete->删除学生信息")
        print("update->修改学生信息")
        print("show->显示学生信息")
        print("save->导出学生信息")
        print("find-->查找学生信息")
        print("return-->返回")
        print("".center(52, '='))
        while True:
            e = input("info>").strip().lower()
            if e == "load":
                self.loadStu()
            elif e == 'insert':
                print("添加学生信息".center(52, '*'))
                #调用添加学生信息方法
                self.insertStu()
            elif e == 'delete':
                print("删除学生信息".center(52, '*'))
                self.delStu()
            elif e == 'update':
                print("修改学生信息".center(52, '*'))
                self.update()
            elif e == 'show':
                self.showStu()
                # print('显示')
            elif e == 'save':
                print("输出学生信息".center(52, '*'))
                self.saveStu()
            elif  e == 'find':
                print("查找学生信息".center(52, '*'))
                self.findStu()
            elif e =='return':
                self.main()
            else:
                print("输入错误请重新输入")

    #主控制函数
    def main(self):
        #显示菜单
        while True:
            print("学生信息管理系统".center(52,"="))
            print("info-->学生基本信息管理")
            print("score->学生成绩管理")
            print("exit-->退出系统")
            print("".center(52,'='))
            s = input("请选择：").strip().lower()
            if s == "info":
                #调用学生基本信息管理函数
                self.info()
            elif s == 'score':
                self.score()
            elif s == 'exit':
                print("退出系统")
                exit()
            else:
                print("输入错误请重新输入")

if __name__ == '__main__':
    st = Student_list()
    st.main()