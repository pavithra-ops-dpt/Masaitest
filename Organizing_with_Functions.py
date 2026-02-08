def calculate_grade(*score,**adjustments):
  average = sum(score)/len(score)
  bonus = sum(adjustments.values())
  final_grade= average + bonus
  return final_grade
  
  
  
grade1=calculate_grade(85,90,78)
print(f"Final Grade:{grade1:.2f}%")
grade2=calculate_grade(70,65,80)
print(f"Final Grade:{grade1:.2f}%")
