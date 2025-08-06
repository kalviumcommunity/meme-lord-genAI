# 🤖 MemeLord CLI

A viral-quality meme generator powered by Google's Gemini AI. Transform any topic into internet gold with GenZ humor and deep meme culture knowledge.

## 🚀 Features

- **AI-Powered Meme Generation**: Uses Gemini with specialized prompts for authentic meme creation
- **Structured Output**: JSON format with template, text, and metadata
- **Adjustable Creativity**: `--wild`, `--safe`, `--balanced` modes
- **Function Calling**: Helper functions for templates, captions, and rendering
- **RAG Integration**: Local corpus of meme formats and trending topics
- **ASCII Art**: Terminal-rendered memes
- **Export Options**: Save as Markdown, JSON, or text

## � Requirements

- Python 3.8 or higher
- Google Gemini API key
- Internet connection for API calls

## �📦 Installation

```bash
git clone https://github.com/kalviumcommunity/meme-lord-genAI.git
cd meme-lord-genAI
pip install -r requirements.txt
```

Set your Gemini API key:
```bash
export GEMINI_API_KEY="your_api_key_here"
```

## 🎯 Usage

```bash
# Basic meme generation
python memelord.py "Tech layoffs in 2025"

# Creativity modes
python memelord.py "My code broke on Monday" --wild
python memelord.py "Remote work struggles" --safe

# Random surprise meme
python memelord.py --random

# Export options
python memelord.py "AI replacing developers" --save markdown
```

## 📋 Output Format

```json
{
  "template": "Drake Hotline Bling",
  "top_text": "Using legacy systems",
  "bottom_text": "Switching to AI workflows", 
  "humor_type": "Tech irony",
  "alt_text": "Drake rejecting outdated tech, smiling at AI"
}
```

## 🏗️ Architecture

```
memelord/
├── memelord.py           # Main CLI entry point
├── core/
│   ├── gemini_client.py  # Gemini API integration
│   ├── prompts.py        # System prompts & templates
│   └── output_parser.py  # JSON structure validation
├── rag/
│   ├── meme_corpus.json  # Meme formats database
│   └── retrieval.py      # RAG implementation
├── utils/
│   ├── ascii_renderer.py # Terminal meme display
│   └── exporters.py      # Save functionality
└── requirements.txt
```

## 🎨 CLI Flags

- `--wild`: Maximum creativity (temp=0.9)
- `--safe`: Conservative humor (temp=0.3)  
- `--balanced`: Default mode (temp=0.6)
- `--random`: Generate random topic meme
- `--save [format]`: Export as markdown/json/txt
- `--ascii`: Render ASCII version in terminal

## 🤝 Contributing

We welcome contributions to make MemeLord even more legendary! Here's how you can help:

### Getting Started
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and test them
4. Commit your changes: `git commit -m 'Add amazing feature'`
5. Push to your branch: `git push origin feature/amazing-feature`
6. Open a Pull Request

### Guidelines
- Ensure your code follows Python best practices
- Add tests for new features
- Update documentation as needed
- Keep memes appropriately dank and inclusive
- Test with different creativity modes

### Ideas for Contributions
- New meme templates
- Additional export formats
- Performance optimizations
- Better error handling
- More creativity modes

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini AI for powering the meme generation
- The meme community for endless inspiration
- Contributors who make this project awesome
