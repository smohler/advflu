from manimlib.imports import *

# To run the code:
# cd.. back into C: drive
# cd manim\manim-master
# To run and produce video
# python -m manim work\animations\advanced_fludis\"file_name.py" Scene -pl

class Lecture2_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture Two')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{The Navier Stokes Equations, pt.2}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

class Lecture2_scene1(Scene):
    def construct(self):
        # what did we do in part one, shout out Dr.Cal
        question = TextMobject('What did we cover last time?')
        question.set_color_by_gradient(BLUE, YELLOW)
        question.shift(2*UP)
        ## list of things
        item1 = TextMobject('Stress Tensor')
        item1.shift(UP)
        item2 = TextMobject('Domain, Coordinates, Boundary')
        item3 = TextMobject('Properties of the Stress Tensor')
        item3.shift(DOWN)
        item4 = TextMobject('Material Derivative')
        item4.shift(2*DOWN)
        # play 
        self.play(Write(question))
        self.play(FadeIn(item1))
        self.play(FadeIn(item2))
        self.play(FadeIn(item3))
        self.play(FadeIn(item4))
        self.wait(3)
        self.play(FadeOut(question), FadeOut(item1), FadeOut(item2), FadeOut(item3), FadeOut(item4))

class Lecture2_scene2(Scene):

    def get_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: np.sin((x+dx)),
            x_min=-4,x_max=4
        )
    
    def construct(self):
        ### Lecture notes 03 pgs. 1
        ### video 02, 7:30

        # better explanation of each later on: motivation for strain tensor
        # lagrangian diagram showing volume being deformed at different times
        # apparently manim coordinate screen is (14.2, 8)
        # start by drawing origin in bottom left
        top = Dot(6.5*LEFT + 2*DOWN)
        zero1 = Dot(6.5*LEFT + 3.1*DOWN)
        zero2 = Dot(6.6*LEFT + 3*DOWN)
        right = Dot(3*DOWN + 5.5*LEFT)
        label = TexMobject(r'\Omega')
        label.next_to(top, RIGHT)
        coordinate = VGroup(Arrow(zero1, top, buff = 0), Arrow(zero2, right, buff = 0), label)
        
        ## double curved arrow to show particle path: play with animation after the fact
        path = self.get_sine_wave()
        cell = Square(side_length = 1, color = BLUE)
        cell.set_fill(BLUE, opacity = 0.3)
        dot = Dot()
        cell_1 = VGroup(cell, dot)

        cell_1.shift(4*RIGHT + 0.75*DOWN)
        cell_2 = cell_1.copy()
        cell_2.center()
        cell_3 = cell_2.copy()
        cell_3.shift(4*LEFT, 0.75*UP)
        
        self.play(Write(coordinate))
        self.play(FadeIn(path))
        self.play(FadeIn(cell_1), FadeIn(cell_2), FadeIn(cell_3))


class Lecture2_scene3(Scene):
    def construct(self):
        ### Lecture notes 03 pgs. 1
        ### video 02, 10:40

        # eaularian diagram showing volume being deformed at different times
        # apparently manim coordinate screen is (14.2, 8)
        # start by drawing origin in bottom left
        top = Dot(6.5*LEFT + 2*DOWN)
        zero1 = Dot(6.5*LEFT + 3.1*DOWN)
        zero2 = Dot(6.6*LEFT + 3*DOWN)
        right = Dot(3*DOWN + 5.5*LEFT)
        label = TexMobject(r'\Omega')
        label.next_to(top, RIGHT)
        coordinate = VGroup(Arrow(zero1, top, buff = 0), Arrow(zero2, right, buff = 0), label)

        # draw cells
        cell = Square(side_length = 1, color = BLUE)
        cell.set_fill(BLUE, opacity = 0.3)
        dot = Dot()
        cell_1 = VGroup(cell, dot)
        #cell_1.shift(4*RIGHT)

        cell_2 = cell_1.copy()
        cell_3 = cell_1.copy()
        cell_4 = cell_1.copy()
        # positioning
        cell_1.shift(5*RIGHT)
        cell_2.shift(2*RIGHT + 0.75*UP)
        cell_3.shift(LEFT + 1*DOWN)
        cell_4.shift(4*LEFT + 2*UP)
        cells = VGroup(cell_1, cell_2, cell_3, cell_4)
        # transform into single cell
        main_cell = cell_1.copy()
        main_cell.center()
        # draw arrow r(t)
        zero_main = Dot(6.55*LEFT + 3.05*DOWN)
        arrow = Arrow(zero_main, [0,0,0], buff = 0)

        # show cel being deformed

        self.play(Write(coordinate))
        self.play(FadeIn(cells))
        self.play(ReplacementTransform(cells, main_cell))
        self.wait(3)
        self.play(ShowCreation(arrow))


class Lecture2_scene4(Scene):
    def construct(self):
        ### Lecture notes 03 pgs. 2 
        ### video 02, 14:00

        # difference between two points explanation. 
        # lead to, dV = ( )dr
        top = Dot(6.5*LEFT + 2*DOWN)
        zero1 = Dot(6.5*LEFT + 3.1*DOWN)
        zero2 = Dot(6.6*LEFT + 3*DOWN)
        right = Dot(3*DOWN + 5.5*LEFT)
        label = TexMobject(r'\Omega')
        label.next_to(top, RIGHT)
        coordinate = VGroup(Arrow(zero1, top, buff = 0), Arrow(zero2, right, buff = 0), label)

        dot_A = Dot(1*RIGHT + 1*DOWN)
        A = TextMobject('A')
        A.next_to(dot_A, LEFT)
        dot_B = Dot(1*LEFT + 1*UP)
        B = TextMobject('B')
        B.next_to(dot_B, LEFT)
        dr = Line(1*RIGHT + 1*DOWN, 1*LEFT + 1*UP, buff = 0)
        dr_label = TexMobject(r'd \vec{r}')
        dr_label.next_to([0,0,0], LEFT)
        first_line = VGroup(dot_A, A, dot_B, B, dr, dr_label)

        dot_A_prime = Dot(3*RIGHT)
        A_prime = TexMobject(r"A^{'}")
        A_prime.next_to(dot_A_prime, RIGHT)
        dot_B_prime = Dot(3*UP)
        B_prime = TexMobject(r"B^{'}")
        B_prime.next_to(dot_B_prime, LEFT) 
        dr_2 = Line(3*RIGHT, 3*UP, buff = 0)
        dr_2_label = TexMobject(r'd \vec{r} + d \vec{s}')
        dr_2_label.next_to(1.5*RIGHT + 1.5*UP, RIGHT)
        second_line = VGroup(dot_A_prime, A_prime, dot_B_prime, B_prime, dr_2, dr_2_label)

        A_arrow = Arrow(1*RIGHT + 1*DOWN, 3*RIGHT, buff = 0)
        B_arrow = Arrow(1*LEFT + 1*UP, 3*UP, buff = 0)
        arrows = VGroup(A_arrow, B_arrow)
        # add other labels
        # remove everything and get into math
        wipe = VGroup(first_line, second_line, arrows, coordinate)

        #equations
        eq1 = TexMobject(r'd \vec{V} = ( \quad) d \vec{r}')
        eq1.scale(2)
        eq2 = TexMobject(r'\vec{V}(x,y,z,t) = \vec{V} \left( \vec{r}(t), t \right)')
        eq2.scale(2)
        eq3 = TexMobject(r'\vec{V} \left( \vec{r}(t), t \right) = \vec{V} \left( \vec{r}(0), 0 \right) + \frac{d}{dt} \vec{V} \left( \vec{r}(0), 0 \right) dt')
        eq3.shift(2*UP)
        eq4 = TexMobject(r'\vec{V} \left( \vec{r}(t), t \right) = \vec{V_o} + \left( \frac{d \vec{V}}{d \vec{r}} \frac{d \vec{r}}{dt} + \frac{d \vec{V}}{dt} \right) dt')
        eq5 = TexMobject(r'\vec{V} \left( \vec{r}(t), t \right) = \vec{V} \left( \vec{r}(dt), dt \right) + \nabla \vec{V} d \vec{r} ')
        eq5.shift(2*DOWN)
        eq6 = TexMobject(r'd \vec{V} = (\nabla \vec{V}) d \vec{r}')
        eq6.scale(2)
        eq6.set_color_by_gradient(BLUE, YELLOW)

        self.play(ShowCreation(coordinate))
        self.play(ShowCreation(first_line))
        self.play(ShowCreation(second_line))
        self.play(ShowCreation(arrows))
        self.play(ReplacementTransform(wipe, eq1))
        self.play(ReplacementTransform(eq1, eq2))
        self.play(ReplacementTransform(eq2, eq3))
        self.play(Write(eq4))
        self.play(Write(eq5))
        self.play(FadeOut(eq3), FadeOut(eq4), FadeOut(eq5))
        self.play(Write(eq6))

class Lecture2_scene5(Scene):
    def construct(self):
        ### Lecture notes 03 pgs. 3
        ### video 02, 26:30

        # show gradients
        # trying out displaying a matrix
        V = TexMobject(r'V = \begin{bmatrix} u \\ v \\ w \end{bmatrix}')
        V.shift(2*LEFT)
        grad = TexMobject(r'\nabla = \begin{bmatrix} \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \end{bmatrix}')
        grad.shift(2*RIGHT)
        grad_V = TexMobject(r'\nabla V = \begin{bmatrix} \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} & \frac{\partial u}{\partial z} \\ \\ \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y} & \frac{\partial v}{\partial z} \\ \\ \frac{\partial w}{\partial x} & \frac{\partial w}{\partial y} & \frac{\partial w}{\partial z} \end{bmatrix}')
        grad_V.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(V), Write(grad))
        self.play(FadeOut(V), FadeOut(grad))
        self.play(Write(grad_V))



class Lecture2_scene6(Scene):
    def construct(self):
        ### Lecture notes 03 pgs. 4
        ### video 02, 31:20

        ## formally declare the strain rate tensor 
        # what is strain. change in length. linear strain
        # volume strain
        # shear strain
        title = TextMobject('Introducing the Strain-Rate Tensor')
        title.shift(3*UP)
        title.set_color_by_gradient(BLUE, YELLOW)
        title.scale(1.5)
        SRT = TexMobject(r'S = \nabla \vec{V}')
        SRT.scale(2)

        # linear strain
        lin_strain = TextMobject('Linear Strain')
        lin_strain.shift(3*UP + 5*LEFT)
        dot1 = Dot(3*LEFT)
        dot2 = Dot(RIGHT)
        L = Line(3*LEFT, RIGHT)
        L_title = TexMobject(r'\textit{l}')
        L_title.next_to(dot1, 8*RIGHT + 0.25*UP)
        L_line = VGroup(dot1, dot2, L, L_title)
        L_line.shift(1.5*UP)

        dL = Line(RIGHT, 3*RIGHT)
        dot3 = Dot(3*RIGHT)
        dL_title = TexMobject(r'\textit{dl}')
        dL_title.next_to(dot3, 3*LEFT + 0.25*UP)
        dL_line = VGroup(dL, dot3, dL_title)
        dL_line.shift(1.5*UP)

        lin_strain_eqn = TexMobject(r'L = \frac{dl}{l}')
        lin_strain_eqn.set_color_by_gradient(BLUE, YELLOW)

        # include rest of explanation

        ## volume strain
        volume_strain = TextMobject('Volume Strain')
        volume_strain.shift(3*UP + 5*LEFT)
        # use vtk image or something to show cube

        ## shear strain
        shear_strain = TextMobject('Shear Strain')
        shear_strain.shift(3*UP + 5*LEFT)
        # write function to make paralelogram
        cell = Square(side_length = 4, color = BLUE)
        cell.set_fill(BLUE, opacity = 0.3)
        tilt1 = DashedLine(2*LEFT + 2*DOWN, 2*RIGHT + 2*UP, positive_space_ratio = 0.25)
        tilt2 = DashedLine(6*RIGHT + 2*UP, 2*DOWN + 2*RIGHT, positive_space_ratio = 0.25)
        cross = DashedLine(2*UP + 2*RIGHT, 2*UP + 6*RIGHT, positive_space_ratio = 0.25)
        tilt = VGroup(tilt1, cross, tilt2)

        H = TexMobject(r'H = dx')
        H.shift(3*LEFT)
        dy = Arrow(2*LEFT + 2.2*UP, 2*RIGHT + 2.2*UP, buff = 0)
        dy_label = TexMobject(r'dy')
        dy_label.shift(2.5*UP)
        labels = VGroup(H, dy, dy_label)
        shear_eqn = TexMobject(r'\epsilon = \frac{dy}{dx}')
        shear_eqn.shift(3*DOWN)
        shear_eqn.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(title), Write(SRT))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(SRT))
        self.play(Write(lin_strain))
        self.play(ShowCreation(L_line))
        self.play(ShowCreation(dL_line))
        self.play(Write(lin_strain_eqn))
        self.wait(3)
        self.play(FadeOut(L_line), FadeOut(dL_line), FadeOut(lin_strain_eqn))
        self.play(ReplacementTransform(lin_strain, volume_strain))
        self.wait(3)
        self.play(ReplacementTransform(volume_strain, shear_strain))
        self.play(FadeIn(cell))
        self.play(ShowCreation(tilt))
        self.play(Write(labels), FadeIn(shear_eqn))
        self.wait(3)


class Lecture2_scene7(Scene):
    def construct(self):
        ### Lecture notes 03 pgs. 5
        ### video 02, 43:15

        # Translation/Rotation
        # translation has no strain
        translation = TextMobject('Translation')
        translation.scale(2)
        translation.shift(3*UP)
        block1 = Square(side_length = 1, color = BLUE)
        dot = Dot()
        block1.set_fill(BLUE, opacity = 0.3)
        Block1 = VGroup(block1, dot)
        Block2 = Block1.copy()
        Block1.shift(2*LEFT)
        Block2.shift(2*RIGHT)
        arrow = Arrow(1.5*LEFT, 1.5*RIGHT, buff = 0)
        
        # rotation has no strain either
        rotation = TextMobject('Rotation')
        rotation.scale(2)
        rotation.shift(3*UP)
        block3 = Square(side_length = 1, color = RED)
        dot = Dot()
        block3.set_fill(RED, opacity = 0.3)
        Block3 = VGroup(block3, dot)
        Block4 = Block3.copy()
        Block3.shift(2*LEFT)
        Block4.shift(2*RIGHT)
        Block4.rotate(45*DEGREES, about_point = 2*RIGHT)
        arrow2 = Arrow(1.5*LEFT, 1.3*RIGHT, buff = 0)

        # goal is to remove rigid body rotation   
        self.play(Write(translation))  
        self.play(FadeIn(Block1))
        self.play(ShowCreation(arrow), FadeIn(Block2))
        self.wait(4)
        self.play(FadeOut(translation), FadeOut(Block1), FadeOut(Block2), FadeOut(arrow), FadeIn(rotation))
        self.play(FadeIn(Block3))
        self.play(ShowCreation(arrow2), FadeIn(Block4))
        self.wait(4)

class Lecture2_scene8(Scene):
    def construct(self):
        ### Lecture notes 03 pgs. 6
        ### video 02, 50:30

        # What is rotation?
        question = TextMobject('What is Rotation?')
        question.scale(2)
        question.shift(3*UP)
        # from solid body mechanics, rotation can be defined as a transformation of a coordinate system based at the center of mass
        coord1 = Arrow([0,0,0], [0, 2, 0], buff = 0)
        coord2 = Arrow([0,0,0], [2*np.cos(30*np.pi/180), -2*np.sin(30*np.pi/180), 0], buff = 0)
        coord3 = Arrow([0,0,0], [-2*np.cos(30*np.pi/180), -2*np.sin(30*np.pi/180), 0], buff = 0)
        coord = VGroup(coord1, coord2, coord3)

        coord2 = coord.copy()
        coord2.rotate(45*DEGREES, [0, 0, 0])

        R_arrow = CurvedArrow(1*DOWN + 1.2*LEFT, 1*DOWN + 1.2*RIGHT, angle = -TAU/4)
        R = TexMobject(r'\mathbb{R}')
        R.scale(2)
        coord.shift(1*DOWN + 3*LEFT)
        coord2.shift(1*DOWN + 3*RIGHT)
        R_eqn = TexMobject(r'\mathbb{R} = \begin{bmatrix} f_1 (\quad) & f_2 (\quad) & f_3 (\quad) \\ f_4 (\quad) & f_5 (\quad) & f_6 (\quad) \\ f_7 (\quad) & f_8 (\quad) & f_9 (\quad) \end{bmatrix}')
        R_eqn.scale(1.5)
        R_eqn.set_color_by_gradient(BLUE, YELLOW)
        
        # rotation matrix, R: 9 components, look up

        # dR/dt = [0 a3 -a2; -a3 0 a1; a2 -a1 0]

        # rottion --> anitsymmetry a_ij = -a_ji

        self.play(Write(question))
        self.play(FadeIn(coord))
        self.play(FadeIn(R_arrow), Write(R), FadeIn(coord2))
        self.wait(3)
        self.play(FadeOut(coord), FadeOut(coord2), FadeOut(R_arrow))
        self.play(ReplacementTransform(R, R_eqn))

class Lecture2_scene9(Scene):
    def construct(self):
        ### Lecture notes 03 pgs. 7
        ### video 02, 1:01:30
        
        ## Break Strain-rate tensor into symetric and anti-symmetric components
        # S = A* + At
        # S^T = A* - At (transpose)
        # A* = 1/2 (S + S^T) symmetric part
        # At = 1/2 (S - S^T) anti-symmetric part

        SRT_decomp = TextMobject('Strain Rate Tensor Decomposition')
        SRT_decomp.scale(1.2)
        SRT_decomp.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(SRT_decomp))

class Lecture2_scene10(Scene):
    def construct(self):
        ### Lecture notes 03 pgs. 8
        ### video 02, 1:06:20

        ## Let's review
        # started with idea that dV = (grad V) dr
        # V(r(t),t) = Vo + (1/2 (grad V + grad Vt) + 1/2 (grad V - grad Vt)) dr
        #          translation,   deformations(S*),       rigid body rotation(S^T)
        # deformation, volume strain 
        # d omega/ omega = ( mess of stuff)/ (dx dy dz) = continuity-esque
        # volume strain + deviatoric strain

        recap = TextMobject('Review')
        recap.scale(1.2)
        recap.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(recap))

class Lecture2_scene11(Scene):
    def construct(self):
        ### Lecture notes 03 pgs. 9
        ### video 02, 1:24:30

        ## strain --> stress --> velocity, repeat
        # stress tensor Sigma = F(S) = F(S*) + F(St)
        # 1) Need to show that this is a linear funtion
        # 2) Rotational Inverient, R*Sigma = Sigma = Sigma * F(S*)
        # Shures Lemma, F(S*) = alpha e* I + beta S tilde *, e* = 1/3 trace(S*)

        relate = TextMobject('Relating Stress to Strain')
        relate.scale(1.2)
        relate.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(relate))

class Lecture2_scene12(Scene):
    def construct(self):
        ### Lecture notes 03 pgs. 10
        ### video 02, 1:33:10

        ## assumptions: newtonian fluids
        # sigma prime = mu grad V, in oure shear mode
        # sigma prime represents thermodynamical pressures
        # tau  =mu (du/ dy)
        # second viscosity: sigma prime = lambda (grad dot V) (gases)
        # stokes hypothesis: 1/3 trace(sigma) = -rho. averge of mechanical pressure = thermodynamic pressures
        # bulk viscosity

        assump = TextMobject('Some Assumptions')
        assump.scale(1.2)
        assump.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(assump))

class Lecture2_scene13(Scene):
    def construct(self):
        ### Lecture notes 03 pgs. 13
        ### video 02, 1:50:10

        ## writing out navier stokes equatinos
        # F = ma
        # sum dmi dv/dt = sum F_surf + sum F_vol
        # move to integral concept
        # surface integral to volume integral
        # move to one side. boom
        # divegene of the stress tensor

        NVS = TextMobject('Navier Stokes')
        NVS.scale(1.2)
        NVS.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(NVS))

class Lecture2_scene14(Scene):
    def construct(self):
        ### Lecture notes 03 pgs. 15
        ### video 02, 2:00:00

        ## continuity derivation
        # follow math from video, idk
        # constituative equation

        mass = TextMobject('Conserving Mass')
        mass.scale(1.2)
        mass.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(mass))

class Lecture2_scene15(Scene):
    def construct(self):
        ### Lecture notes 03 pgs. 16
        ### video 02, 2:08:00

        ## assemble everything
        # NVS ~ 3 equations
        # continuity ~ 1 equation
        # pressure(eqn state) ~ 1 equation, P = f(e, rho) [energy/mass]
        # go into that thermo tangent, what is e?
        # the final equations  

        final = TextMobject('Finally')
        final.scale(1.2)
        final.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(final))






       