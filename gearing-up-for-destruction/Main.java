

public class Main {
    public static void main(String[] args) {
        int [] a = {4,30,50};
        solution(a);
    }

    public static int[] solution(int[] pegs) {
        int[] res = {-1,-1};
        double r = 0;
        for (int n = 1; n <= 10000; n++) {
            for (int d = n-1; d >= 1; d--) {
                int n1 = n;
                for (int i = 0; i < pegs.length-1; i++) {
                    if ((pegs[i]+(n1/d)>=pegs[i+1]-1)){
                        break;
                    }else {
                        n1= (pegs[i+1]*d) - ((pegs[i]*d) + (n1));
                        r= ((double) n / (double) d)/((double) n1 / (double) d);
                        if ((i == pegs.length-2)&&(r==2)){
                            res[0] =n;
                            res[1]= d;
                            System.out.println(res[0] + " " +  res[1]);
                            return res;
                        }
                    }
                }
            }
        }
        System.out.println(res[0] + " " +  res[1]);
        return res;
    }
}