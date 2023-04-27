import re

from objects import (
    Parameter,
    Class,
    Interface,
    Enum,
    Record,
    Method,
    JavaDoc,
    Object,
    banned_keywords,
    visibility_scopes,
    modifiers
    )
from pattern import Pattern


class Parser:
    """
    This class is responsible for parsing the Java code.
    """

    def __init__(self, code: str) -> None:
        self.code = self.format_java_code(code)

    def format_java_code(self, java_code: str, indent: int = 4) -> str:
        """
        Format the Java code.

        :param java_code: The Java code to format.
        :param indent: The number of spaces to indent.
        :return: The formatted Java code.
        """
        lines = java_code.split("\n")

        lines = [line.strip().split("//")[0].strip() for line in lines]
        lines = [line for line in lines if line]

        indent_level = 0
        formatted_code = ""

        for line in lines:
            if line.startswith("}"):
                indent_level -= 1

            formatted_code += (" " * indent) * indent_level + line + "\n"

            if line.endswith("{"):
                indent_level += 1

        return formatted_code.strip()

    def replace_with_mnemonic(self, text: str) -> str:
        """
        Replace all symbols with mnemonics.

        :param text: text to replace
        :return: text with mnemonics
        """
        symbol_mnemonics = {
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#39;",
        }

        # Replace symbols with their mnemonics
        for symbol, mnemonic in symbol_mnemonics.items():
            text = text.replace(symbol, mnemonic)

        return text

    def _get_nesting_level(self, line: str) -> int:
        """
        Get the nesting level of a line.

        :param line: The line to get the nesting level of. (Default: 4)
        :return: The nesting level of the line.
        """
        return (len(line) - len(line.lstrip())) // 4

    def get_parameters(self, parameters: str) -> list[Parameter]:
        """
        Get the parameters of a method.

        :param parameters: String containing parameters of the method.
        :return: List of parameters of the method.
        """
        params = re.findall(
            r"([\w\d]+(?:<.*?>)?(?:\[\])?)\s+([\w\d_$]+)",
            parameters
        )
        java_parameters = []

        for java_type, name in params:
            java_type = self.replace_with_mnemonic(java_type)
            optional = "..." in java_type
            java_parameters.append(Parameter(java_type, name, optional))

        return java_parameters

    def get_method(
        self,
        match: re.Match[str],
        nesting_level: int
    ) -> Method | None:
        """
        Get the method of a class.
        :param match: The match of the method.
        :param nesting_level: The nesting level of the method.
        :return: The method of the class.
        """
        _modifiers, return_type, name, parameters = match.groups()

        visibility = "default"
        generic = False
        found_modifiers = []

        for modifier in ((_modifiers or "") + return_type).strip().split(" "):
            modifier.strip()

            if modifier in banned_keywords:
                return

            if modifier in visibility_scopes:
                visibility = modifier

            generic = generic or bool(Pattern.GENERIC.search(modifier))

            if modifier in modifiers:
                found_modifiers.append(modifier)

        parameters = self.get_parameters(parameters)

        return Method(
            nesting_level,
            name,
            visibility,
            return_type,
            parameters,
            found_modifiers,
            generic=generic,
        )

    def get_class(
        self, match: re.Match[str], nesting_level: int
    ) -> Class | Interface | Record | Enum:
        """
        Get the class/interface/record/enum.
        :param match: The match of the class/interface/record/enum.
        :param nesting_level: The nesting level of the class.
        :return: The class/interface/record/enum.
        """
        _modifiers, kind, name = match.groups()

        match kind:
            case "class":
                kind = Class
            case "interface":
                kind = Interface
            case "record":
                kind = Record
            case "enum":
                kind = Enum

        visibility = "default"
        found_modifiers = []
        for modifier in _modifiers.strip().split(" "):
            modifier.strip()

            if modifier in visibility_scopes:
                visibility = modifier

            if modifier in modifiers:
                found_modifiers.append(modifier)

        return kind(
            nesting_level,
            self.replace_with_mnemonic(name),
            visibility,
            found_modifiers
        )

    def get_javadoc(self, javadoc: JavaDoc | None, line: str):
        """
        Get the javadoc of a method or class.
        :param javadoc: The javadoc of the method or class.
        :param line: Current line of the file.

        :return: The javadoc of the method or class.
        """
        line = (
            line.strip()
                .removesuffix("*/")
                .removeprefix("/*")
                .removeprefix("*")
                .strip()
        )

        tag_mappings = {
            "@param": ("param", lambda line: " ".join(line.split()[1:])),
            "@return": ("return_", lambda line: " ".join(line.split()[1:])),
            "@throws": ("throws", lambda line: " ".join(line.split()[1:])),
            "@see": ("see", lambda line: " ".join(line.split()[1:])),
            "@deprecated":
                ("deprecated", lambda line: " ".join(line.split()[1:])),
            "@author": ("author", lambda line: " ".join(line.split()[1:])),
            "@since": ("since", lambda line: " ".join(line.split()[1:])),
            "@version": ("version", lambda line: " ".join(line.split()[1:])),
        }

        for tag, (attr, parser) in tag_mappings.items():
            if line.startswith(tag):
                if isinstance(lst := getattr(javadoc, attr), list):
                    lst.append(parser(line))
                else:
                    setattr(javadoc, attr, parser(line))
                return

        if line:
            javadoc.text += line + "\n"

    def parse(self) -> list[Class | Interface | Record | Enum]:
        """
        Parse the Java code.

        :return: List of classes/interfaces/records/enums.
        """
        classes: list[Class] = []
        parent_tree: list[Class] = []
        parent: Class = None

        in_javadoc: bool = False
        javadoc: JavaDoc = None

        entity: Object = None

        for line in self.code.split("\n"):
            if entity:
                if extends := Pattern.EXTENDS.search(line):
                    match = re.match(
                        r"([\w\d.]+(?:<.*?>)?)",
                        extends.group(1).split("implements")[0]
                    )
                    entity.extends = match.group(1) if match else None

                if implements := Pattern.IMPLEMENTS.search(line):
                    entity.implements.extend(
                        re.findall(
                            r"([\w\d.]+(?:<.*?>)?)",
                            implements.group(1).split("extends")[0],
                        )
                    )

                if throws := Pattern.THROWS.search(line):
                    entity.throws.extend(
                        re.findall(
                            r"([\w\d.]+(?:<.*?>)?)",
                            throws.group(1),
                        )
                    )

                if line.strip().removesuffix("}").endswith("{") or (
                    line.strip().endswith(";") and isinstance(entity, Method)
                ):
                    entity = None
                    continue

            if line.strip().startswith("/*"):
                javadoc = JavaDoc()
                in_javadoc = True

            if in_javadoc:
                self.get_javadoc(javadoc, line)

                if line.endswith("*/"):
                    javadoc.text = re.sub(
                        r"{@code (.*?)}",
                        r"<span class='code'>\1</span>",
                        javadoc.text,
                        flags=re.S,
                    )
                    javadoc.text = re.sub(
                        r"{@link (.*?)}",
                        r"<span class='link'>\1</span>",
                        javadoc.text,
                        flags=re.S,
                    )

                    in_javadoc = False
                    continue

            elif cls := Pattern.TYPES.search(line):
                nesting_level = self._get_nesting_level(line)

                new = self.get_class(cls, nesting_level)

                if extends := Pattern.EXTENDS.search(line):
                    match = re.match(
                        r"([\w\d.]+(?:<.*?>)?)",
                        extends.group(1).split("implements")[0]
                    )
                    new.extends = match.group(1) if match else None

                if implements := Pattern.IMPLEMENTS.search(line):
                    new.implements.extend(
                        [
                            self.replace_with_mnemonic(impl)
                            for impl in re.findall(
                                r"([\w\d.]+(?:<.*?>)?)",
                                implements.group(1).split("extends")[0],
                            )
                        ]
                    )

                if javadoc:
                    new.javadoc = javadoc
                    javadoc = None

                if not line.strip().endswith("{"):
                    entity = new

                if parent and (
                    parent.nesting_level == self._get_nesting_level(line)
                ):
                    if parent_tree:
                        parent_tree.pop()
                    parent = parent_tree[-1] if parent_tree else classes[-1]

                if parent and parent.nesting_level < new.nesting_level:
                    parent.add_child(new)

                parent = new
                parent_tree.append(parent)

                if nesting_level == 0:
                    classes.append(parent)

            elif mtd := Pattern.METHOD.search(line):
                new = self.get_method(mtd, self._get_nesting_level(line))

                if not new:
                    continue

                if javadoc:
                    new.javadoc = javadoc
                    javadoc = None

                if throws := Pattern.THROWS.search(line):
                    new.throws.extend(
                        re.findall(
                            r"([\w\d.]+(?:<.*?>)?)",
                            throws.group(1),
                        )
                    )

                if (not line.strip().endswith("{")) or (
                    line.strip().endswith(";")
                ):
                    entity = new

                if parent and (
                    parent.nesting_level == self._get_nesting_level(line)
                ):
                    if parent_tree:
                        parent_tree.pop()
                    parent = parent_tree[-1] if parent_tree else classes[-1]

                if parent and parent.nesting_level < new.nesting_level:
                    parent.add_child(new)

        return classes
