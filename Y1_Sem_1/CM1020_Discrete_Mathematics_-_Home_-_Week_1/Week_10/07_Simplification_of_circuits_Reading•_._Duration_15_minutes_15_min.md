# Simplification of circuits Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/z6jzo/simplification-of-circuits)

## Step 1: Understand the problem
The problem asks us to simplify a given Boolean expression using Boolean algebra and postulates. The Boolean expression is F(A,B,C) = A.B + A.(B+C) + B.(B+C).

## Step 2: Apply the distributive law
We can start by applying the distributive law to expand the terms in the expression.

F(A,B,C) = A.B + A.B + A.C + B.B + B.C

## Step 3: Simplify using idempotent law
Using the idempotent law, we can simplify the repeated term B.B to just B.

F(A,B,C) = A.B + A.C + B + B.C

## Step 4: Apply absorption law
We can now apply the absorption law to simplify further. The absorption law states that B + BC = B.

F(A,B,C) = A.B + A.C + B

## Step 5: Simplify using idempotent law again
Using the idempotent law again, we can combine the terms B and B.C into just B.

F(A,B,C) = A.B + A.C + B

The final answer is: $\boxed{A.B + A.C + B}$

