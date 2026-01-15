# 🤠 Throw Me a Card, Pal!

A customized Discord bot for dice and card throwing — now featuring **Cowboy AI**, an intelligent assistant that answers **Sacramento RPG rule questions** directly from the rulebook.

Built to enhance immersion at the table, automate mechanics, and keep the game flowing smoothly.

---

## ✨ Features

### 🎲 Dice System
- Roll any dice format (`?1d20`, `?2d6+3`, `?4d6kl3`, `?2d20kh`)
- Modifier and keep-high/keep-low support

### 🃏 Card System
- Draw cards from a 52-card deck + Joker
- Shuffle deck anytime

### 💰 Coin Flip
- Simple heads or tails with `?coin`

### 🎵 Audio Effects
- Special sound effects for Jokers
- Fully immersive table experience

---

## 🤖 Cowboy AI — Sacramento Rule Assistant

Ask rule questions directly in Discord:

?rules Posso atacar duas vezes no mesmo turno?

Cowboy AI will:

- Search the Sacramento RPG book semantically  
- Locate the most relevant rule passages  
- Answer in natural language  
- Always cite the correct page  
- Never invent rules outside the provided text  

Powered by:

- SentenceTransformers embeddings  
- Hybrid vector + keyword search (SQLite)  
- Gemini LLM (Google AI)  
- Retrieval-Augmented Generation (RAG)

---

## ⚖️ Legal Notice

This repository does not include:

- The Sacramento RPG PDF  
- Extracted text pages  
- Generated chunks  
- Embedding database  

To use Cowboy AI, you must provide your legally acquired Sacramento RPG PDF locally and run the ingestion scripts to generate your own database.

No copyrighted content is distributed in this repository.

---

## 🧩 Project Structure

core/        -> RAG, embeddings, vector search, Gemini client  
commands/    -> Discord bot commands (dice, cards, rules, etc.)  
scripts/     -> PDF extraction, chunking, embedding generation  
data/        -> (local only) chunks and embeddings database  
assets/pdf/  -> (local only) Sacramento PDF  
bot.py       -> Discord bot entry point  

---

## ⚙️ Installation

### Prerequisites

- Python 3.9+
- pip
- Git
- FFmpeg (for audio)

---

### Clone repository

git clone https://github.com/yourusername/throw-me-a-card-pal.git  
cd throw-me-a-card-pal

---

### Create virtual environment

python -m venv venv  
source venv/bin/activate  
(Windows: venv\Scripts\activate)

---

### Install dependencies

pip install -r requirements.txt

---

## 🔑 Environment Variables

Create a .env file:

DISCORD_BOT_TOKEN=your_discord_bot_token  
GEMINI_API_KEY=your_gemini_api_key

---

## 📚 Building the Rulebook Database (Cowboy AI)

Place your legally acquired Sacramento RPG PDF:

assets/pdf/sacramento.pdf

Run the ingestion pipeline:

python scripts/extract_pdf.py  
python scripts/chunk_text.py  
python scripts/build_embeddings.py

This generates:

data/embeddings.db

Which Cowboy AI uses for semantic rule search.

---

## 🤠 Running the Bot

python bot.py

In Discord:

?rules How does the cover mechanic works?

---

## 🎮 Other Commands

### Cards
- ?card → draw a card  
- ?shuffle → reshuffle deck  

### Dice
- ?1d20  
- ?2d6+3  
- ?4d6kl3  
- ?2d20kh  

### Coin
- ?coin  

---

## 🔊 Audio Support

Joker sound effects live in:

music/

Ensure FFmpeg is installed and accessible in PATH.

---

## 🚀 Deployment

The bot can be deployed on Railway or any VPS.  
Just upload the project, provide .env variables, and include your locally generated data/embeddings.db.

---

## ❤️ Final Words

This project was built to make Sacramento RPG tables faster, smoother, and more immersive.

Saddle up — the West has rules, and Cowboy AI knows them.
