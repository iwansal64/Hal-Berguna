import java.util.Scanner;

public class KalkulatorJava {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int x = scan.nextInt();
		String operasi = scan.next();
		int y = scan.nextInt();
		
		if(operasi.equals("+")) {
			System.out.println(x+y);
		}
		else if(operasi.equals("-")) {
			System.out.println(x-y);
		}
		else if(operasi.equals(":")){
			System.out.println(x/y);
		}
		else if(operasi.equals("x")) {
			System.out.println(x*y);
		}
		else {
			System.out.println("operasi tidak dikenali..");
		}
	}
}
