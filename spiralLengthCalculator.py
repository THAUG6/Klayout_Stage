import numpy as np



def length(center_length, number_of_loops = 10, bend_radius = 10, separation = 6):
    bend_length = bend_radius * np.pi /2
    total_bend_length = bend_length * ((number_of_loops * 4) + 6)
    bottom_one = separation * number_of_loops * 2 + center_length
    
    spiral_length = center_length + 50 + (10 * separation * 2) + center_length + total_bend_length + 36 + 98 + bottom_one
    for i in range(number_of_loops):
        print(i)
        #top side
        spiral_length += (i * 2  * separation) + 20 + separation + center_length
        #Bottom side
        spiral_length += (i * 2 * separation) + 20 + separation + center_length
        #Left and right side
        spiral_length += (separation + (i * 2 * separation)) * 2

    return spiral_length



print(length(900))






