import re


class Pattern:
    """
    Precompiled regular expressions for deconstructing Java code.
    """

    # Matches: visibility scope, type, name.
    TYPES = re.compile(r"\b(.*)(class|record|interface|enum)\s+(\w+(?:<.*?>)?)")

    # Matches: (Visibility, Generic, Static?); Return type; Method name; Parameters.
    METHOD = re.compile(r"\b\s*(.*?)?(\w+)\s+(\w+)\((.*)\) *(.*{|;)")

    # Matches: Generic type declaration (<T>)
    GENERIC = re.compile(r"^<\w+>")

    # regex will watch all after extends/implements; need to split('implements')[0] ig
    IMPLEMENTS = re.compile(r"implements ([\w<., >_$]+)")

    EXTENDS = re.compile(r"extends ([\w<., >_$]+)")

    THROWS = re.compile(r"throws ([\w<., >_$]+)")

    # Matches: Visibility scope?; Static?; Return type; Field name; Equals?.
    FIELD = re.compile(
        r"\b(private|protected|public)?\s*(static\s+)?([a-zA-Z0-9_$<>]+)\s+([a-zA-Z0-9_$]+)(\s*[=][^;]+)?\s*;"
    )
