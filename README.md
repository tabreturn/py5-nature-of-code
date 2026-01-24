# Nature of Code (2), py5 Port

*py5 implementations of Daniel Shiffman's "The Nature of Code" (2024 edition)*

**Built with [py5](https://py5coding.org) using [Thonny-py5mode](https://github.com/py5coding/thonny-py5mode)**

I have taken a few liberties in my interpretation. First, the examples in the book and its accompanying [p5.js sketches](https://natureofcode.com/examples) do not always match exactly. Second, in a few places, minor adjustments were necessary to support an idiomatic, py5-compatible Python implementation. Throughout, however, my aim has been to balance faithfulness to the original material with Python best practices and clarity for readers working through this [fantastic book](https://natureofcode.com).

To run the sketches, install [Thonny-py5mode](https://github.com/py5coding/thonny-py5mode) and activate **py5 → Imported mode for py5** in the editor.

Where text is displayed, the sketches use the *DejaVu Sans Mono* font.

![](banner.png)


---


<em><b>NOTE:</b> I initially started porting Chapters 09, 10, and 11. Task 11.04 required restarting from Chapter 00. I'm currently working through and completing Chapters 00--05. Then I'll return to finish Chapter 11. Finally, I will complete Chapters 06--08.</em>


---


## Part 1: Inanimate Objects

### Ch. 00 - Randomness

- **00.01 - traditional_random_walk** |
  py5: [ch00_randomness/00.01](ch00_randomness/00.01) |
  p5.js: [5C69XyrlsR](https://editor.p5js.org/natureofcode/sketches/5C69XyrlsR)

- **00.02 - random_number_distribution** |
  py5: [ch00_randomness/00.02](ch00_randomness/00.02) |
  p5.js: [u4vTwZuhT](https://editor.p5js.org/natureofcode/sketches/u4vTwZuhT)

- **00.03 - walker_tends_right** |
  py5: [ch00_randomness/00.03](ch00_randomness/00.03) |
  p5.js: [iAjs_70DF](https://editor.p5js.org/natureofcode/sketches/iAjs_70DF)

- **00.04 - gaussian_distribution** |
  py5: [ch00_randomness/00.04](ch00_randomness/00.04) |
  p5.js: [Yk_eSiNOR](https://editor.p5js.org/natureofcode/sketches/Yk_eSiNOR)

- **00.05 - accept_reject_distribution** |
  py5: [ch00_randomness/00.05](ch00_randomness/00.05) |
  p5.js: [3t5iHwA7Q](https://editor.p5js.org/natureofcode/sketches/3t5iHwA7Q)

- **00.06 - perlin_noise_walker** |
  py5: [ch00_randomness/00.06](ch00_randomness/00.06) |
  p5.js: [qyNwGUy59](https://editor.p5js.org/natureofcode/sketches/qyNwGUy59)

### Ch. 01 - Vectors

- **01.01 - bouncing_ball_no_vectors** |
  py5: [ch01_randomness/01.01](ch00_randomness/01.01) |
  p5.js: [oadKdOndU](https://editor.p5js.org/natureofcode/sketches/oadKdOndU)

- **01.02 - bouncing_ball_vectors** |
  py5: [ch01_randomness/01.02](ch00_randomness/01.02) |
  p5.js: [qU5oPJijX](https://editor.p5js.org/natureofcode/sketches/qU5oPJijX)

- **01.03 - vector_subtraction** |
  py5: [ch01_randomness/01.03](ch00_randomness/01.03) |
  p5.js: [HtXiElQbC](https://editor.p5js.org/natureofcode/sketches/HtXiElQbC)

- **01.04 - vector_multiplication** |
  py5: [ch01_randomness/01.04](ch00_randomness/01.04) |
  p5.js: [VQfwqpDlv](https://editor.p5js.org/natureofcode/sketches/VQfwqpDlv)

- **01.05 - vector_magnitude** |
  py5: [ch01_randomness/01.05](ch00_randomness/01.05) |
  p5.js: [rld_CtioUU](https://editor.p5js.org/natureofcode/sketches/rld_CtioUU)

- **01.06 - vector_normalization** |
  py5: [ch01_randomness/01.06](ch00_randomness/01.06) |
  p5.js: [5dWkegAID](https://editor.p5js.org/natureofcode/sketches/5dWkegAID)

- **01.07 - motion_101_velocity** |
  py5: [ch01_randomness/01.07](ch00_randomness/01.07) |
  p5.js: [6foX0NUfS](https://editor.p5js.org/natureofcode/sketches/6foX0NUfS)

- **01.08 - motion_101_velocity_constant_accel** |
  py5: [ch01_randomness/01.08](ch00_randomness/01.08) |
  p5.js: [4GSialOpQw](https://editor.p5js.org/natureofcode/sketches/4GSialOpQw)

- **01.09 - motion_101_velocity_random_accel** |
  py5: [ch01_randomness/01.09](ch00_randomness/01.09) |
  p5.js: [w9DU8ccWMf](https://editor.p5js.org/natureofcode/sketches/w9DU8ccWMf)

- **01.10 - motion_101_accel_toward_mouse** |
  py5: [ch01_randomness/01.10](ch00_randomness/01.10) |
  p5.js: [gYJHm1EFL](https://editor.p5js.org/natureofcode/sketches/gYJHm1EFL)

### Ch. 02 - Forces

- **02.01 - forces** |
  py5: [ch02_randomness/02.01](ch00_randomness/02.01) |
  p5.js: [4IRI8BEVE](https://editor.p5js.org/natureofcode/sketches/4IRI8BEVE)

- **02.02 - forces_two_objects** |
  py5: [ch02_randomness/02.02](ch00_randomness/02.02) |
  p5.js: [ePLfo-OGu](https://editor.p5js.org/natureofcode/sketches/ePLfo-OGu)

- **02.03 - gravity_scaled_mass** |
  py5: [ch02_randomness/02.03](ch00_randomness/02.03) |
  p5.js: [0RiwMFOQ7](https://editor.p5js.org/natureofcode/sketches/0RiwMFOQ7)

- **02.04 - including_friction** |
  py5: [ch02_randomness/02.04](ch00_randomness/02.04) |
  p5.js: [I4wC4aXd-E](https://editor.p5js.org/natureofcode/sketches/I4wC4aXd-E)

- **02.05 - fluid_resistance** |
  py5: [ch02_randomness/02.05](ch00_randomness/02.05) |
  p5.js: [FknzcAaVh](https://editor.p5js.org/natureofcode/sketches/FknzcAaVh)

- **02.06 - attraction** |
  py5: [ch02_randomness/02.06](ch00_randomness/02.06) |
  p5.js: [Cl0Eeaz_V](https://editor.p5js.org/natureofcode/sketches/Cl0Eeaz_V)

- IN PROGRESS ...


---


## Part 2: It's Alive!

### Ch. 05 - Autonomous Agents

- IN PROGRESS ...


---


## Part 3: Intelligence


### Ch. 09 - Evolutionary Computing

- **09.01 - ga_shakespeare** |
  py5: [ch09_evolutionary_computing/09.01](ch09_evolutionary_computing/09.01) |
  p5.js: [q4F192JCV](https://editor.p5js.org/natureofcode/sketches/q4F192JCV)

- **09.02 - smart_rockets** |
  py5: [ch09_evolutionary_computing/09.02](ch09_evolutionary_computing/09.02) |
  p5.js: [jzfy_9p1ES](https://editor.p5js.org/natureofcode/sketches/jzfy_9p1ES)

- **09.03 - smarter_rockets** |
  py5: [ch09_evolutionary_computing/09.03](ch09_evolutionary_computing/09.03) |
  p5.js: [565K_KXSA](https://editor.p5js.org/natureofcode/sketches/565K_KXSA)

- **09.04 - interactive_selection** |
  py5: [ch09_evolutionary_computing/09.04](ch09_evolutionary_computing/09.04) |
  p5.js: [dUeAaapkQ](https://editor.p5js.org/natureofcode/sketches/dUeAaapkQ)

- **09.05 - evolving_ecosystem** |
  py5: [ch09_evolutionary_computing/09.05](ch09_evolutionary_computing/09.05) |
  p5.js: [1HDlp_tKF](https://editor.p5js.org/natureofcode/sketches/1HDlp_tKF)


### Ch. 10 - Neural Networks

- **10.01 - the_perceptron** |
  py5: [ch10_neural_networks/10.01](ch10_neural_networks/10.01) |
  p5.js: [sMozIaMCW](https://editor.p5js.org/natureofcode/sketches/sMozIaMCW)

- **10.02 - gesture_classifier** |
  py5: [ch10_neural_networks/10.02](ch10_neural_networks/10.02) |
  p5.js: [SbfSv_GhM](https://editor.p5js.org/natureofcode/sketches/SbfSv_GhM)


### Ch. 11 - Neuroevolution

- **11.01 - flappy_bird** |
  py5: [ch11_neuroevolution/11.01](ch11_neuroevolution/11.01) |
  p5.js: [Pv-JlO0cl](https://editor.p5js.org/natureofcode/sketches/Pv-JlO0cl)

- **11.02 - flappy_bird_neuro_evolution** |
  py5: [ch11_neuroevolution/11.02](ch11_neuroevolution/11.02) |
  p5.js: [PEUKc5dpZ](https://editor.p5js.org/natureofcode/sketches/PEUKc5dpZ)

- **11.03 - smart_rockets_neuroevolution** |
  py5: [ch11_neuroevolution/11.03](ch11_neuroevolution/11.03) |
  p5.js: [KkV4lTS4H](https://editor.p5js.org/natureofcode/sketches/KkV4lTS4H)

- 11.04 - IN PROGRESS ... |
  py5: [ch11_neuroevolution/11.04](ch11_neuroevolution/11.04) |
  p5.js: [fZDfxxVrf](https://editor.p5js.org/natureofcode/sketches/fZDfxxVrf)

- 11.05 - IN PROGRESS ... |
  py5: [ch11_neuroevolution/11.05](ch11_neuroevolution/11.05) |
  p5.js: [vCTMtXXSS](https://editor.p5js.org/natureofcode/sketches/vCTMtXXSS)

- 11.06 - IN PROGRESS ... |
  py5: [ch11_neuroevolution/11.06](ch11_neuroevolution/11.06) |
  p5.js: [IQbcREjUK](https://editor.p5js.org/natureofcode/sketches/IQbcREjUK)

