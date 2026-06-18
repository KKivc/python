menu = '''
##########  教务管理系统 ##########
#        1. 添加学生信息         #
#        2. 修改学生信息         #
#        3. 删除学生信息         #
#        4. 查询学生信息         #
#        5. 列出所有学生         #
#        6. 统计班级成绩         #
#        7. 退出系统             #
'''

stu = {}

while True:
    print(menu)
    choice = input('请选择操作: ')
    match choice:
        case '1':
            stu_name = input('请输入学生姓名: ')
            if stu_name in stu:
                print('该学生已存在，请重新选择')
            else:
                stu_chinese = int(input('请输入学生语文成绩: '))
                stu_math = int(input('请输入学生数学成绩: '))
                stu_english = int(input('请输入学生英语成绩: '))
                stu[stu_name] = {
                    'chinese': stu_chinese,
                    'math': stu_math,
                    'english': stu_english
                }
                print('学生信息添加成功')
        case '2':
            stu_name = input('请输入要修改的学生姓名: ')
            if stu_name in stu:
                stu_chinese = float(input('请输入新的学生语文成绩: '))
                stu_math = float(input('请输入新的学生数学成绩: '))
                stu_english = float(input('请输入新的学生英语成绩: '))
                stu[stu_name] = {
                    'chinese': stu_chinese,
                    'math': stu_math,
                    'english': stu_english
                }
                print('学生信息修改成功')
            else:
                print('该学生不存在，请重新选择')
        case '3':
            stu_name = input('请输入要删除的学生姓名: ')
            if stu_name in stu:
                del stu[stu_name]
                print('学生信息删除成功')
            else:
                print('该学生不存在，请重新选择')
        case '4':
            stu_name = input('请输入要查询的学生姓名: ')

            if stu_name in stu:
                print(f'学生姓名: {stu_name}')
                print(f'学生语文成绩: {stu[stu_name]['chinese']}')
                print(f'学生数学成绩：{stu[stu_name]['math']}')
                print(f'学生英语成绩：{stu[stu_name]['english']}')
            else:
                print('该学生不存在，请重新选择')
        case '5':
          for stu_name in stu.keys():
              stu_info = stu[stu_name]
              print(f'学生姓名: {stu_name}, 学生语文成绩: {stu_info["chinese"]}, 学生数学成绩: {stu_info["math"]}, 学生英语成绩: {stu_info["english"]}')
        case '6':
            if len(stu) == 0:
                print('没有学生信息，请先添加学生信息')
            else:
                n = len(stu)

                # 定义一个临时列表
                chinese = [stu_info['chinese'] for stu_info in stu.values()]
                math = [stu_info['math'] for stu_info in stu.values()]
                english = [stu_info['english'] for stu_info in stu.values()]

                max_chinese = max(chinese)
                min_chinese = min(chinese)
                avg_chinese = sum(chinese) / n

                max_math = max(math)
                min_math = min(math)
                avg_math = sum(math) / n

                max_english = max(english)
                min_english = min(english)
                avg_english = sum(english) / n

                max_chinese_name = [stu_name for stu_name, stu_info in stu.items() if stu_info['chinese'] == max_chinese]
                min_chinese_name = [stu_name for stu_name, stu_info in stu.items() if stu_info['chinese'] == min_chinese]
                max_math_name = [stu_name for stu_name, stu_info in stu.items() if stu_info['math'] == max_math]
                min_math_name = [stu_name for stu_name, stu_info in stu.items() if stu_info['math'] == min_math]
                max_english_name = [stu_name for stu_name, stu_info in stu.items() if stu_info['english'] == max_english]
                min_english_name = [stu_name for stu_name, stu_info in stu.items() if stu_info['english'] == min_english]

                print(f'语文成绩最高分: {max_chinese}, 学生姓名: {", ".join(max_chinese_name)}')
                print(f'语文成绩最低分: {min_chinese}, 学生姓名: {", ".join(min_chinese_name)}')
                print(f'语文成绩平均分: {avg_chinese:.1f}')
                print(f'数学成绩最高分: {max_math}, 学生姓名: {", ".join(max_math_name)}')
                print(f'数学成绩最低分: {min_math}, 学生姓名: {", ".join(min_math_name)}')
                print(f'数学成绩平均分: {avg_math:.1f}')
                print(f'英语成绩最高分: {max_english}, 学生姓名: {", ".join(max_english_name)}')
                print(f'英语成绩最低分: {min_english}, 学生姓名: {", ".join(min_english_name)}')
                print(f'英语成绩平均分: {avg_english:.1f}')
                                                            
        case '7':
            print('退出系统')
            break
        case _:
            print('无效的选择，请重新选择')

