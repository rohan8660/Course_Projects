package pro;
import static java.lang.System.exit;
import java.util.Scanner;
public class Pro {

    public static void main(String[] args) {
           int amt=0,unit=0;
         Scanner scan =new Scanner(System.in);
         for(;;){
         System.out.println(" 1: INDUSTRIAL USER  2:COMMERCIAL USER   3:PUBLIC USER     4:EXIT" );/* display the choices */
         System.out.println("ENTER YOUR CHOICE");
        int  var = scan.nextInt ();  /* Input of choice */
        switch(var){
                    case 1: System.out.println("Enter the units used");
                             unit=scan.nextInt(); /* input of units used */
                            
                             if(unit<=1500)
                             {
                                amt=1000+(8*unit);/*calculate amount*/
                             }
                             else if(unit>1499 && unit<3500)
                             {
                                amt=1000+(9*unit);  /*calculate amount*/                                       
                             }
                             
                             else if(unit>3499 && unit<5000) 
                             {
                                 amt=1000+(10*unit);/*calculate amount*/
                             }
                             else if(unit>=5000)
                             {
                                 amt=1000+(12*unit);/*calculate amount*/
                             }
                             break;
                             
                    case 2: System.out.println("Enter the units used");
                              unit=scan.nextInt(); 
                           
                             if(unit<=1000)
                             {
                                amt=500+(6*unit);/*calculate amount*/
                             }
                             else if(unit>999 && unit<1500)
                             {
                                amt=500+(7*unit);    /*calculate amount*/                                     
                             }
                             else if(unit>1499 && unit<2500)
                             {
                               amt=500+(8*unit); /*calculate amount*/
                             }
                             
                             else if(unit>=2500)
                             {
                                 amt=500+(10*unit);/*calculate amount*/
                             }
                             break;
                    case 3: System.out.println("Enter the units used");
                              unit=scan.nextInt(); 
                             
                             if(unit<=100)
                             {
                                amt=300+(3*unit);/*calculate amount*/
                             }
                             else if(unit>99 &&  unit<350)
                             {
                                amt=300+(4* unit);
                             }
                             else if( unit>350 &&  unit<500)
                             {
                               amt=300+(5* unit);/*calculate amount*/
                             }
                             
                             else if( unit>=500)
                             {
                                 amt=300+(8* unit);/*calculate amount*/
                             }
                             break;
                     case 4:System.out.println("");
                                System.out.println("THANK YOU");
                                exit(0);     /*Terminating the program*/  
                    default:System.out.println("INVALID CHOICE");                 
         }
        System.out.println("-----------------------------------------------------------------");
        System.out.println("*****************************************************************");
        System.out.println("-----------------------------------------------------------------");
        System.out.println("                           H E S C O M                           ");
        System.out.println("                         ELECTRICITY BILL                        ");
        System.out.println();
        System.out.println("NUMBER OF UNIT(S) USED   = "+unit+" units"                        );
        System.out.println("THE AMOUNT TO BE PAID IS = Rs."+amt                               );
        System.out.println();
        System.out.println("                             THANK YOU                            ");
        System.out.println("-----------------------------------------------------------------");
        System.out.println("*****************************************************************");
        System.out.println("-----------------------------------------------------------------");
        System.out.println();
     }   
    }
}  
