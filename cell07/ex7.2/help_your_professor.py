def average(student_scores):
    """
    Calculates the average score of students in a dictionary.

    Args:
        student_scores (dict): A dictionary where keys are student names and values are scores.

    Returns:
        float: The average score.
    """
    if not student_scores:  # Handle empty dictionary case
        return 0.0
    total_score = sum(student_scores.values())
    return total_score / len(student_scores)

if __name__ == "__main__":
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
    }
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
    }
    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")