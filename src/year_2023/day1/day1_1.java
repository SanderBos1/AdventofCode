package src.year_2023.day1;

public class day1_1 {

    private static int parseInput(String input) {

        int sum = 0;

        String[] groups = input.split("\n");
        for (int i = 0; i < groups.length; i++) {
            String s = groups[i];
            int temp = clean(s);
            sum = sum + temp;
        }
        return sum;

    }

    private static int clean(String line) {
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
