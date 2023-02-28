import openai
import pandas as pd

openai.api_key = "YOUR_KEY"


def rate_review(review):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(
            f"Rate the following review on a scale of 1 to 10, "
            f"where 1 is negative and 10 is positive:"
            f"\n\n{review}\n\nRating:"
        ),
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.5,
    )
    rating = int(response.choices[0].text.strip())
    return rating


df = pd.read_csv("reviews.csv")
df["rate"] = df["review text"].apply(rate_review)
df = df.sort_values(by=["rate"], ascending=False)

filename = "reviews.csv"
output_filename = f"{filename.split('.')[0]}_analyzed.csv"
df.to_csv(output_filename, index=False)
