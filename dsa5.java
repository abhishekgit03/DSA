import java.util.Scanner;
public class dsa5{  
    int i;
    static int j=0;
    static int c=0;
    static Scanner sc=new Scanner(System.in);  
    public static void main(String args[]){  
    int a[]=new int[50];
    System.out.println("Enter the elements:");
    for(int i=0;i<5;i++)
    {
        a[i]=sc.nextInt();  
    }
    for(int i=0;i<4;i++)
    {
       if(a[i]<0)
       {
       if(i!=j)
       {
         c=a[i];
         a[i]=a[j];
         a[j]=c;
       }
       j++;
    }
    } 
    for(int i=0;i<5;i++)
    {
        System.out.print(a[i]+" "); 
    }
    }
}  