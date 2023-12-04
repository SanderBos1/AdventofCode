package src.year_2023.day3;

import java.util.ArrayList;

class day3_1 {

    private static int parseInput(String input) {
        String[] groups = input.split("\n");
        int sum = 0;

        for (int i = 0; i < groups.length; i++) {
            if (i == 0) {
                String[] select_groups = { groups[i], groups[i + 1] };
                int check = partNumber(select_groups);
                sum = sum + check;
            } else if (i == groups.length - 1) {
                String[] select_groups = { groups[i], groups[i - 1] };
                int check = partNumber(select_groups);
                sum = sum + check;
            } else {
                String[] select_groups = new String[] { groups[i], groups[i + 1], groups[i - 1] };
                int partNumber = partNumber(select_groups);
                sum = sum + partNumber;
            }
        }
        return sum;

    }

    private static int partNumber(String[] groups) {

        String temp = "";
        ArrayList<Integer> toCheck = new ArrayList<Integer>();
        int sum = 0;
        if (groups.length > 2) {
            System.out.println("group 2 " + groups[2]);
        }
        System.out.println("group 0 " + groups[0]);
        System.out.println("group 1 " + groups[1]);

        for (int j = 0; j < groups[0].length(); j++) {
            char intrest = groups[0].charAt(j);
            if (Character.isDigit(intrest)) {
                System.out.println(intrest);
                temp = temp + intrest;
                toCheck.add(toCheck.size(), j);
            } else {
                if (temp != "") {
                    System.out.println("do i get in the if");
                    int number2 = Integer.valueOf(temp);
                    System.out.println("test " + number2);
                    Boolean checkifPart2 = checkIsPart_all(groups, toCheck);

                    System.out.println("test " + checkifPart2);
                    if (checkifPart2) {
                        sum = sum + number2;
                    }

                }
                temp = "";
                toCheck = new ArrayList<Integer>();
            }

        }
        if (temp != "") {
            int number2 = Integer.valueOf(temp);
            Boolean checkifPart2 = checkIsPart_all(groups, toCheck);
            System.out.println("test " + number2);
            System.out.println("test " + checkifPart2);
            if (checkifPart2) {
                sum = sum + number2;
            }

        }

        return sum;
    }

    private static Boolean checkIsPart_all(String[] groups, ArrayList<Integer> placeNumbers) {
        // System.out.println("groupslength" + groups.length);
        for (int i = 0; i < groups.length; i++) {
            // System.out.println("should return :" + checkIsPart(groups[i], placeNumbers));
            if (checkIsPart(groups[i], placeNumbers)) {
                return true;
            }

        }
        return false;
    }

    private static Boolean checkIsPart(String line, ArrayList<Integer> placeNumbers) {

        // System.out.println("this is line" + line);
        // System.out.println(line.charAt(5));

        // System.out.println(placeNumbers);

        Boolean checklength = Integer
                .parseInt(String.valueOf(placeNumbers.get(placeNumbers.size() - 1))) < line.length() - 1;
        // System.out.println("does it work " + checklength);

        if (placeNumbers.get(0) != 0) {
            if (line.charAt(placeNumbers.get(0) - 1) != '.') {
                return true;
            }
        }

        if (checklength) {
            // System.out.println("do i get here");
            int testnumber = Integer.parseInt(String.valueOf(placeNumbers.get(placeNumbers.size() - 1))) + 1;
            // System.out.println("this is testnumber " + testnumber);
            if (line.charAt(testnumber) != '.') {
                return true;
            }
        }

        for (int i = 0; i < placeNumbers.size(); i++) {
            if (line.charAt(placeNumbers.get(i)) != '.' && !Character.isDigit(line.charAt(placeNumbers.get(i)))) {
                return true;
            }
        }

        return false;

    }

    public static void Execute(String input) {

        int sum = parseInput(input);
        System.out.println(sum);
    }
}
