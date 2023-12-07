package lab0;

public class Variant4 {

    public static int integerNumbersTask(int A, int B) {
        assert B > 0 : "Invalid input: B must be positive.";
        assert A > B : "Invalid input: A must be greater than B.";
        return A / B;
    }

    public static void main(String... strings) {
        System.out.println("Start of zero lab");
        System.out.println("Done!!!");
    }

    public static boolean booleanTask(int A, int B) {
        return A > 2 && B != 3;
    }
    public static int ifTask(int number1, int number2, int number3) {
        int positiveCount = 0;

        if (number1 > 0) {
            positiveCount++;
        }

        if (number2 > 0) {
            positiveCount++;
        }

        if (number3 > 0) {
            positiveCount++;
        }

        return positiveCount;
    }
    public static int switchTask(int month) {
        switch (month) {
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                return 31;
            case 4:
            case 6:
            case 9:
            case 11:
                return 30;
            case 2:
                return 28;
            default:
                throw new IllegalArgumentException("Invalid month number. Month should be in the range 1-12.");
        }
    }

    public static double[] forTask(double price) {
        double[] costs = new double[10];
        for (int kg = 1; kg <= 10; kg++) {
            costs[kg - 1] = kg * price;
        }
        return costs;
    }


    public static boolean whileTask(int N) {
        if (N <= 0) {
            return false;
        }

        while (N % 3 == 0) {
            N /= 3;
        }

        return N == 1;
    }


    public static int minmaxTask(int[] array) {
        if (array == null || array.length == 0) {
            return -1;
        }

        int minIndex = 0;

        for (int i = 1; i < array.length; i++) {
            if (array[i] < array[minIndex]) {
                minIndex = i;
            }
        }

        return minIndex;
    }

    public static double[] arrayTask(int N, double A, double D) {
        if (N <= 1) {
            throw new IllegalArgumentException("N should be greater than 1.");
        }

        double[] result = new double[N];
        result[0] = A;

        for (int i = 1; i < N; i++) {
            result[i] = A * Math.pow(D, i);
        }

        return result;
    }


    public static int[][] matrixTask(int M, int N, int[] numbers) {
        if (N != numbers.length) {
            throw new IllegalArgumentException("Invalid matrix dimensions.");
        }

        int[][] matrix = new int[M][N];

        int index;
        for (int i = 0; i < M; i++) {
            index = 0;
            for (int j = 0; j < N; j++) {
                matrix[i][j] = numbers[index++];
            }
        }

        return matrix;
    }
}
