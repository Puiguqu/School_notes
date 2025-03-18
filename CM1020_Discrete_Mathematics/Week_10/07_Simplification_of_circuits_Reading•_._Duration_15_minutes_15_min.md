# Simplification of circuits Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-discrete-mathematics/supplement/z6jzo/simplification-of-circuits)

Here are the key points from the text:

The simplification of circuits using Boolean algebra involves applying postulates and theorems to reduce complexity and simplify digital circuits.

A common technique for simplifying Boolean expressions is by using rules of Boolean algebra such as distributive law, idempotent law, absorption law.

Consider a circuit with two OR gates and three AND gates. The output F(A,B,C) can be simplified using Boolean algebra as follows:

F(A,B,C) = A.B + A.(B+C) + B.(B+C)

By applying the distributive law, we get:

F(A,B,C) = A.B + A.B + A.C + B.B + B.C

Using idempotent law and absorption law, we simplify further:

F(A,B,C) = A.B + A.C + B + B.C

This simplifies to:

F(A,B,C) = B + AC

The original circuit can be simplified to two basic digital logic gates: an AND gate and an OR gate.

Another way of simplifying circuits is by using a Karnaugh map to simplify the corresponding Boolean expression.

