package src.year_2022.day4;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day4_1 {

    private static int loadInput() {

        int sum = 0;

        try {
            File myObj = new File("Inputs/day4Input.txt");
            Scanner myReader = new Scanner(myObj);

            while (myReader.hasNextLine()) {
                int[] values = { 0, 0, 0, 0 };
                String input = myReader.nextLine();

                String[] consideration = input.split(",");
                int[] elfRange = elfRange(consideration[0]);
                int[] elfRange1 = elfRange(consideration[1]);

                values[0] = elfRange[0];
                values[1] = elfRange[1];
                values[2] = elfRange1[0];
                values[3] = elfRange1[1];

                Boolean isOverlap = contains(values[0], values[1], values[2], values[3]);
                System.out.println(isOverlap);
                if (isOverlap) {
                    sum++;
                }

            }
            myReader.close();

        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        return sum;

    }

    private static int[] elfRange(String elfRange1) {
        String[] consideration = elfRange1.split("-");
        int start = Integer.valueOf(consideration[0]);
        int end = Integer.valueOf(consideration[1]);
        int[] realElfRange = { start, end };
        return realElfRange;

    }

    private static boolean contains(int value11, int value12, int value21, int value22) {
        if (value11 <= value21 && value12 >= value22) {
            return true;
        } else if (value21 <= value11 && value22 >= value12) {
            return true;
        } else {
            return false;
        }
    }

    public static void Execute() {
        int sum = loadInput();
        System.out.println(sum);
    }
}
