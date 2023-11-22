"""
reference.py

Module for handling references
"""
# pylint: disable=import-error, no-name-in-module
from src.references.reference import Reference

def create_reference(author: str, title: str, year: str):
    """
    Module function for creating Reference object
    """
    ref = Reference(author, title, year)

    return ref
