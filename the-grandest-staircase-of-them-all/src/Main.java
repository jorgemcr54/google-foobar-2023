import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        System.out.println(solution(200));
        System.out.println(solution(3));
    }
    public static int solution(int n) {
        recursiveSearch(2,0,)
    }

    public static boolean isValid(List<Integer> staircase, int totalBricks){
        return staircase.stream()
                .mapToInt(Integer::intValue)
                .sum() == totalBricks;
    }

    public static int recursiveSearch(int steps, int cont, int pos, List<Integer> staircase ,int total){
        if (pos>steps)
        {
            return cont;
        }
        for (int i = 1; i <= total ; i++) {
            staircase.set(pos,staircase.get(pos)+1);
            if (isValid(staircase,total)){
                cont += 1;
                staircase.forEach(System.out::println);
            }
            recursiveSearch(steps,cont,pos+1,staircase,total);
        }

    }
}