# Biped Trajectory Optimization
## NOTE : This project is still in developement
- [Biped Trajectory Optimization](#biped-trajectory-optimization)
  * [Dynamic Walking on sinusoidal terrain](#dynamic-walk-on-sinusoidal-terrain)
    + [Human gait](#human-gait)
    + [Ostrich gait](#ostrich-gait)
  * [Dynamic Walking on staired terrain](#dynamic-walk-on-staired-terrain)
    + [Human gait](#human-gait)
    + [Ostrich gait](#ostrich-gait)  
  * [Dynamic Walking on sloped terrain](#dynamic-walk-on-sloped-terrain)
    + [Human gait](#human-gait)    
    + [Ostrich gait](#ostrich-gait)
  * [Dynamic Walking on flat terrain](#dynamic-walk-on-flat-terrain)
    + [Human gait](#human-gait)
    + [Ostrich gait](#ostrich-gait)
  * [Gait Generation for single step](#gait-generation-for-single-step)
    + [using CasADi library in python](#using-casadi-library-in-python)
  * [Trajectory Optimization on some basic systems](#trajectory-optimization-on-some-basic-systems)
    + [cartpole on python using CasADi](#cartpole-on-python-using-casadi)
    + [simple pendulum](#simple-pendulum)
    + [cartpole on C++](#cartpole-on-c)
  * [Passive Walking of 2-link bipedal system](#passive-walking-of-2-link-bipedal-system)

<!-- ## Dynamic Walking on sinusoidal terrain

### Human gait

![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/sin_walk_10.gif)
![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/sin_walk_10.png) 

### Ostrich gait

![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/osin_walk_10.gif)
![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/osin_walk_10.png) 


## Dynamic Walking on staired terrain

### Human gait

![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/stairs_walk_10.gif)
![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/stairs_walk_10.png) 
![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/stairs_down_walk_10.gif)

### Ostrich gait

![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/ostairs_walk_10.gif)
![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/ostairs_walk_10.png) 
![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/ostairs_down_walk_10.gif)


## Dynamic Walking on sloped terrain

### Human gait

![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/slope_walk_10.gif)
![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/slope_walk_10.png) 

### Ostrich gait

![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/oslope_walk_10.gif)
![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/oslope_walk_10.png) 

## Dynamic Walking on flat terrain

### Human gait

##### Test
![](#five-link-path-generation/uneven-terrain/results/flat_walk_10.gif)

![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/flat_walk_10.gif)
![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/flat_walk_10.png) 

### Ostrich gait

![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/oflat_walk_10.gif)
![](https://github.com/IvLabs/biped_trajectory_optimization/blob/aditya-shirwatkar/five-link-path-generation/uneven-terrain/results/oflat_walk_10.png)  -->

## Dynamic Walking on sinusoidal terrain

### Human gait

![](five-link-path-generation/uneven-terrain/results/sin_walk_10.gif)
![](five-link-path-generation/uneven-terrain/results/sin_walk_10.png) 

### Ostrich gait

![](five-link-path-generation/uneven-terrain/results/osin_walk_10.gif)
![](five-link-path-generation/uneven-terrain/results/osin_walk_10.png) 


## Dynamic Walking on staired terrain

### Human gait

![](five-link-path-generation/uneven-terrain/results/stairs_walk_10.gif)
![](five-link-path-generation/uneven-terrain/results/stairs_walk_10.png) 
![](five-link-path-generation/uneven-terrain/results/stairs_down_walk_10.gif)

### Ostrich gait

![](five-link-path-generation/uneven-terrain/results/ostairs_walk_10.gif)
![](five-link-path-generation/uneven-terrain/results/ostairs_walk_10.png) 
![](five-link-path-generation/uneven-terrain/results/ostairs_down_walk_10.gif)


## Dynamic Walking on sloped terrain

### Human gait

![](five-link-path-generation/uneven-terrain/results/slope_walk_10.gif)
![](five-link-path-generation/uneven-terrain/results/slope_walk_10.png) 

### Ostrich gait

![](five-link-path-generation/uneven-terrain/results/oslope_walk_10.gif)
![](five-link-path-generation/uneven-terrain/results/oslope_walk_10.png) 

## Dynamic Walking on flat terrain

### Human gait

![](five-link-path-generation/uneven-terrain/results/flat_walk_10.gif)
![](five-link-path-generation/uneven-terrain/results/flat_walk_10.png) 

### Ostrich gait

![](five-link-path-generation/uneven-terrain/results/oflat_walk_10.gif)
![](five-link-path-generation/uneven-terrain/results/oflat_walk_10.png) 

## Gait Generation for single step
### using CasADi library in python

![](https://github.com/IvLabs/biped_trajectory_optimization/blob/master/five-link-gait-generation/animation2.gif) ![](https://github.com/IvLabs/biped_trajectory_optimization/blob/master/five-link-gait-generation/graph.png)

## Trajectory Optimization on some basic systems
### cartpole on python using CasADi
![](https://github.com/IvLabs/biped_trajectory_optimization/blob/master/basic_tasks/catpole-python/cartpole.gif) ![](https://github.com/IvLabs/biped_trajectory_optimization/blob/master/basic_tasks/catpole-python/Graph.png)

### [simple pendulum](https://github.com/IvLabs/biped_trajectory_optimization/blob/master/basic-tasks/simple_pendulum.m)

### [cartpole on C++](https://github.com/IvLabs/biped_trajectory_optimization/tree/master/basic-tasks/cartpole-cpp)

## [Passive Walking of 2-link bipedal system](https://github.com/IvLabs/biped_trajectory_optimization/tree/master/passive-walker)


