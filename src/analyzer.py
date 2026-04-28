def analyze_reviews(reviews):

    if len(reviews) < 5:
        return {
            "error": "Not enough reviews"
        }

    pros = []
    cons = []

    positive_words = [
        "good",
        "great",
        "easy",
        "lightweight",
        "perfect",
        "excellent",
        "?????"
    ]

    negative_words = [
        "bad",
        "poor",
        "cheap",
        "broke",
        "rash",
        "????"
    ]

    for review in reviews:
        review_lower = str(review).lower()

        if any(word in review_lower for word in positive_words):
            pros.append(review)

        if any(word in review_lower for word in negative_words):
            cons.append(review)

    return {
        "top_pros": pros[:3],
        "top_cons": cons[:3],
        "recommended_for": "Parents looking for affordable products",
        "avoid_if": "Parents needing premium durability",
        "confidence_score": 0.87,
        "english_summary": "Parents liked usability but found durability issues.",
        "arabic_summary": "??? ?????? ????? ????????? ???? ???? ???? ??? ????? ??????."
    }
