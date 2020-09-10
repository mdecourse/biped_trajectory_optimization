import numpy as np
import casadi as ca
from matplotlib import pyplot as plt
from matplotlib import animation

from trajopt_formulation import NonlinearProgram

class TrajOptSolve():
    def __init__(self):
        super().__init__()
        self.formulation = NonlinearProgram(dt=0.05, steps=1, total_duration=0.5, model='hopper')
        p_opts = {"expand":True}
        s_opts = {"max_iter": 3000}
        self.formulation.opti.solver("ipopt",p_opts,s_opts)

    def solve(self):
        sol = self.formulation.opti.solve_limited()
        self.sol_q  = [] 
        # self.sol_q2  = [] 
        # self.sol_q3  = [] 
        self.sol_rx  = [] 
        self.sol_ry  = [] 
        # self.sol_f   = []
        self.sol_px  = []
        self.sol_py  = []
        
        # self.sol_q2  = [] 
        # self.sol_dq2 = []
        
        # self.sol_q3  = [] 
        # self.sol_dq3 = []

        # self.sol_cx  = [] 
        # self.sol_cy  = [] 

        self.sol_fx  = [] 
        self.sol_fy  = []

        # self.sol_u1 = []
        # self.sol_u2 = []

        # for step in range(self.formulation.num_phases):

        #     for knot_point in range(self.formulation.knot_points_per_phase):
        #         self.sol_q1.append(sol.value(self.formulation.q[str(step)][knot_point][0]))
        #         self.sol_q2.append(sol.value(self.formulation.q[str(step)][knot_point][1]))
        #         self.sol_q3.append(sol.value(self.formulation.q[str(step)][knot_point][2]))

        #         self.sol_dq1.append(sol.value(self.formulation.qdot[str(step)][knot_point][0]))
        #         self.sol_dq2.append(sol.value(self.formulation.qdot[str(step)][knot_point][1]))
        #         self.sol_dq3.append(sol.value(self.formulation.qdot[str(step)][knot_point][2]))

        #         self.sol_fx.append(sol.value(self.formulation.f10[str(step)][knot_point][0]))
        #         self.sol_fy.append(sol.value(self.formulation.f10[str(step)][knot_point][1]))

        #         self.sol_c3x.append(sol.value(self.formulation.c3[str(step)][knot_point][0]))
        #         self.sol_c3y.append(sol.value(self.formulation.c3[str(step)][knot_point][1]))
        
        #         self.sol_u1.append(sol.value(self.formulation.u[str(step)][knot_point][0]))
        #         self.sol_u2.append(sol.value(self.formulation.u[str(step)][knot_point][1]))

        for n in range(len(self.formulation.q)):
            self.sol_fx.append(sol.value(self.formulation.f[n])[0])
            self.sol_fy.append(sol.value(self.formulation.f[n])[1])
            self.sol_px.append(sol.value(self.formulation.p[n])[0])
            self.sol_py.append(sol.value(self.formulation.p[n])[1])
            self.sol_rx.append(sol.value(self.formulation.r[n])[0])
            self.sol_ry.append(sol.value(self.formulation.r[n])[1])
            self.sol_q.append((sol.value(self.formulation.q[n])))
            # self.sol_q2.append((sol.value(self.formulation.q[n]))[1])
            # self.sol_q3.append((sol.value(self.formulation.q[n]))[2])

        self.interpolate()

    def interpolate(self):
        self.time = np.linspace(0.0, self.formulation.total_duration, len(self.sol_q))

        rx = ca.interpolant('LUT','bspline',[self.time],self.sol_rx)
        ry = ca.interpolant('LUT','bspline',[self.time],self.sol_ry)
        time_space = np.linspace(0.0, self.formulation.total_duration, 20*len(self.sol_q))
        
        self.spline_rx = rx(time_space)
        self.spline_ry = ry(time_space)

        fx = ca.interpolant('LUT','bspline',[self.time],self.sol_fx)
        fy = ca.interpolant('LUT','bspline',[self.time],self.sol_fy)
        time_space = np.linspace(0.0, self.formulation.total_duration, 20*len(self.sol_q))
        
        self.spline_fx = fx(time_space)
        self.spline_fy = fy(time_space)

        plt.plot(time_space, (np.array(self.spline_fx)**2 + np.array(self.spline_fy)**2)**(1/2))
        plt.plot(time_space, (np.array(self.spline_rx)**2 + np.array(self.spline_ry)**2)**(1/2))
        plt.show()

    def plot(self):
        fig = plt.figure()
        fig.tight_layout()

        ax1 = fig.add_subplot(311)
        ax1.plot(self.time, (np.array(self.sol_fx)**2 + np.array(self.sol_fy)**2)**(1/2), 'ro', label='f')
        ax1.grid()
        ax1.legend()

        ax2 = fig.add_subplot(312)
        ax2.plot(self.time, (np.array(self.sol_rx)**2 + np.array(self.sol_ry)**2)**(1/2), 'bo', label='r')
        ax2.grid()
        ax2.legend()

        ax3 = fig.add_subplot(313)
        ax3.plot(self.time, (np.array(self.sol_px)**2 + np.array(self.sol_py)**2)**(1/2), 'o', label='pe')
        # ax3.plot(self.time, self.sol_q2, 'o', label='q2')
        # ax3.plot(self.time, self.sol_q3, 'o', label='q3')
        ax3.grid()
        ax3.legend()

        # ax1 = fig.add_subplot(521)
        # ax1.plot(self.time, self.sol_q1, label='q1')
        # ax1.plot(self.time, self.sol_q2, label='q2')
        # ax1.plot(self.time, self.sol_q3, label='q3')
        # ax1.legend()

        # ax2 = fig.add_subplot(523)
        # ax2.plot(self.time, self.sol_dq1, label='dq1')
        # ax2.plot(self.time, self.sol_dq2, label='dq2')
        # ax2.plot(self.time, self.sol_dq3, label='dq3')
        # ax2.legend()

        # ax3 = fig.add_subplot(525)
        # ax3.plot(self.time, self.sol_u1, label='u1')
        # ax3.plot(self.time, self.sol_u2, label='u2')
        # ax3.legend()

        # ax4 = fig.add_subplot(522)
        # ax4.plot(self.time, self.sol_fx, label='fx')
        # ax4.plot(self.time, self.sol_fy, label='fy')
        # ax4.legend()

        # ax5 = fig.add_subplot(524)
        # ax5.plot(self.time, self.sol_c3x, label='c3x')
        # ax5.plot(self.time, self.sol_c3y, label='c3y')
        # ax5.legend()

        plt.show()

    def visualize(self):
        l   = self.formulation.model.length
        m   = self.formulation.model.mass   
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.grid()

        # lc3 = [self.sol_lpx[0], self.sol_lpy[0]]
        # rc3 = [self.sol_rpx[0], self.sol_rpy[0]]

        # l_link1_x = [lc3[0], l[0]*np.sin(self.sol_lq1[0]) + lc3[0]]
        # l_link1_y = [lc3[1], l[0]*np.cos(self.sol_lq1[0]) + lc3[1]]

        # print(l_link1_x, l_link1_y)

        p1, = ax.plot([],[],'r')
        p2, = ax.plot([],[],'g')
        p3,  = ax.plot([],[],'blue')
        feet, = ax.plot([],[],'yo')
        com, = ax.plot([],[],'go')
        base, = ax.plot([],[],'r', lw=5)
        terrain, = ax.plot([],[],'black')
        force, = ax.plot([],[],'c') 
        ax.set_xlim([-2, 2])
        ax.set_ylim([-2, 2])
        
        def init():
            p1.set_data([], [])
            p2.set_data([], [])
            p3.set_data( [], [])
            feet.set_data([],[])
            com.set_data([],[])
            base.set_data([],[])
            force.set_data([],[])
            terrain.set_data([],[])
            return base, feet, com, force, terrain

        def animate(i):

            c3 = [self.sol_rx[i], self.sol_ry[i]]
            pe = [self.sol_px[i], self.sol_py[i]]
            
            base_x = [c3[0] - l[0]*np.sin(self.sol_q[i])/2, l[0]*np.sin(self.sol_q[i])/2 + c3[0]]
            base_y = [c3[1] - l[0]*np.cos(self.sol_q[i])/2, l[0]*np.cos(self.sol_q[i])/2 + c3[1]]

            # link2_x = [link1_x[1], link1_x[1] + l[1]*np.sin(self.sol_q2[i])]
            # link2_y = [link1_y[1], link1_y[1] + l[1]*np.cos(self.sol_q2[i])]

            # link3_x = [link2_x[1],link2_x[1] + l[2]*np.sin(self.sol_q3[i])]
            # link3_y = [link2_y[1],link2_y[1] + l[2]*np.cos(self.sol_q3[i])]
            force_x = [pe[0], (self.sol_fx[i]+1e-3)/(1e-3+self.sol_fx[i]**2 + self.sol_fy[i]**2)**(1/2) + pe[0]]
            force_y = [pe[1], (self.sol_fy[i]+1e-3)/(1e-3+self.sol_fx[i]**2 + self.sol_fy[i]**2)**(1/2) + pe[1]]
            
            # ax.set_xlim([-2+l_link2_x[1], 2+l_link2_x[1]])
            # ax.set_ylim([-2+l_link2_y[1], 2+l_link2_y[1]])
            
            # terrain.set_data([-2+l_link2_x[1], 2+l_link2_x[1]], [0, 0])

            # ax.set_xlim([-2, 2])
            # ax.set_ylim([-2, 2])
        
            terrain.set_data([-2, 2], [0, 0])


            # p1.set_data(link1_x, link1_y)
            # p2.set_data(link2_x, link2_y)
            # p3.set_data(link3_x, link3_y)
            base.set_data(base_x, base_y)
            feet.set_data(pe[0], pe[1])
            com.set_data(c3[0], c3[1])
            force.set_data(force_x,force_y)
            return base, feet, com, force, terrain

        ani = animation.FuncAnimation(fig, animate, np.arange(0, len(self.time)), init_func=init,
                               interval=60, blit=True)

        plt.show()

problem = TrajOptSolve()
problem.solve()
problem.plot()
problem.visualize()
