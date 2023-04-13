import unittest
import os
import sys
import subprocess
from pathlib import Path

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))
from javadoctohtml import JavaDocToHtml


class TestJavaDocToHtml(unittest.TestCase):
    def test_empty_file(self):
        Path("tests/temp").mkdir(parents=True, exist_ok=True)

        with open("tests/temp/empty.java", "w", encoding="utf-8") as file:
            file.write("")

        JavaDocToHtml("tests/temp/empty.java")
        self.assertTrue(os.path.isfile("out/empty.html"))
    
    def test_directory(self):
        Path("tests/temp").mkdir(parents=True, exist_ok=True)

        with open("tests/temp/empty.java", "w", encoding="utf-8") as file:
            file.write("")
        
        JavaDocToHtml("tests/temp")
        self.assertTrue(os.path.isfile("out/empty.html"))

    def test_wrong(self):
        before = os.listdir("out")
        JavaDocToHtml("tests/nothing.java")
        after = os.listdir("out")

        self.assertEqual(len(before), len(after))