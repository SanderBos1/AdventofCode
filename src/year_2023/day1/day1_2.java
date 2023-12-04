package src.year_2023.day1;

public class day1_2 {

    private static int parseInput(String input) {

        int sum = 0;

        String[] groups = input.split("\n");
        for (int i = 0; i < groups.length; i++) {
            String s = groups[i];
            String[] validDigits = { "oneight", "threeight", "fiveight", "nineight", "twone", "sevenine", "eightwo" };
            String[] correct = { "oneeight", "threeeight", "fiveeight", "nineeight", "twoone", "sevennine",
                    "eighttwo" };

            for (int j = 0; j < validDigits.length; j++) {
                s = s.replace(validDigits[j], correct[j]);
            }
            System.out.println(s);
            int first_int = first_int(s);
            sum = sum + first_int;

        }

        return sum;

    }

    private static int first_int(String line) {
        String[] validDigits = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
        for (int j = 0; j < validDigits.length; j++) {
            line = line.replace(validDigits[j], Integer.toString(j));
        }
        System.out.println(line);

        String clean = line.replaceAll("\\D", "");
        int firstInt = clean.charAt(0) - '0';
        int lastInt = clean.charAt(clean.length() - 1) - '0';
        int both = Integer.parseInt(firstInt + "" + lastInt);
        return both;

    }

    public static void Execute(String input) {

        int resultingSum = parseInput(input);

        System.out.println(resultingSum);
    }
}
