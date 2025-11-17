#!/usr/bin/env python3
"""Simple addition utility.

Provides an `addition` function and a tiny CLI for adding two integers.
Usage: pass two integers as command-line args or enter them interactively.
Returns 0 on success; non-zero exit codes indicate invalid input or errors.
Prints a helpful error message on invalid input.
"""

from __future__ import annotations
import sys
from typing import Sequence


def addition(a: int, b: int) -> int:
	"""Return the sum of two integers.

	Args:
		a: first integer
		b: second integer

	Returns:
		Sum of a and b.
	"""
	return a + b


def main(argv: Sequence[str] | None = None) -> int:
	"""Parse inputs and print the sum. Returns exit code.

	If two command-line arguments are provided, they are parsed as integers.
	Otherwise the user is prompted to enter two integers.
	"""
	argv = list(argv) if argv is not None else list(sys.argv[1:])

	if len(argv) >= 2:
		try:
			a = int(argv[0])
			b = int(argv[1])
		except ValueError:
			print("Error: both arguments must be integers.")
			return 2
	else:
		try:
			a = int(input("Enter first integer: ").strip())
			b = int(input("Enter second integer: ").strip())
		except ValueError:
			print("Error: input must be integers.")
			return 2

	result = addition(a, b)
	print("The sum for the two numbers is", result)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())