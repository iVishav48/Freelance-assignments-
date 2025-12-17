# Question 3 - Recursive Geometric Patterns

This question involves creating recursive geometric patterns using the Koch snowflake algorithm and turtle graphics.

## Problem Description
Implement a program that draws recursive geometric patterns based on user input for polygon sides, side length, and recursion depth.

## Algorithm Details
The program uses the Koch snowflake algorithm applied to regular polygons:

### Koch Edge Algorithm
- Base case (depth = 0): Draw straight line
- Recursive case: Divide line into 3 segments and create the classic Koch pattern:
  1. Draw first segment
  2. Turn left 60°, draw second segment
  3. Turn right 120°, draw third segment
  4. Turn left 60°, draw fourth segment

### Implementation Features
- **Interactive Input**: User specifies number of sides, side length, and recursion depth
- **Automatic Positioning**: Calculates radius to center the polygon
- **Visual Output**: Uses turtle graphics for drawing

## Files Available
- `v1.py` - Basic implementation with user input dialogs
- `v2.py` - Alternative implementation (may have variations)
- `v3.py` - Another variant implementation

## Usage
1. Run any of the Python files (`v1.py`, `v2.py`, or `v3.py`)
2. Enter the following when prompted:
   - Number of sides for the polygon
   - Side length of each edge
   - Recursion depth (higher = more detail)
3. The program will display the recursive pattern

## Examples
- **Triangle (3 sides)**: Creates Koch snowflake
- **Square (4 sides)**: Creates Koch square
- **Pentagon (5 sides)**: Creates Koch pentagon
- Higher recursion depths create more intricate patterns

## Requirements
- Python turtle graphics library
- Graphical display capability
