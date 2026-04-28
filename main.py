import json
from src.data_loader import load_reviews
from src.review_analyzer import analyze_reviews


def main():
    print("\n==============================")
    print("      MomsVerdict AI")
    print("==============================")

    try:
        df = load_reviews()

        print("\nSample Reviews Loaded Successfully:")
        print(df.head())

        reviews = df["review"].tolist()

        result = analyze_reviews(reviews)

        print("\nFinal Structured Output:")
        print(json.dumps(result, indent=4, ensure_ascii=False))

    except FileNotFoundError:
        print("Error: reviews.csv file not found inside data folder")

    except KeyError:
        print("Error: 'review' column missing in reviews.csv")

    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()