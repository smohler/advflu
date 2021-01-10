from manimlib.imports import *

# To run the code:
# cd.. back into C: drive
# cd manim\manim-master
# To run and produce video
# python -m manim work\animations\advanced_fludis\"file_name.py" Scene -pl

class Lecture15_Introduction(Scene):
    def construct(self):
        # title card: can work one something which can appear in each lecture
        title = TextMobject('Fluid Mechanics: Lecture Fifteen')
        title.set_color_by_gradient(BLUE, YELLOW)
        title.center()
        title.shift(UP)
        ## lecture topic
        topic = TexMobject(r'\textit{Life at High Reynolds}')
        topic.center()
        # play
        self.play(Write(title))
        self.play(FadeIn(topic))
        self.wait(4)
        self.play(FadeOut(title), FadeOut(topic))

class Lecture15_scene1(Scene):
    def construct(self):
        ### Lecture notes 15 pgs. 1
        ### video 15, 0:00

        ### Re --> infty
        # we live at high reynolds (ideal flow = potential flow)
        # V = grad(phi) <=> grad X V = 0
        # We also usually experience, Ma << 1
        # we are usually incompressible, grad*V = 0
        ### plot showing differenct regiemes for Re
        # stokes flow (linear), moderate (asymptotics), compressible flow
        # empty region, Re -> infty
        # critical reynolds number. split into potential theory portion and turbulence theory (totally 3D)
        # use experimentation to try and characterize turbulence
        # show velocity vs. time for small/large Re
        ### turbulence characters
        # mean = <u>, fluxuation = u'
        # properties of flucuation?
        # V = u(x) + u(x,t) (mean flow plus flucuation)
        # "model for solution of NVS?"
        # <u> ~ mean flow, steady state
        # u' ~ flucuation, no bias, zero mean
        # <u> = int_{0}_{T}(u(x,t))dt. works the same for <v>, <w>
        # now there are 6 unknowns, 3 means and 3 flucuations
        # lim_{T->infty}*int_{0}_{T}(dt) = < >
        ### properties
        # 1) <<f>> = <f>
        # 2) <f'> = 0
        # 3) <f+g> = <f> + <g>
        # 4) <f*<g>> = <f>*<g>
        # 5) d/dx <f> = <df/dx>, assumes lots of smoothness on f
        ### RANS
        # evaluate NVS with this
        # <grad*V> = grad*<V> = 0, mean conserves mass
        # grad*(<V> + V~) => grad*V~ = 0, flucuationsconserve mass
        # 0) assume solution form. V = <V> + V~
        # 1) pick < > mean
        # 2) assumptions on V~ properties (zero mean)
        # 3) <NVS> and NVS(<V> + V~)

        RE = TexMobject(r'Re \rightarrow \infty')
        RE.scale(1.5)
        RE.set_color_by_gradient(YELLOW, RED) 

        self.play(Write(RE))

class Lecture15_scene2(Scene):
    def construct(self):
        ### Lecture notes 15 pgs. 16
        ### video 15, 48:00

        ### Turbulence Methods
        # RANS, LES, DNS
        # draw inverted triangle with accuracy increasing downward
        # DNS - pure numerical method
        # new triangle with $/time increasing upwards
        # LES picks a super fancy average
        # < > = int int G(x-r)*V dr dt, filtering function
        # smallest eddy, need 4 cells
        # <momentum> compare to momentum(<V> + V~), assume mean is steady
        # write SS. RANS eqn. has extra term called reynolds stress
        # can write US RANS. includes stress tensor
        # stress tensor, T = mu*grad(<V>) - rho*<V~ * V~^T>
        # remember A*A^T = matrix, where A is a vector
        # there is a newtoninan viscous stress component and a turbulent shear stress component
        # closure problem. more unknowns than equations <= V = <V> + V~, 6 total unknwons just in this eqn
        # just like Stokes hypothesis. we gotta assume, bro
        # 1898 say the trubulent shear stress divided by divergence of mean flows  = mu_T 
        # turbulent shear stress is linearly related to the mean strain rate tensor
        # can rewrite stress tensor where the effective turbulence can be characterized by an added viscosity, eddy viscosity
        ### what is turbulence
        # presence of eddys
        # scales. scale turbulent kinematic viscosity, is a local property
        # stress tensor as a function of strain rate tensor
        # stress tensor(strain rate tensor) = linear term + quadratic term
        # linear term ~ newtonian approximation, quadratic term ~ mixing length
        ### what is the length scale
        # imagine turbulent near wall, full 3D, ton of vorticity coming from wall
        # there are now regions: outer, intermediate, inner (matched asymptotics)
        # inner ~ y+, outer ~ eta
        # inner wall: L ~ y^2
        # intermediate(overlap): L ~ kappa*y
        # outer wall: L ~ c_o*l
        # what's happening for y. show couette flow
        # <u> = f(tau_w, rho, mu, y) (inner)
        # U_infty = <u> + g(tau_w, rho, mu, y) (outer)
        # u+ = <u>/U_o = f(y*U_o/nu), U_o ~ sqrt(tau_w/rho) wall friction velocity
        # this is the diffusion of momentumthrought the forces of turbulnt stresses. similar to viscous diffusion velocity
        # u*_infty = u_infty/U_o + g(y/delta)
        # f(deta*U_o*y/nu*delta) = U*_infty - g(y/delya)
        # eta = y/delta, y+ = y*U_o/nu = y*(v*)/nu
        # multiplication of inputs turns into addition of terms
        # this means f and g must logarithimic. information theory (claude ...)
        # u*(y*) = 1/kappa ln(y+) + B
        # U*_infty = U*(eta) - 1/kappa ln(eta) + A
        # kappa = 0.4 or 0.41
        # B = 5.0, 5.5
        # A changes with the flow
        ### energy cascade
        # <energy> compare to energy(<V> + V~)
        # q^2 = u'^2 + v'^2 + w'^2 = V~*V~^T = V~ * V~
        # write out material derivative of energy ...
        # convective diffusion, production term, work by turbulent stresses, turbulent dissapation
        ### 3D-ness
        # draw fountain diagram
        # top is stokes, then inertial terms (linear kinetic energy, irrotational flows), bottom is rotational kinetic energy
        # turbulence is hard. no one understand rotational coordinates lol
        # a) more pressur needed for same flow (x10 for channels)
        # b) curvature is localized next to walls
        # c) Most energy is held up in large eddys
        # d) wave number stuff. E(k) ~ k^-5/3
        # f) basic mu_T effect
        # LES ignores small eddys
        # always will need experiment or mind for more equations
        # experimentation is solving the NVS in full 3D
        # mind is coming up with model for solution form

        TM = TextMobject('Turbulence Methods') 
        TM.scale(1.5)
        TM.set_color_by_gradient(RED, BLUE)

        self.play(Write(TM))