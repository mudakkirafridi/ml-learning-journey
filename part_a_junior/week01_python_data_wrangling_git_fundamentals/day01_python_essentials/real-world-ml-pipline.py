"""
BEGINNER-FRIENDLY ML WORKFLOW
Predict if a customer will purchase
Using Python essentials (lists, dicts, OOP)
"""

import random
from typing import List, Dict, Tuple

# ============================================
# STEP 1: CONFIGURATION (Dictionary)
# ============================================

CONFIG = {
    "data": {
        "num_customers": 100,
        "random_seed": 42
    },
    "training": {
        "test_ratio": 0.2
    },
    "model": {
        "threshold": 50   # spending score threshold
    }
}

# ============================================
# STEP 2: DATA GENERATION (Lists + Functions)
# ============================================

def generate_customer_data(config: Dict) -> List[Dict]:
    """
    Generate fake customer data.
    Each customer has:
    - age
    - income
    - spending_score
    - purchased (0 or 1)
    """
    random.seed(config["data"]["random_seed"])
    customers = []

    for _ in range(config["data"]["num_customers"]):
        age = random.randint(18, 60)
        income = random.randint(20000, 100000)
        spending_score = random.randint(0, 100)

        # Simple rule to simulate purchase
        purchased = 1 if spending_score > 50 else 0

        customers.append({
            "age": age,
            "income": income,
            "spending_score": spending_score,
            "purchased": purchased
        })

    return customers


# ============================================
# STEP 3: TRAIN / TEST SPLIT
# ============================================

def train_test_split(data: List[Dict], test_ratio: float) -> Tuple[List, List]:
    split_index = int(len(data) * (1 - test_ratio))
    return data[:split_index], data[split_index:]


# ============================================
# STEP 4: MODEL CLASS (OOP)
# ============================================

class PurchasePredictor:
    """
    Very simple rule-based model.
    If spending_score > threshold → predict purchase.
    """

    def __init__(self, threshold: int):
        self.threshold = threshold
        self.trained = False

    def fit(self, data: List[Dict]):
        """
        In real ML, we would learn parameters.
        Here we just simulate training.
        """
        print("Training model...")
        self.trained = True

    def predict(self, customer: Dict) -> int:
        if not self.trained:
            raise Exception("Model not trained yet!")

        if customer["spending_score"] > self.threshold:
            return 1
        return 0

    def evaluate(self, test_data: List[Dict]) -> float:
        correct = 0

        for customer in test_data:
            prediction = self.predict(customer)
            if prediction == customer["purchased"]:
                correct += 1

        accuracy = correct / len(test_data)
        return accuracy


# ============================================
# STEP 5: MAIN PIPELINE
# ============================================

def main():
    print("=" * 50)
    print("🚀 CUSTOMER PURCHASE ML SYSTEM")
    print("=" * 50)

    # 1. Generate Data
    print("\n📦 Generating data...")
    data = generate_customer_data(CONFIG)
    print(f"Total customers: {len(data)}")

    # 2. Split Data
    train_data, test_data = train_test_split(
        data,
        CONFIG["training"]["test_ratio"]
    )

    print(f"Train size: {len(train_data)}")
    print(f"Test size: {len(test_data)}")

    # 3. Initialize Model
    model = PurchasePredictor(
        threshold=CONFIG["model"]["threshold"]
    )

    # 4. Train
    model.fit(train_data)

    # 5. Evaluate
    accuracy = model.evaluate(test_data)

    print("\n📊 Model Performance:")
    print(f"Accuracy: {accuracy:.2f}")

    print("\n✅ Pipeline Complete!")


if __name__ == "__main__":
    main()