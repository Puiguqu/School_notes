# Week 6 - CM3015 Machine Learning and Neural Networks - Topic 1: Machine learning fundamentals – part 1 - Week 1

## 01_3.301_Gradient_descent_in_1D_Video_9_min

# 3.301 Gradient descent in 1D
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/26Vwa/3-301-gradient-descent-in-1d

The text introduces Gradient Descent, a core method for fitting data by minimizing error, following discussions on simple line fitting. A starting example uses three data points, where the error is measured using the Least Square Error, or the L2 loss. This L2 loss measures the distance between the actual label ($y$) and the hypothesis output ($\hat{y}$), calculated by squaring the difference and summing it across all data points. The loss function is plotted as a curve against varying parameters, such as $\Theta_1$. If the parameter values are chosen correctly, the loss reaches zero, indicating a perfect fit at a minimum point.

When sweeping across all possible parameter values, the resulting loss function forms a bowl-shaped curve, which is defined as convex. Convexity is crucial because it guarantees the existence of a single global minimum, which is the optimal point for fitting the line. This feature allows the use of the iterative technique known as Gradient Descent. The primary goal of Gradient Descent is to find the optimal parameter values that minimize this loss function.

The technique works by starting at a random point on the loss curve and iteratively moving "downhill." To move downhill, one must ascertain the gradient of the loss curve at the current point. This means calculating the slope and moving in the opposite direction of the steepest ascent. The basic principle requires the ability to differentiate the loss function.

The loss function involves the linear equation, $\Theta_0 + \Theta_1 \cdot x$, subtracted from the label $y$, squared, and summed over data points, often divided by 2 to simplify gradient calculation. Since there are multiple parameters ($\Theta_0$ and $\Theta_1$), partial derivatives must be computed. Focusing on $\Theta_1$, the partial derivative is a straightforward function derived from the loss.

To implement Gradient Descent, the core process involves taking the current parameter value and subtracting a term dependent on the calculated gradient. This term incorporates the learning rate, $\alpha$, which controls the speed of the algorithm. The Gradient Descent update rule is: $\text{Parameter} \leftarrow \text{Parameter} - \alpha \cdot \text{Derivative}$.

If the current slope is steep and positive, subtracting a large quantity moves the parameter far away from that steep ascent. As the algorithm approaches the convergence point (the bottom of the bowl), the slope decreases, leading to smaller, more incremental steps. Convergence is reached when the change between consecutive steps or steps in loss becomes negligible.

Gradient Descent fundamentally requires the loss function to be differentiable and convex. In summary, the algorithm operates by: finding a point, calculating the loss, determining the gradient (derivative) at that point, and applying the update rule. This iterative process continues until a minimum point (convergence) is found. Setting the learning rate $\alpha$ is critical: if $\alpha$ is too small, convergence is painfully slow; if $\alpha$ is too large, the algorithm may never converge, instead oscillating around the minimum.

---

## 02_3.303_Gradient_descent_in_2D_Video_6_min

# 3.303 Gradient descent in 2D
Video • 6 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/Fsxao/3-303-gradient-descent-in-2d

This curriculum introduces fundamental machine learning concepts starting with general fundamentals in Weeks 1 and 2. The course progresses to classification methods in Weeks 3 and 4, followed by an in-depth study of regression models in Weeks 5 and 6. A core technical component is introduced via Gradient Descent (Section 3.3), covered through 1D and 2D video tutorials (3.301, 3.303) and practice assignments.

Further technical topics include applying linear regression with multiple variables (3.304) and understanding data scaling (3.305). The curriculum also details Polynomial regression, complemented by dedicated practice assignments (3.306, 3.307). Intensive application and theoretical practice involve the Gradient Descent Lab (3.401) and associated further readings (3.402).

Week 7 shifts focus to vital practices, dedicated to model evaluation and improvement techniques. The sequence then moves into advanced probabilistic classification in Week 8, followed by the principles of unsupervised learning across Weeks 9 and 10.

The program then enters the specialized realm of deep learning, commencing with Neural Networks and Deep Learning in Week 11. This phase is dedicated to the mathematical building blocks of neural networks over Weeks 12, 13, and 14. Subsequent weeks (15 through 18) provide hands-on experience and introduction to practical neural network implementation.

Finally, the last two weeks (19 and 20) consolidate learning by revisiting the core fundamentals of machine learning, ensuring a complete foundational understanding. The structure ensures students cover theory, practical labs, and specific technical implementations across all modules.

---

## 03_3.305_Data_scaling_Video_3_min

# 3.305 Data scaling
Video • 3 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/Sirol/3-305-data-scaling

When handling multivariate data, significant issues arise, particularly when implementing gradient descent. The magnitude discrepancy between features is often vast; for instance, error counts might be in the tens or hundreds, while home kilowatt-hours can exceed 10,000. This massive difference in value scaling causes problems during the learning of a linear model. Specifically, the resulting $\Theta$ values become unbalanced, leading to some coefficients being very large and others being very small. To mitigate these instabilities, a crucial practical step in machine learning is to scale the data beforehand.

A common method employed for scaling is min-max normalization. This technique forces all raw data points to fall within the range of zero and one, inclusive. The formula for min-max normalization involves taking a single data point, subtracting the minimum value of that feature, and then dividing by the range (maximum value minus minimum value). This ensures that all features fit neatly between 0 and 1, as illustrated in the provided example table.

Scaling is often essential for the successful operation of gradient descent. When exploring parameters $\Theta_1$ and $\Theta_2$, an unscaled dataset can produce an elongated loss curve. In this scenario, one parameter ($\Theta_2$) may be stretched into the hundreds of thousands, while another ($\Theta_1$) remains small. Attempting gradient descent on such unscaled data requires an excessively large number of steps to converge, thereby creating significant problems with the optimization process.

By scaling the data to comparable and equivalent values, the convergence speed of gradient descent is drastically accelerated. While min-max normalization is one technique, there are several other popular scaling methods.

Another widely used approach is range normalization centered on the mean. Unlike min-max normalization, which bounds data between zero and one, this method centers the data around its mean. This technique performs particularly well when the dataset tends to be normally distributed.

A third approach is standardization, which is also known as the Z-score method. Standardization centers the data on the mean, but instead of bounding it between zero and one, it divides all data points by the standard deviation of the dataset. Each of these scaling methods (min-max, range, standardization) possesses different advantages and disadvantages. Determining the best approach requires examining the specific characteristics of the data through literature review. The associated module covering this topic is 3.305 Data scaling.

---

## 04_3.306_Polynomial_regression_Video_2_min

# 3.306 Polynomial regression
Video • 2 min - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/lecture/EtIvW/3-306-polynomial-regression

The curriculum begins by establishing Machine Learning fundamentals, followed by laboratory exercises reinforcing these core concepts in Weeks 1 and 2. Weeks 3 and 4 are dedicated to Classification, which introduces techniques necessary for categorizing data. The focus shifts in Week 5 and Week 6 to Regression, a critical aspect of predicting continuous variables.

A major technical deep dive occurs in Section 3.3, covering Gradient Descent, starting with 1D and 2D video applications. This section further includes practical assignments on Gradient Descent and Linear Regression with Multiple Variables. Specialized topics within Regression include Data Scaling and Polynomial Regression, both addressed in dedicated videos and practice assignments.

Following the core topics, Week 3.4 focuses on a dedicated Gradient Descent Lab and further theoretical reading. Week 7 introduces Model Evaluation and Improvement, essential for assessing algorithm efficacy. Progression continues with probabilistic classification in Week 8 and an exploration of Unsupervised Learning across Weeks 9 and 10.

Weeks 11 through 14 are dedicated to Neural Networks and Deep Learning, culminating in an understanding of the mathematical building blocks of these complex models. Weeks 15 through 18 are hands-on sessions designed for getting started with neural network implementation. The course concludes by reviewing the core tenets of Machine Learning fundamentals in Weeks 19 and 20. This structured path covers fundamental concepts, advanced topics like deep learning, and practical application via multiple lab assignments.

---

## 05_3.402_Further_reading_Reading_1h

# 3.402 Further reading
Reading • 1h - Summary

URL: https://www.coursera.org/learn/uol-cm3015-machine-learning-and-neural-networks/supplement/TmTxB/3-402-further-reading

The core concept discussed is Gradient descent, detailed in Chapter 2, section 2.4 of the Chollet course textbook, with a specific focus on its application within deep neural networks. This material is cataloged as Further reading (3.402) and will be revisited at a later point in the course curriculum.

---

