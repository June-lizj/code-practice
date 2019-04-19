package Offer;

public class Code000_TwoDimensionsArrayFinding {
    public static void main(String[] args) {
        int[][] array0 = {
                {},{}
        };
        int[][] array1 = {
                {1, 3, 5},
                {2, 4, 6},
                {7, 8, 9}
        };
        System.out.println(Find2(124, array0));

    }

    //running time 148ms,occupied memory 17436k
    public static boolean Find0(int target, int[][] array) {
        for (int[] row : array) {
            for (int ele : row) {
                if (ele == target) {
                    return true;
                }
            }
        }
        return false;
    }

    //running time 192ms,occupied memory 18816k
    public static boolean Find1(int target, int[][] array) {
        int row = 0;
        int col = array[0].length - 1;
        while (row <= array.length - 1 & col >= 0) {
            if (target == array[row][col])
                return true;
            else if (target > array[row][col])
                row++;
            else
                col--;

        }
        return false;

    }

    //running time 179ms,occupied memory 17724k
    public static boolean Find2(int target, int[][] array) {
        for (int row = 0; row < array.length; row++) {
            int low = 0;
            int high = array[row].length - 1;
            while (low <= high) {
                int mid = (low + high) / 2;
                if (target < array[row][mid]) {
                    high = mid - 1;
                } else if (target > array[row][mid]) {
                    low = mid + 1;
                } else
                    return true;
            }
        }
        return false;
    }
}
