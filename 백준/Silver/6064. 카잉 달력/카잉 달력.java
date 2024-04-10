import java.io.*;
import java.util.*;

public class Main{
    public static void main(String args[])throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int t = Integer.parseInt(br.readLine());
        while(t-->0){
            String[] input = br.readLine().split(" ");
            int M = Integer.parseInt(input[0]);
            int N = Integer.parseInt(input[1]);
            int x = Integer.parseInt(input[2]);
            int y = Integer.parseInt(input[3]);
            
            //10*12=120
            int MAXxy = M * N;
            int index = 0;
            if(y==N) y=0;
            int result = -1;
            
            while(true){
                if((M*index+x)%N==y){
                    result = M*index +x;
                    break;
                }
                if(M*index+x>MAXxy)
                    break;
                index++;
            }
            System.out.println(result);
        }
    }
}