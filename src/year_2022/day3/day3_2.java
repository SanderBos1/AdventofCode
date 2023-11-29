package src.year_2022.day3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day3_2 {

    private static int loadInput() {

        int sum = 0;

        try {
            File myObj = new File("Inputs/day3Input.txt");
            Scanner myReader = new Scanner(myObj);

            while (myReader.hasNextLine()) {

                int temp = 0;
                String[] inputParts = { "", "", "" };
                while (temp < 3) {
                    String input = myReader.nextLine();
                    inputParts[temp] = input;
                    temp++;
                }

                String inboth = inBoth(inputParts[0], inputParts[1], inputParts[2]);
                int index = index(inboth);
                sum = sum + index;

            }
            myReader.close();

        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        return sum;

    }

    private static int index(String inboth) {
        int sum = 0;
        String alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

        for (int i = 0; i < inboth.length(); i++) {

            int index = alphabet.indexOf(inboth.charAt(i)) + 1;
            sum = sum + index;
        }

        return sum;
    }

    private static String inBoth(String first, String second, String third) {

        String inboth = "";

        for (int i = 0; i < first.length(); i++) {
            char c = first.charAt(i);
            if (second.indexOf(c) != -1 && !inboth.contains(Character.toString(c))) {
                if (third.indexOf(c) != -1 && !inboth.contains(Character.toString(c)))
                    inboth = inboth + c;

            }
        }
        return inboth;
    }

    public static void Execute() {
        int sum = loadInput();
        System.out.println(sum);
    }
}
