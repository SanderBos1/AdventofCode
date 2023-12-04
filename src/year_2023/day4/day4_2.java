package src.year_2023.day4;

import java.util.ArrayList;
import java.util.Collections;

class day4_2 {

    private static int parseInput(String input) {
        int sum = 0;

        String[] groups = input.split("\n");
        int howManyGroups = groups.length;
        int[] occurences = occurences(howManyGroups, groups);
        for (int i = 0; i < occurences.length; i++) {
            sum = sum + occurences[i];
        }

        return sum;

    }

    private static int[] occurences(int how_many, String[] groups) {

        int[] allOccurences = new int[how_many];

        for (int i = 0; i < groups.length; i++) {

            groups[i] = groups[i].substring(groups[i].indexOf(": ") + 1).trim();
            groups[i] = groups[i].replace(" ", ".");
            groups[i] = groups[i].replace("..", ".");
            String[] line = groups[i].split(".\\|.");
            // System.out.println("this is current group " + line[0]);

            int check = sumLine(line);
            // System.out.println("How many maching numbers " + check);
            allOccurences[i] = allOccurences[i] + 1;
            // System.out.println("this is how much " + i + "occureces" + allOccurences[i]);

            int placeholder = allOccurences[i];
            while (placeholder > 0) {
                int placeHolderInner = check;
                // System.out.println("How many_loops");
                // System.out.println("");

                while (placeHolderInner > 0) {
                    int place = i + placeHolderInner;
                    if (place < allOccurences.length)
                        allOccurences[place] = allOccurences[place] + 1;
                    placeHolderInner--;
                }

                for (int j = 0; j < allOccurences.length; j++) {
                    // System.out.print(allOccurences[j]);
                    // System.out.println("");

                }
                placeholder--;

            }

        }

        return allOccurences;

    }

    private static int sumLine(String[] oneLine) {

        Boolean firstSeen = false;
        int sum = 0;

        ArrayList<Integer> firstNumbers = convertNumbers(oneLine[0]);
        ArrayList<Integer> secondNumbers = convertNumbers(oneLine[1]);

        for (int i = 0; i < firstNumbers.size(); i++) {
            int occurrences = Collections.frequency(secondNumbers, firstNumbers.get(i));
            if (occurrences >= 1 && !firstSeen) {
                firstSeen = true;
                sum = 1;
                occurrences = occurrences - 1;
                while (occurrences > 0) {
                    sum++;
                    occurrences--;
                }
            } else {
                while (occurrences > 0) {
                    sum++;
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

        return allFirstNumbers;

    }

    public static void Execute(String input) {

        int sum = parseInput(input);
        System.out.println(sum);
    }
}
