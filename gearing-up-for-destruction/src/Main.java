import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        int [] a = {4,30,50};
        solution(a);
    }

    public static int[] solution(int[] pegs) {
        List<Integer> ratios = new ArrayList<>();
        for (int i = 1; i < pegs[1]-pegs[0]; i++) {
            ratios.add(i);
            for (int j = 1; j < pegs.length; j++) {

            }
            ratios.forEach(System.out::println);
            ratios.clear();
            System.out.println("otro");
        }



        int[] a= {1,1};
        return a;
    }

    public static boolean finalRpm(int[] list){
        double v=1;
        for (int i = 0; i < list.length-1; i++) {
            v= list[i]*v/(list[i+1]);
        }
        return (v==2);
    }
}