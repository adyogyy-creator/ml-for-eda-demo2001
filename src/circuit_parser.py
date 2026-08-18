"""
V1: Circuit parser for the ML-for-EDA demo.

This module will convert a simple circuit/netlist description
into a structured representation that later versions can
turn into a graph for machine learning.
"""

def parse_netlist(netlist_text):
    """Parse a simple gate-level netlist."""
    gates = []

    for line in netlist_text.strip().splitlines():
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        parts = line.split()

        if len(parts) >= 4:
            gate_type = parts[0]
            gate_name = parts[1]
            inputs = parts[2:-1]
            output = parts[-1]

            gates.append({
                "type": gate_type,
                "name": gate_name,
                "inputs": inputs,
                "output": output,
            })

    return gates