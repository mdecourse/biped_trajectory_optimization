from casadi.casadi import sqrt
import numpy as np
import casadi as ca

try:
    import biped_trajectory_optimization.phase_based_new.hopper.helper_functions as hf
except:
    import helper_functions as hf

"A centeroidal dynamics based model hopper"
class Hopper():
    def __init__(self):
        super().__init__()
        self.num_ee  = 1
        self.name    = 'hopper'
        self.length  = np.array([0.75,0.75,0.75])
        self.mass    = np.array([1,1,20])

        # self.i_qcom  = np.zeros((1,1))
        # self.f_qcom  = np.zeros((1,1))

        self.inertia = self.mass * (self.length**2)/4
        self.gravity = 10

        self.mcom = np.sum(self.mass)
        print(self.mcom)
        self.icom = self.mcom * (self.length[-1]**2 + 0.1**2)/12
        print(self.icom)

        self.gravity_vector = ca.DM.zeros(2)
        self.gravity_vector[1,0] = self.gravity

        self.b = ca.DM([3*(self.length[0]),2*(self.length[0])])
        self.nominal_pe = ca.DM([0, 2.5*(self.length[0])])

        self.setKinematicsConstraint()
        self.setCenteroidalDynamics()

    def setState(self, r, q, pe, fe):
        self.q     = ca.reshape(q , 1, 1)
        self.r     = ca.reshape(r , 2, 1)
        self.pe    = ca.reshape(pe, 2, 1)
        self.fe    = ca.reshape(fe, 2, 1)

        self.kinematic_constraint = self.kinematic_model(r=self.r, q=self.q, pe=self.pe)

        self.dynamic_constraints = self.dynamic_model(r=self.r, pe=self.pe, f=self.fe)

    def setKinematicsConstraint(self):
        q     = ca.MX.sym( 'q', 1, 1)
        r     = ca.MX.sym( 'r', 2, 1)
        pe    = ca.MX.sym('pe', 2, 1)
        
        R_q = ca.MX.zeros(2,2)
        R_q[0,0], R_q[0,1] = ca.cos(q), -ca.sin(q)
        R_q[1,0], R_q[1,1] = ca.sin(q),  ca.cos(q)

        y = ca.fabs(R_q @ (pe - r) - (R_q @ r - self.nominal_pe))

        self.kinematic_model = ca.Function('FullKinematics', [r, q, pe], 
                                                  [R_q, y],
                                                  ['r', 'q', 'pe'],
                                                  ['Rotation', 'constraint'])

    def setCenteroidalDynamics(self):
        r     = ca.MX.sym( 'r', 2, 1)
        pe    = ca.MX.sym('pe', 2, 1)
        fe    = ca.MX.sym('fe', 2, 1)

        mcom  = self.mcom
        g     = self.gravity_vector
        icom  = self.icom

        r_ddot = (fe - mcom*g)/mcom
        q_dot = (hf.crossProduct2D(fe,r - pe)/icom) 

        self.dynamic_model = ca.Function('CenteroidalDynamics', [r, pe, fe], 
                                                [r_ddot, q_dot], 
                                                ['r','pe','f'],
                                                ['r_ddot','q_dot'])
        

# test check for sanity

# test_hopper = Hopper()
# q     = ca.MX.sym(    'q', 1, 1)
# # q_dot = ca.MX.sym('q_dot', 3, 1)
# r     = ca.MX.sym(    'r', 2, 1)
# # r_dot = ca.MX.sym('r_dot', 2, 1)
# pe    = ca.MX.sym(   'pe', 2, 1)
# f     = ca.MX.sym(    'f', 2, 1)

# test_hopper.setState(r, q, pe, f)

# print('-----Symbolic Test-------')
# print(test_hopper.kinematic_model(r, q, pe))
# print(test_hopper.dynamic_model(r, pe, f))

# q     = ca.DM([np.pi/3])
# # q_dot = ca.DM([1.]*3)
# r     = ca.DM([3, 1])
# # r_dot = ca.DM([.2, .1])
# pe    = ca.DM([2, 1])
# f     = ca.DM([test_hopper.mcom*test_hopper.gravity/sqrt(2), test_hopper.mcom*test_hopper.gravity/sqrt(2)])

# test_hopper.setState(r, q, pe, f)

# print('-----Numeric Test-------')
# print(test_hopper.kinematic_model(r, q, pe))
# print(test_hopper.dynamic_model(r, pe, f))


###############################################
###############################################
###############################################

# test_hopper = Hopper()
# q    = ca.MX.sym(   'q', 3, 1)
# dq   = ca.MX.sym(  'dq', 3, 1)

# c3   = ca.MX.sym(  'c3', 2, 1)
# dc3  = ca.MX.sym( 'dc3', 2, 1)
# ddc3 = ca.MX.sym('ddc3', 2, 1)

# u    = ca.MX.sym(   'u', 2, 1)
# f10  = ca.MX.sym( 'f10', 2, 1)

# test_hopper.setFullState(q, dq, c3, dc3, ddc3, u, f10)

# print(test_hopper.dynamics)

###############################################
###############################################
###############################################

    # def setFullState(self, q, dq, c3, dc3, u, f10):
    #     self.q   = ca.reshape( q, 3, 1)
    #     self.dq  = ca.reshape(dq, 3, 1)

    #     self.c3   = ca.reshape(  c3, 2, 1)
    #     self.dc3  = ca.reshape( dc3, 2, 1)

    #     self.u   = ca.reshape(  u, 2, 1)
    #     self.f10 = ca.reshape(f10, 2, 1)

    #     self.p, self.dp, self.ddp, self.c, self.dc, self.ddc = self.getKinematics()
    #     self.dynamics = self.getDynamics()

    # def getKinematics(self):        
    #     # Assume p,c as 2x1

    #     ##################
    #     #####--Leg--######
    #     ##################
    #     p = ca.MX.zeros(2, 4)
    #     c = ca.MX.zeros(2, 3)

    #     c3 = self.c3

        # p[0,3],p[1,3] =  self.length[2]*ca.sin(self.q[2])/2 + c3[0,0],  self.length[2]*ca.cos(self.q[2])/2 + c3[1,0]
        # p[0,2],p[1,2] = -self.length[2]*ca.sin(self.q[2])/2 + c3[0,0], -self.length[2]*ca.cos(self.q[2])/2 + c3[1,0]
        # p[0,1],p[1,1] = -self.length[1]*ca.sin(self.q[1]) + p[0,2]   , -self.length[1]*ca.cos(self.q[1]) + p[1,2]
        # p[0,0],p[1,0] = -self.length[0]*ca.sin(self.q[0]) + p[0,1]   , -self.length[1]*ca.cos(self.q[0]) + p[1,1]

    #     c[0,2],c[1,2] = c3[0,0], c3[1,0]
    #     c[0,1],c[1,1] = -self.length[1]*ca.sin(self.q[1])/2 + p[0,2], -self.length[1]*ca.cos(self.q[1])/2 + p[1,2]
    #     c[0,0],c[1,0] = -self.length[0]*ca.sin(self.q[0])/2 + p[0,1], -self.length[0]*ca.cos(self.q[0])/2 + p[1,1]
 
    #     ###--Derivatives--###
    #     dp  = ca.jtimes( p, self.q, self.dq) + self.dc3
    #     dc  = ca.jtimes( c, self.q, self.dq) + self.dc3

    #     ddp = ca.jtimes(dp, self.q, self.dq**2)
    #     ddc = ca.jtimes(dc, self.q, self.dq**2)


    #     ###--Form a dictionary--###
    #     p   = {'Leg' :   p, 'Constraint' : (self.q[0]<=self.q[1])}
    #     dp  = {'Leg' :  dp}
    #     ddp = {'Leg' : ddp}

    #     c   = {'Leg' :   c}
    #     dc  = {'Leg' :  dc}
    #     ddc = {'Leg' : ddc}

    #     return p,dp,ddp,c,dc,ddc      

    # def getDynamics(self):

    #     ###--Leg--###
    #     ddq  = ca.MX.zeros(3)
    #     c3  = self.c3
    #     p   = self.p  ['Leg']
    #     c   = self.c  ['Leg']
    #     ddc = self.ddc['Leg']
    #     f10 = self.f10

    #     f32 = self.mass[2]*(ddc[:,2] - self.gravity_vector)
    #     ddq[2] = self.u[1] + hf.crossProduct2D(p[:,2]-c[:,2], f32)

    #     f12 = self.mass[0]*(ddc[:,0] - self.gravity_vector) - f10
    #     ddq[0] = -self.u[0] + hf.crossProduct2D(p[:,1]-c[:,0], f12) + hf.crossProduct2D(p[:,0]-c[:,0], f10)

    #     f21 = -f12
    #     f23 = -f32
    #     ddq[1] = self.u[0]-self.u[1] + hf.crossProduct2D(p[:,2]-c[:,1], f23) + hf.crossProduct2D(p[:,1]-c[:,1], f21)

    #     ddq /= self.inertia

    #     dynamics = {'Leg': ddq}

    #     return dynamics
