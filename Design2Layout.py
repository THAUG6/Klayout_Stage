from GratingCouplerClass import GratingCoupler

design = GratingCoupler()

for i in range(3):
    for j in range(3):
        if i == 0:  
            design.grating_coupler(0.6 + (j * 0.1), fill_factor = 0.75, waveguide_width= 1, pos_x=-j * 230, pos_y=-100 * 2 * i, rot=180, wg_length=150)
            design.text("P:" + str(0.6 + (j * 0.1)) + "F:0.75", size=25, position=(j * 230 - 50, 50))
        if i == 1:
            design.grating_coupler(period = 0.9 + (j * 0.1), fill_factor = 0.75, waveguide_width= 1, pos_x=-j * 230, pos_y=-100 * 2 * i, rot=180, wg_length=150)
            design.text("P:" + str(0.9 + (j * 0.1)) + "F:0.75", size=25, position=(j * 230 - 50, 50 - 100 * 2))
        if i == 2:
            design.grating_coupler(period = 1.2 + (j * 0.1), fill_factor = 0.75, waveguide_width= 1, pos_x=-j * 230, pos_y=-100 * 2 * i, rot=180, wg_length=150)
            design.text("P:" + str(1.2 + (j * 0.1)) + "F:0.75", size=25, position=(j * 230 - 50, 50 - 100 * 4))

for i in range(3):
    for j in range(3):
        if i == 0:
            design.grating_coupler(period = 1.108, fill_factor = 0.4 + (j * 0.05), waveguide_width= 1, pos_x=-j * 230, pos_y=-100 * 2 * i - 100 * 6, rot=180, wg_length=150)
            design.text("P:1.1F:" + str(0.4 + (j * 0.05)), size=25, position=(j * 230 - 50, 50 - 100 * 6))
        if i == 1:
            design.grating_coupler(period = 1.108, fill_factor = 0.55 + (j * 0.05), waveguide_width= 1, pos_x=-j * 230, pos_y=-100 * 2 * i - 100 * 6, rot=180, wg_length=150)
            design.text("P:1.1F:" + "{:.2f}".format(0.55 + (j * 0.05)), size=25, position=(j * 230 - 50, 50 - 100 * 8))
        if i == 2:
            design.grating_coupler(period = 1.108, fill_factor = 0.7 + (j * 0.05), waveguide_width= 1, pos_x=-j * 230, pos_y=-100 * i * 2 - 100 * 6, rot=180, wg_length=150)
            design.text("P:1.1F:" + "{:.2f}".format(0.7 + (j * 0.05)), size=25, position=(j * 230 - 50, 50 - 100 * 10))


design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -350 * 3 + 220, pos_y = -16.9 - 80.508 + 40.2, lengthx=25)
design.text("25", size=25, position = (335 * 3 -100, 50))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -350 * 3 + 150, pos_y = -16.9 - 80.508+40.2 + 127 * 2 -65, lengthx=100)
design.text("100", size=25, position = (335 * 3 -120, 50 - 137 * 2))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -350 * 3 + 80, pos_y = -16.9 - 80.508+40.2 + 127 * 4 + 60 - 185, lengthx=175)
design.text("175", size=25, position = (381 * 3 -140, 50 - 127 * 4))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -350 * 3 , pos_y = -16.9 - 80.508+40.2 + 127 * 6 + 60 - 235, lengthx=250)
design.text("250", size=25, position = (381 * 3 -140, 50 - 127 * 6))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -350 * 3 -70, pos_y = -16.9 - 80.508+40.2 + 127 * 8 + 60 - 295, lengthx=325)
design.text("325", size=25, position = (381 * 3 -140, 50 - 127 * 8))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -350 * 3 -140, pos_y = -16.9 - 80.508+40.2 + 127 * 10 + 60 - 335, lengthx=400)
design.text("400", size=25, position = (381 * 3 -140, 50 - 127 * 10))

design.MZI(period=1.108, fill_factor = 0.75, delta=50, x_length=150, pos_x=800 + 361, pos_y = -2.5 * 100 - 30)
design.text("50", size = 25, position = (381 * 3 - 100, 60 - 127 * 10))

design.MZI(period=1.108, fill_factor = 0.75, delta=100, x_length=150, pos_x=750 + 361, pos_y = -1 * 100 + 15)
design.text("100", size = 25, position = (381 * 3 - 100, 60 - 127 * 10))

design.MZI(period=1.108, fill_factor = 0.75, delta=150, x_length=150, pos_x=1050, pos_y = 100)
design.text("150", size = 25, position = (381 * 3 - 100, 200))

design.write_gds("Klayout_Grating_Coupler2")