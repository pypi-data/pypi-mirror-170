# StarkChat
Stark chatbot client based on AIML

# Installation

```sh
pip3 install starkchat
```

# Example

```py
from StarkChat import starkchat

chatbot = starkchat.StarkChat()

while True:
    question = input("You: ")
    answer = chatbot.chat(question)
    print("Bot:", answer)
```

## Created and maintained by Sathishzus ❄️
