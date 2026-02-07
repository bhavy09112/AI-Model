# AI Hackathon Model with Groq

A Python project for building AI models using the Groq API for fast inference.

## Project Structure

```
├── src/                    # Source code
│   ├── main.py            # Main entry point
│   └── groq_client.py     # Groq API client module
├── models/                # Trained models storage
├── data/                  # Data files
├── notebooks/             # Jupyter notebooks for experimentation
├── .env.example           # Environment variables template
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Setup

### 1. Clone the repository
```bash
git clone <repository-url>
cd "AI Model"
```

### 2. Create a virtual environment
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # On Windows PowerShell
# or
venv\Scripts\activate.bat    # On Windows Command Prompt
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Groq API
- Get your API key from [Groq Console](https://console.groq.com)
- Copy `.env.example` to `.env`
- Add your Groq API key to `.env`:
```
GROQ_API_KEY=your_actual_api_key
GROQ_MODEL=mixtral-8x7b-32768
```

### 5. Run the project
```bash
python src/main.py
```

## Available Groq Models

- `mixtral-8x7b-32768` - Default high-performance model
- `llama-2-70b-chat` - Meta's Llama 2 70B Chat
- `gemma-7b-it` - Google's Gemma 7B Instruct

Check [Groq Documentation](https://console.groq.com/docs) for the latest models.

## Usage

### Quick Start Example

```python
from src.groq_client import GroqClient

# Initialize client
client = GroqClient()

# Get a simple completion
response = client.get_completion("What is AI?")
print(response)

# Have a chat conversation
messages = [
    {"role": "user", "content": "Hello, how are you?"},
]
response = client.get_chat_response(messages)
print(response)
```

## Development

### Running Notebooks
```bash
jupyter notebook
```

Then navigate to the `notebooks/` directory.

## Contributing

1. Create a feature branch (`git checkout -b feature/your-feature`)
2. Commit your changes (`git commit -am 'Add your feature'`)
3. Push to the branch (`git push origin feature/your-feature`)
4. Open a Pull Request

## License

MIT License

## Resources

- [Groq Documentation](https://console.groq.com/docs)
- [Groq Python SDK](https://github.com/groq/groq-python)
- [Hackathon Information](#) - Add your hackathon link here

## Notes for Hackathon

- Remember to add your `.env` file to `.gitignore` (already done)
- Never commit your API keys
- Test your code regularly with Groq's fast inference
- Use the notebooks directory for experimentation and documentation
