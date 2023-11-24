"""
reference.py

Module for handling references
"""
# pylint: disable=import-error, no-name-in-module
from src.references.reference import Reference

references = []

def create_reference(author: str, title: str, year: str):
    """
    Module function for creating Reference object
    """
    ref = Reference(author, title, year)
    references.append(ref)

    return ref

def get_references():
    """Returns current references"""
    return references
