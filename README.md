# GrasshopperBottleneckBuddy
Collects and sorts all Grasshopper components (`GH_Component`) by their execution time, helping you identify performance bottlenecks in your definitions.

---

## Features
- **Lists all `GH_Component`s** found in the current document.
- **Sorts by execution time** (descending), so you see the slowest components first.
- **Outputs component names** and their **times in milliseconds** in parallel lists.
- **Lightweight and straightforward** GHPython code, easy to modify or extend.

---

## Requirements
- **Rhino 6 or later** (running Grasshopper).
- **Grasshopper** 1.0 or later.
- **GHPython** component installed by default in Grasshopper.

---

## Installation & Usage

1. **Add a GHPython component** to the Grasshopper canvas.
2. **Rename Inputs** (if desired):
   - `run` (Boolean): When `True`, the script executes.
3. **Rename Outputs**:
   - `names` (Text): The sorted component names (slowest first).
   - `times` (Number): Corresponding execution times (ms).
4. **Connect a Toggle** (or Button) to `run`. Leave it `False` until you’re ready.
5. **Open the GHPython Editor** (double-click the component) and paste the script below.
