shopping_cart = {}

menu = '''
########## 购物车系统 ##########
#        1. 添加购物车         #
#        2. 修改购物车         #
#        3. 删除购物车         #
#        4. 查询购物车         #
#        5. 退出购物车         #
################################
'''
while True:
    print(menu)
    choice = input('请选择操作: ')
    match choice:
        case '1':
            goods_name = input('请输入商品名称: ')

            if goods_name in shopping_cart:
                print('该商品已存在，请重新选择')
            else:
                goods_price = float(input('请输入商品价格: '))
                goods_num = int(input('请输入商品数量: '))
                shopping_cart[goods_name] = {
                    'price': goods_price,
                    'num': goods_num
                }
                print('商品添加成功')
        case '2':
            goods_name = input('请输入要修改的商品名称: ')

            if goods_name in shopping_cart:
                goods_price = float(input('请输入新的商品价格: '))
                goods_num = int(input('请输入新的商品数量: '))
                shopping_cart[goods_name] = {
                    'price': goods_price,
                    'num': goods_num
                }
                print('商品修改成功')
            else:
                print('该商品不存在，请重新选择')
        case '3':
            goods_name = input('请输入要删除的商品名称: ')

            if goods_name in shopping_cart:
                del shopping_cart[goods_name]
                print('商品删除成功')
            else:
                print('该商品不存在，请重新选择')
        case '4':
            goods_name = input('请输入要查询的商品名称: ')

            if goods_name in shopping_cart:
                print(f'商品名称: {goods_name}')
                print(f'商品价格: {shopping_cart[goods_name]["price"]}')
                print(f'商品数量：{shopping_cart[goods_name]["num"]}')
            else:
                print('该商品不存在，请重新选择')
        case '5':
            print('退出购物车系统')
            break
        case _:
            print('无效数字，请重新选择')