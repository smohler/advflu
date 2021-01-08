from manimlib.imports import *

# To run the code:
# cd.. back into C: drive
# cd manim\manim-master
# To run and produce video
# python -m manim work\animations\advanced_fludis\"file_name.py" Scene -pl

class Lecture14_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture Fourteen')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{Life at Low Reynolds}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

class Lecture14_scene1(Scene):
    def construct(self):
        ### Lecture notes 14 pgs. 1
        ### video 14, 0:00

        ### Re --> 0
        # we don't live here
        # L ~ 1.7m, water(nu) ~ 1.7*10^-6
        # Re ~ U*10^6
        # for this to be small U must be incredibly tiny
        # say U = [0.001 - 100] (m/s)
        # 10^4 < Re < 10^8
        ### nondim material derivative of velocity
        # compare scales
        # bounary layers and stokes flow
        ### bugs?
        # L ~ 1mm, (water) nu ~ 1.7*10^-6
        # Re ~ U*10^3
        # bug still has to be moving very slowly
        # U = 10^-4 for Re = 0.1 (~ 1.2 feet per day)
        ### cilia or microbes
        # L ~ 1 micrometer
        # Re ~ 1
        ### glaciers/mantle flows 
        # draw pic of mountain
        # track flags yearly. looks like poiselle flow
        # L ~ 1km, (ice) nu ~ 1.1
        # Re = U_glacier (0.3m/year)
        # Re ~ 10^-7
        ### why do cilla have corkscrew tails
        # why do they travel ~ 30 mirometers
        # mantle, moffet vorticies
        ### if career -> biofluidics, geothermal flows, climate change, soil flows
        # these eqns are relevent
        # as Re -> 0
        # delta P = mu grad^2 V
        # you can't scale away pressure
        # 0 = grad^2 W, 0 = grad^2 P
        # write more mathy here
        # why P ~ mu*U/L not rho*U^2
        # pressure scale: what is the characteristic energy
        # creep assumption ||u||<<1
        # kinetic energy vs work done by friction
        # KE: m*|U|^2, FRIC: mu*|U|*L^2
        # there can still be time variations
        # t_intertia ~ L/U
        # talk abour oscillations
        # alpha = t_boundary/t_inertia
        # draw figure 
        # alpha>>1 slow boundary fast material
        # alpha ~ 1 "slow + slow"
        # alpha<<1 fast boundary slow material
        # write steady/unsteady gov eqns for stokes flow
        # essentially 3 heat eqns
        # heat eqn is beaten to death
        ### nature of the flow
        # a) P ~ mu*U/L NOT rho*U^2
        # b) flow around symmetrical object is also symmetrical (no wake)
        # c) regardless of shapedrag in +x and -x are equal
        # how do you move then? with a corkscrew
        # d) moffet vorticies (corner vorticies, show pic)
        # e) particle interactions felt at large distances
        # f) swars of particles fall slower than isolated particle
        # something falling close to a boundary will fall slower
        # show math to highlight the scales that prove this
        ### how do cilla move?
        # horz, vet lines. vert line is 2x horz. plate
        # mu >> 1 very viscous fluid
        # drop an oblique pin, drifting wooooo
        # componentize drag force into normal and tangential
        # cilla corckscrew is just a bunch of oblique pins. using oblique shape to get net imbalance
        # microbe must supply some torque. efficiency is ~ 1%
        
        RE = TexMobject(r'Re \rightarrow 0')
        RE.scale(1.5)
        RE.set_color_by_gradient(YELLOW, RED)

        self.play(Write(RE))

class Lecture14_scene2(Scene):
    def construct(self):
        ### Lecture notes 14 pgs. 8
        ### video 14, 1:22:00

        ### flow over a sphere
        # v important solution
        # inscribed circles
        # can use this to get a range for the possible drag
        # scale for pressure
        # F = P*A, get expression for drag force
        # streamy functions, radial, BC's
        # follow streamfunction math
        # write general gov. eqn for symmetric flows
        # imaginary numbers
        # we we need to do is pose some g(z) function
        # write f(z), g(z) functions
        ### recap
        # streamfunctions work really well
        # p ~ mu*U/L is work done by friction
        # world of microbes and glaciers
        # -V means -P, equal and opposite forces

        FS = TextMobject('Flow Over a Sphere')
        FS.scale(1.5)
        FS.set_color_by_gradient(YELLOW, BLUE)

        self.play(Write(FS))