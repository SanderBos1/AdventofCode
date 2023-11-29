package src.year_2022.day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Arrays;

public class day1_2 {

    private static int loadInput() {

        int[] sums = { 0, 0, 0 };

        try {
            File myObj = new File("Inputs/day1Input.txt");
            Scanner myReader = new Scanner(myObj);
            int tempsom = 0;

            while (myReader.hasNextLine()) {

                String input = myReader.nextLine();

                if (input.length() > 0) {
                    tempsom = tempsom + Integer.parseInt(input);
                } else {
                    if (tempsom > sums[0]) {
                        sums[0] = tempsom;

                    }
                    Arrays.sort(sums);
                    tempsom = 0;

                }

            }
            if (tempsom > sums[0]) {
                sums[0] = tempsom;
                Arrays.sort(sums);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        int total_calories = sums[0] + sums[1] + sums[2];
        return total_calories;

    }

    public static void Execute() {

        int input = loadInput();
        System.out.println(input);

    }
}
