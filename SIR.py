### ENGR 102 - Lab 4.
### Due Friday, March 26 at 11:59pm

## To turn in - upload SIR.py to Canvas.


### Based on Ch 11 of Modeling and Simulation in Python.

## The SIR model is a common model for studying the spread of disease in a population.
### It breaks the population into three groups:
## 1. susceptible (s)- the fraction who are vulnerable to the disease
## 2. Infected. (i) The fraction who currently have the disease.
## 3. Recovered. (r) The fraction who have had the disease and developed immunity

## Note that this assumes that you can only get the disease once, and that everyone recovers.

## SIR uses two parameters:
# beta, which is the rate at which people contact each other, and
# gamma, which is the recovery rate, or the fraction of people who recover each day.

### so,
## if there are N people in a population:
## sN is the number of susceptible people
## beta * sN is the number of contacts those people have.
## beta * i * sN is the number of contacts where an infection might spread. (for now, let's assume that the
# probability of spread is 100%.

## so, we expect there to be: gamma * i * N people recovering each day.

## and we expect there to be: beta * s * i * N new infections per day.
## alternatively, beta * s *i is the fraction of the population that is infected every day.

## This is an example of what's called a compartment model. There are three groups of people, and individuals move
## between those groups.

## So how do we implement this?
## To do so, we're going to use a new Python construct called a class. A class lets us define our own data types,
## rather than being limited to the built-in ones. Let's make a class called State.

class State :
    def __init__(self, s, i, r):
        self.s = s
        self.i = i
        self.r = r

## So what's going on here?
## The class keyword says that we're creating a State. Each instance of a State is referred to as an object.
## __init__ is what's called a constructor. It's the method that's called when we create a new State.
## self is a built-in keyword that objects use to refer to themselves. It's an implicit parameter - when we
## create a new state, Python passes it in for us.

## We can create a State like so:

state1 = State(.0, .3, .6)

## note that we're storing the fraction in each group, not the total.

## let's assume that we know beta and gamma
beta = 0.3
gamma = 0.25

## We might also want to track our states through time, so that we can easily distinguish days from each other.
## So let's add a time variable.

class State :
    def __init__(self, s, i, r, t):
        self.s = s
        self.i = i
        self.r = r
        self.time = t

    def __repr__(self):
        return "(%.2f %.2f %.2f)" % (self.s, self.i, self.r)

## 1. Create five different states with different s,i,r, and t values.

## Now, we need to be able to update the world. Let's do this with a function called update.

def update(currentState, beta, gamma) :

    currentTime = currentState.time
    newlyInfected = beta * currentState.i * currentState.s
    newlyRecovered = gamma * currentState.i
    newS = currentState.s - newlyInfected
    newI = currentState.i + newlyInfected - newlyRecovered
    newR = currentState.r + newlyRecovered
    return State(newS, newI, newR, currentTime + 1)

## 2. Try writing a for loop to start with 90% of the population susceptible and 10% infected and run for 20 iterations.\\
## At each iteration, print out S,I,R and time.
## what happens?
## What if we increase beta?
## What if we increase gamma?










### Now let's capture and plot the data. Rather than just printing out the data, let's store all the states in a list
## as they're generated.

stateList = []

### copy your loop from above, but add in:
# s0 = update(s0, beta, gamma)
# stateList.append(s0)

## now, we want to make a plot of this. Let's start by importing matplotlib
import matplotlib.pyplot as plt

## We need to get the separate member vsariables out of our list of States.
## We can do this with a list comprehension.
## for example:
[item.s for item in stateList]

## 3.
#Create a plot showing the S, I and R values over time when beta is 0.3 and gamma is 0.25.
#Create a second plot with beta=0.75 and gamma 0.25
# Create a third plot with beta = 0.3 and gamma = 0.75.




## 4. add in vaccination

def vaccinate(currentState, vaxRate) :
    currentState.s -= vaxRate
    currentState.r += vaxRate



## 5. add in hand washing

def handWashing(beta, factor) :
   return beta * factor

## Run the simulation once more with beta - 0.35, comparing hand washing and not handwashing.

## Now let's count the total number of people infected. Let's make ourselves a function to help out.

def simulate(beta, gamma) :
    totalStudents = 100
    currentState = State(0.9, 0.1, 0, 1)
    totalInfected = 0
    for i in range(50) :
        newlyInfected = beta * currentState.i * currentState.s
        totalInfected += newlyInfected
        currentState = update(currentState, beta, gamma)
    return totalInfected * totalStudents

## now, let's see how the number of people infected changes as hand-washing becomes more effective.
## Write a function which contains a loop that calls simulate 8 times, for handwashing factors of
# 0.1, 0.2, ...,0.9, captures the total number of students infected, and then plots those.





