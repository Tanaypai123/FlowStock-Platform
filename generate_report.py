#!/usr/bin/env python3
"""
FlowStock Report Generator Wrapper
Delegates to scripts/generate_report.py for backward compatibility.
"""
import os
import sys

script_path = os.path.join(os.path.dirname(__file__), "scripts", "generate_report.py")
if os.path.exists(script_path):
    with open(script_path, "r", encoding="utf-8") as f:
        code = compile(f.read(), script_path, "exec")
        exec(code, globals())
else:
    print(f"[ERROR] scripts/generate_report.py not found at {script_path}")
    sys.exit(1)
