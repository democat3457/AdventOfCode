import java.util.*;
import java.util.stream.*;
import java.math.*;

public class Main
{
	public static void main(String[] args) {
		System.out.println(day6p2().toString());
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
	
	public static int sum(Collection<Integer> c) {
	    return c.stream().mapToInt(Integer::intValue).sum();
	}

	public static BigInteger day6p2() {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		sc.close();

		Map<Integer, BigInteger> fishMap = new HashMap<>();

		for (String str : s.split(",")) {
			int i = Integer.parseInt(str);
			fishMap.put(i, fishMap.getOrDefault(i, BigInteger.ZERO).add(BigInteger.ONE));
		}

		BigInteger sum = BigInteger.valueOf(s.split(",").length);
		int day = 1;

		while (sum.compareTo(new BigInteger("150000000000000000000000000000000000000000000000000000000").divide(new BigInteger("4"))) < 0) {
			Map<Integer, BigInteger> newMap = new HashMap<>();
			for (int i = 1; i <= 8; i++) {
				newMap.put(i-1, fishMap.getOrDefault(i, BigInteger.ZERO));
			}
			BigInteger toAdd = fishMap.getOrDefault(0, BigInteger.ZERO);
			newMap.put(8, newMap.getOrDefault(8, BigInteger.ZERO).add(toAdd));
			newMap.put(6, newMap.getOrDefault(6, BigInteger.ZERO).add(toAdd));

			sum = sum.add(toAdd);

			System.out.println(day + ": " + sum);
			fishMap.clear();
			fishMap.putAll(newMap);
			day++;
		}

		System.out.println(s.split(",").length);
		return sum;
	}

	public static long day6p1() {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		List<String> temp = new ArrayList<>(Arrays.asList(s.split(",")));
		sc.close();

		List<byte[]> fish = temp.stream().map((val) -> new byte[]{Byte.parseByte(val)}).collect(Collectors.toList());

		for (int day = 1; day <= 256; day++) {
			List<byte[]> toAdd = new ArrayList<>();
			for (byte[] daysLeft : fish) {
				if (daysLeft[0] == 0) {
					toAdd.add(new byte[]{8});
					daysLeft[0] = 6;
				} else daysLeft[0]--;
			}
			fish.addAll(toAdd);
			System.out.println(day + ": " + fish.size());
		}

		return fish.size();
	}

	public static long day5p2() {
		Scanner sc = new Scanner(System.in);
		int[][] plot = new int[1000][1000];

		while (sc.hasNext()) {
			try {
				String s = sc.nextLine();
				if (s.equals("quit"))
					break;
				String pt1 = s.split(" -> ")[0];
				String pt2 = s.split(" -> ")[1];

				int pt1x = Integer.parseInt(pt1.split(",")[0]);
				int pt1y = Integer.parseInt(pt1.split(",")[1]);

				int pt2x = Integer.parseInt(pt2.split(",")[0]);
				int pt2y = Integer.parseInt(pt2.split(",")[1]);

				if (pt1x == pt2x || pt1y == pt2y) {
					for (int x = Math.min(pt1x, pt2x); x <= Math.max(pt1x, pt2x); x++) {
						for (int y = Math.min(pt1y, pt2y); y <= Math.max(pt1y, pt2y); y++) {
							plot[x][y]++;
						}
					}
				} else { // Diagonals
					boolean xIncreasing = pt1x < pt2x;
					boolean yIncreasing = pt1y < pt2y;

					for (int i = 0; i <= Math.abs(pt2x - pt1x); i++) {
						plot[pt1x + (i * (xIncreasing ? 1 : -1))][pt1y + (i * (yIncreasing ? 1 : -1))]++;
					}
				}
			} catch (Exception e) {
				break;
			}
		}
		sc.close();

		long total = Arrays.stream(plot).map((arr) -> {
			return Arrays.stream(arr).filter((e) -> e >= 2).count();
		}).mapToLong(Long::longValue).sum();

		return total;
	}

	public static long day5p1() {
		Scanner sc = new Scanner(System.in);
		int[][] plot = new int[1000][1000];

		while (sc.hasNext()) {
			try {
				String s = sc.nextLine();
				if (s.equals("quit")) break;
				String pt1 = s.split(" -> ")[0];
				String pt2 = s.split(" -> ")[1];

				int pt1x = Integer.parseInt(pt1.split(",")[0]);
				int pt1y = Integer.parseInt(pt1.split(",")[1]);

				int pt2x = Integer.parseInt(pt2.split(",")[0]);
				int pt2y = Integer.parseInt(pt2.split(",")[1]);

				if (pt1x == pt2x || pt1y == pt2y) {
					for (int x = Math.min(pt1x, pt2x); x <= Math.max(pt1x, pt2x); x++) {
						for (int y = Math.min(pt1y, pt2y); y <= Math.max(pt1y, pt2y); y++) {
							plot[x][y]++;
						}
					}
				}
			} catch (Exception e) {
				break;
			}
		}
		sc.close();

		long total = Arrays.stream(plot).map((arr) -> {
			return Arrays.stream(arr).filter((e) -> e >= 2).count();
		}).mapToLong(Long::longValue).sum();

		return total;
	}

    public static int day4p2() {
        Scanner sc = new Scanner(System.in);
        List<Integer> nums = new ArrayList<>(Arrays.asList(sc.nextLine().split(",")).stream()
                .map(s -> Integer.parseInt(s)).collect(Collectors.toList()));
        List<Map<Integer, Boolean>> boards = new ArrayList<>();

        while (sc.hasNextInt()) {
            try {
                Map<Integer, Boolean> board = new LinkedHashMap<>();

                for (int i = 0; i < 25; i++) {
                    board.put(sc.nextInt(), false);
                }

                boards.add(board);
            } catch (Exception e) {
                break;
            }
        }
        sc.close();

        System.out.println(boards);

        Map<Integer, Boolean> lastWinning = null;
        String winMethod = "";
        int lastNum = 0;

        out: for (int i = 0; i < nums.size(); i++) {
            int num = nums.get(i);
            lastNum = num;

            List<Map<Integer, Boolean>> boardsToRemove = new ArrayList<>();

            boardsList:
            for (Map<Integer, Boolean> board : boards) {
                board.replaceAll((k, v) -> {
                    if (k == num)
                        return true;
                    else
                        return v;
                });

                List<Map.Entry<Integer, Boolean>> boardNums = new ArrayList<>();
                boardNums.addAll(board.entrySet());

                // rows
                for (int j = 0; j < 5; j++) {
                    if (boardNums.subList(j * 5, j * 5 + 5).stream().allMatch(e -> e.getValue())) {
                        boardsToRemove.add(board);
                        winMethod = "row " + (j + 1);

                        if (boards.size() == 1) {
                            lastWinning = boards.get(0);
                            break out;
                        }

                        continue boardsList;
                    }
                }

                // columns
                for (int j = 0; j < 5; j++) {
                    final int temp = j;
                    if (Arrays.stream(new int[] { 0, 1, 2, 3, 4 }).mapToObj(k -> boardNums.get(k * 5 + temp))
                            .allMatch(e -> e.getValue())) {
                        boardsToRemove.add(board);
                        winMethod = "column " + (j + 1);

                        if (boards.size() == 1) {
                            lastWinning = boards.get(0);
                            break out;
                        }

                        continue boardsList;
                    }
                }
            }

            for (Map<Integer, Boolean> board : boardsToRemove) {
                boards.remove(board);
            }
        }

        List<Map.Entry<Integer, Boolean>> boardNums = new ArrayList<>(lastWinning.entrySet());

        int unmarkedNumbersTotal = sum(
                boardNums.stream().filter(e -> e.getValue() != true).map(e -> e.getKey()).collect(Collectors.toList()));

        System.out.println(boardNums);
        System.out.println(unmarkedNumbersTotal + " " + lastNum);
        System.out.println(winMethod);

        return unmarkedNumbersTotal * lastNum;
    }
	
	public static int day4p1() {
	    Scanner sc = new Scanner(System.in);
		List<Integer> nums = new ArrayList<>(Arrays.asList(sc.nextLine().split(",")).stream().map(s -> Integer.parseInt(s)).collect(Collectors.toList()));
		List<Map<Integer, Boolean>> boards = new ArrayList<>();
		
		while (sc.hasNextInt()) {
		    try {
		        Map<Integer, Boolean> board = new LinkedHashMap<>();
		        
		        for (int i = 0; i < 25; i++) {
		            board.put(sc.nextInt(), false);
		        }
		        
		        boards.add(board);
		    } catch (Exception e) {
		        break;
		    }
		}
		sc.close();
		
		System.out.println(boards);
		
		Map<Integer, Boolean> winningBoard = null;
		String winMethod = "";
		int lastNum = 0;
		
		out:
		for (int i = 0; i < nums.size(); i++) {
		    int num = nums.get(i);
		    lastNum = num;
		    
		    for (Map<Integer, Boolean> board : boards) {
		        board.replaceAll((k, v) -> {
		            if (k == num) return true;
		            else return v;
		        });
		        
		        List<Map.Entry<Integer, Boolean>> boardNums = new ArrayList<>();
		        boardNums.addAll(board.entrySet());
		        
		        // rows
		        for (int j = 0; j < 5; j++) {
		            if (boardNums.subList(j*5, j*5+5).stream().allMatch(e -> e.getValue())) {
		                winningBoard = board;
		                winMethod = "row " + (j + 1);
		                break out;
		            }
		        }
		        
		        // columns
		        for (int j = 0; j < 5; j++) {
		            final int temp = j;
		            if (Arrays.stream(new int[] {0,1,2,3,4}).mapToObj(k -> boardNums.get(k*5 + temp)).allMatch(e -> e.getValue())) {
		                winningBoard = board;
		                winMethod = "column " + (j + 1);
		                break out;
		            }
		        }
		    }
		}
		        
        List<Map.Entry<Integer, Boolean>> boardNums = new ArrayList<>(winningBoard.entrySet());
		
		int unmarkedNumbersTotal = sum(boardNums
		                                .stream()
		                                .filter(e -> e.getValue() != true).map(e -> e.getKey())
		                                .collect(Collectors.toList()));
		
		System.out.println(boardNums);
		System.out.println(unmarkedNumbersTotal + " " + lastNum);
		System.out.println(winMethod);
		
		return unmarkedNumbersTotal * lastNum;
	}
	
	public static int day3p2() {
	    Scanner sc = new Scanner(System.in);
		List<String> l = new ArrayList<>();
		while (sc.hasNext()) {
		    try {
		        String s = sc.nextLine();
		        if (s.equals("quit")) break;
		        l.add(s);
		    } catch (Exception e) {
		        break;
		    }
		}
		sc.close();
		
		int bitLength = l.get(0).length();
		
		List<String> modified = new ArrayList<>(l);
		
		String outputGamma = "";
		
		for (int i = 0; i < bitLength; i++) {
		    if (modified.size() == 1) {
		        outputGamma = modified.get(0);
		        break;
		    }
		    
		    int positiveBits = 0;
    		
    		for (String s : modified) {
    		    if (s.toCharArray()[i] == '1') positiveBits++;
    		}
    		
    		if (positiveBits == modified.size() || positiveBits == 0) continue;
    		System.out.println(positiveBits + " " + modified.size());
    		
    		char checkFor = (positiveBits >= (modified.size() / 2.0)) ? '1' : '0';
    		System.out.println(checkFor);
    		
    		List<String> toRemove = new ArrayList<>();
    		
    		for (String s : modified) {
    		    if (s.toCharArray()[i] != checkFor) toRemove.add(s);
    		}
    		
    		for (String s : toRemove) {
    		    modified.remove(s);
    		}
		}
	    if (modified.size() == 1) {
	        outputGamma = modified.get(0);
	    }
		
		modified = new ArrayList<>(l);
		
		String outputOther = "";
		
		for (int i = 0; i < bitLength; i++) {
		    if (modified.size() == 1) {
		        outputOther = modified.get(0);
		        break;
		    }
		    
		    int positiveBits = 0;
    		
    		for (String s : modified) {
    		    if (s.toCharArray()[i] == '0') positiveBits++;
    		}
    		
    		if (positiveBits == modified.size() || positiveBits == 0) continue;
    		System.out.println(positiveBits + " " + modified.size());
    		
    		char checkFor = (positiveBits <= (modified.size() / 2.0)) ? '0' : '1';
    		System.out.println(checkFor);
    		
    		List<String> toRemove = new ArrayList<>();
    		
    		for (String s : modified) {
    		    if (s.toCharArray()[i] != checkFor) toRemove.add(s);
    		}
    		
    		for (String s : toRemove) {
    		    modified.remove(s);
    		}
		}
	    if (modified.size() == 1) {
	        outputOther = modified.get(0);
	    }
		
		System.out.println(outputGamma + " " + outputOther);
		System.out.println(Integer.parseInt(outputGamma, 2) + "*" + Integer.parseInt(outputOther, 2));
		
		return Integer.parseInt(outputGamma, 2) * Integer.parseInt(outputOther, 2);
	}
	
	public static int day3p1() {
	    Scanner sc = new Scanner(System.in);
		List<String> l = new ArrayList<>();
		while (sc.hasNext()) {
		    try {
		        String s = sc.nextLine();
		        if (s.equals("quit")) break;
		        l.add(s);
		    } catch (Exception e) {
		        break;
		    }
		}
		sc.close();
		
		System.out.println(l.size());
		
		int bitLength = l.get(0).length();
		int[] positiveBits = new int[bitLength];
		
		for (String s : l) {
		    char[] chars = s.toCharArray();
		    for (int i = 0; i < bitLength; i++) {
		        if (chars[i] == '1') positiveBits[i] ++;
		    }
		}
		
		String outputGamma = "";
		String outputOther = "";
		
		for (int i = 0; i < bitLength; i++) {
		    if (positiveBits[i] > (l.size() / 2.0)) {
		        outputGamma += "1";
		        outputOther += "0";
		    }
		    else {
		        outputGamma += "0";
		        outputOther += "1";
		    }
		}
		
		System.out.println(outputGamma + " " + outputOther);
		System.out.println(Arrays.toString(positiveBits));
		System.out.println(Integer.parseInt(outputGamma, 2) + "*" + Integer.parseInt(outputOther, 2));
		
		return Integer.parseInt(outputGamma, 2) * Integer.parseInt(outputOther, 2);
	}
	
	public static int day2p2() {
	    Scanner sc = new Scanner(System.in);
		int pos = 0;
		int depth = 0;
		int aim = 0;
		while (true) {
		        String s = sc.nextLine();
		        if (s.equals("quit")) break;
		        
		        String cmd = s.split(" ")[0];
		        int amount = Integer.parseInt(s.split(" ")[1]);
		        
		        switch (cmd) {
		            case "forward":
		                pos += amount;
		                depth += aim * amount;
		                break;
		            case "down":
		                aim += amount;
		                break;
		            case "up":
		                aim -= amount;
		                break;
		            default:
		        }
		}
		sc.close();
		
		return pos * depth;
	}
	
	public static int day2p1() {
	    Scanner sc = new Scanner(System.in);
		int pos = 0;
		int depth = 0;
		while (true) {
		        String s = sc.nextLine();
		        if (s.equals("quit")) break;
		        
		        String cmd = s.split(" ")[0];
		        int amount = Integer.parseInt(s.split(" ")[1]);
		        
		        switch (cmd) {
		            case "forward":
		                pos += amount;
		                break;
		            case "down":
		                depth += amount;
		                break;
		            case "up":
		                depth -= amount;
		                break;
		            default:
		        }
		}
		sc.close();
		
		return pos * depth;
	}
	
	public static int day1p2() {
	    Scanner sc = new Scanner(System.in);
		LinkedList<Integer> l = new LinkedList<>();
		int lastTotal = 0;
		int count = 0;
		while (sc.hasNext()) {
		    try {
		        l.offer(Integer.parseInt(sc.nextLine()));
		        if (l.size() > 3) l.poll();
		        
		        if (l.size() < 3) continue;
		        int sum = sum(l);
		        if (sum > lastTotal && lastTotal > 0) {
		            count++;
		        }
		        lastTotal = sum;
		    } catch (Exception e) {
		        break;
		    }
		}
		sc.close();
		
		return count;
	}
	
	public static int day1p1() {
	    Scanner sc = new Scanner(System.in);
		int lastInt = 0;
		int count = 0;
		while (sc.hasNext()) {
		    try {
		        int n = Integer.parseInt(sc.nextLine());
		        if (n > lastInt && lastInt > 0) {
		            count++;
		        }
		        lastInt = n;
		    } catch (Exception e) {
		        break;
		    }
		}
		sc.close();
		return count;
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

