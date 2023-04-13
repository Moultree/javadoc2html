import unittest
import os
import sys

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))
import parse
from objects import *


class ParserTest(unittest.TestCase):
    def test_empty(self):
        code = ""
        parser = parse.Parser(code)
        self.assertFalse(parser.parse())

    def test_class(self):
        code = """
        public abstract class A extends C implements B {
            /* Body */
        }
        """

        cls = Class(
            0, "A", "public", modifiers=["abstract"], implements=["B"], extends="C"
        )
        parser = parse.Parser(code)
        self.assertEqual(parser.parse(), [cls])

    def test_multiline_class(self):
        code = """
        public abstract class A
            extends C implements B {
            /* Body */
        }
        """

        cls = Class(
            0, "A", "public", modifiers=["abstract"], implements=["B"], extends="C"
        )
        parser = parse.Parser(code)
        self.assertEqual(parser.parse(), [cls])

    def test_parameters(self):
        code = """
        class A {
            public static void foo(int a) {
                return a * 2;
            }

            void bar() {
                File f = new File("foo.txt");
                return;
            }
        }
        """
        param = Parameter("int", "a", False)
        parser = parse.Parser(code)
        self.assertEqual(parser.parse()[0].children[0].parameters[0], param)

    def test_kinds(self):
        code = """
        interface A { }
        enum B { }
        record C { }
        """
        parser = parse.Parser(code)
        classes = [
            Interface(0, "A", "default"),
            Enum(0, "B", "default"),
            Record(0, "C", "default"),
        ]
        self.assertEqual(
            parser.parse(),
            classes,
        )

    def test_method_javadoc(self):
        code = """
        class A {
            /**
            * @param a value to double
            * @return integer
            */
            public int foo(int a) {
                return a * 2;
            }
        }
        """
        parser = parse.Parser(code)
        self.assertEqual(
            parser.parse()[0].children[0].javadoc,
            JavaDoc(param=["a value to double"], return_="integer"),
        )

    def test_class_javadoc(self):
        code = """
        /**
        * This is example javadoc.
        */
        public class A {
            /**
            * @param a value to double
            * @return integer
            */
            public int foo(int a) {
                return a * 2;
            }
        }
        """
        parser = parse.Parser(code)
        self.assertEqual(
            parser.parse()[0].javadoc,
            JavaDoc("This is example javadoc.\n"),
        )

    def test_throws(self):
        code = """
        class A {
            public int foo(int a) throws Exception {
                return a * 2;
            }
        }
        """

        parser = parse.Parser(code)
        self.assertEqual(
            parser.parse()[0].children[0].throws[0],
            "Exception",
        )

    def test_throws_multiline(self):
        code = """
            class A {
                public int foo(int a, int b, int c) 
                    throws Exception {
                    return a * b * c;
                }
            }
        """

        parser = parse.Parser(code)
        self.assertEqual(
            parser.parse()[0].children[0].throws[0],
            "Exception",
        )

    def test_inner_class(self):
        code = """
        public class A {
            public class B {
                /* Body */
            }

            void bar() {
                return;
            }
        }
        """

        parser = parse.Parser(code)
        self.assertEqual(
            parser.parse()[0].children[0],
            Class(1, "B", "public"),
        )


if __name__ == "__main__":
    unittest.main()
