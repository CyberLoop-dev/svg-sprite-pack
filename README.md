<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0d9488&height=170&section=header&text=SVG%20Sprite%20Pack&fontSize=40&fontColor=ffffff&animation=fadeIn" width="100%" alt="SVG Sprite Pack banner">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=21&pause=900&color=2DD4BF&center=true&vCenter=true&width=700&lines=Pack%20SVG%20icons%20into%20reusable%20symbol%20sprites" alt="Animated project title">
</p>
<p align="center">
<a href="https://github.com/CyberLoop-dev/svg-sprite-pack/blob/main/LICENSE"><img src="https://img.shields.io/github/license/CyberLoop-dev/svg-sprite-pack?style=flat-square" alt="License"></a>
<img src="https://img.shields.io/badge/language-Python-0d9488?style=flat-square" alt="Python">
<a href="https://github.com/CyberLoop-dev/svg-sprite-pack/stargazers"><img src="https://img.shields.io/github/stars/CyberLoop-dev/svg-sprite-pack?style=flat-square" alt="Stars"></a>
<img src="https://img.shields.io/github/last-commit/CyberLoop-dev/svg-sprite-pack?style=flat-square" alt="Last commit">
</p>
<p align="center"><img src="assets/icon.svg" width="520" alt="SVG Sprite Pack illustration"></p>

## 🧭 Overview
Combine a folder of SVG icons into one reusable symbol sprite for web interfaces.

## ✨ Features
- 🧩 Turn individual SVG files into reusable symbol elements.
- 🏷️ Create stable IDs from filenames and preserve each viewBox.
- 📁 Process a whole icon directory in one command.
- 🧪 Reject malformed SVG input with a clear filename-level error.

## 🖥️ Demo
~~~bash
python main.py examples/icons --output dist/icons.svg
~~~
Try it with the included sample input or your own local files.

## 🚀 Quick Start
~~~bash
git clone https://github.com/CyberLoop-dev/svg-sprite-pack.git
cd svg-sprite-pack
python main.py examples/icons --output dist/icons.svg
~~~

## 🧰 Tech Stack
- Python 3.10+
- xml.etree.ElementTree, pathlib, argparse (standard library)

## 🗂️ Folder Structure
~~~text
svg-sprite-pack/\n├── assets/icon.svg\n├── examples/icons/\n├── tests/test_main.py\n├── LICENSE\n├── README.md\n├── main.py\n└── requirements.txt
~~~

## 🗺️ Roadmap
- [ ] Add optional CSS class prefixing.
- [ ] Add a JSON manifest of generated symbol IDs.

## 🤝 Contributing
Issues and focused pull requests are welcome. Add tests for behavior changes and keep the project easy to run locally.

## 📄 License
Released under the MIT License. See LICENSE.

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d9488,100:111827&height=110&section=footer" width="100%" alt="Animated wave footer"></p>
