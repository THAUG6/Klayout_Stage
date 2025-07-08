from GratingCouplerClass import GratingCoupler

design = GratingCoupler()

for i in range(3):
    for j in range(3):
        if i == 0:
            design.grating_coupler(period = 0.6 + (j * 0.1), fill_factor = 0.75, waveguide_width= 1, pos_x=-j * 381, pos_y=-127 * 2 * i, rot=180, wg_length=200)
            design.text("P: " + str(0.6 + (j * 0.1)) + "  FF: 0.75", size=25, position=(j * 375 - 70, 50))
        if i == 1:
            design.grating_coupler(period = 0.9 + (j * 0.1), fill_factor = 0.75, waveguide_width= 1, pos_x=-j * 381, pos_y=-127 * 2 * i, rot=180, wg_length=200)
            design.text("P: " + str(0.9 + (j * 0.1)) + "  FF: 0.75", size=25, position=(j * 375 - 70, 50 - 127 * 2))
        if i == 2:
            design.grating_coupler(period = 1.2 + (j * 0.1), fill_factor = 0.75, waveguide_width= 1, pos_x=-j * 381, pos_y=-127 * 2 * i, rot=180, wg_length=200)
            design.text("P: " + str(1.2 + (j * 0.1)) + "  FF: 0.75", size=25, position=(j * 375 - 70, 50 - 127 * 4))

for i in range(3):
    for j in range(3):
        if i == 0:
            design.grating_coupler(period = 1.108, fill_factor = 0.4 + (j * 0.05), waveguide_width= 1, pos_x=-j * 381, pos_y=-127 * 2 * i - 127 * 6, rot=180, wg_length=200)
            design.text("P: 1.108  FF: " + str(0.4 + (j * 0.05)), size=25, position=(j * 375 - 90, 50 - 127 * 6))
        if i == 1:
            design.grating_coupler(period = 1.108, fill_factor = 0.55 + (j * 0.05), waveguide_width= 1, pos_x=-j * 381, pos_y=-127 * 2 * i - 127 * 6, rot=180, wg_length=200)
            design.text("P: 1.108  FF: " + "{:.2f}".format(0.55 + (j * 0.05)), size=25, position=(j * 375 - 90, 50 - 127 * 8))
        if i == 2:
            design.grating_coupler(period = 1.108, fill_factor = 0.7 + (j * 0.05), waveguide_width= 1, pos_x=-j * 381, pos_y=-127 * i * 2 - 127 * 6, rot=180, wg_length=200)
            design.text("P: 1.108  FF: " + "{:.2f}".format(0.7 + (j * 0.05)), size=25, position=(j * 375 - 90, 50 - 127 * 10))


design.snake(period=1.108, fill_factor=0.75, number_of_loops = 6, pos_x = -381 * 3 - 100, pos_y = -16.9 - 80.508 + 40.2, lengthx=25)
design.text("L: 25", size=25, position = (381 * 3 -100, 50))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 6, pos_x = -381 * 3 - 123.2 - 50, pos_y = -16.9 - 80.508+40.2 + 127 * 2, lengthx=100)
design.text("L: 100", size=25, position = (381 * 3 -120, 50 - 127 * 2))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 6, pos_x = -381 * 3 - 123.2 -100, pos_y = -16.9 - 80.508+40.2 + 127 * 4, lengthx=175)
design.text("L: 175", size=25, position = (381 * 3 -140, 50 - 127 * 4))

design.MZI(period=1.108, fill_factor = 0.75, delta=50, x_length=150, pos_x=800 + 361, pos_y = -5 * 127)
design.text("D: 50", size = 25, position = (381 * 3 - 100, 60 - 127 * 6))

design.MZI(period=1.108, fill_factor = 0.75, delta=100, x_length=150, pos_x=800 + 361, pos_y = -7 * 127)
design.text("D: 100", size = 25, position = (381 * 3 - 100, 60 - 127 * 8))

design.MZI(period=1.108, fill_factor = 0.75, delta=150, x_length=150, pos_x=800 + 361, pos_y = -9 * 127)
design.text("D: 150", size = 25, position = (381 * 3 - 100, 60 - 127 * 10))

design.write_gds("Klayout_Grating_Coupler")

