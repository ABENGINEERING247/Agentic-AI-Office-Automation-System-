# Deployment Instructions

## Option 1: Streamlit Community Cloud (Free & Easy)

1. Push your repository to GitHub.
2. Log into [share.streamlit.io](https://share.streamlit.io/).
3. Select your repository, branch (`main`), and set the main file path to `app.py`.
4. (Optional) Add your `OPENAI_API_KEY` under **Advanced Settings -> Secrets**.
5. Click **Deploy**!

## Option 2: Docker Container

Create a `Dockerfile` with the following contents:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:
```bash
docker build -t agentic-ai-office .
docker run -p 8501:8501 agentic-ai-office
```
