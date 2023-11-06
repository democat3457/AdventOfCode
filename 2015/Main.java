import java.util.*;
import java.util.AbstractMap.SimpleEntry;
import java.security.*;
import javax.xml.bind.DatatypeConverter;

public class Main
{
	public static void main(String[] args) {
		System.out.println(day8p2());
	}
	
	public static int day8p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    int totalChars = 0;
	    int encodedChars = 0;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        totalChars += str.length();
	        
	        str = str.replaceAll("\\\\", "\\\\\\\\");
	        str = str.replaceAll("\"", "\\\\\"");
	        str = "\"" + str + "\"";
	        System.out.println(str);
	        encodedChars += str.length();
	    }
	    
	    return encodedChars - totalChars;
	}
	
	public static int day8p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    int totalChars = 0;
	    int reducedChars = 0;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        totalChars += str.length();
	        
	        str = str.substring(1, str.length()-1);
	        str = str.replaceAll("\\\\\\\\", "\\\\");
	        str = str.replaceAll("\\\\\"", "\\\"");
	        str = str.replaceAll("\\\\x[0-9a-f]{2}", "'");
	       // System.out.println(str);
	        reducedChars += str.length();
	    }
	    
	    return totalChars - reducedChars;
	}
	
	public static int day7p2() {
	    /* OpCodes
	     * 0 = as-is
	     * 1 = AND
	     * 2 = OR
	     * 3 = LSHIFT
	     * 4 = RSHIFT
	     * 5 = NOT
	     */
	    
	    Scanner sc = new Scanner(System.in);
	    
	    Map<String, Map.Entry<Integer, String[]>> wires = new HashMap<>();
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        String[] temp1 = str.split(" -> ");
	        
	        if (str.contains("AND")) {
	            String[] temp2 = temp1[0].split(" AND ");
	            wires.put(temp1[1], new SimpleEntry(1, temp2));
	        } else if (str.contains("OR")) {
	            String[] temp2 = temp1[0].split(" OR ");
	            wires.put(temp1[1], new SimpleEntry(2, temp2));
	        } else if (str.contains("LSHIFT")) {
	            String[] temp2 = temp1[0].split(" LSHIFT ");
	            wires.put(temp1[1], new SimpleEntry(3, temp2));
	        } else if (str.contains("RSHIFT")) {
	            String[] temp2 = temp1[0].split(" RSHIFT ");
	            wires.put(temp1[1], new SimpleEntry(4, temp2));
	        } else if (str.contains("NOT")) {
	            String temp2 = temp1[0].replace("NOT ", "");
	            wires.put(temp1[1], new SimpleEntry(5, new String[]{temp2}));
	        } else {
	            wires.put(temp1[1], new SimpleEntry(0, new String[]{temp1[0]}));
	        }
	    }
	    
	    sc.close();
	    
	    int a = parseWireCount(wires, "a");
	    wireCache.clear();
	    wireCache.put("b", a);
	    return parseWireCount(wires, "a");
	}
	
	public static int day7p1() {
	    /* OpCodes
	     * 0 = as-is
	     * 1 = AND
	     * 2 = OR
	     * 3 = LSHIFT
	     * 4 = RSHIFT
	     * 5 = NOT
	     */
	    
	    Scanner sc = new Scanner(System.in);
	    
	    Map<String, Map.Entry<Integer, String[]>> wires = new HashMap<>();
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        String[] temp1 = str.split(" -> ");
	        
	        if (str.contains("AND")) {
	            String[] temp2 = temp1[0].split(" AND ");
	            wires.put(temp1[1], new SimpleEntry(1, temp2));
	        } else if (str.contains("OR")) {
	            String[] temp2 = temp1[0].split(" OR ");
	            wires.put(temp1[1], new SimpleEntry(2, temp2));
	        } else if (str.contains("LSHIFT")) {
	            String[] temp2 = temp1[0].split(" LSHIFT ");
	            wires.put(temp1[1], new SimpleEntry(3, temp2));
	        } else if (str.contains("RSHIFT")) {
	            String[] temp2 = temp1[0].split(" RSHIFT ");
	            wires.put(temp1[1], new SimpleEntry(4, temp2));
	        } else if (str.contains("NOT")) {
	            String temp2 = temp1[0].replace("NOT ", "");
	            wires.put(temp1[1], new SimpleEntry(5, new String[]{temp2}));
	        } else {
	            wires.put(temp1[1], new SimpleEntry(0, new String[]{temp1[0]}));
	        }
	    }
	    
	    sc.close();
	    
	    return parseWireCount(wires, "a");
	}
	
	public static Map<String, Integer> wireCache = new HashMap<>();
	
	public static int parseWireCount(Map<String, Map.Entry<Integer, String[]>> wires, String wire) {
	    if (!wireCache.containsKey(wire)) {
    	    try {
    	        wireCache.put(wire, Integer.parseInt(wire));
    	        return Integer.parseInt(wire);
    	    } catch (NumberFormatException e) {
    	        int temp = getWireCount(wires, wire);
    	        wireCache.put(wire, temp);
    	        return temp;
    	    }
	    } else {
	        return wireCache.get(wire).intValue();
	    }
	}
	
	public static int getWireCount(Map<String, Map.Entry<Integer, String[]>> wires, String wire) {
	    if (!wires.containsKey(wire)) return -1;
	    
	    int opCode = wires.get(wire).getKey();
	    String[] values = wires.get(wire).getValue();
	    
	    System.out.print(wire + " ");
	    
	    switch (opCode) {
	        case 0:
	            return parseWireCount(wires, values[0]);
	        case 1:
	            return parseWireCount(wires, values[0]) & parseWireCount(wires, values[1]);
	        case 2:
	            return parseWireCount(wires, values[0]) | parseWireCount(wires, values[1]);
	        case 3:
	            return parseWireCount(wires, values[0]) << parseWireCount(wires, values[1]);
	        case 4:
	            return parseWireCount(wires, values[0]) >> parseWireCount(wires, values[1]);
	        case 5:
	            return 65535 - parseWireCount(wires, values[0]);
	        default:
	            return -1;
	    }
	}
	
	public static int day6p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    List<List<Integer>> lights = new ArrayList<>(1000);
	    for (int i = 0; i < 1000; i++) {
	        List<Integer> l = new ArrayList<>(1000);
	        for (int j = 0; j < 1000; j++)
	            l.add(0);
	        lights.add(l);
	    }
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        if (str.startsWith("turn on")) {
	            String[] temp1 = str.replace("turn on ", "").split(" through ");
	            String[] temp2 = temp1[0].split(",");
	            String[] temp3 = temp1[1].split(",");
	            int startingX = Integer.parseInt(temp2[0]);
	            int startingY = Integer.parseInt(temp2[1]);
	            int endingX = Integer.parseInt(temp3[0]);
	            int endingY = Integer.parseInt(temp3[1]);
	            
	            for (int i = startingX; i <= endingX; i++)
	                for (int j = startingY; j <= endingY; j++)
	                    lights.get(i).set(j, lights.get(i).get(j)+1);
	           
	        } else if (str.startsWith("turn off")) {
	            String[] temp1 = str.replace("turn off ", "").split(" through ");
	            String[] temp2 = temp1[0].split(",");
	            String[] temp3 = temp1[1].split(",");
	            int startingX = Integer.parseInt(temp2[0]);
	            int startingY = Integer.parseInt(temp2[1]);
	            int endingX = Integer.parseInt(temp3[0]);
	            int endingY = Integer.parseInt(temp3[1]);
	            
	            for (int i = startingX; i <= endingX; i++)
	                for (int j = startingY; j <= endingY; j++)
	                    lights.get(i).set(j, Math.max(lights.get(i).get(j)-1, 0));
	        } else {
	            String[] temp1 = str.replace("toggle ", "").split(" through ");
	            String[] temp2 = temp1[0].split(",");
	            String[] temp3 = temp1[1].split(",");
	            int startingX = Integer.parseInt(temp2[0]);
	            int startingY = Integer.parseInt(temp2[1]);
	            int endingX = Integer.parseInt(temp3[0]);
	            int endingY = Integer.parseInt(temp3[1]);
	            
	            for (int i = startingX; i <= endingX; i++)
	                for (int j = startingY; j <= endingY; j++)
	                    lights.get(i).set(j, lights.get(i).get(j)+2);
	        }
	    }
	    
	    int sum = 0;
	    for (List<Integer> l : lights)
	        for (Integer i : l)
	            sum += i.intValue();
	    return sum;
	}
	
	public static int day6p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    List<BitSet> lights = new ArrayList<>(1000);
	    for (int i = 0; i < 1000; i++)
	        lights.add(new BitSet(1000));
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        if (str.startsWith("turn on")) {
	            String[] temp1 = str.replace("turn on ", "").split(" through ");
	            String[] temp2 = temp1[0].split(",");
	            String[] temp3 = temp1[1].split(",");
	            int startingX = Integer.parseInt(temp2[0]);
	            int startingY = Integer.parseInt(temp2[1]);
	            int endingX = Integer.parseInt(temp3[0]);
	            int endingY = Integer.parseInt(temp3[1]);
	            
	            for (int i = startingX; i <= endingX; i++)
	                lights.get(i).set(startingY, endingY+1, true);
	           
	        } else if (str.startsWith("turn off")) {
	            String[] temp1 = str.replace("turn off ", "").split(" through ");
	            String[] temp2 = temp1[0].split(",");
	            String[] temp3 = temp1[1].split(",");
	            int startingX = Integer.parseInt(temp2[0]);
	            int startingY = Integer.parseInt(temp2[1]);
	            int endingX = Integer.parseInt(temp3[0]);
	            int endingY = Integer.parseInt(temp3[1]);
	            
	            for (int i = startingX; i <= endingX; i++)
	                lights.get(i).set(startingY, endingY+1, false);
	        } else {
	            String[] temp1 = str.replace("toggle ", "").split(" through ");
	            String[] temp2 = temp1[0].split(",");
	            String[] temp3 = temp1[1].split(",");
	            int startingX = Integer.parseInt(temp2[0]);
	            int startingY = Integer.parseInt(temp2[1]);
	            int endingX = Integer.parseInt(temp3[0]);
	            int endingY = Integer.parseInt(temp3[1]);
	            
	            for (int i = startingX; i <= endingX; i++)
	                lights.get(i).flip(startingY, endingY+1);
	        }
	    }
	    
	    int sum = 0;
	    for (BitSet bs : lights)
	        sum += bs.cardinality();
	    return sum;
	}
	
	public static int day5p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    int total = 0;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        if (!str.matches(".*(\\w\\w).*\\1.*")) continue;
	        
	        if (!str.matches(".*(\\w)\\w\\1.*")) continue;
	        
	        total++;
	    }
	    
	    return total;
	}
	
	public static int day5p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    int total = 0;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        if (str.contains("ab") ||
	            str.contains("cd") ||
	            str.contains("pq") ||
	            str.contains("xy")) continue;
	        
	        if (!str.matches(".*(\\w)\\1.*")) continue;
	        
	        if (!str.matches("^([^aeiou\\n\\r]*[aeiou]){3,}[^aeiou\\n\\r]*$")) continue;
	        
	        total++;
	    }
	    
	    return total;
	}
	
	public static int day4p2() {
	    String key = "yzbqklnj";
	    String hash = "";
	    int num = -1;
	    
	    do {
	        num++;
	        try {
	            MessageDigest md = MessageDigest.getInstance("MD5");
                md.update((key + num).getBytes());
                byte[] digest = md.digest();
	            hash = DatatypeConverter
                  .printHexBinary(digest).toLowerCase();
	        } catch (NoSuchAlgorithmException e) {
	            // do nothing
	        }
	    } while (!hash.startsWith("000000"));
	    
	    return num;
	}
	
	public static int day4p1() {
	    String key = "yzbqklnj";
	    String hash = "";
	    int num = -1;
	    
	    do {
	        num++;
	        try {
	            MessageDigest md = MessageDigest.getInstance("MD5");
                md.update((key + num).getBytes());
                byte[] digest = md.digest();
	            hash = DatatypeConverter
                  .printHexBinary(digest).toLowerCase();
	        } catch (NoSuchAlgorithmException e) {
	            // do nothing
	        }
	    } while (!hash.startsWith("00000"));
	    
	    return num;
	}
	
	public static int day3p2() {
	    Scanner sc = new Scanner(System.in);
	    Set<SimpleEntry<Integer, Integer>> s = new HashSet<>();
	    int[] x = new int[]{0, 0};
	    int[] y = new int[]{0, 0};
	    
	    int turn = 0;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        for (char c : str.toCharArray()) {
	            int i = turn % 2;
	            
    	        s.add(new SimpleEntry<>(x[i], y[i]));
    	        
    	        if (c == '>') x[i]++;
    	        if (c == '<') x[i]--;
    	        if (c == '^') y[i]++;
    	        if (c == 'v') y[i]--;
    	        
    	        s.add(new SimpleEntry<>(x[i], y[i]));
    	        
    	        turn++;
	        }
	    }
	    sc.close();
	    
	    return s.size();
	}
	
	public static int day3p1() {
	    Scanner sc = new Scanner(System.in);
	    Set<SimpleEntry<Integer, Integer>> s = new HashSet<>();
	    int x = 0;
	    int y = 0;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        for (char c : str.toCharArray()) {
    	        s.add(new SimpleEntry<>(x, y));
    	        
    	        if (c == '>') x++;
    	        if (c == '<') x--;
    	        if (c == '^') y++;
    	        if (c == 'v') y--;
	        }
	    }
	    sc.close();
	    
	    return s.size();
	}
	
	public static int day2p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    int total = 0;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        String[] temp = str.split("x");
	        int l = Integer.parseInt(temp[0]);
	        int w = Integer.parseInt(temp[1]);
	        int h = Integer.parseInt(temp[2]);
	        
	        int a = l + w;
	        int b = w + h;
	        int c = l + h;
	        
	        int lowest = Math.min(Math.min(a, b), c);
	        
	        total += 2 * lowest + l * w * h;
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
	        
	        String[] temp = str.split("x");
	        int l = Integer.parseInt(temp[0]);
	        int w = Integer.parseInt(temp[1]);
	        int h = Integer.parseInt(temp[2]);
	        
	        int a = l * w;
	        int b = w * h;
	        int c = l * h;
	        
	        int lowest = Math.min(Math.min(a, b), c);
	        
	        total += 2 * a + 2 * b + 2 * c + lowest;
	    }
	    sc.close();
	    
	    return total;
	}
	
	public static int day1p2() {
	    Scanner sc = new Scanner(System.in);
	    
	    int total = 0;
	    int index = 0;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        char[] chars = str.toCharArray();
	        for (char c : chars) {
	            index++;
	            
	            if (c == '(') total++;
	            else if (c == ')') total--;
	            
	            if (total < 0) return index;
	        }
	    }
	    sc.close();
	    
	    return 0;
	}
	
	public static int day1p1() {
	    Scanner sc = new Scanner(System.in);
	    
	    int total = 0;
	    
	    while (sc.hasNext()) {
	        String str = sc.nextLine();
	        if (str.equals("stop")) break;
	        
	        char[] chars = str.toCharArray();
	        for (char c : chars) {
	            if (c == '(') total++;
	            else if (c == ')') total--;
	        }
	    }
	    sc.close();
	    
	    return total;
	}
}

