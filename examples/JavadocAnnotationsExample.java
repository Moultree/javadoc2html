/**
 * This is a sample class that includes every Javadoc annotation.
 *
 * @version 1.0
 * @author zxcursed
 * @since 2023-03-29
 */
public class JavadocAnnotationsExample {

    /**
     * This is a sample method that includes every Javadoc annotation.
     *
     * @param arg1 The first argument.
     * @param arg2 The second argument.
     * @return The result of the computation.
     * @throws NullPointerException If any of the arguments are null.
     * @throws IllegalArgumentException If the second argument is zero.
     * @deprecated This method is deprecated and should not be used.
     */
    @Deprecated
    public static int compute(int arg1, int arg2) throws NullPointerException, IllegalArgumentException {
        if (arg1 == 0) {
            throw new NullPointerException("Argument 1 is null");
        }
        if (arg2 == 0) {
            throw new IllegalArgumentException("Argument 2 is zero");
        }
        if (arg1 < 0 || arg2 < 0) {
            throw new UnsupportedOperationException("Negative arguments are not supported");
        }
        return arg1 / arg2;
    }

    /**
     * This is a sample field that includes every Javadoc annotation.
     *
     * @serial This field is serializable.
     * @see #compute(int, int)
     * @since 1.0
     */
    @Deprecated
    @SuppressWarnings("unused")
    private int field = 0;
}