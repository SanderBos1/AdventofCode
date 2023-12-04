package src.year_2023.day2;

class day2_2 {

    private static double parseInput(String input) {
        String[] groups = input.split("\n");

        double sum = 0;

        for (int i = 0; i < groups.length; i++) {
            System.out.println(groups[i]);
            int index = groups[i].indexOf(":");
            String temp = groups[i].substring(0, index);
            System.out.println(temp);
            String tempInt = temp.replace("Game ", "");
            int gameID = Integer.parseInt(tempInt);
            groups[i] = groups[i].substring(index + 1, groups[i].length());
            System.out.println("this is groups[i]" + groups[i]);
            double check = check_false(groups[i]);

            sum = sum + check;

            // String clean = gameIdArray[0].replaceAll("\\D", "");
            // int solution = Integer.parseInt(clean);
        }
        return sum;

    }

    private static int check_false(String groups) {
        String sets[] = groups.split(";");
        int min_power = 99999;

        for (int j = 0; j < sets.length; j++) {

            System.out.println("sets " + sets[j]);

            int checkCorrect = loopString(sets);
            if (checkCorrect < min_power) {
                min_power = checkCorrect;
            }
        }
        return min_power;
    }

    private static int how_many(String line) {
        String[] numbers = line.split(" ");
        int number = Integer.parseInt(numbers[0]);
        return number;

    }

    private static int loopString(String[] parts) {
        int min_green = 0;
        int min_red = 0;
        int min_blue = 0;

        for (int k = 0; k < parts.length; k++) {
            parts[k] = parts[k].replace(" ", "");
            int[] temp = check_correct(parts[k]);
            System.out.println("this is temp 2 " + temp[2]);

            if (temp[0] > min_green) {
                min_green = temp[0];
            }
            if (temp[1] > min_red) {
                min_red = temp[1];
            }
            if (temp[2] > min_blue) {
                min_blue = temp[2];
            }
        }

        int sum = min_blue * min_green * min_red;

        System.out.println("green " + min_green);
        System.out.println("red " + min_red);
        System.out.println("blue " + min_blue);

        System.out.println(sum);
        return sum;

    }

    private static int[] check_correct(String parts) {

        int green = 0;
        int red = 0;
        int blue = 0;

        String[] commaSeperated = parts.split(",");

        for (int j = 0; j < commaSeperated.length; j++) {
            if (commaSeperated[j].contains("green")) {
                commaSeperated[j] = commaSeperated[j].replace("green", "");
                green = green + how_many(commaSeperated[j]);
            } else if (commaSeperated[j].contains("blue")) {
                commaSeperated[j] = commaSeperated[j].replace("blue", "");
                blue = blue + how_many(commaSeperated[j]);

            } else if (commaSeperated[j].contains("red")) {
                commaSeperated[j] = commaSeperated[j].replace("red", "");
                red = red + how_many(commaSeperated[j]);
            }
        }
        int[] colors = { green, red, blue };
        return colors;
    }

    public static void Execute(String input) {

        double correct = parseInput(input);

        System.out.println(correct);
    }
}
