# ===========================================
# Simple Recommendation System
# Author: Sauvik Sharma
# ===========================================

# Dataset of items and their categories
recommendations = {
    "Python Programming": ["python", "coding", "programming", "ai", "data science"],
    "Machine Learning": ["ai", "machine learning", "python", "data science"],
    "Web Development": ["html", "css", "javascript", "web", "coding"],
    "Mobile App Development": ["android", "ios", "flutter", "coding"],
    "Cyber Security": ["security", "network", "hacking", "linux"],
    "Cloud Computing": ["aws", "azure", "cloud", "devops"],
    "Data Analytics": ["data", "excel", "sql", "power bi"],
    "Graphic Design": ["photoshop", "illustrator", "design"],
    "Photography": ["camera", "photo", "editing"],
    "Digital Marketing": ["marketing", "seo", "social media"],
    "Artificial Intelligence": ["ai", "deep learning", "python"],
    "Game Development": ["unity", "games", "c#", "coding"],
}

print("=" * 55)
print("     SIMPLE RECOMMENDATION SYSTEM")
print("=" * 55)

print("\nEnter your interests separated by commas.")
print("Example: python, ai, coding\n")

# User input
user_input = input("Your interests: ").lower()

# Convert input into list
user_preferences = [item.strip() for item in user_input.split(",")]

scores = {}

# Matching Logic
for item, tags in recommendations.items():
    score = 0

    for preference in user_preferences:
        if preference in tags:
            score += 1

    if score > 0:
        scores[item] = score

# Display Results
print("\n" + "=" * 55)

if scores:
    print("Recommended for You\n")

    # Sort by highest score
    sorted_items = sorted(scores.items(),
                          key=lambda x: x[1],
                          reverse=True)

    for i, (item, score) in enumerate(sorted_items, start=1):
        print(f"{i}. {item} (Match Score: {score})")
else:
    print("No exact recommendations found.")
    print("Try different interests.")

print("=" * 55)