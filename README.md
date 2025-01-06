# RAG Research NextJS

A research project exploring Retrieval-Augmented Generation (RAG) implementations with NextJS frontend.

## Requirements

- Python ≥3.12
- uv package manager

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/rag-research-nextjs.git
cd rag-research-nextjs
```

2. Install dependencies using uv:

```bash
uv pip install .
```

## Key Dependencies

- FastAPI - Web framework for building APIs
- DSPy - Deep learning framework for language models
- LanceDB - Vector database for embeddings
- SentenceTransformers - For generating text embeddings
- Transformers (from source) - Hugging Face's transformer models

## Development

1. Create a `.env` file based on `.env.example` and set required environment variables

2. Start the development server:

```bash
uvicorn app.main:app --reload
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## MIT License

Copyright (c) 2024 Rafael Garcia

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
