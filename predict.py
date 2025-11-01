import pickle

# Load the saved model pipeline
with open("pipeline_v1.bin", "rb") as f_in:
    pipeline = pickle.load(f_in)

# Record to score
record = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

# Predict probability
X = [record]
proba = pipeline.predict_proba(X)[0, 1]

print(f"Probability that this lead will convert: {proba:.3f}")
