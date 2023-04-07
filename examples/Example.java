class Base<T> {

}

/**
 * This is a simple Java class with Javadoc.
 */
public class Example<T> extends Base<T> implements java.io.Serializable, java.lang.Cloneable {

  /**
   * This method adds two integers and returns the result.
   * 
   * @param a the first integer to add
   * @param b the second integer to add
   * @return the sum of a and b
   */
  public int add(int a, int b) {
    return a + b;
  }

  /**
   * This method returns the square of an integer.
   * 
   * @param a the integer to square
   * @return the square of a
   * @deprecated Use pow(a, 2) instead
   */
  private int square(int a) {
    return a * a;
  }

  /**
   * This method returns true if a given integer is even, and false otherwise.
   * 
   * @param a the integer to check
   * @return true if a is even, false otherwise
   */
  protected boolean isEven(int a) {
    return a % 2 == 0;
  }

}