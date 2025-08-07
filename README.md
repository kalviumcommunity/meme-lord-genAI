# 🤖 MemeLord CLI

A viral-quality meme generator powered by Google's Gemini AI. Transform any topic into internet gold with GenZ humor and deep meme culture knowledge.

## 🧠 GenAI Implementation Details

### System & User Prompts
MemeLord uses carefully crafted system prompts to make Gemini act as a sarcastic, Gen Z meme expert with deep knowledge of internet culture. The prompts include:
- Meme format expertise and cultural context understanding
- Slang and internet language patterns for authentic humor
- Template-specific instructions for different meme formats
- Contextual awareness for current trends and references

### Structured Output
All meme responses follow a strict JSON schema ensuring consistency:
```json
{
  "template": "Popular meme format name",
  "top_text": "Setup text or reaction",
  "bottom_text": "Punchline or contrast",
  "humor_type": "Category of humor used",
  "alt_text": "Accessibility description",
  "confidence_score": 0.95,
  "trending_score": 0.87
}
```

### Function Calling Architecture
The CLI implements several specialized functions:
- `get_meme_templates()`: Retrieves available meme formats with usage stats
- `generate_caption(prompt, style, temperature)`: Creates contextual text
- `analyze_humor_type(content)`: Categorizes joke style
- `render_ascii_meme(template, texts)`: Terminal visualization
- `validate_output_structure(json)`: Ensures proper formatting

### RAG (Retrieval Augmented Generation)
Enhanced context through local knowledge base:
- **Meme Corpus**: 500+ popular meme formats with usage examples
- **Trend Database**: Current internet slang and viral topics
- **Template Metadata**: Success rates, audience preferences, cultural context
- **Dynamic Retrieval**: Matches user input to most relevant meme styles
- **Context Injection**: Provides Gemini with format-specific examples

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

## 🏗️ Architecture & Performance

```
memelord/
├── memelord.py           # Main CLI entry point
├── core/
│   ├── gemini_client.py  # Gemini API integration with rate limiting
│   ├── prompts.py        # System prompts & templates
│   └── output_parser.py  # JSON structure validation
├── rag/
│   ├── meme_corpus.json  # Meme formats database (500+ templates)
│   ├── trending_data.json # Current internet trends & slang
│   └── retrieval.py      # Efficient vector-based RAG
├── utils/
│   ├── ascii_renderer.py # Terminal meme display
│   ├── exporters.py      # Save functionality
│   └── cache.py          # Response caching for efficiency
└── requirements.txt
```

### Performance & Scalability Features
- **Caching System**: Reduces API calls by caching similar requests
- **Rate Limiting**: Handles API quotas gracefully with exponential backoff
- **Async Processing**: Non-blocking operations for better responsiveness  
- **Vector Search**: Efficient RAG retrieval using embeddings
- **Batch Processing**: Support for multiple meme generation
- **Memory Management**: Optimized for large corpus datasets

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
