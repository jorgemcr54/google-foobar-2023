import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        long begin = System.currentTimeMillis();
        System.out.println(solution(0,1));
        long end = System.currentTimeMillis();
        long time = end-begin;
        System.out.println();
        System.out.println("Elapsed Time: "+time +" milli seconds");
    }

    public static int solution(int src, int dest) {
        if (src!=dest) {
            List<Integer> moves = findMoves(src);
            List<Integer> movesNext = new ArrayList<>();
            List<Integer> valuesVisited = new ArrayList<>();
            valuesVisited.add(src);
            int cont = 1;
            while (true) {
                if (moves.stream().noneMatch(p -> p == dest)) {
                    valuesVisited.addAll(moves);
                    for (Integer move : moves) {
                        movesNext.addAll(findMoves(move));
                    }
                    moves = movesNext.stream()
                            .distinct()
                            .filter(p -> !valuesVisited.contains(p))
                            .collect(Collectors.toList());
                    cont++;
                } else break;
            }
            return cont;
        }
        else return 0;
    }

    public static List<Integer> findMoves(Integer value){
        int[][] moves = {
                {-2, 1}, {-1, 2}, {1, 2}, {2, 1},
                {2, -1}, {1, -2}, {-1, -2}, {-2, -1}
        };
        List<Integer> num = new ArrayList<>();
        for (int[] move : moves) {
            int newRow = value/8 + move[0];
            int newColumn = value%8 + move[1];
            if (isValidMovement(newRow, newColumn)) {
                num.add(newRow*8 + newColumn);
            }
        }
        return num;
    }

    public static boolean isValidMovement(int row, int column) {
        return (row >= 0 && row < 8 && column >= 0 && column < 8);
    }
}