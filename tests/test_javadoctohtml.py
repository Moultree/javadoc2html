import unittest
import os
import sys
from pathlib import Path

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))
from javadoctohtml import JavaDocToHtml


class TestJavaDocToHtml(unittest.TestCase):
    def test_empty_file(self):
        Path("tests/temp").mkdir(parents=True, exist_ok=True)

        with open("tests/temp/empty.java", "w") as f:
            f.write("")

        JavaDocToHtml("tests/temp/empty.java")
        self.assertTrue(os.path.isfile("out/empty.html"))
