public class dsa6{  
    public static void main(String args[]){  
    int i,j,k=0;
    int a[]={1,2,3,4,5,6};
    int b[]={100,3,900,1,5};
    for(i=0;i<a.length;i++)
    {
      k=a[i];
      
      for(j=0;j<b.length;j++)
      {
          if(k==b[j])
          {
           System.out.println(k);
          }
  
      }
    }

    


    }
}