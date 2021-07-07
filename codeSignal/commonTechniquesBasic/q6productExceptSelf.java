package Fundamentals.codeSignal.commonTechniquesBasic;

import java.math.BigInteger;
import java.util.ArrayList;

public class q6productExceptSelf {

    static int productExceptSelf(int[] nums, int m) {
        ArrayList<BigInteger> listBI = new ArrayList<BigInteger>();
        BigInteger max = BigInteger.ONE;
        BigInteger mod = BigInteger.valueOf(m);
        for (int val : nums){
            BigInteger current = BigInteger.valueOf(val);
            max = max.multiply(current);
            listBI.add(current);
        }
        BigInteger accum = BigInteger.ZERO;
        for(BigInteger val : listBI) {
            accum = accum.add((max.divide(val)).mod(mod));
        }
            return accum.mod(mod).intValue();

        /*
        Double dm = Double.valueOf(m);
        List<Double> dStream = Arrays.stream(nums).parallel().mapToDouble(x->x).boxed().collect(Collectors.toList());
        //boxed().mapToDouble(x->x).collect(Collectors.toList());

        final Optional<Double> max = dStream.stream().reduce((v1,v2) -> v1 * v2);
        if(!max.isPresent()) return -1;
        Optional<Double> streamReducer = dStream.stream().map(x -> (max.get() / x) % dm).reduce(Double::sum);
        
        int retInt = ((int) (streamReducer.get() % dm));
        //.map(i -> new BigInteger(i.toString())).collect(Collectors.toList());
        return retInt;
        /*final BigInteger mod = new BigInteger(String.valueOf(m));
        List<BigInteger> objList = Arrays.stream(nums).parallel().boxed().map(i -> new BigInteger(i.toString())).collect(Collectors.toList());
        Optional<BigInteger> sum = objList.stream().parallel().reduce((v1, v2) -> v1.multiply(v2));

        Optional<BigInteger> k = objList.stream().parallel().map(x -> sum.get().divide(new BigInteger(x.toString())).mod(mod)).reduce((v1, v2) -> v1.add(v2));
    return k.get().mod(mod).intValue();*/
}
    public static void main(String[] args){
        productExceptSelf(new int[]{2,100},24);
    }
}
