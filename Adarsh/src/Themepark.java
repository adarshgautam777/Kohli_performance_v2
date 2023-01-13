import java.util.*;
abstract class Themepark
{
  abstract void playGame();
  abstract public void calculate(int adult, int child);
}

class Queensland extends Themepark
 {
     public void calculate(int adult, int child)
  {
    System.out.println("Tickets Bought:Adult="+adult + "\tchild ="+child);
    System.out.println("Total cost="+((adult*500)*(child*300)));
  }
   public void playGame()
   {
     Scanner sc = new Scanner(System.in);
     System.out.println("Disclaimer: Every game can be played only once!!");
     boolean games[] = new boolean[30];
     int choice =-1;
     while(choice!=0)
     {
       System.out.println("There are total 30 games.\n\tEnter your choice:");
       System.out.println("To finish enter 0.");
       choice = sc.nextInt();
       if(choice!=0 && (choice>0 && choice<=30))
       {
         if(games[choice]==false)
         {
           System.out.println("You can play the game.");
           games[choice]=true;
         }
         else
        	 System.out.println("You have already played this game.You can't play again.");
       }
       else if(choice==0)
       {
    	   System.out.println("Thank you for visiting.");
       }
       else
       {
    	   System.out.println("Please enter a valid choice!!!!");
       }
     }
   }
}
class wonderla extends Themepark
{
     public void calculate(int adult, int child)
  {
    System.out.println("Tickets Bought:Adult="+adult + "\tchild ="+child);
    System.out.println("Total cost="+((adult*500)*(child*300)));
  }
	public void playGame()
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Disclaimer:Every game can be played multiple times.");
		int games[]=new int[10];
		int choice=-1;
		while(choice!=0)
		{
			System.out.println("There are total 40 games.\n\tEnter your choice:");
			System.out.println("To finish enter 0.");
			choice=sc.nextInt();
			if(choice>0 && choice<=40)
			{
				System.out.println("you can play the game.");
				games[choice]++;
			}
			else if(choice==0)
				System.out.println("Thank you for visiting.");
			else
				System.out.println("Please enter a valid choice!!");
		}
		System.out.println("List of the games played:");
		for(int i=0; i<games.length;i++)
		{
			if(games[i]!=0)
				System.out.println("Game"+i+"played"+games[i]+"times.");
		}
		System.out.println("\nList of the games not played:");
		for(int i=0;i<games.length;i++)
		{
			if(games[i]==0)
				System.out.println("Game"+i+"\t");
		}
	}
}
class main
{
    public static void main(String args [])
	{
		Queensland Q=new Queensland();
		wonderla W = new wonderla();
		Q.calculate(2, 5);
		W.calculate(5, 7);
		Q.playGame();
		W.playGame();
	}
}