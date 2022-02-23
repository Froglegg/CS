import java.util.Scanner;
import java.lang.Math;

public class BinaryToDecimal 
{
  public static void main(String[] args) 
  {
		// declare and initialize the program variables
	Scanner cin = new Scanner(System.in); 
	
    // display the program menu
    System.out.println("(Binary to Decimal Converter)\n");
    
	int iterations = 5;
	
	while (iterations > 0) {
	    System.out.println("\nEnter an 8 - bit signed Binary Number (e.g., 01101101)\n");

	    String line = "";
	    char a, b, c, d, e, f, g, h;
	    String result = "";

	    // input the sample binary number
	    // flip bits to get one's complement
	    line = cin.nextLine();
	    
	    boolean isNegativeSigned = line.charAt(0) == '1';
	    
	    if(isNegativeSigned) {
		    a = line.charAt(0) == '1' ? '0' : '1';
		    b = line.charAt(1)  == '1' ? '0' : '1';
		    c = line.charAt(2)  == '1' ? '0' : '1';
		    d = line.charAt(3)  == '1' ? '0' : '1';
		    e = line.charAt(4)  == '1' ? '0' : '1';
		    f = line.charAt(5)  == '1' ? '0' : '1';
		    g = line.charAt(6)  == '1' ? '0' : '1';
		    h = line.charAt(7)  == '1' ? '0' : '1';
	    }else {
		    a = line.charAt(0);
		    b = line.charAt(1);
		    c = line.charAt(2);
		    d = line.charAt(3);
		    e = line.charAt(4);
		    f = line.charAt(5);
		    g = line.charAt(6);
		    h = line.charAt(7);
	    }
	    

	    char[] charList={a,b,c,d,e,f,g,h};
	    
	    int decValue = 0;
	    
	    
	    for(int idx =0, bitDepth=charList.length-1; idx < charList.length; idx++, bitDepth--) {
	    	
	    	int charToInteger = Character.getNumericValue(charList[idx]);	 
	
	    	double calculation = charToInteger * Math.pow(2, bitDepth);
	    	
	    	decValue += calculation;
	 
	    }
	    
	    
	    char sign = isNegativeSigned ? '-': ' ';

	    // display the program output 
	    if(isNegativeSigned) {
		    System.out.println("\nthe one's complement of your input is ");
	    	
	    }else {
		    System.out.println("\nYou inputted: ");

	    }

	    result = a + "" + b + "" + c + "" + d + "";
	    result += e + "" + f + "" + g + "" + h;
	    System.out.println(result);
	    System.out.println("");
	    System.out.println("and its decimal equivalent is \n" + sign + decValue);
	
	    iterations--;
		
	}
    cin.close();
    
  }
}

