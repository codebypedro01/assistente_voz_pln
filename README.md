# 🎙️ VoiceCommand Launcher – Assistente de Voz com Python

Este é um assistente de voz simples e funcional, desenvolvido em Python, capaz de reconhecer comandos de voz em português e executar ações como abrir o navegador, Excel, PowerPoint, entre outros programas no seu sistema Windows. O projeto é uma ótima introdução à integração entre Python, reconhecimento de fala e automação de tarefas no sistema operacional.

---

## ⚠️ Observação Importante

> **❗ Este script não é compatível com Python 3.13 ou versões superiores.**  
> Certifique-se de estar utilizando **Python 3.12 ou inferior** para garantir o funcionamento correto da biblioteca `speech_recognition` e dos recursos de áudio do sistema.  

Você pode verificar sua versão atual do Python executando:
```bash
python --version
```

---

## 🚀 Funcionalidades

- 🎧 Reconhecimento de voz com suporte ao idioma **português (pt-BR)**.
- 🤖 Interpretação de comandos falados em tempo real.
- 🖥️ Execução automática de aplicativos como:
  - Google Chrome
  - Microsoft Excel
  - Microsoft PowerPoint
  - Microsoft Edge
- 🛑 Comando de **encerramento** do script com a palavra-chave `"fechar"`.

---

## 🧠 Tecnologias e Bibliotecas Utilizadas

- [Python](https://www.python.org/) (versão 3.12 ou inferior)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [PyAudio](https://pypi.org/project/PyAudio/) *(necessário para captura de áudio via microfone)*
- `os` (módulo nativo do Python)

---

## 🔧 Pré-requisitos

Antes de rodar o script, instale as dependências:

```bash
pip install SpeechRecognition
pip install PyAudio
```

> 💡 **Importante**: O `PyAudio` pode ser difícil de instalar diretamente via `pip` em alguns sistemas. Caso encontre erros, recomenda-se instalar via `.whl` do [site oficial do PyAudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) para a sua versão do Python.

---

## ▶️ Como Executar

1. Clone o repositório ou copie o código-fonte.
2. Certifique-se de ter um microfone configurado e funcional.
3. Execute o script com:

```bash
python voice_command.py
```

4. Diga comandos como:
   - `"navegador"` → abre o Google Chrome
   - `"Excel"` → abre o Microsoft Excel
   - `"powerpoint"` → abre o Microsoft PowerPoint
   - `"Edge"` → abre o Microsoft Edge
   - `"fechar"` → encerra o assistente

---

## 🛑 Limitações e Considerações

- A aplicação depende do Google Web Speech API, portanto **requer conexão com a internet**.
- O reconhecimento de voz pode variar conforme a qualidade do microfone e o nível de ruído ambiente.
- O script foi desenvolvido para **Windows**, e os comandos `os.system('start app.exe')` podem não funcionar em outros sistemas operacionais.

---

## 📂 Estrutura do Projeto

```
voice-command/
│
├── voice_command.py       # Script principal com reconhecimento e execução de comandos
├── README.md              # Este arquivo de documentação
```

---

## 📌 Futuras Melhorias

- Adição de interface gráfica com feedback visual (GUI).
- Suporte a comandos personalizados configuráveis.
- Adaptação multiplataforma (Linux, macOS).
- Feedback sonoro com biblioteca `pyttsx3`.

---

## 👨‍💻 Autor

Desenvolvido por **Pedro**, com o auxílio do **bootcamp da XP Inc em parceria com a DIO** na trilha de **Cloud Computing com Inteligência Artificial**.  
🔗 *Aplicações reais com Python e automação no dia a dia*

---

## 🛡️ Licença

Este projeto é de uso educacional e livre. Sinta-se à vontade para modificar e expandir conforme necessário.
