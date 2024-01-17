height_of_house = float(input())
length_of_side_wall = float(input())
height_of_triangle_wall_of_roof = float(input())

green_paint = 3.4
red_paint = 4.3

front_and_rear_wall_area = height_of_house * height_of_house
front_door_area = 1.2 * 2.00
total_area_front_and_rear_walls = front_and_rear_wall_area * 2 - front_door_area
side_walls_area = height_of_house * length_of_side_wall
window_area = 1.5 * 1.5
total_are_side_walls = side_walls_area * 2 - window_area * 2
total_area_walls = total_area_front_and_rear_walls + total_are_side_walls
needed_paint_walls = total_area_walls / green_paint

rectangle_area_roof = height_of_house * length_of_side_wall
total_rectangle_area = rectangle_area_roof * 2
triangle_area_roof = (height_of_house * height_of_triangle_wall_of_roof) / 2
total_triangle_area = triangle_area_roof * 2
total_area_roof = total_rectangle_area + total_triangle_area
needed_paint_roof = total_area_roof / red_paint

print(f'{needed_paint_walls:.2f}')
print(f'{needed_paint_roof:.2f}')