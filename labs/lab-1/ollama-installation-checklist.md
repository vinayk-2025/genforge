 

# 🧠 Ollama Installation Checklist
This guide walks you through installing Ollama, pulling local LLMs, and verifying prompt execution - all offline and free.


## ✅ Step 2: Pull a Local Model
Example: Pull TinyLLaMA (lightweight model for testing):

```bash
ollama pull tinyllama
```

Other available models:

```bash
ollama list
```


## ✅ Step 4: Use Ollama via Python (Optional)
Install Python bindings:

```bash
pip install ollama
```

Sample script:

```python
import ollama
response = ollama.chat(model='tinyllama', messages=[{'role': 'user', 'content': 'Tell me a joke'}])
print(response['message']['content'])
```


## License
This checklist is licensed under **CC BY-NC 4.0**  
You may share and adapt with attribution - but commercial use is prohibited  
🔗 [License Details](https://creativecommons.org/licenses/by-nc/4.0)

