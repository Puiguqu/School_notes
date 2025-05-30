# CPU simulation Reading• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-how-computers-work/supplement/wGKjs/cpu-simulation)

Here is a summary of the text in 15 sentences:

The interactive simulation will teach how a CPU executes machine instructions by playing the part of the CPU. The simulation consists of a help text at the bottom, guides the user through each stage, and has registers on the right side. Registers are used to store values, and entering a value into a register requires pressing "return". Most instructions involve putting numbers into registers or using existing register values. Register numbers range from 0 to 7, but users should not use the actual values in the operands. Each turn, the user needs to press "Fetch Instruction" to get a new instruction. The instruction is fetched at the memory address in the programme counter. In most cases, the programme counter updates automatically, so no changes are needed. However, when using a JUMP instruction, the programmer must set the programme counter address manually. The MEMLOAD instruction loads data from memory by entering the memory address into the address field and pressing "Fetch". The value appears next to the Fetch button, which can be copied into a register. The MEMSTORE instruction writes values back to memory by putting the memory address in one field and the store value in another, then pressing "return" or "Store" if correct.

Here are some important details:

* Registers 0-7 are used for operands.
* Programme counter updates automatically, unless using JUMP instructions.
* MEMLOAD instruction loads data from memory by fetching at a specific address.
* MEMSTORE instruction writes values back to memory by storing in one field and pressing "Store" if correct.

Overall, the simulation focuses on understanding how a CPU executes machine instructions, including loading and storing data from memory.

