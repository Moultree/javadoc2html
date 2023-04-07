import argparse
import os

from jinja2 import Environment, FileSystemLoader

from objects import *
from parse import Parser


class JavaClassToHtml:
    """
    Class for converting Java classes to HTML
    """

    def __init__(self, filename: str, filenames: list[str], path: str) -> None:
        self.env = Environment(loader=FileSystemLoader("template"))
        self.selected = os.path.basename(filename)
        self.filenames = (
            [os.path.basename(filename) for filename in filenames]
            if filenames
            else [self.selected]
        )
        with open(path, "r") as file:
            parser = Parser(file.read())
            self.classes = parser.parse()

    def generate(self):
        """
        Generates HTML for given Java file
        """
        template = self.env.get_template("template.j2")
        path = os.path.join("out", self.selected.split(".")[0] + ".html")
        with open(path, "w") as out:
            out.write(
                template.render(
                    selected=self.selected, files=self.filenames, classes=self.classes
                )
            )


class JavaDocToHtml:
    """
    Wrapper class for converting Java doc to HTML
    """

    def __init__(self, path: str) -> None:
        self.paths = None

        if os.path.isfile(path):
            self.run(path)
        elif os.path.isdir(path):
            self.paths = self.get_file_paths(path)
            for path in self.paths:
                self.run(path)
        else:
            print("Provide correct path!")

    def get_file_paths(self, directory: str) -> list[str]:
        """
        Returns list of file paths in given directory
        """
        file_paths = []
        for dirpath, _, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith(".java"):
                    file_paths.append(os.path.join(dirpath, filename))
                    print(f"Found file: {os.path.join(dirpath, filename)}")
        return file_paths

    def run(self, path: str):
        """
        Converts Java doc to HTML
        """
        tohtml = JavaClassToHtml(path.split("/")[-1], self.paths, path)
        tohtml.generate()


if __name__ == "__main__":
    argparser = argparse.ArgumentParser("JavaDoc2HTML")
    argparser.add_argument("path")
    args = argparser.parse_args()
    JavaDocToHtml(args.path)
