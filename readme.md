# IsSimilar Grading Script

This simple grading script checks if the supplied response is within a tolerance range defined in `params`. Works exactly like the [numpy.isclose](https://numpy.org/doc/stable/reference/generated/numpy.isclose.html#numpy.isclose) function.

Valid params include `atol` and `rtol`, which can be used in combination, or alone. As the comparison made is the following:

```python
is_correct = abs(res - ans) <= (atol + rtol*abs(ans))
```

```json
{
  "response": "<number>",
  "answer": "<number>",
  "params": {
    "atol": "<number>",
    "rtol": "<number>"
  }
}
```

## `atol`

Absolute tolerance parameter

## `rtol`

Relative tolerance parameter
