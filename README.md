# Runge-Kutta-methods

The most widely known member of the Runge–Kutta family is generally referred to as "RK4", the "classic Runge–Kutta method" or simply as "the Runge–Kutta method".

Let an initial value problem be specified as follows:

![image](https://user-images.githubusercontent.com/90067060/165035062-92448a66-bcf1-41a0-9aab-96245e76e5c4.png)

Here y is an unknown function (scalar or vector) of time t, which we would like to approximate; we are told that ![image](https://user-images.githubusercontent.com/90067060/165035285-6cf513d6-8517-4221-8711-246a2883442d.png)
, the rate at which y changes, is a function of t and of y itself. At the initial time t_{0} the corresponding y value is y_{0}. The function f and the initial conditions y_{0}.

Now pick a step-size h > 0 and define

![image](https://user-images.githubusercontent.com/90067060/165035606-44d365a7-ad66-4017-b4d8-4cfa7dc0a3b7.png)
![image](https://user-images.githubusercontent.com/90067060/165035636-703eae9b-3274-484a-8c94-77f8b0ae0abb.png)

for n = 0, 1, 2, 3, ..., using

![image](https://user-images.githubusercontent.com/90067060/165035729-3c5ea706-fb3b-490b-a25b-c15932a64982.png)
(Note: the above equations have different but equivalent definitions in different texts).

Here y_{n+1} is the RK4 approximation of y(t_{n+1}), and the next value y_{n+1} is determined by the present value y_{n} plus the weighted average of four increments, where each increment is the product of the size of the interval, h, and an estimated slope specified by function f on the right-hand side of the differential equation.

k_{1} is the slope at the beginning of the interval, using y(Euler's method);
k_{2} is the slope at the midpoint of the interval, using y and k_{1};
k_{3} is again the slope at the midpoint, but now using y and k_{2};
k_{4} is the slope at the end of the interval, using y and k_{3}.

In averaging the four slopes, greater weight is given to the slopes at the midpoint. If f is independent of y, so that the differential equation is equivalent to a simple integral, then RK4 is Simpson's rule.

The RK4 method is a fourth-order method, meaning that the local truncation error is on the order of O(h^{5}), while the total accumulated error is on the order of O(h^{4}).

In many practical applications the function f is independent of t (so called autonomous system, or time-invariant system, especially in physics), and their increments are not computed at all and not passed to function f, with only the final formula for t_{n+1}.
