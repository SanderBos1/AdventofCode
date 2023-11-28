package src.year_2022;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day1 {

    private static int loadInput() {
        int sum = 0;

        try {
            File myObj = new File("input.txt");
            Scanner myReader = new Scanner(myObj);
            int tempsom = 0;

            while (myReader.hasNextLine()) {

                String input = myReader.nextLine();
                // System.out.println("this is input " + input);
                // System.out.println("this is input length " + input.length());

                if (input.length() > 0) {
                    tempsom = tempsom + Integer.parseInt(input);
                } else {
                    if (tempsom > sum) {
                        sum = tempsom;

                    }
                    tempsom = 0;

                }

            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        return sum;

    }

    public static void Execute() {

        int input = loadInput();
        System.out.println(input);

    }
}
