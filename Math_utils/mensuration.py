from shapes import Circle, Triangle, Rectangle, Cylinder, Cone, Sphere


def shape_properties(shape_property, shape):
    if shape_property.lower() == Shapes.Properties.AREA:
        print(f"Area = {shape.area()}\n")
    elif shape_property.lower() == Shapes.Properties.PERIMETER:
        print(f"Perimeter = {shape.perimeter()}\n")
    elif shape_property.lower() == Shapes.Properties.VOLUME:
        print(f"Volume = {shape.volume()}\n")
    elif shape_property.lower() == Shapes.Properties.SLANT_HEIGHT:
        print(f"Slant height = {shape.calculate_slant_height()}\n")
    else:
        return False
    return True


class Shapes:
    '''Defining constants for various shapes'''
    GO_BACK = 0
    CIRCLE = 1
    TRIANGLE = 2
    RECTANGLE = 3
    CONE = 4
    CYLINDER = 5
    SPHERE = 6

    class Properties:
        AREA = 'a'
        PERIMETER = 'p'
        VOLUME = 'v'
        SLANT_HEIGHT = 's'

    def menu():
        print("""\nSelect Shape...\n
\t1 -> Circle
\t2 -> Triangle
\t3 -> Rectangle
\t4 -> Cone
\t5 -> Cylinder
\t6 -> Sphare
\t0 -> Back to 'Home Menu'""")
        option = int(input("\t->> "))
        return option


class Mensuration:
    def __init__(self):
        self.__shape = None
        self.__show__operations_menu = True

    def set_shape(self, new_shape):
        self.__shape = new_shape

    def perform_operation(self):
        while self.__show__operations_menu:
            shape = Shapes.menu()  # render shapes menu
            show_properties_menu = True

            if shape == Shapes.GO_BACK:
                self.__show__operations_menu = False

            elif shape == Shapes.CIRCLE:
                radius = int(input("Enter radius: "))
                circle = Circle(radius)
                while show_properties_menu:
                    shape_property = circle.properties_menu()
                    show_properties_menu = shape_properties(shape_property, circle)

            elif shape == Shapes.TRIANGLE:
                print("Enter side1, side2, side3(space separated):")
                sides = map(int, input().split())
                triangle = Triangle(*sides)  # unpacking sides -> side1, side2, side 3

                if triangle.is_possible():
                    while show_properties_menu:
                        shape_property = triangle.properties_menu()
                        show_properties_menu = shape_properties(shape_property, triangle)
                else:
                    print("Invalid Triangle")

            elif shape == Shapes.RECTANGLE:
                print("Enter length, width(space separated):")
                sides = map(int, input().split())
                rectangle = Rectangle(*sides)

                while show_properties_menu:
                    shape_property = rectangle.properties_menu()
                    show_properties_menu = shape_properties(shape_property, rectangle)

            elif shape == Shapes.CYLINDER:
                print("Enter radius, height(space separated):")
                sides = map(int, input().split())
                cylinder = Cylinder(*sides)

                while show_properties_menu:
                    shape_property = cylinder.properties_menu()
                    show_properties_menu = shape_properties(shape_property, cylinder)

            elif shape == Shapes.CONE:
                print("Enter radius, height(space separated):")
                sides = map(int, input().split())
                cone = Cone(*sides)

                while show_properties_menu:
                    shape_property = cone.properties_menu()
                    show_properties_menu = shape_properties(shape_property, cone)

            elif shape == Shapes.SPHERE:
                sides = int(input("Enter radius:"))
                sphere = Sphere(sides)

                while show_properties_menu:
                    shape_property = sphere.properties_menu()
                    show_properties_menu = shape_properties(shape_property, sphere)
