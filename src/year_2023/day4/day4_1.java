package src.year_2023.day4;

import java.util.ArrayList;
import java.util.Collections;

class day4_1 {

    private static int parseInput(String input) {
        int sum = 0;

        String[] groups = input.split("\n");
        for (int i = 0; i < groups.length; i++) {
            groups[i] = groups[i].substring(groups[i].indexOf(": ") + 1).trim();
            groups[i] = groups[i].replace(" ", ".");
            groups[i] = groups[i].replace("..", ".");

            String[] line = groups[i].split(".\\|.");

            System.out.println(groups[i]);

            int lineSum = sumLine(line);
            sum = sum + lineSum;
            System.out.println("this is sum in between " + sum);
        }

        return sum;

    }

    private static int sumLine(String[] oneLine) {

        Boolean firstSeen = false;
        int sum = 0;

        System.out.println(oneLine[0]);
        ArrayList<Integer> firstNumbers = convertNumbers(oneLine[0]);
        System.out.println(oneLine[1]);
        ArrayList<Integer> secondNumbers = convertNumbers(oneLine[1]);

        for (int i = 0; i < firstNumbers.size(); i++) {
            int occurrences = Collections.frequency(secondNumbers, firstNumbers.get(i));
            if (occurrences >= 1 && !firstSeen) {
                firstSeen = true;
                sum = 1;
                occurrences = occurrences - 1;
                while (occurrences > 0) {
                    sum = sum * 2;
                    occurrences--;
                }
            } else {
                while (occurrences > 0) {
                    sum = sum * 2;
                    occurrences--;
                }
            }

        }

        return sum;

    }

    private static ArrayList<Integer> convertNumbers(String leftSide) {

        ArrayList<Integer> allFirstNumbers = new ArrayList<Integer>();

        String temp = "";
        for (int i = 0; i < leftSide.length(); i++) {
            if (leftSide.charAt(i) != '.') {
                temp = temp + leftSide.charAt(i);
            } else {
                int toAdd = Integer.parseInt(temp);
                allFirstNumbers.add(toAdd);
                temp = "";
            }

        }

        int toAdd = Integer.parseInt(temp);
        allFirstNumbers.add(toAdd);

        System.out.println("this is the list" + allFirstNumbers);
        return allFirstNumbers;

    }

    public static void Execute(String input) {

        int sum = parseInput(input);
        System.out.println(sum);
    }
}
