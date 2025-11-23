# XPhrase Generation v1.0.2

**Release Date:** November 23th, 2025

Released on 	2025/11/22 	

Last updated 	2025/11/23

Publisher 	[gerivanc](https://github.com/gerivanc/)

Changelog [Changelog]https://github.com/gerivanc/xphrase/blob/main/CHANGELOG.md)

Release Notes [RELEASE.md](https://github.com/gerivanc/xphrase/blob/main/RELEASE.md)

Reporting Issues	[Report a](https://github.com/gerivanc/xphrase/issues/new/choose)

---

## 📋 Overview
**XPhrase Generation** is a multilingual phrase generator designed for command-line interface (CLI) usage.  
It creates expressive, randomized phrases using words from **Portuguese**, **English**, and **German**, interlinked with special characters and digits.
The principle of randomness enables the generation of over 12.6 trillion unique combinations by interconnecting words from three languages, along with the inclusion of special characters and numerical digits.

This project is:
- 💯 Written 100% in Python
- 🖥️ CLI-compatible for Linux and Windows
- 🌐 The CLI project has been fully converted to the web version of the HTML interface, maintaining the same phrase generation method, now accessible directly in your browser.

---

## 🌍 INTERACTIVE WEB VERSION

Experience the XPhrase Generation directly in your browser! The web version offers all the functionality of the Python script in an intuitive and responsive interface.

### 🚀 Access the Web Version

<div align="center">
  
[**🌐 Try It Now on XPhrase Generation**](https://xphrase.gerivan.me/xphrase.html)

</div>

### ⚡ Interactive Demo

<div align="center">

[**📚 Interactive Readme**](https://xphrase.gerivan.me/)

</div>

---

# 📋 Requirements

- Python 3.8+
- No external dependencies
- Works on:
  - ✅ Linux (Debian, Ubuntu, Arch, etc.)
  - ✅ Windows (PowerShell, CMD)

---

# 💾 Installation

Cloning the repository to install packages.

```
git clone https://github.com/gerivanc/xphrase.git
cd xphrase
```


---

# 📟 COMMAND LINE INTERFACE - CLI

## 🛠️ Support for CLI arguments - Command line usage:

**Generate single phrase with 8 words (default):**
```
python xphrase.py
```

**Generate single phrase with specific word count (5-10 words):**
```
python xphrase.py --count 5    # 1 phrase with 5 words
python xphrase.py --count 6    # 1 phrase with 6 words
python xphrase.py --count 7    # 1 phrase with 7 words
python xphrase.py --count 8    # 1 phrase with 8 words
python xphrase.py --count 9    # 1 phrase with 9 words
python xphrase.py --count 10   # 1 phrase with 10 words
```

**Generate phrases with custom word range, 1 phrase with 5-10 random words:**
```
python xphrase.py --min 5 --max 10
```

**Show version:**
```
python xphrase.py --version
```

**Interactive mode:**
```
python xphrase.py --interactive
```

---

### 🎮 Interactive Mode
**XPhrase Generation - Expressive phrase generator**  
==================================================

**Options:**

1. **Generate single phrase**  
   - Asks: "generate between 3-21 words?"  
   - Generates one phrase with the specified word count (3-21 words)

2. **Generate multiple phrases**  
   - First asks: "generate between 3-21 words?" (words per phrase)  
   - Then asks: "generate between 5-10 phrases?" (number of phrases)  
   - Generates multiple phrases with consistent word count

3. **Exit**  
   - Closes the phrase generator

---

## 📬 Feedback
Help us improve by reporting issues using our [issue template](https://github.com/gerivanc/xphrase/blob/main/.github/ISSUE_TEMPLATE/issue_template.md).

Thank you for supporting **XPhrase Generation**! 🚀🔑
---

#### Copyright © 2025 Gerivan Costa dos Santos
