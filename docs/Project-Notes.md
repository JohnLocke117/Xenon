# Xenon Project Notes

### Docstring Format
It is mandatory to add a proper docstring at:
- Module Level (Top of File)
- Functions
- Classes

In this project, we're going ahead with Google-Styled Docstrings:

```python
def calculate_velocity(distance: float, time: float) -> float:
    """
    Calculates the Average Velocity of a moving object.

    This section provides an optional extended description of the 
    function and its overall purpose.

    Args:
        distance: The total physical distance covered in meters
        time: The total time duration taken in seconds
    
    Returns:
        The computed average velocity in meters per second
    
    Raises:
        ValueError: If the time parameter is less than or equal to zero.
    """

    if time <= 0:
        raise ValueError("Time must be a non-zero positive value")
    
    return distance / time
```

```python
class SmartDevice:
    """Represents a basic connected household IoT appliance.

    Class docstrings summarize the object's purpose. Public attributes
    are explicitly declared in the Attributes section.

    Attributes:
        device_id: A unique string identifier for the hardware.
        status: The current operational state (e.g., "online").
    """

    def __init__(self, device_id: str):
        """Initializes the SmartDevice instance.

        Args:
            device_id: The unique identifier assigned to the hardware.
        """
        self.device_id = device_id
        self.status = "offline"
```

