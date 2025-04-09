# score_calculator.py

def calculate_total_and_average(scores):
    total = sum(scores)
    average = total / len(scores) if scores else 0
    return {"total": total, "average": average}

