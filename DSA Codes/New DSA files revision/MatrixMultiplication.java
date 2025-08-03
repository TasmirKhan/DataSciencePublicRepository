public class MatrixMultiplication {

    public static void main(String[] args) {
        // Define two matrices
        int[][] matrixA = {
            {1, 2, 3},
            {4, 5, 6}
        };
        
        int[][] matrixB = {
            {7, 8},
            {9, 10},
            {11, 12}
        };

        // Check if multiplication is possible
        if (matrixA[0].length != matrixB.length) {
            System.out.println("Matrix multiplication is not possible.");
            return;
        }

        // Resultant matrix
        int[][] result = new int[matrixA.length][matrixB[0].length];

        // Perform multiplication
        for (int i = 0; i < matrixA.length; i++) { // Loop through rows of matrixA
            for (int j = 0; j < matrixB[0].length; j++) { // Loop through columns of matrixB
                for (int k = 0; k < matrixA[0].length; k++) { // Loop through columns of matrixA / rows of matrixB
                    result[i][j] += matrixA[i][k] * matrixB[k][j];
                }
            }
        }

        // Display the result
        System.out.println("Resultant Matrix:");
        for (int i = 0; i < result.length; i++) { // Loop through rows of result
            for (int j = 0; j < result[0].length; j++) { // Loop through columns of result
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
    }
}
