# Machine Learning Note


## Intro
### Most machine learning algorithms consist of:
* Dataset
* Cost function: equivalent to MSE
* Optimization procedure
* A model

### Additional features are:
* Activation function: eg) Rectified Linear Unit(ReLU), sigmoid, hyperbolic tangent(tanh)
* Loss function: equivalent to 'residuals'
* Fine tuning: refers to playing with the hyperparameters

### Information Theory
* About quantifying how much information is present in a signal
* Key properties:  
    1) Likely events should have low information content. Events that are guaranteed to happen should have no information content.
    2) Less likely events should have higher information content.
    3) Independent events should have additive information. eg) 'a tossed coin gave heads twice' has twice as much information as 'a tossed coin gave heads once'
* **Self-information** of an event X=x:  
I(x) = -ln(P(x)) where P is some distribution,  
I(x) is written in units of **nats**.  
1 nats = Amount of info gained by observing an event of prob 1/e
* Self-info deals with only a single outcome. 
* Quantify the amount of uncertainty in an entire probability distribution using **Shannon entropy**  
(entropy = the amount of uncertainty)  
H(x) = E(I(x)) = -E(ln(P(x))) = H(P)  
* Tells us the expected amount of info in an event drawn from that dist.
* It gives a lower bound on the number of bits needed on average to encode symbols drawn from a dist P.
* Dist that are nearly deterministic have low entropy; dist that are closer to uniform have high entropy.
* When x = continuous, the Shannon entropy is known as **differential entropy**
* KL-divergence: measures the difference between two dist P and Q  
D(P||Q) = E{ln [P(x) / Q(x)]}
* Tells us the extra amount of info needed to send a message containing symbols drawn from prob. dist. P, when we use a code that has designed to minimize the length of message drawn from prob. dist. Q
* Is useful because it's non-negative.
* Is asymmetric i.e.) D(P||Q) =/= D(Q||P). Which one to minimize is problem dependent.
* **Cross-entropy** is closely related to KL-divergence.  
H(P,Q) = H(P) + D(P||Q)
* Minimizing cross-entropy with respect to Q is equivalent to minimizing KL divergence.
* When run into 0 ln 0, treat this as lim x &rarr; 0 x log x = 0

### Kernel Trick
* Good for midsized dataset
* Gaussian kernel is most commonly used.

### Stochastic Gradient Descent
* Uses a small portion of the dataset (i.e. minibatch) to calculate the gradients
* The idea is that it is computationally too expensive to calculate the gradient for each gradient step
* The minibatch is drawn uniformly from the training set

## Deep Networks: Modern Practice
### Deep Feedforward Network
#### Intro
* Also called **feedforward neural network** or **multilayer perceptrons(MLP)**
* 'feedforawrd' because information flows from x  
&rarr; the intermediate computations used to define f  
&rarr; to the output y
* If the network includes feedback connection, it is called **recurrent neural network**
* Consists of input layer, hidden layer, output layer
  
#### Gradient-based learning
* Most modern NN are trained using maximum likelihood(ml)
* Meaning cost function = -ve log-likelihood or **cross entropy** between the training data and the model distribution
* J(theta) = -E( ln p(y|x) )
* Softmax: Used when the output has n discrete outcomes. Each z in n has prob [0,1] and the sum of the z's = 1
* softmax(z) = exp(zi) / summation(exp(zi))
  
### Regularization
#### Intro
* Reduce the test errors at the expense of increased training error
* 3 major methods:  
    1) Put extra constraints on ML model eg) add restriction on parameter values
    2) Add extra terms in the objective functions
    3) Ensemble methods. Combine multiple hypotheses
  
#### Parameter norm penalties
* Add PNP term omega to the objective function J
* L2 parameter regularization (ridge regression)
* L1 parameter regularization (LASSO)
  
#### Bagging and dropout
##### Bagging
* Short for **bootstrap aggregating**.
* Reduce generalization error by training several models separately then have them vote on the output.
* The technique allows the same kind of model, algorithm, objective function to be reused several times.
* The techniques employing this strategy is called **Ensemble methods**.
* This is done by constructing k different bootstrap datasets (i.e. draw sample with replacement).
* Boosting: construct an ensemble with higher capacity than the individual models.  
Applied to add NNs to the ensemble, and to interpret an individual NN as an ensemble adding hidden units to the network  
  
##### Dropout
* Computationally less expensive than bagging but powerful regularization technique.
* This time, the models share the parameters, with each model inheriting a different subset of parameters from the parent NN
* Compare to bagging:
    - In bagging, each model is trained to convergence on its respective training set.
    - In dropout, most models are not explicitly trained at all. Only a small fraction of the possible subnetworks are each trained for a single step, and the parameter sharing causes the remaining subnetworks to arrive at good settings of the parameters.
* Take arithmetic or geometric mean of the outputs to get the prediction.
* Geometric mean has been demonstrated to have a better result than the arithmetic mean.
* Dropout is good when the dataset is large.
* For smaller datasets, Bayesian NN outperforms dropout.
* When additional unlabeled data is available, unsupervised feature learning is better.
* On linear models, dropout is equivalent to L2 weight decay with different weight decay coefficient for each input feature.
* However, for deep models, dropout is not equivalent to L2 or L1.
* Dropout prevents the weights from being dependent to each other.
* Destroying extracted feature rather than original values allows the destruction process to make use of all the knowledge about the input distribution that the model has acquired so far.
  
### Optimization for training deep models
* Aims to find theta of NN that significantly reduce the cost function J(theta)
#### Empirical risk minimization
* risk = Expected loss(residual)
* Since we don't know the true distribution P(x, y), we try to reduce the empirical risk by using P_hat(x, y)
* 1/m * summation(loss) where m = number of training examples
* Prone to overfitting. Not feasible. Rarely used.
* Need to have some other approach
#### Surrogate loss function
* The actuall loss function(eg. classification error) sometimes cannot be optimized efficiently.
* Typically optimize surrogate loss function instead(eg. log-likelihood surrogate on 0-1 loss) 

### Clustering
#### Gaussian Mixture Model (GMM)
* Assumes that the observations are generated from a mixture of several Gaussian distributions with unknown parameters.
* Each cluster can have a different ellipsoidal shape, size, density, etc.
