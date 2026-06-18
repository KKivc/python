from EduManagement import Student, StudentManagement

m = StudentManagement()
m.students.append(Student('张三', 80, 90, 85))
m.students.append(Student('李四', 70, 75, 72))

# 测试 find_student
assert m.find_student('张三') != 0, '应该找到张三'
assert m.find_student('王五') == 0, '不应该找到王五'

# 测试修改
s = m.find_student('张三')
s.chinese = 95
assert m.students[0].chinese == 95

# 测试删除
s = m.find_student('李四')
m.students.remove(s)
assert len(m.students) == 1

# 测试 __str__
assert '张三' in str(m.students[0])

print('CI 测试全部通过!')
