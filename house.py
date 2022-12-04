class furniture():
    def __init__(self, item, area):
        self.item = item
        self.area = area

    def __str__(self):
        return "%s covers %.2f square meter" % (self.item, self.area)

bed = furniture("席梦思", 4)
chest = furniture("衣柜", 2)
table = furniture("餐桌", 1.5)

print(bed)
print(chest)
print(table)

class House():
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型: %s \n 总面积: %.2f[剩余: %.2f]\n家具: %s"
                % (self.house_type,
                   self.area,
                   self.free_area,
                   self.item_list))

    def add_item(self, item):

        print("要添加 %s" % item)
        # 1. 判断家具面积是否大于剩余面积
        if self.free_area < item.area:
            return

        # 2. 将家具的名称追加到名称列表中
        self.item_list.append(item)


        # 3. 计算剩余面积
        self.free_area -= item.area


my_home = House("两室一厅", 60)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)





