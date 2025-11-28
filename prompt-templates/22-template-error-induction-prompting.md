# Error-Induction Prompting Template

## Purpose
Provide a flawed example and ask the model to correct it.

## Template Structure
Instruction: [Describe the correction task]  
Example: [Insert flawed or incorrect response]  
Directive: "Identify and correct the errors."  
Output: [Corrected answer]

## Example Prompt
Instruction: Correct the following flawed code.  
Example: def add(a, b): return a - b  
Directive: Identify and correct the errors.  
Output: def add(a, b): return a + b
