# Task 1
shopping_list = [
    {"item": "Milk", "price": 50},
    {"item": "Bread", "price": 30},
    {"item": "Eggs", "price": 60},
    {"item": "Rice", "price": 120}
]

shopping_list.append({"item": "Butter", "price": 80})
shopping_list.pop(0)                                  
print("Number of items now:", len(shopping_list))
#Task 2
total_cost = sum(item["price"] for item in shopping_list)
costly_item = {"price": 0}
for item in shopping_list:
    if item["price"] > costly_item["price"]:
        costly_item = item

print("Most expensive item:", costly_item["item"], "-", costly_item["price"])
print("Total cost:", total_cost)
#Task 3
summary = {
    "total_items": len(shopping_list),
    "total_cost": total_cost,
    "average_price": round(total_cost / len(shopping_list))
}

print(summary)
