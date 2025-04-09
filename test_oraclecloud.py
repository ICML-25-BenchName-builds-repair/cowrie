#!/usr/bin/env python3
"""
Test script for oraclecloud.py to verify linting issues are fixed
"""

import sys
import subprocess

def run_ruff_check():
    """Run ruff check on oraclecloud.py and return the output"""
    result = subprocess.run(
        ["ruff", "check", "src/cowrie/output/oraclecloud.py"],
        capture_output=True,
        text=True
    )
    return result.stdout, result.returncode

if __name__ == "__main__":
    print("Running ruff check on oraclecloud.py...")
    output, exit_code = run_ruff_check()
    print(output)
    
    if exit_code == 0:
        print("Success! No linting issues found.")
        sys.exit(0)
    else:
        print(f"Failed! Linting issues found. Exit code: {exit_code}")
        sys.exit(1)