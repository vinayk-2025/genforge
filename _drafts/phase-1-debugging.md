 

# 🐞 Phase 1 - Debugging Installation Issues
📅 **Date**: 17-11-2025  
👨‍🏫 Curated by: Satya Prakash Nigam  

This guide helps students resolve common installation and configuration errors encountered during Phase 1 environment setup.


## 👤 Git Identity Missing
**Symptom:** Commits show “unknown author” or push fails.  
**Fix:**  
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```
Verify with `git config --list`.


## 🤖 Ollama Model Download Fails
**Symptom:** `ollama run tinyllama` errors out.  
**Fix:**  
- Run `ollama pull tinyllama` explicitly.  
- Check firewall/proxy settings.  
- Ensure disk space is available.  


## 🧪 Jupyter Notebook Issues
**Symptom:** `jupyter notebook` fails to launch.  
**Fix:**  
- Ensure `pip install notebook` is run.  
- Add `%USERPROFILE%\AppData\Roaming\Python\Scripts` to PATH (Windows).  
- Try `jupyter lab` as alternative.


## License
This guide is licensed under **CC BY-NC 4.0**  
You may share and adapt with attribution - but commercial use is prohibited  
🔗 [License Details](https://creativecommons.org/licenses/by-nc/4.0)

