# 购物车自身
class ShoppingCart:
    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.number = number
    def __str__(self):
        return f"商品名称为:{self.name}, 商品价格为:{self.price}, 商品数量为:{self.number}"
    # 更新购物车
    def update_cart(self, name = None, price = None, number = None):
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if number is not None:
            self.number = number
# 购物车管理系统
class CartManagement:
    def __init__(self):
        self.cart_list = [] # 购物车列表
    # 添加购物车
    def add_cart(self):
        name = input("请输入商品名称: ")
        for s in self.cart_list:
            if s.name == name:
                print("商品已存在")
                return
        price = int(input("请输入商品价格: "))
        number = int(input("请输入商品数量: "))
        # 判断价格和数量是否大于零
        if not (price > 0 and number > 0):
            print("输入错误,请重新输入")
        else:
            item = ShoppingCart(name, price, number)
            self.cart_list.append(item)
    def update_cart(self):
        name = input("请输入要修改的商品名称: ")
        for s in self.cart_list:
            if s.name == name:
                print(f"当前信息为:{s}")
                price = int(input("请输入修改后的价格: "))
                number = int(input("请输入修改后的数量: "))
                if not price > 0 and number > 0:
                    print("价格和数量必须大于零")
                    return
                else:
                    s.update_cart(name, price, number)
                    print("修改成功")
                    print(f"修改后的数据为{s}")
                    return
        print("修改失败, 不存在此商品")
   # 删除购物车
    def delete_cart(self):
        name = input("请输入要删除的商品的名称: ")
        for s in self.cart_list:
            if s.name == name:
                self.cart_list.remove(s)
                print("删除成功")
                return
    # 查询购物车
    def search_cart(self):
        for s in self.cart_list:
            print(s)

    def run(self):
        print("欢迎来到购物车系统~:")
        while True:
            print("1. 添加购物车")
            print("2. 修改购物车")
            print("3. 删除购物车")
            print("4. 查询购物车")
            print("5. 退出购物车")
            choice = int(input("请输入你的操作: "))
            match choice:
                case 1:
                    self.add_cart()
                case 2:
                    self.update_cart()
                case 3:
                    self.delete_cart()
                case 4:
                    self.search_cart()
                case 5:
                    print("欢迎再次使用")
                    break
                case _:
                    print("无效指令")

# 测试
if __name__ == "__main__":
    cart = CartManagement()
    cart.run()