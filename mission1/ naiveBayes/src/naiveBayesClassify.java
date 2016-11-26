import java.io.IOException;
import java.util.ArrayList;


/**
 * Created by linli on 2016/11/25.
 */
public class naiveBayesClassify {

    public static void main(String args[]) throws IOException {
        String trainDataFile = "adult.data.txt";
        String testDataFile = "adult.test.txt";
        naiveBayes bayes = new naiveBayes();
        ReadFile rf = new ReadFile();
        ArrayList<ArrayList<String>> trainData = rf.readData(trainDataFile);
        ArrayList<ArrayList<String>> testData = rf.readData(testDataFile);
        int total = testData.size();
        int count = 0;
        int fail =0;
        for(int i = 0;i < testData.size();i++){
            //System.out.println(i);
            ArrayList<String> currentTestData = testData.get(i);
            String result = currentTestData.get(currentTestData.size()-1);
            result = result.substring(0,result.length()-1);
            //System.out.print(result+"    ");
            currentTestData.remove(currentTestData.size()-1);
            String predictResult = bayes.predictClass(trainData,currentTestData);
            if(result.equals(predictResult)) {
                count++;
            }
            if(predictResult.equals("fail")){
                fail++;
            }
        }

        System.out.println(count);

        System.out.println(fail);

        double p = DecimalCalculate.div(count,total);

        System.out.println(total);

        System.out.println("the accuracy: " + p);

    }
}
