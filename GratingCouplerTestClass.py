import gdsfactory as gf
import numpy as np
from gdsfactory.generic_tech import get_generic_pdk



#Class to test grating couplers
class GratingCouplerTest():

    #Initialize Components and pdk
    def __init__(self):
        self.c = gf.Component()
        PDK = get_generic_pdk()
        PDK.activate()

    #Select KLayout file used for drawing 
    def write_gds(self, filename):
        self.filename = filename
        self.c.write_gds(filename + ".gds")


    #Draws C-Shape, with two grating couplers
    def CSHAPE(self, period, fill_factor, waveguide_width, pos_x, pos_y, rot, wg_length):

        #C-shape design parameters
        self.period = period #Period of the grating
        self.fill_factor = fill_factor #Fill-Factor (Duty-Cycle) of the grating
        self.waveguide_width = waveguide_width #Waveguide width at the end of the taper
        self.pos_x = pos_x # x position in .gds file
        self.pos_y = pos_y # y position in .gds file
        self.rot = rot # Rotation of the grating coupler (0: Input from right to left, 180: Input from left to right)
        self.wg_length = wg_length #Length of the waveguide after grating coupler

        #Creation of waveguides in C-Shape
        wg3 = gf.components.straight(length = wg_length, width=waveguide_width)

        #Creation of grating coupler
        gap = period * (1 - fill_factor)
        width = period * fill_factor
        gc = gf.components.grating_coupler_elliptical_arbitrary(
            tuple(gap for _ in range(round(20 / period))),
            tuple(width for _ in range(round(20 / period))),
            polarization="te",
            wavelength=1.55,

            cross_section=gf.cross_section.strip(width=waveguide_width, layer=(1, 0))
        )
        gc_ref = self.c.add_ref(gc)
        gc_ref.move((pos_x, pos_y))
        gc_ref.rotate(rot)
        wg = gf.components.straight(length = wg_length, width=waveguide_width)
        wg_ref = self.c.add_ref(wg)
        wg_ref.move((wg_length, pos_y))
        wg_ref.connect("o2", gc_ref.ports["o1"])
        upArc = gf.path.arc(radius=5, angle=90)
        upArc_shape = upArc.extrude(width = waveguide_width, layer=(1, 0))
        upArc_ref = self.c.add_ref(upArc_shape)
        upArc_ref.rotate(0)
        upArc_ref.move((-pos_x + wg_length, pos_y))
        wg2 = gf.components.straight(length=117, width=waveguide_width)
        wg_ref2 = self.c.add_ref(wg2)
        wg_ref2.rotate(90)
        wg_ref2.connect("o1", upArc_ref.ports["o2"])
        wg_ref.connect("o1", upArc_ref.ports["o1"])
        gc_ref.connect("o1", wg_ref.ports["o2"])
        downArc = gf.path.arc(radius= 5, angle=-90)
        downArc_shape = downArc.extrude(width = waveguide_width, layer=(1, 0))
        downArc_ref = self.c.add_ref(downArc_shape)
        downArc_ref.move((pos_x + wg_length, pos_y - 127))
        downArc_ref.rotate(0)
        downArc_ref.connect("o2", wg_ref2.ports["o2"])
        gc2 = gf.components.grating_coupler_elliptical_arbitrary(
        tuple(gap for _ in range(round(20 / period))),
        tuple(width for _ in range(round(20 / period))),
        polarization="te",
        wavelength=1.55,

        cross_section=gf.cross_section.strip(width=waveguide_width, layer=(1, 0))
        )
        gc2_ref = self.c.add_ref(gc2)
        gc2_ref.move((pos_x, pos_y - 127))
        gc2_ref.rotate(rot)
        wg_ref3 = self.c.add_ref(wg3)
        wg_ref3.move((wg_length, pos_y))
        wg_ref3.connect("o1", downArc_ref.ports["o1"])
        gc2_ref.connect("o1", wg_ref3.ports["o2"])


    #Function for drawing spiral, with two grating couplers
    def spiral(self, period, fill_factor, number_of_loops, pos_x, pos_y, lengthx):
        #Spiral parameters
        self.period, self.fill_factor, self.number_of_loops = period, fill_factor, number_of_loops
        self.pos_x, self.pos_y = pos_x, pos_y
        self.lengthx = lengthx

        #Creation of spiral
        snake = gf.components.spiral(length = lengthx, spacing=6, bend="bend_euler", n_loops = number_of_loops, cross_section=gf.cross_section.strip(width=1, layer=(1, 0)))
        snake_ref = self.c.add_ref(snake)
        snake_ref.move((pos_x, pos_y))
        snake_ref.rotate(180)

        #Creation of grating coupler
        gap = period * (1 - fill_factor)
        width = period * fill_factor
        gc = gf.components.grating_coupler_elliptical_arbitrary(
            tuple(gap for _ in range(round(20 / period))),
            tuple(width for _ in range(round(20 / period))),
            polarization="te",
            wavelength=1.55,

            cross_section=gf.cross_section.strip(width=1, layer=(1, 0))
        )
        wgplus = gf.components.straight(length=50, width=1)
        wgplus_ref = self.c.add_ref(wgplus)
        wgplus_ref.connect("o2", snake_ref.ports["o2"])
        gc_ref = self.c.add_ref(gc)
        gc_ref.move((pos_x, pos_y))
        gc_ref.rotate(180)
        gc_ref.connect("o1", wgplus_ref.ports["o1"])

        arcdown = gf.path.arc(radius=10, angle=-90)
        arcdown_shape = arcdown.extrude(width=1, layer=(1, 0))
        arcdown_ref = self.c.add_ref(arcdown_shape)
        arcdown_ref.connect("o2", snake_ref.ports["o1"])

        wgdown = gf.components.straight(length=97, width=1)
        wgdown_ref = self.c.add_ref(wgdown)
        wgdown_ref.rotate(90)
        wgdown_ref.connect("o1", arcdown_ref.ports["o1"])


        arcup = gf.path.arc(radius=10, angle=90)
        arcup_shape = arcup.extrude(width=1, layer=(1, 0))
        arcup_ref = self.c.add_ref(arcup_shape)  
        arcup_ref.connect("o2", wgdown_ref.ports["o2"])

        wgminus = gf.components.straight(length=36, width=1)
        wgminus_ref = self.c.add_ref(wgminus)
        wgminus_ref.connect("o1", arcup_ref.ports["o1"])

        gc2 = gf.components.grating_coupler_elliptical_arbitrary(
            tuple(gap for _ in range(round(20 / period))),
            tuple(width for _ in range(round(20 / period))),
            polarization="te",
            wavelength=1.55,
            cross_section=gf.cross_section.strip(width=1, layer=(1, 0))
        )
        gc2_ref = self.c.add_ref(gc2)
        gc2_ref.connect("o1", wgminus_ref.ports["o2"])
        snake_ref.flatten()

    #Creation of text layer in Klayout drawing
    def text(self, texts, size, position):
        self.texts = texts
        self.size = size
        self.position = position
        self.text_component = gf.components.text(text=texts, size=size, position=position, justify='left', layer=(2, 0))
        self.text_ref = self.c.add_ref(self.text_component)
        return self.text_ref
    
    #Creation of MZIs in Klayout drawing
    def MZI(self, period, fill_factor, delta, x_length, pos_x, pos_y):
        self.period = period #Period of grating
        self.fill_factor = fill_factor #Fill factor of grating
        self.xlength = x_length #x length of MZI's arms
        self.pos_x, self.pos_y = pos_x, pos_y #Position of MZI
        self.delta = delta  # Length difference betweem the two arms
        mzi = gf.components.mzi(delta_length=delta, length_y=0.1, length_x=x_length, bend='bend_euler', straight='straight', splitter=self.mmi1x2_custom(), with_splitter=True, port_e1_splitter='o2', port_e0_splitter='o3', port_e1_combiner='o2', port_e0_combiner='o3', port1='o1', port2='o2', nbends=2, cross_section=gf.cross_section.strip(width = 1), cross_section_x_bot=gf.cross_section.strip(width = 1),cross_section_x_top=gf.cross_section.strip(width = 1), mirror_bot=False, add_optical_ports_arms=False, min_length=0.01, auto_rename_ports=True).copy()
        mzi_ref = self.c.add_ref(mzi)
        mzi_ref.move((pos_x, pos_y))

        arcup = gf.path.arc(radius=5, angle=90)
        arcup_shape = arcup.extrude(width=1, layer=(1, 0))
        arcup_ref = self.c.add_ref(arcup_shape)  
        arcup_ref.connect("o2", mzi_ref.ports["o2"])

        wgminus = gf.components.straight(length=117, width=1)
        wgminus_ref = self.c.add_ref(wgminus)
        wgminus_ref.connect("o1", arcup_ref.ports["o1"])

        arcdown = gf.path.arc(radius=5, angle=-90)
        arcdown_shape = arcdown.extrude(width=1, layer=(1,  0))
        arcdown_ref = self.c.add_ref(arcdown_shape)
        arcdown_ref.connect("o1", wgminus_ref.ports["o2"])

        downwg = gf.components.straight(length=90 + x_length, width=1)
        downwg_ref = self.c.add_ref(downwg)
        downwg_ref.connect("o1", arcdown_ref.ports["o2"])

        gap = period * (1 - fill_factor)
        width = period * fill_factor

        gc = gf.components.grating_coupler_elliptical_arbitrary(
            tuple(gap for _ in range(round(20 / period))),
            tuple(width for _ in range(round(20 / period))),
            polarization="te",
            wavelength=1.55,
            cross_section=gf.cross_section.strip(width=1, layer=(1, 0))
        )
        gc_ref = self.c.add_ref(gc)
        gc_ref.rotate(180)
        gc_ref.connect("o1", downwg_ref.ports["o2"])

        gc2 = gf.components.grating_coupler_elliptical_arbitrary(
        tuple(gap for _ in range(round(20 / period))),
        tuple(width for _ in range(round(20 / period))),
        polarization="te",
        wavelength=1.55,
        cross_section=gf.cross_section.strip(width=1, layer=(1, 0))
        )
        gc2_ref = self.c.add_ref(gc2)
        gc2_ref.rotate(180)
        gc2_ref.connect("o1", mzi_ref.ports["o1"])
        mzi.flatten()
    
    #Creation of MZI splitter shape
    def mmi1x2_custom(self):
        return gf.components.mmi1x2(
            width=1.0,  
            width_taper=1.0,  
            cross_section=gf.cross_section.strip(width=1.0)
    )








