from manimlib.imports import *

# To run the code:
# cd.. back into C: drive
# cd manim\manim-master
# To run and produce video
# python -m manim work\animations\advanced_fludis\"file_name.py" Scene -pl

class Lecture4_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture Four')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{Simple Incompressible Flows, pt.1}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

class Lecture4_scene1(Scene):
    def construct(self):
        ### Lecture notes 05 pgs. NA
        ### video 04, 6:30

        ### Simple Incompressible FLow
        # Simple --> can write down the velocity field as a function V(x,t) [explicit, implicit]
        # Incomporessible --> is a statement about flow, not fluid
        # this is a small set if the 'solutinos' to the NVS eqns
        # good to study simple probs since we can translate over to different cases via scaling

        SIF = TextMobject('Simple Incompressible Flows')
        SIF.scale(1.5)
        SIF.set_color_by_gradient(BLUE, YELLOW)

        self.play(Write(SIF))

class Lecture4_scene2(Scene):
    def construct(self):
        ### Lecture notes 05 pgs. 2
        ### video 04, 11:00
        
        ### Generalized Parallel Flow
        # 3D sketch, thin slot flow, write down coordinate system
        # x is parallel to pressure gradient
        # omega = {(x,y,z)|0<y<H, 0<x<L, 0<z<W}
        # H/L << 1 (longer than it is tall), L/W << 1 (wider than it is long)
        # 1/H + 1/L + 1/W = 1/H

        # Break up into smaller chucks

        ### NVS: consider eqn of state plus continuity
        # pressure = f(rho, temp), [rho, temp = f(x, y, z, t)]
        # D rho/Dt = -rho(grad*V)
        # follow math on pg.3 of notes from here
        # end up with 2 eqns: thermodynamic and momentum change in density field
        # now we non-dimensionalize
        # x ~ L, t ~ L/U, V ~ U, alpha ~ alpha_o, beta ~ beta_o, k ~ k_o, Cp ~ Cp_o, mu ~ mu_o, g ~ L/U^2
        # must pick a pressure scale, scale by dynamic pressure: P ~ rho U^2
        # follow math to write non-dimensinalized form
        # reason that Ma^2 is small enough to call 0 (epsilon really). that way we have D rho/Dt = 0
        # now write out final dimensinoal and nondimensional incomp. NVS

        ### returning to parallel flow problem 
        # non-dimensionalize gradient operator. Define new matrix, L, which has the scales. everything works the same
        # factor out the trace (sum of diagonal) of L. new matrix with diagonal like 1/(x*Tr(L)). fancy way of writing the same thing
        # come to conclusin the partial V/partial y = 0
        # cycle of simplify NVS --> scales + nondim. repeat
        # explain this
        # show what would happen if you had chosen a different pressure scale. Reynolds number woulf have posed s different functional form
        # it is possible to scale by the sum of some pressures

        ### once again returning to parallel flow problem
        # w--> infinity, means 2D problem, kills off z-momentum
        # apply no-slip at all boundaries, does not depend on time
        # no -slip is really saying fluid must match velocity of boundary surface. Mention dust on fan example
        # initial conditions (t = 0). assign some initial vector field

        ### again coming back to the parallel flow problem, now in 2D
        # assume we are past entrance region, left with: partial v/partial y = 0
        # consider pressure equation, talk about thermodynamic pressure in addition to the driving gradient
        # follow math from here
        # cross suction flow
        # say no suction flow
        # pressure gradient in x direction must be a constant, consistancy thing. fully developed 
        # write final ODE with BC and IC

        ### talk about similar but different problems
        # river with segmented regions
        # what is the shear on the fishies scales
        # modeling the real world.

        sam = TextMobject("We'll have to break this one up")
        sam.scale(1.5)
        sam.set_color_by_gradient(RED, YELLOW)

        self.play(Write(sam))