import random


EMPLOYMENT_TYPES = [
    "Entrepreneur",
    "Gig Worker",
    "Government",
    "Retired",
    "Salaried",
    "Self-Employed"
]


def generate_sample_data():

    employment_type = random.choice(
        EMPLOYMENT_TYPES
    )

    if employment_type in [
        "Gig Worker",
        "Retired"
    ]:
        employed = "No"
    else:
        employed = "Yes"

    return {
        "age": random.randint(21, 75),
        "income": random.randint(15000, 250000),
        "credit_score": random.randint(300, 900),
        "existing_loans": random.randint(0, 5),
        "existing_loan_emi": random.randint(4000, 18000),
        "employed": employed,
        "loan_amount": random.randint(
            50000,
            2000000
        ),
        "loan_tenure_months": random.choice(
            [12, 18, 24, 30, 36]
        ),
        "employment_type": employment_type
    }