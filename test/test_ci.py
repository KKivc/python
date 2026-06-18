from EduManagement import Student, StudentManagement

m = StudentManagement()
# 添加
m.add_student('tt', 55, 65, 78)

s = m.find_student('tt')

# 验证存在
assert s != 0

# 验证同名
m.add_student('tt', 55, 65, 78)

s = m.find_student('tt')

assert s != 0

# 修改
m.modify_student('tt', 98,67, 87)
s = m.find_student('tt')
assert s.chinese == 98 and s.math == 67 and s.english == 87

# 删除
m.del_student('tt')
s = m.find_student('tt')
assert s == 0

# 不存在
s = m.find_student('uu')
assert s == 0