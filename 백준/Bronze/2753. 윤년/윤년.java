import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        //시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
        Scanner sc = new Scanner(System.in);
        int a= sc.nextInt();



        if(a%4==0&&true&&a%100!=0||a%400==0){
            System.out.println("1");
        }

        else {
            System.out.println("0");
        }

    }
}