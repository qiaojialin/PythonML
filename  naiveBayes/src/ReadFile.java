import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

/**
 * Created by linli on 2016/11/25.
 */
public class ReadFile {
    public ArrayList<ArrayList<String>> readData(String filePath) throws IOException {
        ArrayList<ArrayList<String>> datas = new ArrayList<ArrayList<String>>();
        //BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(filePath)));
        String str = "";
        while (!(str = reader.readLine()).equals("")) {
            StringTokenizer tokenizer = new StringTokenizer(str);
            ArrayList<String> s = new ArrayList<String>();
            while (tokenizer.hasMoreTokens()) {
                s.add(tokenizer.nextToken());
            }

            //fnlweight continous
            String temp = s.get(2);
            temp = temp.substring(0,temp.length()-1);
            int temp2 = Integer.parseInt(temp);
            temp2 = temp2/10000;
            s.set(2,Integer.toString(temp2));

            //captital gain: discrete
            temp = s.get(10);
            temp = temp.substring(0,temp.length()-1);
            temp2 = Integer.parseInt(temp);
            temp2 = temp2/100;
            s.set(10,Integer.toString(temp2));

            //capital loss:discrete
            temp = s.get(11);
            temp = temp.substring(0,temp.length()-1);
            temp2 = Integer.parseInt(temp);
            temp2 = temp2/100;
            s.set(11,Integer.toString(temp2));

            datas.add(s);
            //System.out.println(s);
        }
        return datas;
    }
}
