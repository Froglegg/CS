public class App {
    public static void main(String[] args) throws Exception {
        // char[] copyFrom = { 'd', 'e', 'c', 'a', 'f', 'f', 'e',
        // 'i', 'n', 'a', 't', 'e', 'd' };
        // char[] copyTo = new char[7];

        // System.out.println(new String(copyFrom));

        // System.arraycopy(copyFrom, 2, copyTo, 0, 7);
        // System.out.println(new String(copyTo) + copyTo[4]);
        char[] anArray1;
        // declares an array of characters - original array

        anArray1 = new char[7];
        // allocates memory for 7 characters

        anArray1[0] = 'h'; // initialize first element
        anArray1[1] = 'i'; // initialize second element
        anArray1[2] = 's'; // etc.
        anArray1[3] = 't';
        anArray1[4] = 'o';
        anArray1[5] = 'r';
        anArray1[6] = 'y';


        System.out.println("\nArray before copying:\n");
        for (int i = 0; i < anArray1.length; i++) {
            System.out.println("Element at index " + i + ": " + anArray1[i]);
        }

        char[] anArray2;

        anArray2 = new char[5];

        System.arraycopy(anArray1, 2, anArray2, 0, 5);

        System.out.println("\nArray after copying:\n");

        for (int i = 0; i < anArray2.length; i++) {
            System.out.println("Element at index " + i + ": " + anArray2[i]);
        }


    }
}


class ArrayDemo {
    public static void main(String[] args) {
        int[] anArray; // declares an array of integers

        anArray = new int[10]; // allocates memory for 10 integers

        anArray[0] = 100; // initialize first element
        anArray[1] = 200; // initialize second element
        anArray[2] = 300; // etc.
        anArray[3] = 400;
        anArray[4] = 500;
        anArray[5] = 600;
        anArray[6] = 700;
        anArray[7] = 800;
        anArray[8] = 900;
        anArray[9] = 1000;

        System.out.println("Element at index 0: " + anArray[0]);
        System.out.println("Element at index 1: " + anArray[1]);
        System.out.println("Element at index 2: " + anArray[2]);
        System.out.println("Element at index 3: " + anArray[3]);
        System.out.println("Element at index 4: " + anArray[4]);
        System.out.println("Element at index 5: " + anArray[5]);
        System.out.println("Element at index 6: " + anArray[6]);
        System.out.println("Element at index 7: " + anArray[7]);
        System.out.println("Element at index 8: " + anArray[8]);
        System.out.println("Element at index 9: " + anArray[9]);
    }
}

