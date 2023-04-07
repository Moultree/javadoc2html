from __future__ import annotations

from dataclasses import dataclass, field


banned_keywords = [
    "assert",
    "break",
    "case",
    "catch",
    "class",
    "const",
    "continue",
    "default",
    "do",
    "else",
    "enum",
    "exports",
    "finally",
    "for",
    "goto",
    "if",
    "import",
    "instanceof",
    "interface",
    "module",
    "new",
    "open",
    "opens",
    "package",
    "provides",
    "requires",
    "return",
    "strictfp",
    "super",
    "switch",
    "this",
    "throw",
    "try",
    "uses",
    "var",
    "while",
    "with",
]

modifiers = [
    "static",
    "final",
    "abstract",
    "synchronized",
    "native",
    "default",
    "volatile",
    "transient",
]

visibility_scopes = ["public", "protected", "private", "default"]


class JavaObject(object):
    """
    Base class for all Java objects.
    """

    pass


@dataclass
class JavaDoc(JavaObject):
    """
    Represents a JavaDoc comment.
    """

    text: str = ""

    author: list[str] = field(default_factory=list)
    version: str = ""
    since: str = ""

    param: list[str] = field(default_factory=list)
    return_: str = None
    throws: list[str] = field(default_factory=list)
    see: list[str] = field(default_factory=list)
    deprecated: str = None


@dataclass
class Object(JavaObject):
    """
    Represents a Java structure.
    """

    nesting_level: int
    name: str
    visibility: str

    def __repr__(self) -> str:
        return (
            f"Object(\n"
            f"  nesting_level = {self.nesting_level}\n"
            f"  name = {self.name}\n"
            f"  visibility = {self.visibility}\n"
            ")"
        )


@dataclass
class Class(Object):
    """
    Represents a Java class.
    """

    modifiers: list[Object] = field(default_factory=list)
    children: list[Object] = field(default_factory=list)
    javadoc: JavaDoc = None

    extends: str = ""
    implements: list[str] = field(default_factory=list)

    def add_child(self, child: Object):
        self.children.append(child)

    def __repr__(self) -> str:
        children_repr = [child.name for child in self.children]

        return (
            f"Class(\n"
            f"  javadoc = {self.javadoc}\n"
            f"  nesting_level = {self.nesting_level}\n"
            f"  name = {self.name}\n"
            f"  visibility = {self.visibility}\n"
            f"  children = (\n"
            f"    {children_repr}"
            f"\n  )\n"
            ")"
        )


@dataclass
class Method(Object):
    """
    Represents a Java method.
    """

    return_type: str
    parameters: list[Parameter] = field(default_factory=list)
    modifiers: list[str] = field(default_factory=list)
    generic: bool = False
    javadoc: JavaDoc = None

    throws: list[str] = field(default_factory=list)

    def __repr__(self) -> str:
        return (
            f"Method(\n"
            f"  javadoc = {self.javadoc}\n"
            f"  nesting_level = {self.nesting_level}\n"
            f"  modifiers = {self.modifiers}\n"
            f"  visibility = {self.visibility}\n"
            f"  generic = {self.generic}\n"
            f"  return_type = {self.return_type}\n"
            f"  name = {self.name}\n"
            f"  parameters = {self.parameters}\n"
            ")"
        )


@dataclass
class Field(Object):
    """
    Represents a Java field.
    """

    java_type: str
    modifiers: list[str]
    javadoc: JavaDoc = None


@dataclass
class Parameter(JavaObject):
    """
    Represents a Java parameter.
    """

    java_type: str
    name: str
    optional: bool = False

    def __repr__(self) -> str:
        return (
            f"Parameter("
            f"type = {self.java_type}, "
            f"name = {self.name}, "
            f"optional = {self.optional}"
            ")"
        )


@dataclass
class Interface(Class):
    """
    Represents a Java interface.
    """

    pass


@dataclass
class Record(Class):
    """
    Represents a Java record.
    """

    pass


@dataclass
class Enum(Class):
    """
    Represents a Java enum.
    """

    pass
