package src.year_2023.day2;

class day2_1 {

    private static int parseInput(String input) {
        String[] groups = input.split("\n");

        int sum = 0;

        for (int i = 0; i < groups.length; i++) {
            System.out.println(groups[i]);
            int index = groups[i].indexOf(":");
            String temp = groups[i].substring(0, index);
            System.out.println(temp);
            String tempInt = temp.replace("Game ", "");
            int gameID = Integer.parseInt(tempInt);
            groups[i] = groups[i].substring(index + 1, groups[i].length());
            System.out.println("this is groups[i]" + groups[i]);
            Boolean check = check_false(groups[i]);
            if (check) {
                sum = sum + gameID;
            }

            // String clean = gameIdArray[0].replaceAll("\\D", "");
            // int solution = Integer.parseInt(clean);
        }
        return sum;

    }

    private static Boolean check_false(String groups) {
        String sets[] = groups.split(";");

        for (int j = 0; j < sets.length; j++) {

            System.out.println("sets " + sets[j]);

            Boolean checkCorrect = loopString(sets);
            System.out.println("checkCorrect " + checkCorrect);
            if (!checkCorrect) {
                return false;
            }
        }
        return true;
    }

    private static int how_many(String line) {
        String[] numbers = line.split(" ");
        int number = Integer.parseInt(numbers[0]);
        return number;

    }

    private static Boolean loopString(String[] parts) {

        for (int k = 0; k < parts.length; k++) {
            parts[k] = parts[k].replace(" ", "");

            if (!check_correct(parts[k])) {
                return false;
            }
        }
        return true;

    }

    private static Boolean check_correct(String parts) {

        int green = 0;
        int red = 0;
        int blue = 0;

        System.out.println("this is parts " + parts);
        String[] commaSeperated = parts.split(",");

        for (int j = 0; j < commaSeperated.length; j++) {
            System.out.println(commaSeperated[j]);
            if (commaSeperated[j].contains("green")) {
                commaSeperated[j] = commaSeperated[j].replace("green", "");
                // System.out.println("do i get here" + parts[j]);
                green = green + how_many(commaSeperated[j]);
                if (green > 13) {
                    return false;
                }
            } else if (commaSeperated[j].contains("blue")) {
                commaSeperated[j] = commaSeperated[j].replace("blue", "");
                blue = blue + how_many(commaSeperated[j]);
                if (blue > 14) {
                    return false;
                }
            } else if (commaSeperated[j].contains("red")) {
                commaSeperated[j] = commaSeperated[j].replace("red", "");
                red = red + how_many(commaSeperated[j]);
                System.out.println("this is red " + red);
                if (red > 12) {
                    // System.out.println("this is false");
                    return false;
                }
            }

        }

        return true;
    }

    public static void Execute(String input) {

        int correct = parseInput(input);

        System.out.println(correct);
    }
}
