package src.year_2022.day2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day2_1 {

    private static int loadInput() {
        int score = 0;

        try {
            File myObj = new File("Inputs/day2Input.txt");
            Scanner myReader = new Scanner(myObj);

            while (myReader.hasNextLine()) {

                String input = myReader.nextLine();
                char Opponent = input.charAt(0);
                char yourself = input.charAt(2);

                int value_pick = valuePick(yourself);
                int outcome = outcome(yourself, Opponent);

                score = score + outcome + value_pick;

            }
            myReader.close();

        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        return score;
    }

    private static int outcome(char chosen, char opponent) {
        if (opponent == 'A') {
            if (chosen == 'Y') {
                return 6;
            } else if (chosen == 'X') {
                return 3;
            } else {
                return 0;
            }
        } else if (opponent == 'B') {
            if (chosen == 'Z') {
                return 6;
            } else if (chosen == 'Y') {
                return 3;
            } else {
                return 0;
            }
        } else {
            if (chosen == 'X') {
                return 6;
            } else if (chosen == 'Z') {
                return 3;
            } else {
                return 0;
            }
        }
    }

    private static int valuePick(char chosen) {

        if (chosen == 'X') {
            return 1;
        } else if (chosen == 'Y') {
            return 2;
        } else {
            return 3;
        }
    }

    public static void Execute() {
        int sum = loadInput();
        System.out.println(sum);
    }

}
