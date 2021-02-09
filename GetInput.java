/*
 * Rheanna Howell.
 * CIS-115-0901
 * Program 21 page 52
 * 20210209
 */
package getinput;

import java.util.Scanner;

public class GetInput 
{
    public static void main(String[] args) 
    {
     Scanner keyboard = new Scanner(System.in);
     String name;
     double payRate;
     int hours;
      
     System.out.print("Enter your name: ");
     name = keyboard.nextLine();
      
     System.out.print("Enter your hourly pay rate: ");
     payRate = keyboard.nextDouble();
     
     System.out.print("Enter the number of hours worked: ");
     hours = keyboard.nextInt();
     
     System.out.println("Here are the values that you entered:");
     System.out.println(name);
     System.out.println(payRate);
     System.out.println(hours);
    }
    
}
