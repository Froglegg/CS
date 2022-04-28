import java.util.Scanner;
 
public class Add_Matrices 
{
	Scanner scan;
	int matrix1[][], matrix2[][], sum[][];
	int row, column;
 
	void create() {
		
	scan = new Scanner(System.in);
		
	System.out.println("Matrix Addition");
		
	// the first matrix is created

	System.out.println("\nEnter number of rows & columns");
	row = Integer.parseInt(scan.nextLine());
	column = Integer.parseInt(scan.nextLine());
		
	matrix1 = new int[row][column];
	matrix2 = new int[row][column];
	sum = new int[row][column];
 
	System.out.println("enter the data for first matrix :");
 
	for(int i = 0; i < row; i++) 
	{
	  for(int j = 0; j < column; j++) 
	  {
	    matrix1[i][j] = scan.nextInt();
	  }
	}
		
	// the second matrix is created

	System.out.println("enter the data for second matrix :");
 
		for(int i = 0; i < row; i++) {
			
			for(int j = 0; j < column; j++) {
				
				matrix2[i][j] = scan.nextInt();
			}
		}
	}
    void display() {
		
		System.out.println("\nThe First Matrix is :");
		
		for(int i = 0; i < row; i++) {
			
			for(int j = 0; j < column; j++) {
				
				System.out.print("\t" + matrix1[i][j]);
			}
			System.out.println();
		}
		
		System.out.println("\n\nThe Second Matrix is :");
		
		for(int i = 0; i < row; i++) {
			
			for(int j = 0; j < column; j++) {
				
				System.out.print("\t" + matrix2[i][j]);
			}
			System.out.println();
		}
	}
	
void add() {
		
		for(int i = 0; i < row; i++) {
			
			for(int j = 0; j < column; j++) {
				
				sum[i][j] = matrix1[i][j] + matrix2[i][j];
			}
		}
		
		System.out.println("\n\nThe Sum is :");
		
		for(int i = 0; i < row; i++) {
			
			for(int j = 0; j < column; j++) {
				
				System.out.print("\t" + sum[i][j]);
			}
			System.out.println();
		}
	}
}
class MainClass 
{
    public static void main(String args[]) 
   {
		// a class object is created	
		Add_Matrices obj = new Add_Matrices();
		// the class object performs a sequence of actions
		obj.create();
		// start the clock
		long preTime = System.currentTimeMillis();
		System.out.println("\n\nStart time: %s ms".formatted(preTime));
		// perform matrix addition
		obj.display();
		obj.add();
		// stop the clock
		long postTime = System.currentTimeMillis();
		System.out.println("\n\nEnd time: %s ms".formatted(postTime));
		// print total time elapsed
		long timeElapsed = postTime - preTime;
		System.out.println("\n\nTime elapsed: %s ms".formatted(timeElapsed));
	}
}
