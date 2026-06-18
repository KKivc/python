class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f'姓名: {self.name} \t 语文：{self.chinese} \t 数学: {self.math} \t 英语: {self.english}'
    

class StudentManagement:
    def __init__(self):
        self.students = []

    # 寻找学生
    def find_student(self, stu_name):
        
        for s in self.students:
            if s.name == stu_name:
                return s
            
        return 0

    # 添加学生信息
    def add_student(self, stu_name, chinese, math, english):
        s = self.find_student(stu_name)

        if s != 0:
            print('该学生已存在，请重新选择')
            return
            
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            self.students.append(Student(stu_name, chinese, math, english))
            print('学生信息添加成功')
            return
        else:
            print('成绩输入有误，请重新输入')
            return
            
    def add_student_menu(self):
        name = input('请输入学生姓名')
        chinese = int(input('请输入语文成绩：'))
        math = int(input('请输入数学成绩：'))
        english = int(input('请输入英语成绩：'))
        self.add_student(name, chinese, math, english)

    # 修改学生信息
    def modify_student(self, stu_name, chinese, math, english):
        s = self.find_student(stu_name)

        if s == 0:
                print('学生不存在')

        else:
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.chinese = chinese
                    s.math = math
                    s.english = english
                    print('学生信息修改成功')
                    return
                else:
                    print('成绩输入有误，请重新输入')
                    return
        
            
    def modify_student_menu(self):
        name = input('请输入要修改的学生姓名: ')
        chinese = int(input('请输入新的学生语文成绩: '))
        math = int(input('请输入新的学生数学成绩: '))
        english = int(input('请输入新的学生英语成绩: '))
        self.modify_student(name, chinese, math, english)
                

    # 删除学生信息
    def del_student(self, stu_name):
        s = self.find_student(stu_name)
        if s != 0:
                self.students.remove(s)
                print('学生信息删除成功')
                return

        else:
            print('学生不存在')

    def del_student_menu(self):
        name = input('请输入要删除的学生姓名: ')
        self.del_student(name)

    # 查询学生信息
    def query_student(self, stu_name):
        s = self.find_student(stu_name)

        if s != 0:
                print(f'学生信息：{s}')
                return

        else:
            print('学生不存在')

    def query_student_menu(self):
        name = input('请输入要查询的学生姓名: ')
        self.query_student(name)

    # 展示全部学生
    def list_allstudent(self):
        for s in self.students:
            print(s)

        
    # 运行系统
    def run(self):
        while True:
            print('##########  教务管理系统 ##########')
            print('#        1. 添加学生信息          #')
            print('#        2. 修改学生信息          #')
            print('#        3. 删除学生信息          #')
            print('#        4. 查询学生信息          #')
            print('#        5. 列出所有学生          #')
            print('#        6. 退出系统              #')

            choice = input('请选择操作: ')
            try:

                match choice:
                    case '1':
                        self.add_student_menu()

                    case '2':
                        self.modify_student_menu()

                    case '3':
                        self.del_student_menu()

                    case '4':
                        self.query_student_menu()

                    case '5':
                        self.list_allstudent()

                    case '6':
                        print('退出系统')
                        break
                
                    case _:
                        print('无效操作，请重新选择')
            except Exception:
                print('运行出错，请重新检查')


# 测试
if __name__ == '__main__':
    edu_management = StudentManagement()
    edu_management.run()
