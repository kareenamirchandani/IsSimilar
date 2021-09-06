def grading_function(body: dict) -> dict:
    """
    Function used to grade a student response.
    ---
    The handler function passes only one argument to grading_function(),
    which is a dictionary of the structure of the API request body
    deserialised from JSON.

    The output of this function is what is returned as the API response
    and therefore must be JSON-encodable. This is also subject to
    standard response specifications.

    Any standard python library may be used, as well as any package
    available on pip (provided it is added to requirements.txt).

    The way you wish to structure you code (all in this function, or
    split into many) is entirely up to you. All that matters are the
    return types and that grading_function() is the main function used
    to output the grading response.
    """

    diff_mode = body["params"]["diff_mode"]
    diff = body["params"]["diff"]
    res = body["response"]
    ans = body["answer"]

    is_correct = None
    real_diff = None

    if diff_mode == "absolute":
        is_correct = res >= ans - diff and res <= ans + diff
        real_diff = res - ans

    elif diff_mode == "relative":
        is_correct = res >= ans * (1 - diff) and res <= ans * (1 + diff)
        real_diff = (res / ans) - 1

    return {"is_correct": is_correct, "real_diff": real_diff}
