# IsSimilar

This simple evaluation function checks if the supplied response is within a tolerance range defined in `params`. Works exactly like the [numpy.isclose](https://numpy.org/doc/stable/reference/generated/numpy.isclose.html#numpy.isclose) function.

Valid params include `atol` and `rtol`, which can be used in combination, or alone. As the comparison made is the following:

```python
is_correct = abs(res - ans) <= (atol + rtol*abs(ans))
```

## Inputs

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

### `atol`

Absolute tolerance parameter

### `rtol`

Relative tolerance parameter

## Outputs
```json
{
  "is_correct": "<bool>",
  "real_diff": "<number>",
  "allowed_diff": "<number>",
}
```

### `real_diff`
Real difference between the given answer and response

### `allowed_diff`
Allowed difference between answer and response, calculated using the supplied `atol` and `rtol` parameters


## Examples