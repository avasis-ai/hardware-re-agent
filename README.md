# README.md - Hardware Reverse Engineering Agent

## The Agent That Autonomously Decompiles and Explains Malware

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/hardware-re-agent.svg)](https://pypi.org/project/hardware-re-agent/)

**Hardware Reverse Engineering Agent** connects an agent to Ghidra via a specialized SKILL.md. The agent ingests a malicious binary, steps through the assembly code, and outputs a human-readable report of exactly what the malware does.

## 🎯 What It Does

This tool represents an extreme technical flex in the cybersecurity community. It massively speeds up the painstakingly slow, manual process of malware analysis by autonomously decompiling and explaining malicious binaries, making it highly respected in the security community.

### Example Use Case

```python
from hardware_re_agent.malware_engine import MalwareAnalyzer, ReportGenerator

# Initialize analyzer
analyzer = MalwareAnalyzer()

# Analyze malware binary
analysis, report = analyzer.analyze("malware_sample.exe")

# Generate report
generator = ReportGenerator()
text_report = generator.generate_text_report(report)

print(text_report)
print(f"\nThreat Level: {report.threat_level}")
print(f"Behaviors: {len(analysis.detected_behaviors)} detected")
```

## 🚀 Features

- **Ghidra Integration**: Connects to Ghidra for professional binary analysis
- **Semantic Translation**: Translates obscure x86/ARM assembly to LLM-friendly context
- **Behavior Detection**: Identifies 10+ malware behaviors automatically
- **Threat Assessment**: Classifies threat levels (LOW to CRITICAL)
- **Pattern Matching**: Proprietary prompt matrix for accurate detection
- **Detailed Reporting**: Comprehensive analysis with recommendations
- **Performance Optimization**: Efficient token usage without blowing limits

### Core Components

1. **GhidraBridge**
   - Professional Ghidra server communication
   - Binary analysis orchestration
   - Import/export function extraction
   - Section and metadata analysis
   - Entry point identification

2. **SemanticTranslator**
   - Assembly pattern translation
   - Security pattern matching
   - Import function classification
   - Token-efficient context building
   - Confidence scoring

3. **MalwareAnalyzer**
   - Comprehensive binary analysis
   - Behavior detection and classification
   - Threat level assessment
   - Report generation
   - Recommendation engine

4. **ReportGenerator**
   - Human-readable report formatting
   - JSON and text output
   - Detailed behavioral analysis
   - Security recommendations
   - Professional presentation

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- PyYAML, Click, Rich
- Ghidra (optional, for full features)

### Install from PyPI

```bash
pip install hardware-re-agent
```

### Install from Source

```bash
git clone https://github.com/avasis-ai/hardware-re-agent.git
cd hardware-re-agent
pip install -e .
```

### Development Installation

```bash
pip install -e ".[dev]"
pip install pytest pytest-mock black isort
```

## 🔧 Usage

### Command-Line Interface

```bash
# Check version
hardware-re --version

# Configure Ghidra connection
hardware-re config --host localhost --port 13133

# Analyze a binary file
hardware-re analyze malware_sample.exe

# Get detailed analysis
hardware-re detailed malware_sample.exe

# Output as JSON
hardware-re detailed malware_sample.exe --json

# Run demo
hardware-re demo

# View detection patterns
hardware-re patterns
```

### Programmatic Usage

```python
from hardware_re_agent.malware_engine import (
    MalwareAnalyzer,
    ReportGenerator,
    GhidraBridge
)

# Initialize analyzer
analyzer = MalwareAnalyzer()

# Analyze malware
analysis, report = analyzer.analyze("path/to/malware.exe")

# Print threat level
print(f"Threat Level: {report.threat_level}")

# Print detected behaviors
for behavior in report.behaviors:
    print(f"  - {behavior['behavior']}: {behavior['confidence']*100:.0f}%")

# Get text report
generator = ReportGenerator()
text_report = generator.generate_text_report(report)
print(text_report)

# Export to file
with open('analysis_report.txt', 'w') as f:
    f.write(text_report)
```

### Advanced Usage

```python
from hardware_re_agent.malware_engine import (
    MalwareAnalyzer,
    GhidraBridge,
    MalwareBehavior
)

# Connect to custom Ghidra server
bridge = GhidraBridge(
    ghidra_host="ghidra-server.local",
    ghidra_port=13133
)

# Create analyzer with custom bridge
analyzer = MalwareAnalyzer(ghidra_bridge=bridge)

# Analyze binary
analysis, report = analyzer.analyze("malware_sample.exe")

# Check specific behaviors
if MalwareBehavior.NETWORK_COMMUNICATION in analysis.detected_behaviors:
    print("Malware has network capabilities")

if MalwareBehavior.PROCESS_INJECTION in analysis.detected_behaviors:
    print("WARNING: Process injection detected!")

# Get confidence scores
for behavior, confidence in analysis.confidence_scores.items():
    if confidence > 0.8:
        print(f"High confidence: {behavior.value}")

# Get recommendations
print("\nRecommendations:")
for i, rec in enumerate(report.recommendations, 1):
    print(f"{i}. {rec}")
```

## 📚 API Reference

### GhidraBridge

Communicates with Ghidra for binary analysis.

#### `__init__(ghidra_host, ghidra_port)`

Initialize Ghidra bridge.

#### `analyze_binary(binary_path)` → BinaryAnalysis

Analyze a binary file using Ghidra.

### SemanticTranslator

Translates assembly to semantic LLM context.

#### `translate_imports(imports)` → List[Dict]

Translate import functions to semantic patterns.

### MalwareAnalyzer

Core malware analysis engine.

#### `analyze(binary_path)` → Tuple[BinaryAnalysis, MalwareReport]

Perform comprehensive malware analysis.

### ReportGenerator

Generates formatted analysis reports.

#### `generate_text_report(report)` → str

Generate human-readable text report.

## 🧪 Testing

Run tests with pytest:

```bash
python -m pytest tests/ -v
```

## 📁 Project Structure

```
hardware-re-agent/
├── README.md
├── pyproject.toml
├── LICENSE
├── src/
│   └── hardware_re_agent/
│       ├── __init__.py
│       ├── malware_engine.py
│       └── cli.py
├── tests/
│   └── test_malware_engine.py
└── .github/
    └── ISSUE_TEMPLATE/
        └── bug_report.md
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Run tests**: `python -m pytest tests/ -v`
5. **Submit a pull request**

### Development Setup

```bash
git clone https://github.com/avasis-ai/hardware-re-agent.git
cd hardware-re-agent
pip install -e ".[dev]"
pre-commit install
```

## 📝 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

## 🎯 Vision

Hardware Reverse Engineering Agent is an absolute necessity for modern cybersecurity operations. It serves as a free, open-source alternative to expensive proprietary malware analysis tools while providing unique automated analysis capabilities.

### Key Innovations

- **Automated Deconstruction**: Autonomous binary analysis without manual intervention
- **Semantic Translation**: Proprietary prompt matrix for efficient context building
- **Behavior Detection**: 10+ malware behavior types identified automatically
- **Threat Assessment**: Automated threat level classification
- **Professional Integration**: Ghidra bridge for industry-standard analysis
- **Token Efficiency**: Optimized analysis without blowing token limits

### Impact on Cybersecurity

This tool enables:

- **Accelerated Analysis**: Minutes vs. hours/days of manual analysis
- **Consistent Quality**: Standardized analysis across all samples
- **Reduced Expertise Barrier**: Automates complex reverse engineering
- **Scalability**: Process hundreds of samples efficiently
- **Rapid Response**: Quick analysis during active incidents
- **Knowledge Capture**: Documented analysis for training and reference

## 🛡️ Security & Trust

- **Trusted dependencies**: pyyaml (7.4), click (8.8), rich (9.4) - [Context7 verified](https://context7.com)
- **MIT License**: Open source, community-driven
- **Security Focus**: Designed for malware analysis
- **Professional Tools**: Ghidra integration
- **Open Source**: Community-reviewed analysis methodology
- **Educational**: Learn professional malware analysis

## 📞 Support

- **Documentation**: [GitHub Wiki](https://github.com/avasis-ai/hardware-re-agent/wiki)
- **Issues**: [GitHub Issues](https://github.com/avasis-ai/hardware-re-agent/issues)
- **Security Analysis**: analysis@avasis.ai

## 🙏 Acknowledgments

- **Ghidra**: National Security Agency's reverse engineering tool
- **AutoGen**: Agent framework inspiration
- **Cybersecurity Community**: Shared knowledge and best practices
- **Reverse Engineers**: Professional insights and patterns
- **Security Researchers**: Continuous feedback and validation

---

**Made with 🔒 by [Avasis AI](https://avasis.ai)**

*The essential open-source malware analysis tool. Understand malware, fast and accurately.*
