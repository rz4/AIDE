# AIDE - A.I. Development Environment
Version 0.1

Last Updated: **Feb. 14, 2016**

Lead Maintainer: [Rafael Zamora](https://github.com/rz4)

**AIDE** is a Java library for the development and testing of
intelligent agents. It is used to create and interface custom
agents and environments. It also contains tools to run
simulations and gather results.

**Agents** will have access to the following information:
- Array of legal *Actions* in an **Environment**.
- Array of *Percepts* passed from **Environment** each cycle.
- Array of *Goal Percepts* for the **Environment**.

Using this input information, the **Agents** should decide what
*Action* to take, and the **Environment** will be updated
according to the selected *Action*.

## Code Example
### Agents
The following is code used to define a **Random Agent**:

```java
public class RandomAgent extends Agent{

  private Random rand;

  public RandomAgent(){
    super();
    rand = new Random();
  }

  @Override
  public void compute() {
    updateGoals(nextPercepts);
    if(goalsActive()) setActive(false);
    else nextAction = possibleActions[rand.nextInt(possibleActions.length)];
  }

}
```
All agent behavior should be defined in the `compute()` method.
This method will be called during the simulation, after the
environment has passed `nextPercepts` to the agent and before the
environment updates using the agent's`nextAction'.

The **Random Agent** selects a random action from `possibleActions`. The
environment continues to pass on sensory information and actuate
the agent's actions as long as the agent is active.
`goalsActive()` is used to determine if the agents goals are met.
If all goals have been met, then the agent will be set inactive.
`updateGoals(nextPercept)` is used to check the goals against the
percepts, setting them inactive if they have been met.

## Motivation

This project is designed with the intention of rapid prototyping
agents and environments for A.I. research. The project will be
used to facilitate Artificial General Intelligence research by
creating a framework for agents to be tested in multiple unique
and unknown environments.

## Installation

Download and import AIDE.jar into Java project.

**Note:** AIDE is still under development and AIDE.jar may be
unavailable.

## Future Development
