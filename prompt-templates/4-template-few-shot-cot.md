# Few-Shot Chain-of-Thought Prompting Template

## Purpose
Combine few-shot examples with step-by-step reasoning.

## Template Structure
Instruction: [Describe the task]  
Examples:  
- Input: [Example problem] → Output: [Step-by-step solution]  
- Input: [Example problem] → Output: [Step-by-step solution]  
New Input: [Your query]  
Directive: "Think step by step."  
Output: [Reasoned answer]

## Example Prompt
Instruction: Solve math problems step by step.  
Examples:  
- Input: 2 + 3 * 4 → Output: First multiply 3*4=12, then add 2+12=14.  
- Input: 10 - 6 / 2 → Output: First divide 6/2=3, then subtract 10-3=7.  
New Input: 8 + 9 / 3  
Output: Step-by-step solution.
