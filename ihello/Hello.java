import java.io.*;
import java.util.*;


class Hello {
    public static void main(String[] argv) {
        Scanner scan = new Scanner(System.in);
        System.out.print("What's your name? ");
        String name = scan.nextLine();
        System.out.println("Hello, " + name);
    }
}

