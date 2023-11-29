package src.year_2022.day2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day2_2 {

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
                int outcome = outcome(Opponent, value_pick);

                score = score + outcome + value_pick;

            }
            myReader.close();

        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        return score;
    }

    private static int outcome(char opponent, int points) {
        if (opponent == 'A') {
            if (points == 6) {
                return 2;
            } else if (points == 0) {
                return 3;
            } else {
                return 1;
            }
        } else if (opponent == 'B') {
            if (points == 6) {
                return 3;
            } else if (points == 0) {
                return 1;
            } else {
                return 2;
            }
        } else {
            if (points == 6) {
                return 1;
            } else if (points == 0) {
                return 2;
            } else {
                return 3;
            }
        }
    }

    private static int valuePick(char chosen) {

        if (chosen == 'Z') {
            return 6;
        } else if (chosen == 'Y') {
            return 3;
        } else {
            return 0;
        }
    }

    public static void Execute() {
        int sum = loadInput();
        System.out.println(sum);
    }

}
