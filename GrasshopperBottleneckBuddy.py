"""Collects & sorts all GH_Components by runtime (descending).
   Also highlights one chosen by rank (1 = slowest).
   Inputs:
       run:  Boolean toggle to execute
       rank: Integer rank of slow component to highlight
   Outputs:
       names: Sorted list of all component names (slowest -> fastest)
       times: Parallel list of their execution times (ms)
"""

import Grasshopper
import Grasshopper.Kernel as ghk

if not run:
    # If 'run' is False, do nothing; output empty
    names = []
    times = []
else:
    # Try to get the current Grasshopper document
    doc = ghenv.Component.OnPingDocument()
    if doc is None:
        print("DEBUG: No GH document found!")
        names = ["No document found"]
        times = [0.0]
    else:
        print("DEBUG: GH document retrieved successfully.")
        
        # (1) Unselect everything to start fresh (optional)
        for obj in doc.Objects:
            obj.Attributes.Selected = False

        # (2) Gather GH_Components with their times
        comps_with_times = []
        for obj in doc.Objects:
            if isinstance(obj, ghk.GH_Component):
                ms = obj.ProcessorTime.TotalMilliseconds
                comp_name = obj.NickName or obj.Name
                comps_with_times.append((obj, comp_name, ms))

        # Debug: How many components did we find?
        print("DEBUG: Found {} GH_Components.".format(len(comps_with_times)))
        for c_obj, c_name, c_ms in comps_with_times:
            print("   - {}: {} ms".format(c_name, c_ms))

        # (3) Sort descending by time
        comps_with_times.sort(key=lambda x: x[2], reverse=True)

        print("\nDEBUG: After sorting by descending time:")
        for i, (c_obj, c_name, c_ms) in enumerate(comps_with_times, start=1):
            print("   {}. {} -> {} ms".format(i, c_name, c_ms))

        # (4) Highlight the chosen rank (1-based)
        if 1 <= rank <= len(comps_with_times):
            selected_obj, selected_name, selected_time = comps_with_times[rank - 1]
            selected_obj.Attributes.Selected = True
            print("\nDEBUG: rank = {} => Selecting '{}', {} ms.".format(
                rank, selected_name, selected_time))
        else:
            print("\nDEBUG: rank = {} is out of range (only {} GH_Components).".format(
                rank, len(comps_with_times)))

        # (5) Output parallel lists: names + times (all components)
        names = [item[1] for item in comps_with_times]  # sorted from slowest -> fastest
        times = [item[2] for item in comps_with_times]
