import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        long begin = System.currentTimeMillis();
        String word = "abcdabcdabcdabcdabcdabcdabcdabcdabcdrabcdabcdabcdabcdabcdabcdabcdabcdabcdr";
        for(int i = 1; i<=word.length(); i++) {
            if(word.length() % i == 0) {
                if (testr(word,i)){
                    System.out.println(word.length()/i + " respuesta correcta");
                    break;
                }
            }
        }
        long end = System.currentTimeMillis();
        long time = end-begin;
        System.out.println();
        System.out.println("Elapsed Time: "+time +" milli seconds");
    }


    private static boolean test(String word, int divisor){
        String seq = word.substring(0,divisor);
        for(int i = divisor ; i <= word.length()-divisor;i=i+divisor){
            if(!word.substring(i,i+divisor).equals(seq)) return false;
        }
        return true;
    }

    public static  boolean testr(String x, int div){
        String a = x.substring(0,div);
        return IntStream.range(0, x.length() / div + 1)
                .mapToObj(i -> x.substring(i * div, Math.min((i + 1) * div, x.length())))
                .filter(str -> !str.isEmpty())
                .allMatch(c -> c.equals(a));
    }


}