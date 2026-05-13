import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def build_loan_default_tree():
    # Step 1: Generate synthetic dataset
    np.random.seed(42)
    n = 500

    data = pd.DataFrame({
        "income": np.random.randint(20000, 150000, n),
        "age": np.random.randint(18, 70, n),
        "loan_amount": np.random.randint(5000, 50000, n),
        "credit_score": np.random.randint(300, 850, n),
        "employment_years": np.random.randint(0, 40, n)
    })

    # Step 2: Create binary target
    data["default"] = np.where(
        (data["credit_score"] < 500) & (data["loan_amount"] > 15000),
        1,
        0
    )

    X = data.drop("default", axis=1)
    y = data["default"]

    # Step 3: Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Step 4: Train DecisionTreeClassifier
    model = DecisionTreeClassifier(
        max_depth=3,
        criterion='gini',
        random_state=42
    )
    model.fit(X_train, y_train)

    # Step 5: Predict and print classification report
    y_pred = model.predict(X_test)
    
    print("Classification Report:\n")
    report = classification_report(y_test, y_pred, output_dict=True)
    print(classification_report(y_test, y_pred))

    # Step 6: Extract and print top feature by importance
    feature_importances = pd.Series(
        model.feature_importances_,
        index=X.columns
    ).sort_values(ascending=False)

    top_feature = feature_importances.index[0]
    print(f"Top Feature by Importance: {top_feature}")

    # Step 7: Check if any class recall < 0.60
    recall_class_0 = report['0']['recall']
    recall_class_1 = report['1']['recall']

    recall_below_threshold = (recall_class_0 < 0.60) or (recall_class_1 < 0.60)
    
    print(f"Is any class recall below 0.60? {'Yes' if recall_below_threshold else 'No'}")


if __name__ == "__main__":
    build_loan_default_tree()
