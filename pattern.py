import re


class Pattern:
    """
    Precompiled regular expressions 
    for deconstructing Java code.
    """

    # Matches: visibility scope, type, name.
    TYPES = (
        re.compile(r"\b(.*)(class|record|interface|enum)\s+(\w+(?:<.*?>)?)")
    )

    # Matches: (Visibility, Generic, Static?);
    # Return type; Method name; Parameters.
    METHOD = re.compile(r"\b\s*(.*?)?(\w+)\s+(\w+)\((.*)\)")

    # Matches: Generic type declaration (<T>)
    GENERIC = re.compile(r"^<\w+>")

    # regex will capture all after extends/implements;
    # need to split('implements')[0]
    IMPLEMENTS = re.compile(r"implements ([\w<., >_$]+)")

    EXTENDS = re.compile(r"extends ([\w<., >_$]+)")

    THROWS = re.compile(r"throws ([\w<., >_$]+)")
