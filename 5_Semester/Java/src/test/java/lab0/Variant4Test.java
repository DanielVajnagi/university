package lab0;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import static org.testng.Assert.*;



public class Variant4Test {

    @Test(dataProvider = "integerProvider")
    public void integerTest(int A, int expectedCount) {
        int result = Variant4.integerNumbersTask(A, 5);
        assertEquals(result, expectedCount);
    }

    @DataProvider
    public Object[][] integerProvider() {
        return new Object[][]{
                {100, 20},  // 100 / 5 = 20
                {12, 2},    // 12 / 5 = 2
                {139, 27},  // 139 / 5 = 27
        };
    }

    @Test(expectedExceptions = AssertionError.class)
    public void negativeIntegerTest() {
        Variant4.integerNumbersTask(-2, 5);
    }
    @Test(dataProvider = "booleanProvider")
    public void testBooleanTask(int A, int B, boolean expectedResult) {
        boolean result = Variant4.booleanTask(A, B);
        assertEquals(result, expectedResult);
    }

    @DataProvider(name = "booleanProvider")
    public Object[][] booleanProvider() {
        return new Object[][] {
                {4, 5, true},   // A > 2 && B != 3 is true
                {1, 2, false},   // A > 2 && B != 3 is false
                {3, 3, false},   // A > 2 && B != 3 is false
                {5, 3, false},    // A > 2 && B != 3 is false
        };
    }
    @Test(dataProvider = "ifTaskProvider")
    public void testIfTask(int number1, int number2, int number3, int expectedCount) {
        int result = Variant4.ifTask(number1, number2, number3);
        assertEquals(result, expectedCount);
    }

    @DataProvider(name = "ifTaskProvider")
    public Object[][] ifTaskProvider() {
        return new Object[][] {
                {1, 2, 3, 3},
                {-1, 0, 5, 1},
                {-1, -2, -3, 0},
                {0, 0, 0, 0},

        };
    }

    @Test(dataProvider = "switchTaskProvider")
    public void testSwitchTask(int month, int expectedDays) {
        int result = Variant4.switchTask(month);
        assertEquals(result, expectedDays);
    }

    @DataProvider(name = "switchTaskProvider")
    public Object[][] switchTaskProvider() {
        return new Object[][] {
                {1, 31},
                {4, 30},
                {7, 31},
                {2, 28},

        };
    }

    @Test(dataProvider = "forTaskProvider")
    public void testForTask(double price, double[] expectedCosts) {
        double[] result = Variant4.forTask(price);
        assertEquals(result, expectedCosts);
    }

    @DataProvider(name = "forTaskProvider")
    public Object[][] forTaskProvider() {
        return new Object[][] {
                {5.0, new double[]{5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0}},
                {2.5, new double[]{2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0}},
        };
    }

    @Test(dataProvider = "whileTaskProvider")
    public void testWhileTask(int N, boolean expectedResult) {
        boolean result = Variant4.whileTask(N);
        assertEquals(result, expectedResult);
    }

    @DataProvider(name = "whileTaskProvider")
    public Object[][] whileTaskProvider() {
        return new Object[][] {
                {1, true},   // 3^0 = 1
                {3, true},   // 3^1 = 3
                {9, true},   // 3^2 = 9
                {27, true},  // 3^3 = 27
                {6, false},  // не є степенем числа 3
                {15, false}, // не є степенем числа 3
        };
    }

    @Test(dataProvider = "minmaxTaskProvider")
    public void testMinmaxTask(int[] array, int expectedMinIndex) {
        int result = Variant4.minmaxTask(array);
        assertEquals(result, expectedMinIndex);
    }

    @DataProvider(name = "minmaxTaskProvider")
    public Object[][] minmaxTaskProvider() {
        return new Object[][] {
                {new int[]{5, 2, 8, 1, 6}, 3},    // мінімальний елемент - 1, його номер - 3
                {new int[]{10, 15, 7, 12, 5}, 4}, // мінімальний елемент - 5, його номер - 4
                {new int[]{3, 3, 3, 3, 3}, 0},    // мінімальний елемент - 3, його номер - 0
                {new int[]{}, -1},                 // порожній масив
                {null, -1}                         // null
        };
    }

    @Test(dataProvider = "arrayTaskProvider")
    public void testArrayTask(int N, double A, double D, double[] expectedArray) {
        double[] result = Variant4.arrayTask(N, A, D);
        assertEquals(result, expectedArray);
    }

    @DataProvider(name = "arrayTaskProvider")
    public Object[][] arrayTaskProvider() {
        return new Object[][] {
                {5, 2.0, 3.0, new double[]{2.0, 6.0, 18.0, 54.0, 162.0}}, // A = 2.0, D = 3.0
                {3, 1.0, 0.5, new double[]{1.0, 0.5, 0.25}},               // A = 1.0, D = 0.5
                {4, 3.0, 2.0, new double[]{3.0, 6.0, 12.0, 24.0}},         // A = 3.0, D = 2.0
        };
    }

    @Test(expectedExceptions = IllegalArgumentException.class)
    public void testArrayTaskInvalidInput() {
        Variant4.arrayTask(1, 2.0, 3.0); // N = 1, що є недопустимим
    }

    @Test(dataProvider = "matrixTaskProvider")
    public void testMatrixTask(int M, int N, int[] inputArray, int[][] expectedMatrix) {
        int[][] resultMatrix = Variant4.matrixTask(M, N, inputArray);
        assertEquals(resultMatrix, expectedMatrix, "Incorrect matrix");

    }

    @DataProvider(name = "matrixTaskProvider")
    public Object[][] matrixTaskProvider() {
        return new Object[][]{
                {2, 3, new int[]{1, 2, 3}, new int[][]{{1, 2, 3}, {1, 2, 3}}},
                {3, 2, new int[]{7,  9}, new int[][]{{7, 9}, {7, 9}, {7, 9}}},
        };
    }
}
