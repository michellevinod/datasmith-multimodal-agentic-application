def explain_code(code_text):

    code_lower = code_text.lower()

    language = "Unknown"

    # Language Detection

    if "def " in code_text:
        language = "Python"

    elif "#include" in code_text:
        language = "C/C++"

    elif "public class" in code_text:
        language = "Java"

    elif "console.log" in code_text:
        language = "JavaScript"


    # Default Responses

    explanation = (
        "The code processes data and "
        "performs logical operations."
    )

    possible_bug = (
        "No major bug detected, "
        "but edge case handling "
        "should be verified."
    )

    complexity = "O(n)"


    # Search Detection

    if (
        "search" in code_lower
        or "binary search" in code_lower
    ):

        explanation = (
            "This code searches for an "
            "element inside a collection "
            "or array."
        )

        possible_bug = (
            "Ensure the target element "
            "exists and boundary "
            "conditions are handled."
        )

        complexity = "O(log n)"


    # Sorting Detection

    elif (
        "sort" in code_lower
        or "bubble" in code_lower
        or "selection" in code_lower
    ):

        explanation = (
            "This code sorts elements "
            "into a specific order."
        )

        possible_bug = (
            "Nested loops may reduce "
            "performance on large datasets."
        )

        complexity = "O(n²)"


    # Factorial Detection

    elif "factorial" in code_lower:

        explanation = (
            "This code calculates the "
            "factorial of a number using "
            "iteration or recursion."
        )

        possible_bug = (
            "Large input values may "
            "cause recursion depth or "
            "overflow issues."
        )

        complexity = "O(n)"


    # Nested Loop Detection

    if (
        code_lower.count("for") >= 2
    ):

        complexity = "O(n²)"


    return f"""
    Code Analysis
    -------------------

    Programming Language:
    {language}

    Explanation:
    {explanation}

    Possible Bug / Warning:
    {possible_bug}

    Estimated Time Complexity:
    {complexity}
    """