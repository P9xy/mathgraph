# mathgraph
Python library to compute and plot trigonometric function without using math library

This lightweight library allow you to plot the curve of some function such as **sine** or **cosine**.
Python's math library is not implemented here. Instead, this program uses the Taylor expansion of supported functions with an order >= 0. Then it asks the upper bound in order to know where it should stop drawing. 

It is also possible to increases/decreases the step between two points. It is recommended to decrease it or at least to leave it as it's default value which is '10⁻¹'. The reason is that the smaller the step will be, the more **precise** the curve will be. You should keep in mind that a smaller value for the step implies more calculation, dividing by ten the step, multiplies the number of calculations by 10.

For more precision:
We apply a congruence modulo 2π to each number before calculating its sine or cosine because they are 2-π periodic. The purpose is to keep the number as close as possible to the neighborhood of the value in which we calculate the Taylor expansion. We are using 4 different Taylor expension each corresponding to a quadrant of the trigonometric circle. The first one is the Taylor expansion of the function at order n at 0. The second at π/2, the third at π, and the last at 3π/2.

