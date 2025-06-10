# Deployment Guide for Google Cloud

## Prerequisites

1. Install Google Cloud SDK
2. Have a Google Cloud Project created
3. Enable required APIs:
   - Cloud Run API
   - Cloud Build API
   - Container Registry API

## Local Testing with Docker

1. Build the Docker image:
```bash
docker build -t revid-api .
```

2. Run with docker-compose:
```bash
docker-compose up
```

## Deploy to Google Cloud Run

### Option 1: Using Cloud Build (Recommended)

1. Set up environment variables in Google Cloud Secret Manager:
```bash
gcloud secrets create api-key --data-file=- <<< "your-revid-api-key"
gcloud secrets create openai-api-key --data-file=- <<< "your-openai-api-key"
gcloud secrets create music-ms-token --data-file=- <<< "your-music-ms-token"
```

2. Submit build to Cloud Build:
```bash
gcloud builds submit --config cloudbuild.yaml \
  --substitutions=_API_KEY=$(gcloud secrets versions access latest --secret=api-key),_OPEN_AI_API_KEY=$(gcloud secrets versions access latest --secret=openai-api-key),_MUSIC_MS_TOKEN=$(gcloud secrets versions access latest --secret=music-ms-token)
```

### Option 2: Manual Deployment

1. Build and push to Container Registry:
```bash
# Configure Docker for GCR
gcloud auth configure-docker

# Build image
docker build -t gcr.io/YOUR_PROJECT_ID/revid-api .

# Push to GCR
docker push gcr.io/YOUR_PROJECT_ID/revid-api
```

2. Deploy to Cloud Run:
```bash
gcloud run deploy revid-api \
  --image gcr.io/YOUR_PROJECT_ID/revid-api \
  --platform managed \
  --region us-central1 \
  --port 5001 \
  --allow-unauthenticated \
  --set-env-vars API_KEY=your-api-key,OPEN_AI_API_KEY=your-openai-key,MUSIC_MS_TOKEN=your-ms-token
```

## Environment Variables

Make sure to set these environment variables:
- `API_KEY`: Your Revid AI API key
- `OPEN_AI_API_KEY`: Your OpenAI API key
- `MUSIC_MS_TOKEN`: Your TikTok music service token

## Accessing Your Deployed Service

After deployment, Cloud Run will provide you with a URL like:
```
https://revid-api-xxxxx-uc.a.run.app
```

You can test it by visiting the root endpoint:
```
curl https://revid-api-xxxxx-uc.a.run.app/
```