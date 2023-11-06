import java.util.*;
import java.util.stream.*;
import java.math.*;

public class Main
{
	public static void main(String[] args) {
		System.out.println(day18p2());
	}
	
	public static BigInteger day18p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    BigInteger sum = BigInteger.ZERO;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        BigInteger val = parseParentheses2(str);
	        System.out.println(val);
	        sum = sum.add(val);
	    }
	    
	    return sum;
	}
	
	public static BigInteger parseParentheses2(String str) {
	    String temp5 = str.replaceAll("(\\d+ \\+ \\d+)", "($1)");
	    String temp6 = str.replaceAll("(\\d+ \\+ \\d+)", "($1)");
	    String temp7 = str.replaceAll("(\\d+ \\+ \\d+)", "($1)");
	    String temp8 = str.replaceAll("(\\d+ \\+ \\d+)", "($1)");
	    String temp9 = str.replaceAll("(\\d+ \\+ \\d+)", "($1)");
	    String temp10 = str.replaceAll("((\\d+|\\(.+\\)) \\+ (\\d+|\\(.+\\)))", "($1)");
	    List<String> parentheses = new ArrayList<>(Arrays.asList(temp10.split("[\\(\\)]")));
	    
	    while (parentheses.size() > 1) {
    	    for (int i = parentheses.size()-1; i >= 0; i--) {
    	        if (!parentheses.get(i).startsWith(" ") && !parentheses.get(i).endsWith(" ") && !parentheses.get(i).equals("")) {
    	            BigInteger val = parseMathExp2(parentheses.get(i));
    	            if (i == 0 && i == parentheses.size() - 1) {
    	                parentheses.set(i, val.toString());
    	            } else if (i == 0) {
    	                parentheses.set(i, val.toString() + parentheses.get(i + 1));
    	                parentheses.remove(i + 1);
    	            } else if (i == parentheses.size() - 1) {
    	                parentheses.set(i - 1, parentheses.get(i - 1) + val.toString());
    	                parentheses.remove(i);
    	            } else {
    	                parentheses.set(i - 1, parentheses.get(i - 1) + val.toString() + parentheses.get(i + 1));
    	                parentheses.remove(i + 1);
    	                parentheses.remove(i);
    	            }
    	        }
    	    }
    	    
    	   // System.out.println("Size: " + parentheses.size());
	    }
	    
	    return parseMathExp2(parentheses.get(0));
	}
	
	public static BigInteger parseMathExp2(String str) {
	    try {
	        return new BigInteger(str);
	    } catch (Exception e) { }
	    
	    String[] terms = str.split(" ");
	    
	    BigInteger total = BigInteger.valueOf(-1);
	    boolean opMultiply = false;
	    
	    for (String term : terms) {
	        if (total.equals(BigInteger.valueOf(-1))) {
	            total = new BigInteger(term);
	            continue;
	        }
	        
	        try {
	            if (opMultiply) total = total.multiply(new BigInteger(term));
	            else total = total.add(new BigInteger(term));
	            opMultiply = false;
	        } catch (Exception e) {
	            if (term.equals("*")) opMultiply = true;
	            else if (term.equals("+")) opMultiply = false;
	            else System.out.println("Unknown term: " + term);
	        }
	    }
	    
	    return total;
	}
	
	public static BigInteger day18p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    BigInteger sum = BigInteger.ZERO;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        long val = parseParentheses(str);
	       // System.out.println(val);
	        sum = sum.add(BigInteger.valueOf(val));
	    }
	    
	    return sum;
	}
	
	public static long parseParentheses(String str) {
	    List<String> parentheses = new ArrayList<>(Arrays.asList(str.split("[\\(\\)]")));
	    
	    while (parentheses.size() > 1) {
    	    for (int i = parentheses.size()-1; i >= 0; i--) {
    	        if (!parentheses.get(i).startsWith(" ") && !parentheses.get(i).endsWith(" ") && !parentheses.get(i).equals("")) {
    	            long val = parseMathExp(parentheses.get(i));
    	            if (i == 0 && i == parentheses.size() - 1) {
    	                parentheses.set(i, String.valueOf(val));
    	            } else if (i == 0) {
    	                parentheses.set(i, String.valueOf(val) + parentheses.get(i + 1));
    	                parentheses.remove(i + 1);
    	            } else if (i == parentheses.size() - 1) {
    	                parentheses.set(i - 1, parentheses.get(i - 1) + String.valueOf(val));
    	                parentheses.remove(i);
    	            } else {
    	                parentheses.set(i - 1, parentheses.get(i - 1) + String.valueOf(val) + parentheses.get(i + 1));
    	                parentheses.remove(i + 1);
    	                parentheses.remove(i);
    	            }
    	        }
    	    }
    	    
    	   // System.out.println("Size: " + parentheses.size());
	    }
	    
	    return parseMathExp(parentheses.get(0));
	}
	
	public static long parseMathExp(String str) {
	    try {
	        return Long.parseLong(str);
	    } catch (Exception e) { }
	    
	    String[] terms = str.split(" ");
	    
	    long total = -1;
	    boolean opMultiply = false;
	    
	    for (String term : terms) {
	        if (total == -1) {
	            total = Long.parseLong(term);
	            continue;
	        }
	        
	        try {
	            if (opMultiply) total *= Long.parseLong(term);
	            else total += Long.parseLong(term);
	            opMultiply = false;
	        } catch (Exception e) {
	            if (term.equals("*")) opMultiply = true;
	            else if (term.equals("+")) opMultiply = false;
	            else System.out.println("Unknown term: " + term);
	        }
	    }
	    
	    return total;
	}
	
	public static int day17p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    int sideLength = Integer.parseInt(sc.nextLine());
        
        boolean[][][][] cubes = new boolean[sideLength + 12][sideLength + 12][13][13];
        
        for (int i = 6; i < sideLength + 6; i++) {
            String str = sc.nextLine();
	        char[] chars = str.toCharArray();
	        for (int j = 6; j < sideLength + 6; j++) {
	            if (chars[j-6] == '#') cubes[i][j][6][6] = true;
	        }
	    }
	    
	    for (int iteration = 0; iteration < 6; iteration++) {
	        boolean[][][][] copy = new boolean[sideLength + 12][sideLength + 12][13][13];
	        for (int i = 0; i < cubes.length; i++)
	            for (int j = 0; j < cubes[i].length; j++)
	                for (int k = 0; k < cubes[i][j].length; k++)
                        copy[i][j][k] = cubes[i][j][k].clone();
            
            for (int x = 0; x < cubes.length; x++) {
                for (int y = 0; y < cubes[x].length; y++) {
                    for (int z = 0; z < cubes[x][y].length; z++) {
                        for (int w = 0; w < cubes[x][y][z].length; w++) {
                            int adjActive = 0;
    	                    
    	                    for (int[] coords : getAdjacentCubes(x, y, z, w)) {
    	                        try {
    	                            if (copy[coords[0]][coords[1]][coords[2]][coords[3]]) adjActive++;
    	                        } catch (Exception e) {}
    	                    }
    	                    
    	                    if (adjActive == 3) cubes[x][y][z][w] = true;
    	                    else if (adjActive == 2 && copy[x][y][z][w]) cubes[x][y][z][w] = true;
    	                    else cubes[x][y][z][w] = false;
                        }
                    }
                }
            }
	    }
	    
	    int total = 0;
	    
	    for (boolean[][][] temp1 : cubes)
    	    for (boolean[][] temp2 : temp1)
    	        for (boolean[] temp3 : temp2)
    	            for (boolean temp4 : temp3)
    	                if (temp4) total++;
	    
	    return total;
	}
	
	public static List<int[]> getAdjacentCubes(int x, int y, int z, int w) {
	    List<int[]> result = new ArrayList<>();
	    
	    for (int dx = -1; dx <= 1; dx++) {
	        for (int dy = -1; dy <= 1; dy++) {
	            for (int dz = -1; dz <= 1; dz++) {
	                for (int dw = -1; dw <= 1; dw++) {
    	                if (dx == 0 && dy == 0 && dz == 0 && dw == 0) continue;
    	                result.add(new int[]{ x + dx, y + dy, z + dz, w + dw });
	                }
	            }
	        }
	    }
	    
	    return result;
	}
	
	public static int day17p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    int sideLength = Integer.parseInt(sc.nextLine());
        
        boolean[][][] cubes = new boolean[sideLength + 12][sideLength + 12][13];
        
        for (int i = 6; i < sideLength + 6; i++) {
            String str = sc.nextLine();
	        char[] chars = str.toCharArray();
	        for (int j = 6; j < sideLength + 6; j++) {
	            if (chars[j-6] == '#') cubes[i][j][6] = true;
	        }
	    }
	    
	    for (int iteration = 0; iteration < 6; iteration++) {
	        boolean[][][] copy = new boolean[sideLength + 12][sideLength + 12][13];
	        for (int i = 0; i < cubes.length; i++)
	            for (int j = 0; j < cubes[i].length; j++)
                    copy[i][j] = cubes[i][j].clone();
            
            for (int x = 0; x < cubes.length; x++) {
                for (int y = 0; y < cubes[x].length; y++) {
                    for (int z = 0; z < cubes[x][y].length; z++) {
                        int adjActive = 0;
	                    
	                    for (int[] coords : getAdjacentCubes(x, y, z)) {
	                        try {
	                            if (copy[coords[0]][coords[1]][coords[2]]) adjActive++;
	                        } catch (Exception e) {}
	                    }
	                    
	                    if (adjActive == 3) cubes[x][y][z] = true;
	                    else if (adjActive == 2 && copy[x][y][z]) cubes[x][y][z] = true;
	                    else cubes[x][y][z] = false;
                    }
                }
            }
	    }
	    
	    int total = 0;
	    
	    for (boolean[][] temp2 : cubes) {
	        for (boolean[] temp3 : temp2) {
	            for (boolean temp4 : temp3) {
	                if (temp4) total++;
	            }
	        }
	    }
	    
	    return total;
	}
	
	public static List<int[]> getAdjacentCubes(int x, int y, int z) {
	    List<int[]> result = new ArrayList<>();
	    
	    for (int dx = -1; dx <= 1; dx++) {
	        for (int dy = -1; dy <= 1; dy++) {
	            for (int dz = -1; dz <= 1; dz++) {
	                if (dx == 0 && dy == 0 && dz == 0) continue;
	                result.add(new int[]{ x + dx, y + dy, z + dz });
	            }
	        }
	    }
	    
	    return result;
	}
	
	public static long day16p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    List<Range> ranges = new ArrayList<>();
	    List<List<Integer>> nearbyTickets = new ArrayList<>();
	    List<Integer> myTickets = new ArrayList<>();
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        if (str.equals("")) continue;
	        
	        if (str.equals("your ticket:")) {
	            String temp7 = sc.nextLine();
	            for (String s : temp7.split(",")) {
	                myTickets.add(Integer.parseInt(s));
	            }
	            sc.nextLine();
	            continue;
	        }
	        
	        if (str.equals("nearby tickets:")) {
	            readLine:
	            while (sc.hasNext()) {
	                String temp = sc.nextLine();
	                if (temp.equals("")) break;
	                
	                List<Integer> temp5 = new ArrayList<>();
	                
	                for (String s : temp.split(",")) {
	                    int n = Integer.parseInt(s);
	                    
	                    boolean valid = false;
	                    for (Range r : ranges) {
	                        if (r.isTrue(n)) valid = true;
	                    }
	                    if (!valid) continue readLine;
	                    
	                    temp5.add(n);
	                }
	                
	                nearbyTickets.add(temp5);
	            }
	            continue;
	        }
	        
	        String temp1 = str.split(": ")[1];
	        String[] temp2 = temp1.split(" or ");
	        String[] temp3 = temp2[0].split("-");
	        String[] temp4 = temp2[1].split("-");
	        
	        ranges.add(new Range(str.split(": ")[0], Integer.parseInt(temp3[0]), Integer.parseInt(temp3[1]), Integer.parseInt(temp4[0]), Integer.parseInt(temp4[1])));
	    }
	    
	    int mult = 1;
	    Map<Range, List<Integer>> validIndexes = new HashMap<>();
	    
	    for (Range r : ranges) {
	       // if (!r.field.startsWith("departure")) continue;
	        List<Integer> validI = new ArrayList<>();
	        indexLoop:
	        for (int i = 0; i < nearbyTickets.get(0).size(); i++) {
	            for (int j = 0; j < nearbyTickets.size(); j++) {
	                if (!r.isTrue(nearbyTickets.get(j).get(i))) {
	                    System.out.println("Range " + r.field + " is false for " + nearbyTickets.get(j).get(i) + " at index " + i + ", line " + j);
	                    continue indexLoop;
	                }
	            }
	            System.out.println(r.field + ": " + i);
	            if (r.field.startsWith("departure")) mult *= myTickets.get(i);
	            validI.add(i);
	        }
	        validIndexes.put(r, validI);
	    }
	    
	    List<Integer> foundIndexes = new ArrayList<>();
	    foundIndexes.add(0);
	    foundIndexes.add(1);
	    foundIndexes.add(4);
	    foundIndexes.add(5);
	    foundIndexes.add(6);
	    foundIndexes.add(7);
	    foundIndexes.add(8);
	    foundIndexes.add(9);
	    foundIndexes.add(10);
	    foundIndexes.add(11);
	    foundIndexes.add(12);
	    foundIndexes.add(13);
	    foundIndexes.add(14);
	    foundIndexes.add(15);
	    foundIndexes.add(18);
	    foundIndexes.add(19);
	    
	    for (Map.Entry<Range, List<Integer>> entry : validIndexes.entrySet()) {
	        Range r = entry.getKey();
	        System.out.println(r.field + ": " + entry.getValue().stream().filter(n -> !foundIndexes.contains(n)).map(String::valueOf).collect(Collectors.joining(", ")));
	    }
	    
	    return (long)myTickets.get(6) * myTickets.get(7) * myTickets.get(12) * myTickets.get(13) * myTickets.get(14) * myTickets.get(18);
	    
	    /*
	    0: arrival location
	    1: class
	    2: route
	    3: train
	    4: arrival platform
	    5: type
	    6: departure station
	    7: departure track
	    8: row
	    9: seat
	    10: arrival track
	    11: zone
	    12: departure date
	    13: departure platform
	    14: departure time
	    15: duration
	    16: price
	    17: wagon
	    18: departure location
	    19: arrival station
	    */
	}
	
	public static int day16p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    Set<Integer> validNums = new HashSet<>();
	    int totalInvalid = 0;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        if (str.equals("")) continue;
	        
	        if (str.equals("your ticket:")) {
	            sc.nextLine();
	            sc.nextLine();
	            continue;
	        }
	        
	        if (str.equals("nearby tickets:")) {
	            while (sc.hasNext()) {
	                String temp = sc.nextLine();
	                if (temp.equals("")) break;
	                
	                for (String s : temp.split(",")) {
	                    int n = Integer.parseInt(s);
	                    if (!validNums.contains(n)) totalInvalid += n;
	                }
	            }
	            continue;
	        }
	        
	        String temp1 = str.split(": ")[1];
	        String[] temp2 = temp1.split(" or ");
	        String[] temp3 = temp2[0].split("-");
	        String[] temp4 = temp2[1].split("-");
	        
	        for (int i = Integer.parseInt(temp3[0]); i <= Integer.parseInt(temp3[1]); i++) validNums.add(i);
	        for (int i = Integer.parseInt(temp4[0]); i <= Integer.parseInt(temp4[1]); i++) validNums.add(i);
	    }
	    
	    return totalInvalid;
	}
	
	public static int day15p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    List<Integer> nums = new ArrayList<>();
	    Map<Integer, Integer> numCache = new HashMap<>();
	    
	    String str = sc.nextLine();
	    String[] temp = str.split(",");
	    for (String s : temp) {
	        nums.add(Integer.parseInt(s));
	        if (nums.size() != temp.length) numCache.put(Integer.parseInt(s), nums.size() - 1);
	    }
	    
	    int index = nums.size() - 1;
	    while (nums.size() < 30000000) {
	        int lastIndex = -1;
	        if (numCache.containsKey(nums.get(index))) lastIndex = numCache.get(nums.get(index));
	        int result = 0;
	        if (lastIndex != -1) result = (index) - lastIndex;
	       // System.out.println(lastIndex + " " + result);
	        nums.add(result);
	        numCache.put(nums.get(index), index);
	        index++;
	        if (nums.size() % 3000000 == 0) System.out.print("=");
	    }
	   // System.out.println();
	    return nums.get(29999999);
	}
	
	public static int day15p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    List<Integer> nums = new ArrayList<>();
	    
	    String str = sc.nextLine();
	    String[] temp = str.split(",");
	    for (String s : temp) {
	        nums.add(Integer.parseInt(s));
	    }
	    
	    int index = nums.size();
	    while (nums.size() < 2020) {
	        int lastIndex = nums.subList(0,index-1).lastIndexOf(nums.get(index-1));
	        int result = 0;
	        if (lastIndex != -1) result = (index-1) - lastIndex;
	        nums.add(result);
	        index++;
	    }
	    
	    return nums.get(2019);
	}
	
	public static BigInteger smallestPositiveMod(BigInteger x, BigInteger mod) {
	    return x.mod(mod);
	}
	
	public static long day14p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    Map<String, Integer> addresses = new HashMap<>();
	    char[] maskChars = new char[36];
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        if (str.startsWith("mask = ")) {
	            String mask = str.replace("mask = ", "");
	            maskChars = mask.toCharArray();
	        } else {
	            str = str.replace("mem[", "");
	            String[] temp = str.split("] = ");
	            int index = Integer.parseInt(temp[0]);
	            int val = Integer.parseInt(temp[1]);
	            String bIndex = String.format("%36s", Integer.toBinaryString(index)).replace(' ', '0');
	            char[] iChars = bIndex.toCharArray();
	            for (int i = 0; i < 36; i++) {
	                if (maskChars[i] == '0') continue;
	               // System.out.println("Setting " + valChars[i] + " to " + maskChars[i]);
	                iChars[i] = maskChars[i];
	            }
	           // System.out.println("Setting index " + new String(iChars));
	            for (String s : possibleIndexes(iChars)) {
	                addresses.put(s, val);
	            }
	        }
	    }
	   // for (Map.Entry<String, Integer> entry : addresses.entrySet()) System.out.println(entry.getKey() + ": " + entry.getValue());
	    return addresses.values().stream().mapToLong(Long::valueOf).sum();
	}
	
	public static List<String> possibleIndexes(char[] iChars) {
	    List<String> result = new ArrayList<>();
	   // System.out.println(new String(iChars));
	    
	    for (int i = 0; i < iChars.length; i++) {
	        if (iChars[i] != 'X') continue;
	        char[] temp1 = Arrays.copyOf(iChars, iChars.length);
	        temp1[i] = '0';
	        result.addAll(possibleIndexes(temp1));
	        char[] temp2 = Arrays.copyOf(iChars, iChars.length);
	        temp2[i] = '1';
	        result.addAll(possibleIndexes(temp2));
	        break;
	    }
	    
	    if (result.size() == 0) result.add(new String(iChars));
	    
	    return result;
	}
	
	public static long day14p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    long[] addresses = new long[100000];
	    char[] maskChars = new char[36];
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        if (str.startsWith("mask = ")) {
	            String mask = str.replace("mask = ", "");
	            maskChars = mask.toCharArray();
	        } else {
	            str = str.replace("mem[", "");
	            String[] temp = str.split("] = ");
	            int index = Integer.parseInt(temp[0]);
	            int val = Integer.parseInt(temp[1]);
	            String bval = String.format("%36s", Integer.toBinaryString(val)).replace(' ', '0');
	           // System.out.println(bval);
	            char[] valChars = bval.toCharArray();
	            for (int i = 0; i < 36; i++) {
	                if (maskChars[i] == 'X') continue;
	               // System.out.println("Setting " + valChars[i] + " to " + maskChars[i]);
	                valChars[i] = maskChars[i];
	            }
	           // System.out.println("Setting index " + index + " to " + Long.parseLong(new String(valChars), 2));
	            addresses[index] = Long.parseLong(new String(valChars), 2);
	        }
	    }
	    
	    return Arrays.stream(addresses).sum();
	}
	
	public static BigInteger day13p2() {
	    /*
	    0	: 17
        7	: 41
        17	: 643
        25	: 23
        30	: 13
        46	: 29
        48	: 433
        54	: 37
        67	: 19
        
        643 & 13 & 433 & 17 = 36662591
	    */
	    Scanner sc = new Scanner(System.in);
	    
	    int irrelevant = Integer.parseInt(sc.nextLine());
	    String[] buses = sc.nextLine().split(",");
	    
	    BigInteger timestamp = new BigInteger("100000000000000");
	    for (int i = 0; i < buses.length; i++) {
	        if (!buses[i].equals("x")) System.out.println(i + "\t: " + buses[i]);
	    }
	    return timestamp;
	    
	    /* User-assisted code
	    Scanner sc = new Scanner(System.in);
        
        while (sc.hasNext()) {
            String str = sc.nextLine();
            if (str.equals("stop")) break;
            
            String[] nums = str.split(" ");
            BigInteger a1 = new BigInteger(nums[0]), n1 = new BigInteger(nums[1]), a2 = new BigInteger(nums[2]), n2 = new BigInteger(nums[3]);
            BigInteger[] temp = gcd(n1, n2);
            BigInteger m1 = temp[1], m2 = temp[2];
            System.out.println(a1.multiply(m2).multiply(n2) + " " + a2.multiply(m1).multiply(n1) + " " + a1.multiply(m2).multiply(n2).add(a2.multiply(m1).multiply(n1)) + " " + smallestPositiveMod(a1.multiply(m2).multiply(n2).add(a2.multiply(m1).multiply(n1)), lcm(n1, n2)) + " " + lcm(n1, n2));
        }
        */
	}
	
	public static BigInteger[] gcd(BigInteger p, BigInteger q) {
        if (q.equals(BigInteger.ZERO))
            return new BigInteger[] { p, BigInteger.ONE, BigInteger.ZERO };
        
        BigInteger[] vals = gcd(q, p.mod(q));
        BigInteger d = vals[0];
        BigInteger a = vals[2];
        BigInteger b = vals[1].subtract(p.divide(q).multiply(vals[2]));
        return new BigInteger[] { d, a, b };
    }
    
    public static BigInteger lcm(BigInteger number1, BigInteger number2) {
        BigInteger gcd = number1.gcd(number2);
        BigInteger absProduct = number1.multiply(number2).abs();
        return absProduct.divide(gcd);
    }
   
    // public static int existenceConstruction(int[] pairs...) {
        
    // }
	
	public static int day13p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    int timestamp = Integer.parseInt(sc.nextLine());
	    String[] buses = sc.nextLine().split(",");
	    
	    int earliestBus = 0;
	    int earliestTime = Integer.MAX_VALUE;
	    
	    for (String bus : buses) {
	        if (bus.equals("x")) continue;
	        int busID = Integer.parseInt(bus);
	        if (busID - (timestamp % busID) < earliestTime) {
	            earliestBus = busID;
	            earliestTime = busID - (timestamp % busID);
	        }
	    }
	    
	    return earliestTime * earliestBus;
	}
	
	public static int day12p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    int x = 0;
	    int y = 0;
	    int wX = 10;
	    int wY = 1;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        char code = str.charAt(0);
	        int val = Integer.parseInt(str.substring(1, str.length()));
	        
	        switch (code) {
	            case 'N':
	                wY += val;
	                break;
	            case 'S':
	                wY -= val;
	                break;
	            case 'E':
	                wX += val;
	                break;
	            case 'W':
	                wX -= val;
	                break;
	            case 'F':
	                x += wX * val;
	                y += wY * val;
	                break;
	            case 'L':
	            case 'R':
	                int[] coords = rotatePoint(code, new int[]{wX, wY}, val);
	                wX = coords[0];
	                wY = coords[1];
	                break;
	            default:
	                break;
	        }
	    }
	    
	    return Math.abs(x) + Math.abs(y);
	}
	
	public static int[] rotatePoint(char code, int[] initCoords, int degrees) {
	    int mult = 1;
	    if (code == 'L') mult = -1;
	    
	    for (int i = 0; i < degrees / 90; i++) {
	        int temp = initCoords[0];
    	    initCoords[0] = mult * initCoords[1];
    	    initCoords[1] = mult * -temp;
	    }
	    
	    return initCoords;
	}
	
	public static int day12p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    char direction = 'E';
	    int x = 0;
	    int y = 0;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        char code = str.charAt(0);
	        int val = Integer.parseInt(str.substring(1, str.length()));
	        
	        switch (code) {
	            case 'N':
	                y += val;
	                break;
	            case 'S':
	                y -= val;
	                break;
	            case 'E':
	                x += val;
	                break;
	            case 'W':
	                x -= val;
	                break;
	            case 'F':
	                switch (direction) {
	                    case 'N':
        	                y += val;
        	                break;
        	            case 'S':
        	                y -= val;
        	                break;
        	            case 'E':
        	                x += val;
        	                break;
        	            case 'W':
        	                x -= val;
        	                break;
        	            default:
        	                break;
	                }
	                break;
	            case 'L':
	            case 'R':
	                direction = rotate(code, direction, val);
	                break;
	            default:
	                break;
	        }
	    }
	    
	    return Math.abs(x) + Math.abs(y);
	}
	
	public static char rotate(char code, char initDir, int degrees) {
	    List<Character> dirs = new ArrayList<>();
	    dirs.add('N');
	    dirs.add('E');
	    dirs.add('S');
	    dirs.add('W');
	    
	    int mult = 1;
	    if (code == 'L') mult = -1;
	    
	    int newIndex = dirs.indexOf(initDir) + mult * degrees / 90;
	    if (newIndex < 0) newIndex += dirs.size();
	    if (newIndex >= dirs.size()) newIndex -= dirs.size();
	    
	    return dirs.get(newIndex);
	}
	
	public static long day11p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    List<List<Character>> seats = new ArrayList<>();
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        List<Character> temp = new ArrayList<>();
	        
	        for (char c : str.toCharArray()) {
	            temp.add(c);
	        }
	        
	        seats.add(temp);
	    }
	    
	    boolean temp2 = true;
	    
	    while (temp2) {
	        Map.Entry<Boolean, List<List<Character>>> result = performRepetitionp2(seats);
	        seats = result.getValue();
	        temp2 = result.getKey();
	        
	       // for (List<Character> temp : seats) {
	       //     for (char c : temp) System.out.print(c);
	       //     System.out.println();
	       // }
	       // sc.nextLine();
	    }
	    
	    long total = 0;
	    
	    for (List<Character> temp : seats) {
	        for (char c : temp) {
	            if (c == '#') total++;
	        }
	    }
	    
	    return total;
	}
	
	public static Map.Entry<Boolean, List<List<Character>>> performRepetitionp2(List<List<Character>> seats) {
	    boolean hasChanged = false;
	    
	    List<List<Character>> copy = new ArrayList<>();
	    for (List<Character> temp3 : seats) {
	        copy.add(new ArrayList<>(temp3));
	    }
	    
	    for (int i = 0; i < copy.size(); i++) {
	        for (int j = 0; j < copy.get(i).size(); j++) {
	            char seat = copy.get(i).get(j);
	            if (seat == '.') continue;
	            
	            if (seat == 'L') {
	                boolean adjEmpty = true;
	                
	                for (char point : seePoints(copy, i, j)) {
                        if (!isSeatEmpty(point)) {
                            adjEmpty = false;
                            break;
                        }
	                }
	                if (adjEmpty) {
	                    seats.get(i).set(j, '#');
	                    hasChanged = true;
	                }
	            }
	            
	            if (seat == '#') {
	                int adjOcc = 0;
	                for (char point : seePoints(copy, i, j)) {
                        if (!isSeatEmpty(point)) {
                            adjOcc++;
                        }
	                }
	                if (adjOcc >= 5) {
	                    seats.get(i).set(j, 'L');
	                    hasChanged = true;
	                }
	            }
	        }
	    }
	    
	    return new AbstractMap.SimpleEntry<>(hasChanged, seats);
	}
	
	public static List<Character> seePoints(List<List<Character>> seats, int i, int j) {
	    List<Character> points = new ArrayList<>();
	    
	    for (int a = -1; a <= 1; a++) {
	        for (int b = -1; b <= 1; b++) {
	            if (a == 0 && b == 0) continue;
        	    for (int k = i+a, l = j+b; k >= 0 && k < seats.size() && l >= 0 && l < seats.get(0).size(); k+=a, l+=b) {
        	        char seat = seats.get(k).get(l);
        	        if (seat == '.') continue;
        	        points.add(seat);
        	        break;
        	    }
	        }
	    }
	    
	    return points;
	}
	
	public static long day11p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    List<List<Character>> seats = new ArrayList<>();
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        List<Character> temp = new ArrayList<>();
	        
	        for (char c : str.toCharArray()) {
	            temp.add(c);
	        }
	        
	        seats.add(temp);
	    }
	    
	    boolean temp2 = true;
	    
	    while (temp2) {
	        Map.Entry<Boolean, List<List<Character>>> result = performRepetitionp1(seats);
	        seats = result.getValue();
	        temp2 = result.getKey();
	        
	       // for (List<Character> temp : seats) {
	       //     for (char c : temp) System.out.print(c);
	       //     System.out.println();
	       // }
	       // sc.nextLine();
	    }
	    
	    long total = 0;
	    
	    for (List<Character> temp : seats) {
	        for (char c : temp) {
	            if (c == '#') total++;
	        }
	    }
	    
	    return total;
	}
	
	public static Map.Entry<Boolean, List<List<Character>>> performRepetitionp1(List<List<Character>> seats) {
	    boolean hasChanged = false;
	    
	    List<List<Character>> copy = new ArrayList<>();
	    for (List<Character> temp3 : seats) {
	        copy.add(new ArrayList<>(temp3));
	    }
	    
	    for (int i = 0; i < copy.size(); i++) {
	        for (int j = 0; j < copy.get(i).size(); j++) {
	            char seat = copy.get(i).get(j);
	            if (seat == '.') continue;
	            
	            if (seat == 'L') {
	                boolean adjEmpty = true;
	                out:
	                for (int k = i - 1; k <= i + 1; k++) {
	                    for (int l = j - 1; l <= j + 1; l++) {
	                        if (k == i && l == j) continue;
	                        if (k < 0 || k >= copy.size() || l < 0 || l >= copy.get(0).size()) continue;
	                        
	                        if (!isSeatEmpty(copy.get(k).get(l))) {
	                            adjEmpty = false;
	                            break out;
	                        }
	                    }
	                }
	                if (adjEmpty) {
	                    seats.get(i).set(j, '#');
	                    hasChanged = true;
	                }
	            }
	            
	            if (seat == '#') {
	                int adjOcc = 0;
	                for (int k = i - 1; k <= i + 1; k++) {
	                    for (int l = j - 1; l <= j + 1; l++) {
	                        if (k == i && l == j) continue;
	                        if (k < 0 || k >= copy.size() || l < 0 || l >= copy.get(0).size()) continue;
	                        
	                        if (!isSeatEmpty(copy.get(k).get(l))) {
	                            adjOcc++;
	                        }
	                    }
	                }
	                if (adjOcc >= 4) {
	                    seats.get(i).set(j, 'L');
	                    hasChanged = true;
	                }
	            }
	        }
	    }
	    
	    return new AbstractMap.SimpleEntry<>(hasChanged, seats);
	}
	
	public static boolean isSeatEmpty(char seat) {
	    return seat == '.' || seat == 'L';
	}
	
	public static long day10p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    List<Integer> jolts = new ArrayList<>();
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        jolts.add(Integer.parseInt(str));
	    }
	    
	    int oneJolt = 0;
	    int threeJolt = 0;
	    int currentJolt = 0;
	    
	    jolts.add(0);
	    jolts.add(Collections.max(jolts) + 3);
	    Collections.sort(jolts);
	    
	    return calculateArrangements(jolts, 0);
	}
	
	public static Map<Integer, Long> joltCache = new HashMap<>();
	
	public static long calculateArrangements(List<Integer> jolts, int startingIndex) {
	    if (joltCache.containsKey(startingIndex)) return joltCache.get(startingIndex);
	    long possibleArrangements = 0;
	    if (startingIndex == jolts.size() - 1) return 1;
	    for (int i = 1; i <= 3; i++) {
	        if (jolts.contains(jolts.get(startingIndex) + i)) possibleArrangements += calculateArrangements(jolts, jolts.indexOf(jolts.get(startingIndex) + i));
	    }
	    joltCache.put(startingIndex, possibleArrangements);
	    return possibleArrangements;
	}
	
	public static int day10p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    List<Integer> jolts = new ArrayList<>();
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        jolts.add(Integer.parseInt(str));
	    }
	    
	    int oneJolt = 0;
	    int threeJolt = 0;
	    int currentJolt = 0;
	    
	    jolts.add(0);
	    jolts.add(Collections.max(jolts) + 3);
	    Collections.sort(jolts);
	    
	    for (int i = 1; i < jolts.size(); i++) {
	        switch (jolts.get(i) - jolts.get(i-1)) {
	            case 1:
	                oneJolt++;
	                break;
	            case 2:
	                break;
	            case 3:
	                threeJolt++;
	                break;
	            default:
	                break;
	        }
	    }
	    
	    return oneJolt * threeJolt;
	}
	
	public static long day9p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    List<Long> nums = new ArrayList<>();
	    long invalidNum = 26134589L;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        long n = Long.parseLong(str);
	        
	        nums.add(n);
	    }
	    
	    for (int i = 0; i < nums.indexOf(invalidNum); i++) {
	        
	        for (int j = 2; j < nums.indexOf(invalidNum) - i; j++) {
	            List<Long> sublist = nums.subList(i, i+j);
	            if (sum(sublist) == invalidNum) {
	                return Collections.min(sublist) + Collections.max(sublist);
	            }
	        }
	    }
	    
	    return -1;
	}
	
	public static long sum(Collection<Long> c) {
	    return c.stream().mapToLong(Long::longValue).sum();
	}
	
	public static long day9p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    List<Long> nums = new ArrayList<>();
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        long n = Long.parseLong(str);
	        
	        nums.add(n);
	    }
	    
	    for (int i = 25; i < nums.size(); i++) {
	        long n = nums.get(i);
	        List<Long> sublist = nums.subList(i - 25, i);
	        boolean foundMatch = false;
	        for (long m : sublist) {
	            if (sublist.contains(n - m)) {
	                foundMatch = true;
	                break;
	            }
	        }
	        if (!foundMatch) return n;
	    }
	    
	    return -1;
	}
	
	public static int day8p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    List<Map.Entry<String, Integer>> entries = new ArrayList<>();
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        String[] temp1 = str.split(" ");
	        String action = temp1[0];
	        int value = Integer.parseInt(temp1[1]);
	        
	        entries.add(new AbstractMap.SimpleEntry(action, value));
	    }
	    
	    for (int i = 0; i < entries.size(); i++) {
	        Map.Entry<String, Integer> entry = entries.get(i);
	        String action = entry.getKey();
	        
	        if (action.equals("jmp")) {
	            List<Map.Entry<String, Integer>> copy = new ArrayList<>(entries);
	            copy.set(i, new AbstractMap.SimpleEntry("nop", entry.getValue()));
	            if (!repeatsLn(copy)) {
	                entries = new ArrayList<>(copy);
	                break;
	            }
	        } else if (action.equals("nop")) {
	            List<Map.Entry<String, Integer>> copy = new ArrayList<>(entries);
	            copy.set(i, new AbstractMap.SimpleEntry("jmp", entry.getValue()));
	            if (!repeatsLn(copy)) {
	                entries = new ArrayList<>(copy);
	                break;
	            }
	        }
	    }
	    
	    int accum = 0;
	    int ln = 0;
	    List<Integer> visitedLn = new ArrayList<>();
	    
	    while (true) {
	        if (ln == entries.size()) break;
	        
	        String action = entries.get(ln).getKey();
	        int value = entries.get(ln).getValue();
	        
	        if (visitedLn.contains(Integer.valueOf(ln))) break;
	        visitedLn.add(ln);
	        
	        if (action.equals("acc")) {
	            accum += value;
	            ln++;
	        } else if (action.equals("nop")) {
	            ln++;
	        } else if (action.equals("jmp")) {
	            ln += value;
	        }
	    }
	    
	    return accum;
	}
	
	public static boolean repeatsLn(List<Map.Entry<String, Integer>> entries) {
	    int ln = 0;
	    List<Integer> visitedLn = new ArrayList<>();
	    
	    while (true) {
	        if (ln == entries.size()) return false;
	        if (ln > entries.size()) return true;
	        
	        String action = entries.get(ln).getKey();
	        int value = entries.get(ln).getValue();
	        
	        if (visitedLn.contains(Integer.valueOf(ln))) return true;
	        visitedLn.add(ln);
	        
	        if (action.equals("acc")) {
	            ln++;
	        } else if (action.equals("nop")) {
	            ln++;
	        } else if (action.equals("jmp")) {
	            ln += value;
	        }
	    }
	}
	
	public static int day8p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    List<Map.Entry<String, Integer>> entries = new ArrayList<>();
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        String[] temp1 = str.split(" ");
	        String action = temp1[0];
	        int value = Integer.parseInt(temp1[1]);
	        
	        entries.add(new AbstractMap.SimpleEntry(action, value));
	    }
	    
	    int accum = 0;
	    int ln = 0;
	    List<Integer> visitedLn = new ArrayList<>();
	    
	    while (true) {
	        String action = entries.get(ln).getKey();
	        int value = entries.get(ln).getValue();
	        
	        if (visitedLn.contains(Integer.valueOf(ln))) break;
	        visitedLn.add(ln);
	        
	        if (action.equals("acc")) {
	            accum += value;
	            ln++;
	        } else if (action.equals("nop")) {
	            ln++;
	        } else if (action.equals("jmp")) {
	            ln += value;
	        }
	    }
	    
	    return accum;
	}
	
	public static int day7p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    Map<String, Map<String, Integer>> bags = new HashMap<>();
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        if (str.contains("no other bags")) continue;
	        
	        String[] temp1 = str.split(" bags contain ");
	        String containingBag = temp1[0];
	        String[] temp2 = temp1[1].replace(" bags", "")
	                                 .replace(" bag", "")
	                                 .replace(".", "")
	                                 .split(", ");
	        
	        Map<String, Integer> containedBags = new HashMap<>();
	        
	        for (String s : temp2) {
	            String[] temp3 = s.split(" ");
	            containedBags.put(temp3[1] + " " + temp3[2], Integer.parseInt(temp3[0]));
	        }
	        
	        bags.put(containingBag, containedBags);
	    }
	    sc.close();
	    
	    return countBags(bags, "shiny gold");
	}
	
	public static int countBags(Map<String, Map<String, Integer>> bags, String bag) {
	    if (!bags.containsKey(bag)) return 0;
	    
	    int total = 0;
	    
	    for (Map.Entry<String, Integer> entry : bags.get(bag).entrySet()) {
	        String b = entry.getKey();
	        int amount = entry.getValue().intValue();
	        
	        total += amount * (countBags(bags, b) + 1);
	    }
	    
	    return total;
	}
	
	public static int day7p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    Map<String, String[]> bags = new HashMap<>();
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        if (str.contains("no other bags")) continue;
	        
	        String[] temp1 = str.split(" bags contain ");
	        String containingBag = temp1[0];
	        String[] containedBags = temp1[1].replace(" bags", "")
	                                 .replace(" bag", "")
	                                 .replace(".", "")
	                                 .replaceAll("\\d ", "")
	                                 .split(", ");
	        
	        bags.put(containingBag, containedBags);
	    }
	    sc.close();
	    
	    int total = 0;
	    
	    for (String bag : bags.keySet()) {
	        if (!bag.equals("shiny gold") && containsShinyGoldBag(bags, bag)) total++;
	    }
	    
	    return total;
	}
	
	public static boolean containsShinyGoldBag(Map<String, String[]> bags, String startBag) {
	    if (bags.get(startBag) == null) return false;
	    if (startBag.equals("shiny gold")) return true;
	    for (String s : bags.get(startBag)) {
	        if (containsShinyGoldBag(bags, s)) return true;
	    }
	    return false;
	}
	
	public static int day6p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    int sum = 0;
	    
	    final Set<Character> def = new HashSet<>();
	    def.add('a');
	    def.add('b');
	    def.add('c');
	    def.add('d');
	    def.add('e');
	    def.add('f');
	    def.add('g');
	    def.add('h');
	    def.add('i');
	    def.add('j');
	    def.add('k');
	    def.add('l');
	    def.add('m');
	    def.add('n');
	    def.add('o');
	    def.add('p');
	    def.add('q');
	    def.add('r');
	    def.add('s');
	    def.add('t');
	    def.add('u');
	    def.add('v');
	    def.add('w');
	    def.add('x');
	    def.add('y');
	    def.add('z');
	    
	    Set<Character> s = new HashSet<>(def);
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        if (str.equals("")) {
	            sum += s.size();
	            s = new HashSet<>(def);
	            continue;
	        }
	        
	        Set<Character> toRetain = new HashSet<>();
	        
	        for (char c : str.toCharArray()) {
	            toRetain.add(c);
	        }
	        
	        s.retainAll(toRetain);
	    }
	    
	    return sum;
	}
	
	public static int day6p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    int sum = 0;
	    
	    Set<Character> s = new HashSet<>();
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        if (str.equals("")) {
	            sum += s.size();
	            s.clear();
	            continue;
	        }
	        
	        for (char c : str.toCharArray()) {
	            s.add(c);
	        }
	    }
	    
	    return sum;
	}
	
	public static int day5p2() {
	    // 27-963
	    List<Integer> nums = new ArrayList<>();
	    for (int i = 27; i <= 963; i++) nums.add(i);
	    
	    Scanner sc = new Scanner(System.in);
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        String rows = str.substring(0, 7);
	        String cols = str.substring(7, 10);
	        
	        int row = Integer.parseInt(rows.replace("F", "0").replace("B", "1"), 2);
	        int col = Integer.parseInt(cols.replace("L", "0").replace("R", "1"), 2);
	        
	        int seatID = row * 8 + col;
	        
	        nums.remove(Integer.valueOf(seatID));
	    }
	    
	    return nums.get(0);
	}
	
	public static int day5p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    int max = 0;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        String rows = str.substring(0, 7);
	        String cols = str.substring(7, 10);
	        
	        int row = Integer.parseInt(rows.replace("F", "0").replace("B", "1"), 2);
	        int col = Integer.parseInt(cols.replace("L", "0").replace("R", "1"), 2);
	        
	        int seatID = row * 8 + col;
	        
	        if (seatID > max) max = seatID;
	    }
	    
	    return max;
	}
	
	public static int day4p2() {
	    Scanner sc = new Scanner(System.in);
	    int total = 0;
	    boolean byr = false, iyr = false, eyr = false, hgt = false, hcl = false, ecl = false, pid = false, cid = false;
	    
		while (sc.hasNext()) {
		    String str = sc.nextLine();
		    if (str.equals("stop")) break;
		    
		    if (str.equals("")) {
		        if (byr && iyr && eyr && hgt && hcl && ecl && pid) total++;
		        byr = false;
		        iyr = false;
		        eyr = false;
		        hgt = false;
		        hcl = false;
		        ecl = false;
		        pid = false;
		        cid = false;
		        continue;
		    }
		    
		    String[] pairs = str.split(" ");
		    for (String pair : pairs) {
		        String[] temp = pair.split(":");
		        int yr = 0;
		        switch(temp[0]) {
		            case "byr":
		                yr = Integer.parseInt(temp[1]);
		                if (yr >= 1920 && yr <= 2002)
		                    byr = true;
		                break;
		            case "iyr":
		                yr = Integer.parseInt(temp[1]);
		                if (yr >= 2010 && yr <= 2020)
		                    iyr = true;
		                break;
		            case "eyr":
		                yr = Integer.parseInt(temp[1]);
		                if (yr >= 2020 && yr <= 2030)
		                    eyr = true;
		                break;
		            case "hgt":
		                if (temp[1].endsWith("cm")) {
		                    int height = Integer.parseInt(temp[1].split("cm")[0]);
		                    hgt = height >= 150 && height <= 193;
		                } else {
		                    int height = Integer.parseInt(temp[1].split("in")[0]);
		                    hgt = height >= 59 && height <= 76;
		                }
		                break;
		            case "hcl":
		                hcl = temp[1].matches("^#[a-f0-9]{6}$");
		                break;
		            case "ecl":
		                ecl =   temp[1].equals("amb") ||
		                        temp[1].equals("blu") ||
		                        temp[1].equals("brn") ||
		                        temp[1].equals("gry") ||
		                        temp[1].equals("grn") ||
		                        temp[1].equals("hzl") ||
		                        temp[1].equals("oth");
		                break;
		            case "pid":
		                pid = temp[1].matches("^[0-9]{9}$");
		                break;
		            case "cid":
		                cid = true;
		                break;
		            default:
		                break;
		        }
		    }
		}
		sc.close();
		
		return total;
	}
	
	public static int day4p1() {
	    Scanner sc = new Scanner(System.in);
	    int total = 0;
	    boolean byr = false, iyr = false, eyr = false, hgt = false, hcl = false, ecl = false, pid = false, cid = false;
	    
		while (sc.hasNext()) {
		    String str = sc.nextLine();
		    if (str.equals("stop")) break;
		    
		    if (str.equals("")) {
		        if (byr && iyr && eyr && hgt && hcl && ecl && pid) total++;
		        byr = false;
		        iyr = false;
		        eyr = false;
		        hgt = false;
		        hcl = false;
		        ecl = false;
		        pid = false;
		        cid = false;
		        continue;
		    }
		    
		    String[] pairs = str.split(" ");
		    for (String pair : pairs) {
		        String[] temp = pair.split(":");
		        switch(temp[0]) {
		            case "byr":
		                byr = true;
		                break;
		            case "iyr":
		                iyr = true;
		                break;
		            case "eyr":
		                eyr = true;
		                break;
		            case "hgt":
		                hgt = true;
		                break;
		            case "hcl":
		                hcl = true;
		                break;
		            case "ecl":
		                ecl = true;
		                break;
		            case "pid":
		                pid = true;
		                break;
		            case "cid":
		                cid = true;
		                break;
		            default:
		                break;
		        }
		    }
		}
		sc.close();
		
		return total;
	}
	
	public static int day3p2() {
	    Scanner sc = new Scanner(System.in);
	    int trees = 0;
	    int i = 0;
	    int j = 0;
	    
	    int xshift = 1, yshift = 2;
	    
		while (sc.hasNext()) {
		    String str = sc.nextLine();
		    if (str.equals("stop")) break;
		    
		    if (j % yshift != 0) {j++;continue;}
		    j++;
		    if (str.charAt(i) == '#') trees++;
		    i = (i + xshift) % str.length();
		}
		sc.close();
		
		return trees;
	}
	
	public static int day3p1() {
	    Scanner sc = new Scanner(System.in);
	    int trees = 0;
	    int i = 0;
	    
	    int xshift = 3, yshift = 1;
	    
		while (sc.hasNext()) {
		    String str = sc.nextLine();
		    if (str.equals("stop")) break;
		    
		    if (str.charAt(i) == '#') trees++;
		    i = (i + xshift) % str.length();
		}
		sc.close();
		
		return trees;
	}
	
	public static int day2p2() {
	    Scanner sc = new Scanner(System.in);
	    int total = 0;
	    
		while (sc.hasNext()) {
		    String str = sc.nextLine();
		    if (str.equals("stop")) break;
		    
		    String[] temp = str.split(": ");
		    String pw = temp[1];
		    String[] temp1 = temp[0].split(" ");
		    char ch = temp1[1].charAt(0);
		    String[] rgx = temp1[0].split("-");
		    int a = Integer.parseInt(rgx[0]) - 1;
		    int b = Integer.parseInt(rgx[1]) - 1;
		    
		    if (pw.charAt(a) == ch ^ pw.charAt(b) == ch) total++;
		}
		sc.close();
		
		return total;
	}
	
	public static int day2p1() {
	    Scanner sc = new Scanner(System.in);
	    int total = 0;
	    
		while (sc.hasNext()) {
		    String str = sc.nextLine();
		    if (str.equals("stop")) break;
		    
		    String[] temp = str.split(": ");
		    String pw = temp[1];
		    String[] temp1 = temp[0].split(" ");
		    String ch = temp1[1];
		    String rgx = temp1[0].replace('-', ',');
		    
		    if (pw.matches("^([^"+ch+"\\n\\r]*"+ch+"){"+rgx+"}[^"+ch+"\\n\\r]*$")) total++;
		}
		sc.close();
		
		return total;
	}
	
	public static int day1p2() {
	    Scanner sc = new Scanner(System.in);
		List<Integer> l = new ArrayList<>();
		while (sc.hasNext()) {
		    try {
		        l.add(Integer.parseInt(sc.nextLine()));
		    } catch (Exception e) {
		        break;
		    }
		}
		sc.close();
		
		for (int i : l) {
		    List<Integer> m = new ArrayList<>(l);
		    m.remove(new Integer(i));
		    for (int j : m) {
		        List<Integer> n = new ArrayList<>(m);
		        n.remove(new Integer(j));
		        if (n.contains(2020 - (i + j))) return (2020 - (i + j)) * i * j;
		    }
		}
		return 0;
	}
	
	public static int day1p1() {
	    Scanner sc = new Scanner(System.in);
		List<Integer> l = new ArrayList<>();
		while (sc.hasNext()) {
		    try {
		        l.add(Integer.parseInt(sc.nextLine()));
		    } catch (Exception e) {
		        break;
		    }
		}
		sc.close();
		
		for (int i : l) {
		    if (l.contains(2020 - i)) return (2020-i) * i;
		}
		return 0;
	}
}

// Day 16 Part 2
class Range {
    String field = "";
    
    int lowerBound1 = 0;
    int upperBound1 = 0;
    
    int lowerBound2 = 0;
    int upperBound2 = 0;
    
    Range(String field, int lowerBound1, int upperBound1, int lowerBound2, int upperBound2) {
        this.field = field;
        this.lowerBound1 = lowerBound1;
        this.upperBound1 = upperBound1;
        this.lowerBound2 = lowerBound2;
        this.upperBound2 = upperBound2;
        System.out.println(field + ": " + lowerBound1 + "-" + upperBound1 + " & " + lowerBound2 + "-" + upperBound2);
    }
    
    boolean isTrue(int num) {
        return (lowerBound1 <= num && num <= upperBound1) || (lowerBound2 <= num && num <= upperBound2);
    }
}







