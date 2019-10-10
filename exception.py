from point import Point

def move_it(point):
    point.move(1, 2)

def main():
    p = Point("10", "20")
    move_it(p)

main()
