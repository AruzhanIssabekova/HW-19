# class Device:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def vkl(self):
#         print(f"{self.brand} {self.model} включен.")
#
#     def vikl(self):
#         print(f"{self.brand} {self.model} включен.")
#
# class CoffeeMachine(Device):
#     def __init__(self, brand, model, coffee_type):
#         super().__init__(brand, model)
#         self.coffee_type = coffee_type
#
#     def make_coffee(self):
#         print(f"{self.brand} {self.model} сделал {self.coffee_type}.")
# class Blender(Device):
#     def __init__(self, brand, model, speed_levels):
#         super().__init__(brand, model)
#         self.speed_levels = speed_levels
#
#     def blend(self):
#         print(f"{self.brand} {self.model} перемашивает со скоростью {self.speed_levels}.")
#
# class MeatGrinder(Device):
#     def __init__(self, brand, model, power):
#         super().__init__(brand, model)
#         self.power = power
#
#     def grind_meat(self):
#         print(f"{self.brand} {self.model} рубит мясо с мощьностью {self.power}.")






# class Ship:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#     def start(self):
#         print(f"{self.name} начала движение.")
#
#     def stop(self):
#         print(f"{self.name} закончила движение.")
#
# class Frigate(Ship):
#     def __init__(self, name, weight, kol_orudi):
#         super().__init__(name, weight)
#         self.kol_orudi = kol_orudi
#
#     def ogon(self):
#         print(f"{self.name} начал огонь из {self.kol_orudi} орудий.")
#
# class Destroyer(Ship):
#     def __int__(self, name, weight, kol_torped):
#         super().__init__((name, weight))
#         self.kol_torped = kol_torped
#
#     def zapusk(self):
#         print(f"{self.name} запуск {self.kol_torped} торпед.")
#
# class Cruiser(Ship):
#     def __init__(self, name, weight, kol_celei):
#         super().__init__(name, weight)
#         self.kol_celei = kol_celei
#
#     def porazhenie(self):
#         print(f"{self.name} поразил {self.kol_celei} целей.")




# class Square:
#     def __init__(self, side_length):
#         self.side_length = side_length
#
#     def calculate_area(self):
#         return self.side_length ** 2
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return 3.14 * self.radius ** 2
#
# class InscribedCircleInSquare(Square, Circle):
#     def __init__(self, side_length):
#         Square.__init__(self, side_length)
#         Circle.__init__(self, side_length/2)
#
#     def calculate_area(self):
#         return Circle.calculate_area(self)


# class Wheels:
#     def __init__(self, number_of_wheels):
#         self.number_of_wheels = number_of_wheels
#     def rotate(self):
#         print("Колеса крутятся.")
#
#
# class Engine:
#     def __init__(self, fuel_type):
#         self.fuel_type = fuel_type
#     def start(self):
#         print(f"Двигатель запускается. Тип топлива:{self.fuel_type}")
#     def stop(self):
#         print("Двигатель останавливается.")
#
#
# class Doors:
#     def __init__(self, number_of_doors):
#         self.number_of_doors = number_of_doors
#     def open(self):
#         print("Двери открываются.")
#     def close(self):
#         print("Двери закрываются.")
#
#
# class Car(Wheels, Engine, Doors):
#     def __init__(self, brand, model, fuel_type, number_of_doors, number_of_wheels):
#         Wheels.__init__(self, number_of_wheels)
#         Engine.__init__(self, fuel_type)
#         Doors.__init__(self, number_of_doors)
#         self.brand = brand
#         self.model = model
#     def drive(self):
#         print(f"{self.brand} {self.model} едет.")




import json
class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type
    def show(self):
        print(f"Shape Type: {self.shape_type}")
    def save(self, file):
        with open(file, 'w') as file:
            json.dump(self.__dict__, file)
    @staticmethod
    def load(file, shape_type=None):
        with open(file, 'r') as file:
            data = json.load(file)
            shape_type = shape_type or data.get('shape_type')
            if shape_type == 'Square':
                return Square(**data)
            elif shape_type == 'Rectangle':
                return Rectangle(**data)
            elif shape_type == 'Circle':
                return Circle(**data)
            elif shape_type == 'Ellipse':
                return Ellipse(**data)
class Square(Shape):
    def __init__(self, left_top_x, left_top_y, side_length):
        super().__init__('Square')
        self.left_top_x = left_top_x
        self.left_top_y = left_top_y
        self.side_length = side_length
    def show(self):
        super().show()
        print(f"Координаты верхнего левого угла: ({self.left_top_x}, {self.left_top_y})")
        print(f"Длина стороны: {self.side_length}")
class Rectangle(Shape):
    def __init__(self, left_top_x, left_top_y, width, height):
        super().__init__('Rectangle')
        self.left_top_x = left_top_x
        self.left_top_y = left_top_y
        self.width = width
        self.height = height
    def show(self):
        super().show()
        print(f"Координаты верхнего левого угла: ({self.left_top_x}, {self.left_top_y})")
        print(f"Ширина: {self.width}, Высота: {self.height}")
class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        super().__init__('Circle')
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
    def show(self):
        super().show()
        print(f"Координаты центра: ({self.center_x}, {self.center_y})")
        print(f"Радиус: {self.radius}")

class Ellipse(Shape):
    def __init__(self, top_left_x, top_left_y, width, height):
        super().__init__('Ellipse')
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.width = width
        self.height = height
    def show(self):
        super().show()
        print(f"Координаты верхнего угла, описанного вокруг него прямоугольника со сторонами, параллельными осям координат: ({self.top_left_x}, {self.top_left_y})")
        print(f"Ширина: {self.width}, Высота: {self.height}")

shapes = [Square(0, 0, 8), Rectangle(0, 0, 6, 4), Circle(0, 0, 8), Ellipse(0, 0, 6, 4)]

for i, shape in enumerate(shapes):
    shape.save(f'shape_{i}.json')

loaded_shapes = [Shape.load(f'shape_{i}.json', shape_type=shape.__class__.__name__) for i, shape in enumerate(shapes)]

for shape in loaded_shapes:
    shape.show()
    print()