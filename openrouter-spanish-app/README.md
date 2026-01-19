# Maestro Español MX (Next.js)

A Next.js app built for Vercel that translates English phrases into Mexican Spanish using OpenRouter, then generates custom practice, study guides, and quizzes based on your translation history.

## Setup

```bash
cd openrouter-spanish-app
cp .env.example .env.local
npm install
npm run dev
```

Open http://localhost:3000

## Environment Variables

- `OPENROUTER_API_KEY` (required): Your OpenRouter API key.
- `OPENROUTER_APP_URL` (optional): Used for the `HTTP-Referer` header.

## Deploy to Vercel

1. Push this repo to GitHub.
2. Create a new Vercel project pointing to `openrouter-spanish-app` as the root directory.
3. Add the environment variables in the Vercel dashboard.
4. Deploy.

## Notes

- Translation history is stored in the browser (localStorage). Add a database if you want cross-device history or user accounts.
- OpenRouter model is set to `openrouter/auto` for flexibility; adjust in `lib/openrouter.ts` if you want a fixed model.
