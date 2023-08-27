public class Main {
    public static void main(String[] args) {
        solution(17,4);
    }
    public static int solution(int start, int length) {
        int cont = length;
        int checksum = 0;
        for (int i = start; i < (length*length) + start; i=i+length) {
            for (int j = 0; j < cont; j++) {
                checksum = checksum^(i+j);
            }
            cont--;
        }
        return checksum;
    }
}