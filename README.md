<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="">
    <img src="https://www.pasternack.com/Images/reference-tools/images/Friis%20Equation.png" alt="Logo" width="160" height="160">
  </a>

  <h3 align="center">CANOPUS - Parameter Estimation for Large-Scale Channel Models</h3>

  <p align="center">
    Wireless Telecommunications
    <br />
    <a href="linkedin.com/in/ali-fathi-vafegh-84bb0a274/">My Linkedin</a>
  </p>
</div>

# Description

In wireless telecommunications, the signal strength decreases or attenuates during transmission, especially over long distances. The attenuation increases exponentially with the distance between the transmitter and the receiver. This report attempts to assist in estimating the attenuation in different conditions. One common model for path loss estimation is the Path Loss Exponent and Shadowing Gaussian Noise models in urban environments, which we will explore using machine learning techniques.

In telecommunications engineering, the Friis equation, also known as the free space path loss (FSPL) equation, is used to calculate the power received by an antenna at a certain distance from a transmitting antenna. The equation depends on factors like transmitted power (Pt), transmitting antenna gain (Gt), receiving antenna gain (Gr), and distance (d).

To calculate the path loss (PL) and power received (Pr), we can simplify the Friis equation as follows:

$$Pr = P_{t} \cdot G_{t} \cdot G_{r} \left( \frac{\lambda}{4 \pi R} \right)^2$$

or in logarithmic form:

$$Pr = P_{t} + G_{t} + G_{r} - P_{L}$$

where the path loss is:

$$P_{L}= \beta \cdot 10~log_{10}(\frac{4\pi d}{\lambda})$$

Further simplifying, we get:

$$P_{r}= P_{0} - \beta \cdot 10~log_{10}(\frac{d}{d_{0}}) + X_{\sigma}$$

Here, $X_{\sigma}$ is Gaussian noise with zero mean and variance $\sigma^2$.

| -------------- | ------------------------------------------- |
| $P_{0}$ | the reference received power |
| $d_{0}$ | reference distance |
| $X_{\sigma}$ | Gaussian noise with standard deviation between 4 and 12 |
