# MomzVerdict AI

### AI-powered product review summarization for Mumzworld

Parents shopping on Mumzworld often face hundreds of reviews for a single product.  
Reading all of them is time-consuming and frustrating.

This project solves that problem by converting **200 multilingual product reviews (English + Arabic)** into a structured shopping verdict that helps parents make faster purchase decisions.

## project folder should now look like:

C:\Users\chand\OneDrive\Desktop\mumzworld-ai
│
├── main.py
├── generate_reviews.py
├── README.md
├── EVALS.md
├── TRADEOFFS.md
├── requirements.txt
│
├── data
│   └── reviews.csv
│
└── src
    ├── data_loader.py
    ├── review_analyzer.py
    └── validator.py

# Problem Statement

A parent looking at a stroller may see:

- hundreds of reviews  
- repeated feedback  
- fake/noisy opinions  
- mixed sentiments  


# Why I Chose This Problem

I selected this because:

- It directly impacts ecommerce conversion
- It solves real review overload
- It was specifically mentioned in Mumzworld’s examples
- It allows meaningful AI engineering within a realistic 5-hour scope

I intentionally avoided overcomplicated ideas like:

- Voice assistants  
- Medical triage systems  
- Full recommendation engines  

Those would have been harder to ship reliably in limited time.

---

# How It Works

### Step 1: Review ingestion
The system loads **200 synthetic product reviews**

- 150 English reviews  
- 50 Arabic reviews  

---

### Step 2: Embedding generation
Reviews are converted into vector embeddings using:

`SentenceTransformer (all-MiniLM-L6-v2)`

This helps identify similar reviews.

---

### Step 3: Review clustering
Using:

`KMeans clustering`

The system groups similar feedback patterns together.

Example:

- portability feedback
- durability complaints
- comfort feedback

---

### Step 4: Sentiment extraction
The system identifies recurring positive and negative feedback.

---

### Step 5: Structured output generation
Final output includes:

- Top pros
- Top cons
- Recommendation
- Avoid recommendation
- Confidence score
- English summary
- Arabic summary

---

### Step 6: Uncertainty handling
If reviews are insufficient:

```json
{
  "error": "Insufficient reviews for reliable recommendation"
}
```

The model avoids hallucinating unsupported conclusions.

---

# Example Output

```json
{
  "reviews_processed": 200,
  "clusters_created": 5,
  "top_pros": [
    "Lightweight and travel-friendly"
  ],
  "top_cons": [
    "Durability concerns"
  ],
  "confidence_score": 0.82
}
```

---

# Tech Stack

- Python
- Pandas
- Sentence Transformers
- Scikit-learn
- JSON
- Synthetic multilingual dataset

---

# How to Run

Clone repo:

```bash
git clone <your-repo-link>
cd mumzworld-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

# Evaluation

I tested the system across:

- Positive-only reviews
- Negative-only reviews
- Mixed sentiment reviews
- Arabic reviews
- Duplicate reviews
- Low review volume
- Noisy reviews
- Conflicting reviews

Detailed results are included in:

`EVALS.md`

---

# Tradeoffs

I prioritized:

- reliability
- explainability
- fast execution

instead of:

- heavy UI work
- expensive APIs
- over-engineered infrastructure

More details:

`TRADEOFFS.md`

---

# Future Improvements

Given more time I would add:

- OpenRouter LLM summarization
- Fake review detection
- Real-time review ingestion
- Better Arabic NLP support
- Product dashboard UI

---

# Time Spent

~5–6 hours total

Most time was spent debugging environment issues and improving AI pipeline depth.

---

# Final Thought

The goal of this project was not to build a flashy demo.

It was to build something practical that Mumzworld could realistically use to reduce review overload and improve customer decision-making.
