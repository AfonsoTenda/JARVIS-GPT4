# Jarvis: Modular Workshop Assistant
![Jarvis Logo](https://i.imgur.com/VZCCfYh.png)

Jarvis is your ultimate workshop assistant, powered by GPT4. Inspired by Iron Man's J.A.R.V.I.S., this real-world implementation is designed to streamline your workshop activities with intuitive voice commands and smart automation.

Instructables - https://www.instructables.com/JARVIS-Workshop-Assistant-Tool/
## Features

- **🧠Intelligent Voice Interface:** Interact with Jarvis using natural language commands for a seamless workshop experience.
- **🛠️Modular Design:** Customize Jarvis to suit your workshop needs with easily integratable modules.
- **🤖Task Automation:** Let Jarvis handle repetitive tasks like inventory management, task reminders, and more.
- **💡Smart Lights Control:** Turn your workshop lights on or off effortlessly with support for Tuya and Wiz smart lights.
- **🏙️Extensibility:** Expand Jarvis's capabilities by integrating with your favorite tools and services.

## Smart Lights Control

Jarvis supports seamless control of your workshop environment with smart lights compatibility. Use voice commands to manage your lights and create the perfect ambiance for productivity.

### Supported Commands

- "Jarvis, turn on the lights."
- "Jarvis, turn off the lights."
- "Activate workshop lights."
- "Deactivate workshop lights."
- You can ask it any questions and it will respond based on a GPT4 reply.
- Other commands that you can add since this project is modular.

## Necessary supplies
- 🍊Orange Pi 3 LTS (With Ubuntu on the SD Card)
- ⚙️3D printer and Filament
- 💡3 LEDS
- 🔊1 Buzzer

The last 3 are only if you want to make a the case.

### 3D Printable Case

![Jarvis Case](https://i.imgur.com/ex3FbFj.png)

Printables: https://www.printables.com/model/855254-jarvis-modular-workshop-assistant

## Getting Started

To get started with Jarvis:

1. **Clone the Repository:**
```bash
git clone https://github.com/AfonsoTenda/JARVIS-GPT4.git
```
2. **Install Ubuntu Dependencies:**
```bash
sudo apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 espeak python3-pip python3-pyaudio flac -y 
```
3. **Install Python Dependencies:** 
```bash 
cd JARVIS-GPT4
pip install -r requirements.txt
```
4. **Install Wiring OP:** Instructions in https://github.com/zhaolei/WiringOP 
5. **Configure it:** INSTRUCTABLES - https://www.instructables.com/JARVIS-Workshop-Assistant-Tool/
6. **Start it:**
```bash
bash start.sh
```

## Contributing

We welcome contributions! If you have ideas, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
