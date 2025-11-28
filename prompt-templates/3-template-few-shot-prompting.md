# Few-Shot Prompting Template

## Purpose
Use when a small set of examples guides the model toward the desired output style.

## Template Structure
Instruction: [Describe the task]  
Examples:  
- Input: [Example input 1] → Output: [Example output 1]  
- Input: [Example input 2] → Output: [Example output 2]  
New Input: [Your query]  
Output: [Model should follow example style]

## Example Prompt
Instruction: Translate English to French.  
Examples:  
- Input: Hello → Output: Bonjour  
- Input: Thank you → Output: Merci  
New Input: Good morning  
Output: [Expected translation]
