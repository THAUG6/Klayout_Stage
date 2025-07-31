from GratingCouplerClass import GratingCoupler

#KLayout design for testing grating couplers with different parameters


design = GratingCoupler()


#Period: 0.6 t0 1.2, Fill Factor: 0.75
for i in range(3):
    for j in range(3):
        if i == 0:  
            design.grating_coupler(0.6 + (j * 0.1), fill_factor = 0.75, waveguide_width= 1, pos_x=-j * 270, pos_y=-100 * 2 * i, rot=180, wg_length=150)
            design.text("P:" + str(0.6 + (j * 0.1)) + "F:0.75", size=25, position=(j * 270 - 50, 50))
        if i == 1:
            design.grating_coupler(period = 0.9 + (j * 0.1), fill_factor = 0.75, waveguide_width= 1, pos_x=-j * 270, pos_y=-100 * 2 * i, rot=180, wg_length=150)
            design.text("P:" + str(0.9 + (j * 0.1)) + "F:0.75", size=25, position=(j * 270 - 50, 50 - 100 * 2))
        if i == 2:
            design.grating_coupler(period = 1.2 + (j * 0.1), fill_factor = 0.75, waveguide_width= 1, pos_x=-j * 270, pos_y=-100 * 2 * i, rot=180, wg_length=150)
            design.text("P:" + str(1.2 + (j * 0.1)) + "F:0.75", size=25, position=(j * 270 - 50, 50 - 100 * 4))

#Period: 1.108, Fill Factor: 0.4 to 0.8
for i in range(3):
    for j in range(3):
        if i == 0:
            design.grating_coupler(period = 1.108, fill_factor = 0.4 + (j * 0.05), waveguide_width= 1, pos_x=-j * 270, pos_y=-100 * 2 * i - 100 * 6, rot=180, wg_length=150)
            design.text("P:1.1F:" + str(0.4 + (j * 0.05)), size=25, position=(j * 270 - 50, 50 - 100 * 6))
        if i == 1:
            design.grating_coupler(period = 1.108, fill_factor = 0.55 + (j * 0.05), waveguide_width= 1, pos_x=-j * 270, pos_y=-100 * 2 * i - 100 * 6, rot=180, wg_length=150)
            design.text("P:1.1F:" + "{:.2f}".format(0.55 + (j * 0.05)), size=25, position=(j * 270 - 50, 50 - 100 * 8))
        if i == 2:
            design.grating_coupler(period = 1.108, fill_factor = 0.7 + (j * 0.05), waveguide_width= 1, pos_x=-j * 270, pos_y=-100 * i * 2 - 100 * 6, rot=180, wg_length=150)
            design.text("P:1.1F:" + "{:.2f}".format(0.7 + (j * 0.05)), size=25, position=(j * 270 - 50, 50 - 100 * 10))

#Period: 1, Fill Factor: 0.4 to 0.8
for i in range(3):
    for j in range(3):
        if i == 0:
            design.grating_coupler(period = 1, fill_factor = 0.4 + (j * 0.05), waveguide_width = 1, pos_x = -j * 270 - 3 * 270, pos_y = -100 * 2 * i, rot=180, wg_length = 150)
            design.text("P:1.0F:" + str(0.4 + (j * 0.05)), size=25, position=(j * 270 - 50 + 270 * 3, 50 - 100 * 0))
        if i == 1:
            design.grating_coupler(period = 1, fill_factor = 0.55 + (j * 0.05), waveguide_width = 1, pos_x = -j * 270 - 3 * 270, pos_y = -100 * 2 * i , rot=180, wg_length = 150)
            design.text("P:1.0F:" + "{:.2f}".format(0.55 + (j * 0.05)), size=25, position=(j * 270 - 50 + 270 * 3, 50 - 100 * 2))

        if i == 2:
            design.grating_coupler(period = 1, fill_factor = 0.7 + (j * 0.05), waveguide_width = 1, pos_x = -j * 270 - 3 * 270, pos_y = -100 * i * 2, rot=180, wg_length = 150)
            design.text("P:1.0F:" + "{:.2f}".format(0.7 + (j * 0.05)), size=25, position=(j * 270 - 50 + 270 * 3, 50 - 100 * 4))


for i in range(3):
    for j in range(3):
        if i == 0:
            design.grating_coupler(period = 1, fill_factor = 0.4 + (j * 0.05), waveguide_width = 1, pos_x = -j * 270 - 3 * 270, pos_y = -100 * 2 * i, rot=180, wg_length = 150)
            design.text("P:1.0F:" + str(0.4 + (j * 0.05)), size=25, position=(j * 270 - 50 + 270 * 3, 50 - 100 * 0))
        if i == 1:
            design.grating_coupler(period = 1, fill_factor = 0.55 + (j * 0.05), waveguide_width = 1, pos_x = -j * 270 - 3 * 270, pos_y = -100 * 2 * i , rot=180, wg_length = 150)
            design.text("P:1.0F:" + "{:.2f}".format(0.55 + (j * 0.05)), size=25, position=(j * 270 - 50 + 270 * 3, 50 - 100 * 2))

        if i == 2:
            design.grating_coupler(period = 1, fill_factor = 0.7 + (j * 0.05), waveguide_width = 1, pos_x = -j * 270 - 3 * 270, pos_y = -100 * i * 2, rot=180, wg_length = 150)
            design.text("P:1.0F:" + "{:.2f}".format(0.7 + (j * 0.05)), size=25, position=(j * 270 - 50 + 270 * 3, 50 - 100 * 4))

#P:1.2, FF:0.4 to 0.8
for i in range(3):
    for j in range(3):
        if i == 0:
            design.grating_coupler(period = 1.2, fill_factor = 0.4 + (j * 0.05), waveguide_width = 1, pos_x = -j * 270 - 3 * 270, pos_y = -100 * 2 * i - 600, rot=180, wg_length = 150)
            design.text("P:1.2F:" + str(0.4 + (j * 0.05)), size=25, position=(j * 270 - 50 + 270 * 3, 50 - 100 * 6))
        if i == 1:
            design.grating_coupler(period = 1.2, fill_factor = 0.55 + (j * 0.05), waveguide_width = 1, pos_x = -j * 270 - 3 * 270, pos_y = -100 * 2 * i - 600, rot=180, wg_length = 150)
            design.text("P:1.2F:" + "{:.2f}".format(0.55 + (j * 0.05)), size=25, position=(j * 270 - 50 + 270 * 3, 50 - 100 * 8))

        if i == 2:
            design.grating_coupler(period = 1.2, fill_factor = 0.7 + (j * 0.05), waveguide_width = 1, pos_x = -j * 270 - 3 * 270, pos_y = -100 * i * 2 - 600, rot=180, wg_length = 150)
            design.text("P:1.2F:" + "{:.2f}".format(0.7 + (j * 0.05)), size=25, position=(j * 270 - 50 + 270 * 3, 50 -100*10))

#P:1 to 1.2, FF : 0.75
for i in range(3):
    for j in range(3):
        if i == 0:
            design.grating_coupler(period = 1 + (j * 0.025), fill_factor = 0.75, waveguide_width = 1, pos_x = -j * 270, pos_y = -100 * 2 * i - 1200, rot=180, wg_length = 150)
            design.text(f"P:{1 + (j * 0.025):.2f}F:0.75", size=25, position=(j * 270 - 50, 50 - 100 * 12))
        if i == 1:
            design.grating_coupler(period = 1.05 + (j * 0.025), fill_factor = 0.75, waveguide_width = 1, pos_x = -j * 270, pos_y = -100 * 2 * i - 1200, rot=180, wg_length = 150)
            design.text(f"P:{1.05 + (j * 0.025):.2f}F:0.75", size=25, position=(j * 270 - 50, 50 - 100 * 14))
        if i == 2:
            design.grating_coupler(period = 1.1 + (j * 0.025), fill_factor = 0.75, waveguide_width = 1, pos_x = -j * 270, pos_y = -100 * 2 * i - 1200, rot=180, wg_length = 150)
            design.text(f"P:{1.1 + (j * 0.025):.2f}F:0.75", size=25, position=(j * 270 - 50, 50 - 100 * 16))

#P:0.6 to 1.4, FF: 0.4
for i in range(3):
    for j in range(3):
        if i == 0:
            design.grating_coupler(period = 0.6 + (j * 0.1), fill_factor = 0.4, waveguide_width = 1, pos_x = -j * 270 - 3 * 270, pos_y = -100 * 2 * i - 1200, rot=180, wg_length = 150)
            design.text("P:" + "{:.2f}".format(0.6 + (j * 0.1)) + "F:0.4", size=25, position=(j * 270 - 50 + 270 * 3, 50 - 100 * 12))
        if i == 1:
            design.grating_coupler(period = 0.9 + (j * 0.1), fill_factor = 0.4, waveguide_width = 1, pos_x = -j * 270 - 3 * 270, pos_y = -100 * 2 * i -1200, rot=180, wg_length = 150)
            design.text("P:" + "{:.2f}".format(0.9 + (j * 0.1)) + "F:0.4", size=25, position=(j * 270 - 50 + 270 * 3, 50 -100*14))
        if i == 2:
            design.grating_coupler(period = 1.2 + (j * 0.1), fill_factor = 0.4, waveguide_width = 1, pos_x = -j * 270 -3 *270 , pos_y = -100 * i *2 -1200, rot=180, wg_length =150)
            design.text("P:" + "{:.2f}".format(1.2 + (j * 0.1)) + "F:0.4", size=25, position=(j * 270 -50 +270*3 ,50-100*16))


#P:0.6 to 1.4, FF: 0.8
for i in range(3):
    for j in range(3):
        if i == 0:
            design.grating_coupler(period = 0.6 + (j * 0.1), fill_factor = 0.8, waveguide_width = 1, pos_x = -j * 270 - 3 * 270, pos_y = -100 * 2 * i - 1800, rot=180, wg_length = 150)
            design.text("P:" + "{:.2f}".format(0.6 + (j * 0.1)) + "F:0.8", size=25, position=(j * 270 - 50 + 270 * 3, 50 - 100 * 18))
        if i == 1:
            design.grating_coupler(period = 0.9 + (j * 0.1), fill_factor = 0.8, waveguide_width = 1, pos_x = -j * 270 - 3 * 270, pos_y = -100 * 2 * i -1800, rot=180, wg_length = 150)
            design.text("P:" + "{:.2f}".format(0.9 + (j * 0.1)) + "F:0.8", size=25, position=(j * 270 - 50 + 270 * 3, 50 -100*20))
        if i == 2:
            design.grating_coupler(period = 1.2 + (j * 0.1), fill_factor = 0.8, waveguide_width = 1, pos_x = -j * 270 -3 *270 , pos_y = -100 * i *2 -1800, rot=180, wg_length =150)
            design.text("P:" + "{:.2f}".format(1.2 + (j * 0.1)) + "F:0.8", size=25, position=(j * 270 -50 +270*3 ,50-100*22))


#P:0.6 to 1.4, FF: 0.6
for i in range(3):
    for j in range(3):
        if i == 0:
            design.grating_coupler(period = 0.6 + (j * 0.1), fill_factor = 0.6, waveguide_width = 1, pos_x = -j * 270 - 0 * 270, pos_y = -100 * 2 * i - 1800, rot=180, wg_length = 150)
            design.text("P:" + "{:.2f}".format(0.6 + (j * 0.1)) + "F:0.6", size=25, position=(j * 270 - 50 + 270 * 0, 50 - 100 * 18))
        if i == 1:
            design.grating_coupler(period = 0.9 + (j * 0.1), fill_factor = 0.6, waveguide_width = 1, pos_x = -j * 270 - 0 * 270, pos_y = -100 * 2 * i -1800, rot=180, wg_length = 150)
            design.text("P:" + "{:.2f}".format(0.9 + (j * 0.1)) + "F:0.6", size=25, position=(j * 270 - 50 + 270 * 0, 50 -100*20))
        if i == 2:
            design.grating_coupler(period = 1.2 + (j * 0.1), fill_factor = 0.6, waveguide_width = 1, pos_x = -j * 270 -0 *270 , pos_y = -100 * i *2 -1800, rot=180, wg_length =150)
            design.text("P:" + "{:.2f}".format(1.2 + (j * 0.1)) + "F:0.6", size=25, position=(j * 270 -50 +270*0 ,50-100*22))


design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -230 * 8, pos_y = -16.9 - 80.508 + 40.2, lengthx=100)
design.text("100", size=25, position = (230 * 6.85, 50))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -230 * 8 -50, pos_y = -16.9 - 80.508+40.2 + 127 * 2 -65, lengthx=150)
design.text("150", size=25, position = (230 * 6.85, 50 - 137 * 1.5))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -230 * 8 -100, pos_y = -16.9 - 80.508+40.2 + 127 * 4 +60 - 185, lengthx=200)
design.text("200", size=25, position = (230 * 6.85, 50 - 137 * 3))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -230 * 8 -150, pos_y = -16.9 - 80.508+40.2 + 127 * 6 +60 - 235, lengthx=250)
design.text("250", size=25, position = (230 * 6.85, 50 - 137 * 4))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -230 * 8 -200, pos_y = -16.9 - 80.508+40.2 + 127 * 8 +60 - 295, lengthx=300)
design.text("300", size=25, position = (230 * 6.85, 50 - 137 * 5.5))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -230 * 8 -250, pos_y = -16.9 - 80.508+40.2 + 127 * 10 +60 - 335, lengthx=350)
design.text("350", size=25, position = (230 * 6.85, 50 - 137 * 7))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -230 * 10 -250, pos_y = -16.9 - 80.508 + 40.2, lengthx=400)
design.text("400", size=25, position = (230 * 9 - 100, 50))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -230 * 10 -250 - 100, pos_y = -16.9 - 80.508+40.2 + 127 * 2 -65, lengthx=450)
design.text("450", size=25, position = (230 * 8.65 + 50, 50 - 137 * 1.5))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -230 * 10 -250 -200, pos_y =-16.9 - 80.508+40.2 + 127 * 4 +60 - 185, lengthx=500)
design.text("500", size=25, position = (230 * 8.55 + 100, 50 - 137 * 2.85))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -230 * 10 -250 -300, pos_y =-16.9 - 80.508+40.2 + 127 * 6 + 60 - 235, lengthx=550)
design.text("550", size=25, position = (230 * 8.65 + 150, 50 - 137 * 4.25))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -230 * 10 -250 -400, pos_y =-16.9 - 80.508+40.2 + 127 * 8 +60 - 295, lengthx=600)
design.text("600", size=25, position = (230 * 8.65 + 200, 50 - 137 * 5.75))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -230 * 10 -250 -500, pos_y =-16.9 - 80.508+40.2 + 127 * 10 +60 - 335, lengthx=650)
design.text("650", size=25, position = (230 * 8.65 + 250, 50 - 137 * 7.25))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x =  -230 * 8 - 600, pos_y =-16.9 - 80.508+40.2 + 127 * 12 +60 - 390, lengthx=700)
design.text("700", size=25, position = (230 * 6.85, 50 - 137 * 8.75))

design.snake(period=1.108, fill_factor=0.75, number_of_loops = 10, pos_x = -230 * 8 - 650, pos_y =-16.9 - 80.508+40.2 + 127 * 14 +60 - 450, lengthx=750)
design.text("750", size=25, position = (230 * 6.85, 50 - 137 * 10.25))

design.MZI(period=1.108, fill_factor = 0.75, delta=50, x_length=500, pos_x=230 * 8-200, pos_y = -1475)
design.text("50", size = 25, position = (230 * 8-200 - 35, -1500 - 63))

design.MZI(period=1.108, fill_factor = 0.75, delta=50, x_length=500, pos_x=230 * 8-200, pos_y = -1475)
design.text("50", size = 25, position = (230 * 8-200 - 35, -1500 - 63))

design.MZI(period=1.108, fill_factor = 0.75, delta=100, x_length=500, pos_x=230 * 8-200, pos_y = -1670)
design.text("100", size = 25, position = (230 * 8-200 - 35, -1700 - 63))

design.MZI(period=1.108, fill_factor = 0.75, delta=150, x_length=500, pos_x=230 * 8-200, pos_y = -1870)
design.text("150", size = 25, position = (230 * 8-200 - 45, -1900 - 63))

design.MZI(period=1.108, fill_factor = 0.75, delta=200, x_length=500, pos_x=230 * 8-200, pos_y = -2070)
design.text("200", size = 25, position = (230 * 8-200 - 45, -2100 - 63))


design.MZI(period=1.108, fill_factor = 0.75, delta=25, x_length=500, pos_x=230 * 11-200, pos_y = -1475)
design.text("25", size = 25, position = (230 * 11-200 - 45, -1500 - 63))

design.MZI(period=1.108, fill_factor = 0.75, delta=75, x_length=500, pos_x=230 * 11-200, pos_y = -1670)
design.text("75", size = 25, position = (230 * 11-200 - 45, -1700 - 63))

design.MZI(period=1.108, fill_factor = 0.75, delta=125, x_length=500, pos_x=230 * 11-200, pos_y = -1870)
design.text("125", size = 25, position = (230 * 11-200 - 45, -1900 - 63))

design.MZI(period=1.108, fill_factor = 0.75, delta=175, x_length=500, pos_x=230 * 11-200, pos_y = -2070)
design.text("175", size = 25, position = (230 * 11-200 - 45, -2070 - 63))


"""
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
design.text("150", size = 25, position = (381 * 3 - 100, 200))"""

design.write_gds("Klayout_Grating_Coupler2")