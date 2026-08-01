# Xenon Project Notes

### Docstring Format

It is mandatory to add a proper docstring at:

- Module Level (Top of File)
- Functions
- Classes

In this project, we're going ahead with Google-Styled Docstrings:

```python
"""
<One-line summary of the module's responsibility>.

<Optional extended description: key concepts, how it fits in the app, important dependencies or side effects. 1–3 sentences max unless warranted.>
"""
```

```python
def fn(arg: str, *, flag: bool = False) -> ReturnType:
    """
    <Imperative summary>

    <Optional extended description.>

    Args:
        arg: <What it represents, constraints, valid values.>
        flag: <What it controls.>

    Returns:
        <What is returned and when.>

    Raises:
        <ExceptionType>: <When/why.>

    Yields:
        <For generators/async generators — what each iteration produces.>
    """
```

```python
class MyClass:
    """
    <One-line summary of what this type represents or does>.

    <Optional extended description.>

    Attributes:
        field_name: <Meaning, not just the type.>

    Note:
        <Important behaviour, invariants, or side effects.>
    """
```

