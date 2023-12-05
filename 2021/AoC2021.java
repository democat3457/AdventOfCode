import java.io.*;
import java.util.*;
import java.util.stream.*;
import java.math.*;

public class AoC2021
{
	public static void main(String[] args) {
		long startTime = System.currentTimeMillis();
		System.out.println(day18p2());
		long endTime = System.currentTimeMillis();

		System.out.println("Elapsed: " + (endTime - startTime) + "ms.");
	}

	public static long day18p2() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			try (Scanner sc = new Scanner(f)) {
				List<OptionalPair> list = new ArrayList<>();

				while (sc.hasNextLine()) {
					OptionalPair root = new OptionalPair(null);
					OptionalPair current = root;

					String s = sc.nextLine();

					String number = "";
					for (char c : s.toCharArray()) {
						int x = Character.getNumericValue(c);

						if (x < 0) {
							if (!number.isEmpty()) {
								if (current.readIndex == 0) {
									current.a = Integer.parseInt(number);
									number = "";
								} else if (current.readIndex == 1) {
									current.b = Integer.parseInt(number);
									number = "";
								} else {
									throw new IllegalStateException("tried to read value from closed pair");
								}
							}

							if (c == '[') {
								OptionalPair temp = new OptionalPair(current);
								if (current.readIndex == 0) {
									temp.indexFromParent = 0;
									current.a = temp;
									current = temp;
								} else if (current.readIndex == 1) {
									temp.indexFromParent = 1;
									current.b = temp;
									current = temp;
								} else {
									throw new IllegalStateException("tried to read value from closed pair");
								}
							} else if (c == ']') {
								current.close();
								current = current.parent;
							} else if (c == ',') {
								current.readIndex++;
							} else {
								throw new IllegalStateException("unknown char: (" + c + ")");
							}
						} else {
							number += c;
						}
					}

					root = (OptionalPair) root.a; // normalizing extra null
					root.parent = null;
					root.indexFromParent = -1;

					list.add(root);

					// System.out.println(root);
				}

				long maxMagnitude = 0L;
				for (int i = 0; i < list.size(); i++) {
					for (int j = 0; j < list.size(); j++) {
						if (i == j) continue;
						OptionalPair running = new OptionalPair(null, list.get(i).copy(), list.get(j).copy());
						((OptionalPair) running.a).parent = running;
						((OptionalPair) running.b).parent = running;
						((OptionalPair) running.a).indexFromParent = 0;
						((OptionalPair) running.b).indexFromParent = 1;

						running.reduce();
						long mag = running.getMagnitude();
						if (mag > maxMagnitude) maxMagnitude = mag;
						// System.out.println(running);
					}
				}

				return maxMagnitude;
			}
		} catch (FileNotFoundException e) {
			return -1L;
		}
	}

	public static long day18p1() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			try (Scanner sc = new Scanner(f)) {
				List<OptionalPair> list = new ArrayList<>();

				while (sc.hasNextLine()) {
					OptionalPair root = new OptionalPair(null);
					OptionalPair current = root;

					String s = sc.nextLine();

					String number = "";
					for (char c : s.toCharArray()) {
						int x = Character.getNumericValue(c);

						if (x < 0) {
							if (!number.isEmpty()) {
								if (current.readIndex == 0) {
									current.a = Integer.parseInt(number);
									number = "";
								} else if (current.readIndex == 1) {
									current.b = Integer.parseInt(number);
									number = "";
								} else {
									throw new IllegalStateException("tried to read value from closed pair");
								}
							}

							if (c == '[') {
								OptionalPair temp = new OptionalPair(current);
								if (current.readIndex == 0) {
									temp.indexFromParent = 0;
									current.a = temp;
									current = temp;
								} else if (current.readIndex == 1) {
									temp.indexFromParent = 1;
									current.b = temp;
									current = temp;
								} else {
									throw new IllegalStateException("tried to read value from closed pair");
								}
							} else if (c == ']') {
								current.close();
								current = current.parent;
							} else if (c == ',') {
								current.readIndex++;
							} else {
								throw new IllegalStateException("unknown char: (" + c + ")");
							}
						} else {
							number += c;
						}
					}

					root = (OptionalPair) root.a; // normalizing extra null
					root.parent = null;
					root.indexFromParent = -1;

					list.add(root);

					// System.out.println(root);
				}

				OptionalPair running = list.get(0);
				for (int i = 1; i < list.size(); i++) {
					running = new OptionalPair(null, running, list.get(i));
					((OptionalPair) running.a).parent = running;
					((OptionalPair) running.b).parent = running;
					((OptionalPair) running.a).indexFromParent = 0;
					((OptionalPair) running.b).indexFromParent = 1;

					running.reduce();
					System.out.println(running);
				}


				return running.getMagnitude();
			}
		} catch (FileNotFoundException e) {
			return -1L;
		}
	}

	public static int day17p2() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);
			String str = sc.nextLine();
			sc.close();

			String rng = str.split("y=")[1];
			// System.out.println(rng);
			int minY = Integer.parseInt(rng.split("\\.\\.")[0]);
			int maxY = Integer.parseInt(rng.split("\\.\\.")[1]);
			rng = str.split(", ")[0].split("x=")[1];
			int minX = Integer.parseInt(rng.split("\\.\\.")[0]);
			int maxX = Integer.parseInt(rng.split("\\.\\.")[1]);

			int count = 0;

			for (int j = 22; j <= 350; j++) {
				for (int i = -100; i <= 100; i++) {
					int xPos = 0;
					int xVel = j;
					int yPos = 0;
					int yVel = i;
					while (yPos >= minY && xPos <= maxX) {
						yPos += yVel;
						xPos += xVel;
						yVel--;
						xVel = Integer.signum(xVel) * (Math.abs(xVel) - 1);
						if (minY <= yPos && yPos <= maxY && minX <= xPos && xPos <= maxX) {
							count++;
							break;
						}
					}
				}
			}

			return count;
		} catch (FileNotFoundException e) {
			return -1;
		}
	}

	public static int day17p1() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);
			String str = sc.nextLine();
			sc.close();

			String rng = str.split("y=")[1];
			System.out.println(rng);
			int minY = Integer.parseInt(rng.split("\\.\\.")[0]);
			int maxY = Integer.parseInt(rng.split("\\.\\.")[1]);

			int maxYVel = 0;

			for (int i = 0; i < 100; i++) {
				int yPos = 0;
				int yVel = i;
				while (yPos >= minY) {
					yPos += yVel;
					yVel--;
					if (minY <= yPos && yPos <= maxY) {
						if (i > maxYVel) {
							maxYVel = i;
						}
					}
				}
			}

			int maxYPos = 0;
			int yPos = 0;
			int yVel = maxYVel;

			while (yPos >= minY) {
				yPos += yVel;
				yVel--;
				if (yPos > maxYPos) {
					maxYPos = yPos;
				}
			}

			return maxYPos;
		} catch (FileNotFoundException e) {
			return -1;
		}
	}

	public static String day16() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);
			String str = sc.nextLine();
			sc.close();

			str = str.replaceAll("0", "0000");
			str = str.replaceAll("1", "0001");
			str = str.replaceAll("2", "0010");
			str = str.replaceAll("3", "0011");
			str = str.replaceAll("4", "0100");
			str = str.replaceAll("5", "0101");
			str = str.replaceAll("6", "0110");
			str = str.replaceAll("7", "0111");
			str = str.replaceAll("8", "1000");
			str = str.replaceAll("9", "1001");
			str = str.replaceAll("A", "1010");
			str = str.replaceAll("B", "1011");
			str = str.replaceAll("C", "1100");
			str = str.replaceAll("D", "1101");
			str = str.replaceAll("E", "1110");
			str = str.replaceAll("F", "1111");

			Packet p = Packet.parse(str).getKey();

			return Packet.parse(str).getKey().toString() + "\n"
						 + (p.getValue());
		} catch (FileNotFoundException e) {
			return "-1";
		}
	}

	public static String[] splice(String str, int numOfChars) {
		return new String[]{ 
			str.substring(0, numOfChars), 
			str.substring(numOfChars) 
		};
	}

	public static long day15p2() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);

			int[][] risks = new int[500][500];
			int[][] minDists = new int[500][500];
			Coords[][] prev = new Coords[500][500];

			boolean[][] checked = new boolean[500][500];

			for (int i = 0; i < 100; i++) {
				String s = sc.nextLine();
				for (int j = 0; j < 100; j++) {
					for (int iMult = 0; iMult < 5; iMult++) {
						for (int jMult = 0; jMult < 5; jMult++) {
							int iRes = i + (iMult * 100);
							int jRes = j + (jMult * 100);
							// System.out.println("Setting (" + iRes + ", " + jRes + ") to "+(((Character.getNumericValue(s.charAt(j))-1+iMult+jMult) % 9) + 1));
							risks[iRes][jRes] = ((Character.getNumericValue(s.charAt(j))-1+iMult+jMult) % 9) + 1;
							minDists[iRes][jRes] = Integer.MAX_VALUE;
						}
					}
				}
			}
			sc.close();

			minDists[0][0] = 0;

			int checkedCount = 0;

			while (!checked[499][499]) {
				// q.sort((c1, c2) -> Integer.compare(minDists[c1.x][c1.y], minDists[c2.x][c2.y]));
				int x = 0, y = 0;
				int min = Integer.MAX_VALUE;
				for (int i = 0;  i < 500; i++) {
					for (int j = 0; j < 500; j++) {
						if (!checked[i][j] && minDists[i][j] < min) {
							x = i;
							y = j;
							min = minDists[i][j];
						}
					}
				}

				checked[x][y] = true;
				checkedCount++;

				if (checkedCount % 100 == 0) System.out.println(checkedCount);

				if (x == 499 && y == 499) {
					System.out.println(minDists[499][499]);
					break;
				}

				Coords nextCoords = Coords.of(x, y);

				for (Coords neighbor : new Coords[] { nextCoords.left(), nextCoords.up(), nextCoords.right(),
						nextCoords.down() }) {
					// System.out.println("c " + neighbor);
					try {
						if (!checked[neighbor.x][neighbor.y]) {
							int newDist = minDists[x][y]
									+ risks[neighbor.x][neighbor.y];
							if (newDist < minDists[neighbor.x][neighbor.y]) {
								minDists[neighbor.x][neighbor.y] = newDist;
								prev[neighbor.x][neighbor.y] = nextCoords;
								// if (q.size() < 125500) System.out.println("yes " + neighbor);
							}
						}
					} catch (IndexOutOfBoundsException e) {
					}
				}
			}

			// Deque<Coords> dq = new LinkedList<>();
			long totalDist = 0L;
			Coords currentCoords = Coords.of(499, 499);
			if (prev[currentCoords.x][currentCoords.y] != null ||
				currentCoords.equals(Coords.of(0,0))) {
				while (currentCoords != null) {
					// dq.addFirst(currentCoords);
					totalDist += risks[currentCoords.x][currentCoords.y];
					currentCoords = prev[currentCoords.x][currentCoords.y];
				}
			}

			return totalDist-1;

			// for (Coords c : dq) {

			// }

			// return Arrays.deepToString(risks).replace("], [", "\n").replace(", ",
			// "").replace("[[", "").replace("]]", "");
		} catch (FileNotFoundException e) {
			return -1;
		}
	}

	public static int day15p1() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);

			int[][] risks = new int[100][100];
			int[][] minDists = new int[100][100];
			Coords[][] prev = new Coords[100][100];

			PriorityQueue<Coords> q = new PriorityQueue<>((c1, c2) -> Integer.compare(minDists[c1.x][c1.y], minDists[c2.x][c2.y]));

			for (int i = 0; i < risks.length; i++) {
				String s = sc.nextLine();
				for (int j = 0; j < risks[i].length; j++) {
					risks[i][j] = Character.getNumericValue(s.charAt(j));
					minDists[i][j] = Integer.MAX_VALUE;
					q.add(Coords.of(i,j));
				}
			}
			sc.close();

			minDists[0][0] = 0;
			System.out.println(q.size());

			while (!q.isEmpty()) {
				Coords nextCoords = q.poll();
				// System.out.println("no " + nextCoords + " " + q.size());

				if (nextCoords.x == 99 && nextCoords.y == 99) {
					break;
				}

				
				for (Coords neighbor : new Coords[]{ 
					nextCoords.left(),
					nextCoords.up(),
					nextCoords.right(),
					nextCoords.down()
				}) {
					// System.out.println("c " + neighbor);
					try {
						if (q.contains(neighbor)) {
							int newDist = minDists[nextCoords.x][nextCoords.y] + risks[neighbor.x][neighbor.y];
							if (newDist < minDists[neighbor.x][neighbor.y]) {
								minDists[neighbor.x][neighbor.y] = newDist;
								prev[neighbor.x][neighbor.y] = nextCoords;
								// System.out.println("yes " + neighbor);

								q.remove(neighbor);
								q.add(neighbor);
							}
						}
					} catch (IndexOutOfBoundsException e) { }
				}
			}

			// Deque<Coords> dq = new LinkedList<>();
			int totalDist = 0;
			Coords currentCoords = Coords.of(99, 99);
			if (prev[currentCoords.x][currentCoords.y] != null || currentCoords.equals(Coords.of(0,0))) {
				while (currentCoords != null) {
					// dq.addFirst(currentCoords);
					totalDist += risks[currentCoords.x][currentCoords.y];
					currentCoords = prev[currentCoords.x][currentCoords.y];
				}
			}

			return totalDist;

			// for (Coords c : dq) {
				
			// }

			// return Arrays.deepToString(risks).replace("], [", "\n").replace(", ", "").replace("[[", "").replace("]]", "");
		} catch (FileNotFoundException e) {
			return -1;
		}
	}

	public static String day14p2() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);

			StringBuilder template = new StringBuilder(sc.nextLine());
			sc.nextLine();

			Pair<Character> endChars = Pair.of(template.charAt(0), template.charAt(template.length()-1));

			Map<Pair<Character>, Character> rules = new HashMap<>();
			while (sc.hasNextLine()) {
				String s = sc.nextLine();
				if (s.equals("quit"))
					break;

				if (s.isBlank())
					continue;

				String[] si = s.split(" -> ");
				rules.put(Pair.of(si[0].charAt(0), si[0].charAt(1)), si[1].charAt(0));
			}
			sc.close();

			System.out.println(template.toString());

			Map<Pair<Character>, Map<Pair<Character>, Long>> rulePairCounts = new HashMap<>();

			List<Pair<Character>> templatePairs = getPairs(template);

			for (Pair<Character> rulePair : rules.keySet()) {
				template.setLength(0);
				template.append(rulePair.obj1);
				template.append(rulePair.obj2);
				for (int step = 1; step <= 10; step++) {
					System.out.println(step);
					for (int i = template.length() - 1; i > 0; i--) {
						Pair<Character> temp = Pair.of(template.charAt(i - 1), template.charAt(i));
						if (rules.containsKey(temp)) {
							template.insert(i, rules.get(temp).charValue());
							// if (step <= 2)
							// System.out.println("inserting " + rules.get(temp).charValue() + " at index "
							// + i
							// + " for pair " + temp);
						}
					}
					if (step <= 3)
						System.out.println(template.toString());
				}
				System.out.println(template.length());

				List<Pair<Character>> rulePairResults = getPairs(template);
				Map<Pair<Character>, Long> counts = new HashMap<>();

				for (Pair<Character> p : rulePairResults)
					counts.put(p, counts.getOrDefault(p, 0L) + 1);

				rulePairCounts.put(rulePair, counts);

				System.out.println("layer 1");
			}

			Map<Pair<Character>, Long> finalPairCounts = new HashMap<>();

			for (Pair<Character> templatePair : templatePairs) {
				finalPairCounts.put(templatePair, finalPairCounts.getOrDefault(templatePair, 0L) + 1);
			}

			for (int i = 0; i < 4; i++) {
				Map<Pair<Character>, Long> tempCounts = new HashMap<>();
				for (Map.Entry<Pair<Character>, Long> entry : finalPairCounts.entrySet()) {
					Map<Pair<Character>, Long> countMult = rulePairCounts.get(entry.getKey());
					for (Map.Entry<Pair<Character>, Long> entry2 : countMult.entrySet()) {
						tempCounts.put(entry2.getKey(), tempCounts.getOrDefault(entry2.getKey(), 0L) + 
								(entry.getValue() * entry2.getValue()));
					}
				}
				finalPairCounts = tempCounts;
			}

			Map<Character, Long> freqs = new HashMap<>();

			for (Map.Entry<Pair<Character>, Long> e : finalPairCounts.entrySet()) {
				freqs.put(e.getKey().obj1, freqs.getOrDefault(e.getKey().obj1, 0L) + e.getValue());
				freqs.put(e.getKey().obj2, freqs.getOrDefault(e.getKey().obj2, 0L) + e.getValue());
			}

			for (Map.Entry<Character, Long> e : freqs.entrySet()) {
				freqs.replace(e.getKey(), e.getValue()/2);
			}

			if (endChars.obj1 == endChars.obj2) {
				freqs.replace(endChars.obj1, freqs.get(endChars.obj1) + 1);
			} else {
				freqs.replace(endChars.obj1, freqs.get(endChars.obj1) + 1);
				freqs.replace(endChars.obj2, freqs.get(endChars.obj2) + 1);
			}

			List<Map.Entry<Character, Long>> entries = new ArrayList<>(freqs.entrySet());
			entries.sort((e1, e2) -> e2.getValue().compareTo(e1.getValue()));

			// return entries.toString();
			return entries.get(0) + " " + entries.get(entries.size() - 1) + 
					" == " + (entries.get(0).getValue() - entries.get(entries.size() - 1).getValue());
		} catch (FileNotFoundException e) {
			return "-1";
		}
	}

	public static List<Pair<Character>> getPairs(StringBuilder sb) {
		return getPairs(sb.toString());
	}

	public static List<Pair<Character>> getPairs(String s) {
		List<Pair<Character>> pairs = new ArrayList<>();
		for (int i = s.length() - 1; i > 0; i--) {
			pairs.add(Pair.of(s.charAt(i - 1), s.charAt(i)));
		}
		return pairs;
	}

	public static String day14p2old() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);

			StringBuilder template = new StringBuilder(sc.nextLine());
			sc.nextLine();

			Map<Pair<Character>, Character> rules = new HashMap<>();
			while (sc.hasNextLine()) {
				String s = sc.nextLine();
				if (s.equals("quit"))
					break;

				if (s.isBlank())
					continue;

				String[] si = s.split(" -> ");
				rules.put(Pair.of(si[0].charAt(0), si[0].charAt(1)), si[1].charAt(0));
			}
			sc.close();

			System.out.println(template.toString());

			List<Pair<Character>> pairs = new ArrayList<>();
			for (int i = template.length()-1; i > 0; i--) {
				pairs.add(Pair.of(template.charAt(i - 1), template.charAt(i)));
			}

			long totalCount = 0;

			List<Pair<Character>> pairs2 = new ArrayList<>();

			Map<Character, Long> freqs = new HashMap<>();

			for (Pair<Character> pair : pairs) {
				template.setLength(0);
				template.append(pair.obj1);
				template.append(pair.obj2);
				for (int step = 1; step <= 10; step++) {
					System.out.println(step);
					for (int i = template.length() - 1; i > 0; i--) {
						Pair<Character> temp = Pair.of(template.charAt(i - 1), template.charAt(i));
						if (rules.containsKey(temp)) {
							template.insert(i, rules.get(temp).charValue());
							// if (step <= 2)
							// 	System.out.println("inserting " + rules.get(temp).charValue() + " at index " + i
							// 			+ " for pair " + temp);
						}
					}
					if (step <= 3)
						System.out.println(template.toString());
				}
				System.out.println(template.length());

				for (int i = template.length() - 1; i > 0; i--) {
					pairs2.add(Pair.of(template.charAt(i - 1), template.charAt(i)));
				}

				System.out.println("layer 1");
			}

			for (Pair<Character> pair : pairs2) {
				template.setLength(0);
				template.append(pair.obj1);
				template.append(pair.obj2);
				for (int step = 1; step <= 10; step++) {
					// System.out.println(step);
					for (int i = template.length() - 1; i > 0; i--) {
						Pair<Character> temp = Pair.of(template.charAt(i - 1), template.charAt(i));
						if (rules.containsKey(temp)) {
							template.insert(i, rules.get(temp).charValue());
							// if (step <= 2)
							// 	System.out.println("inserting " + rules.get(temp).charValue() + " at index " + i
							// 			+ " for pair " + temp);
						}
					}
					if (step <= 3)
						System.out.println(template.toString());
				}
				System.out.println(template.length());

				List<Pair<Character>> pairs3 = new ArrayList<>();
				List<Pair<Character>> pairs4 = new ArrayList<>();

				for (int i = template.length() - 1; i > 0; i--) {
					pairs3.add(Pair.of(template.charAt(i - 1), template.charAt(i)));
				}

				System.out.println("layer 2");

				for (Pair<Character> pair2 : pairs3) {
					template.setLength(0);
					template.append(pair2.obj1);
					template.append(pair2.obj2);
					for (int step = 1; step <= 10; step++) {
						// System.out.println(step);
						for (int i = template.length() - 1; i > 0; i--) {
							Pair<Character> temp = Pair.of(template.charAt(i - 1), template.charAt(i));
							if (rules.containsKey(temp)) {
								template.insert(i, rules.get(temp).charValue());
								// if (step <= 2)
								// 	System.out.println("inserting " + rules.get(temp).charValue() + " at index " + i
								// 			+ " for pair " + temp);
							}
						}
						if (step <= 3)
							System.out.println(template.toString());
					}
					System.out.println(template.length());

					for (int i = template.length() - 1; i > 0; i--) {
						pairs4.add(Pair.of(template.charAt(i - 1), template.charAt(i)));
					}

					System.out.println("layer 3");
				}

				for (Pair<Character> pair2 : pairs4) {
					template.setLength(0);
					template.append(pair2.obj1);
					template.append(pair2.obj2);
					for (int step = 1; step <= 10; step++) {
						// System.out.println(step);
						for (int i = template.length() - 1; i > 0; i--) {
							Pair<Character> temp = Pair.of(template.charAt(i - 1), template.charAt(i));
							if (rules.containsKey(temp)) {
								template.insert(i, rules.get(temp).charValue());
								// if (step <= 2)
								// 	System.out.println("inserting " + rules.get(temp).charValue() + " at index " + i
								// 			+ " for pair " + temp);
							}
						}
						// if (step <= 3)
						// 	System.out.println(template.toString());
					}
					System.out.println(template.length());

					for (char ch : template.toString().toCharArray())
						freqs.put(ch, freqs.getOrDefault(ch, 0L) + 1);
					
					System.out.println("layer 4");
				}
			}

			System.out.println(totalCount);

			List<Map.Entry<Character, Long>> entries = new ArrayList<>(freqs.entrySet());
			entries.sort((e1, e2) -> e2.getValue().compareTo(e1.getValue()));

			// return entries.toString();
			return entries.get(0) + " " + entries.get(entries.size() - 1);
		} catch (FileNotFoundException e) {
			return "-1";
		}
	}

	public static String day14p1() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);

			StringBuffer template = new StringBuffer(sc.nextLine());
			sc.nextLine();

			Map<Pair<Character>, Character> rules = new HashMap<>(); 
			while (sc.hasNextLine()) {
				String s = sc.nextLine();
				if (s.equals("quit"))
					break;

				if (s.isBlank())
					continue;

				String[] si = s.split(" -> ");
				rules.put(Pair.of(si[0].charAt(0), si[0].charAt(1)), si[1].charAt(0));
			}
			sc.close();

			System.out.println(template.toString());

			for (int step = 1; step <= 10; step++) {
				System.out.println(step);
				for (int i = template.length()-1; i > 0; i--) {
					Pair<Character> temp = Pair.of(
						template.charAt(i-1),
						template.charAt(i)
					);
					if (rules.containsKey(temp)) {
						template.insert(i, rules.get(temp).charValue());
						if (step <= 2)
							System.out.println("inserting " + rules.get(temp).charValue() + " at index " + i + " for pair " + temp);
					}
				}
				if  (step <= 4) System.out.println(template.toString());
			}

			System.out.println(template.length());

			Map<Character, Long> freqs = new HashMap<>();
			for (char ch : template.toString().toCharArray())
				freqs.put(ch, freqs.getOrDefault(ch, 0L) + 1);
			
			List<Map.Entry<Character, Long>> entries = new ArrayList<>(freqs.entrySet());
			entries.sort((e1, e2) -> e2.getValue().compareTo(e1.getValue()));

			// return entries.toString();
			return entries.get(0) + " " + entries.get(entries.size()-1);
		} catch (FileNotFoundException e) {
			return "-1";
		}
	}

	public static String day13p2() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);

			Boolean[][] dots = new Boolean[1000][1500];
			List<Entry<Character, Integer>> folds = new ArrayList<>();

			for (int i = 0; i < dots.length; i++) {
				for (int j = 0; j < dots[i].length; j++) {
					dots[i][j] = false;
				}
			} 

			int count = 0;
			while (sc.hasNextLine()) {
				String s = sc.nextLine();
				if (s.equals("quit"))
					break;

				if (s.isBlank())
					continue;

				if (s.contains("fold")) {
					s = s.replace("fold along ", "");
					folds.add(new Entry<>(s.split("=")[0].charAt(0), Integer.parseInt(s.split("=")[1])));
					continue;
				}

				String[] si = s.split(",");
				count++;
				dots[Integer.parseInt(si[1])][Integer.parseInt(si[0])] = Boolean.valueOf(true);
			}
			System.out.println(count);
			sc.close();

			System.out.println(Arrays.stream(dots)
					.mapToLong(ba -> IntStream.range(0, ba.length)
							.mapToObj(idx -> ba[idx])
							.filter(Boolean::booleanValue)
							.count())
					.sum());

			for (int i = 0; i < folds.size(); i++)
				fold_new(dots, folds.get(i).obj1, folds.get(i).obj2);

			long dotCount = Arrays.stream(dots)
					.mapToLong(ba -> IntStream.range(0, ba.length).mapToObj(idx -> ba[idx]).filter(b -> b).count())
					.sum();

			return Arrays.stream(dots).flatMap(ba -> {
				if (Arrays.stream(ba).noneMatch(Boolean::booleanValue)) return Stream.<Character>empty();
				else return Stream.concat(IntStream.range(0, (int) dotCount).mapToObj(i -> ba[i]).map(b -> (b ? 'o' : ' ')), Stream.of('\n'));
			}).reduce("", (str, c) -> str + c, (str1, str2) -> str1 + str2);
		} catch (FileNotFoundException e) {
			return "-1";
		}
	}

	public static long day13p1() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);

			Boolean[][] dots = new Boolean[1000][1500];
			List<Entry<Character, Integer>> folds = new ArrayList<>();

			for (int i = 0; i < dots.length; i++) {
				for (int j = 0; j < dots[i].length; j++) {
					dots[i][j] = false;
				}
			}

			int count = 0;
			while (sc.hasNextLine()) {
				String s = sc.nextLine();
				if (s.equals("quit"))
					break;

				if (s.isBlank()) continue;
				
				if (s.contains("fold")) {
					s = s.replace("fold along ","");
					folds.add(new Entry<>(s.split("=")[0].charAt(0), Integer.parseInt(s.split("=")[1])));
					continue;
				}

				String[] si = s.split(",");
				dots[Integer.parseInt(si[1])][Integer.parseInt(si[0])] = true;
			}
			System.out.println(count);
			sc.close();

			System.out.println(Arrays.stream(dots)
					.mapToLong(ba -> IntStream.range(0, ba.length)
							.mapToObj(idx -> ba[idx])
							.filter(b -> b).count()).sum());

			fold_new(dots, folds.get(0).obj1, folds.get(0).obj2);

			return Arrays.stream(dots)
					.mapToLong(ba -> IntStream.range(0, ba.length).mapToObj(idx -> ba[idx]).filter(b -> b).count())
					.sum();
		} catch (FileNotFoundException e) {
			return -1;
		}
	}

	public static void fold_new(Boolean[][] dots, char dir, int fold) {
		int count = 0;
		for (int y = 0; y < dots.length; y++) {
			for  (int x = 0; x < dots[y].length; x++) {
				if (dir == 'x') {
					if (dots[y][x]) {
						count++;
						if (x > fold) {
							// count++;
							dots[y][fold*2 - x] = true;
							dots[y][x] = false;
							// System.out.println("ran");
						}
					}
				} else {
					if (dots[y][x]) {
						count++;
						if (y > fold) {
							dots[fold*2 - y][x] = true;
							dots[y][x] = false;
						}
					}
				}
			}
		}

		System.out.println("processed " + count + " dots");
	}

	public static void fold(List<Pair<Integer>> dots, List<Entry<String, Integer>> folds, Pair<Integer> paperSize) {
		for (int i = 0; i < 1; i++) { // folds loop
			Entry<String, Integer> fold = folds.get(i);

			if (fold.obj1.equals("x")) {
				ListIterator<Pair<Integer>> it = dots.listIterator();
				while (it.hasNext()) {
					Pair<Integer> dot = it.next();
					// ignore y
					if (dot.obj1 == fold.obj2) {
						it.remove();
						continue;
					}
					if (dot.obj1 > fold.obj2) {
						int newX = fold.obj2 - (dot.obj1 - fold.obj2); // paperSize.obj1 - dot.obj1;
						if (dots.contains(Pair.of(newX, dot.obj2))) {
							System.out.println("dot " + dot.obj1 + " removed");
							it.remove();
							continue;
						}
						System.out.println("dot " + dot.obj1 + " is set to " + newX);
						it.set(Pair.of(newX, dot.obj2));
					}
				}
			}
			else {
				ListIterator<Pair<Integer>> it = dots.listIterator();
				while (it.hasNext()) {
					Pair<Integer> dot = it.next();
					// ignore x
					if (dot.obj2 == fold.obj2) {
						it.remove();
						continue;
					}
					if (dot.obj2 > fold.obj2) {
						int newY = paperSize.obj2 - dot.obj2;
						if (dots.contains(Pair.of(dot.obj1, newY))) {
							System.out.println("dot " + dot.obj2 + " removed");
							it.remove();
							continue;
						}
						// System.out.println("dot " + dot.obj2 + " is set to " + newY);
						it.set(Pair.of(dot.obj1, newY));
					}
				}
			}
		}
	}

	public static int day12() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);

			while (sc.hasNextLine()) {
				String s = sc.nextLine();
				if (s.equals("quit"))
					break;

				String[] si = s.split("-");
				Node.of(si[0]).addConnection(Node.of(si[1]));
			}
			sc.close();

			Set<String> strs = findPath(Node.of("start"));

			// for (String str : strs) {
			// 	System.out.println(str);
			// }

			return strs.size();
		} catch (FileNotFoundException e) {
			return -1;
		}
	}

	public static Set<String> findPath(Node start) {
		if (start.name.equals("end")) return Set.of("end");

		Set<String> paths = new TreeSet<String>() {
			private static final long serialVersionUID = 1L;
			
			@Override
			public boolean add(String e) {
				return super.add((start.isBigNode ? start.name.toUpperCase() : start.name) + "," + e);
			}

			@Override
			public boolean addAll(Collection<? extends String> c) {
				if (c.size() > 0) {
					for (String s : c)
						add(s);
					return true;
				}
				return false;
			}
		};
		start.setVisited();

		for (Node n : start.connections) {
			if (n.getVisited())
				continue;
			try {
				paths.addAll(findPath(n));
			} catch (Error e) {
				System.err.println(e.getClass());
				return Set.of("no");
			}
		}

		start.reset(false);

		if (Node.twoSmall == null && !start.isBigNode && !start.name.equals("start")) {
			// also try having two
			Node.twoSmall = start;
			start.setVisited();

			// System.out.println("trying twoSmall for node " + start.name);

			for (Node n : start.connections) {
				if (n.getVisited())
					continue;
				paths.addAll(findPath(n));
			}

			Node.twoSmall = null;
		}

		start.reset(Node.twoSmall != start);
		return paths;
	}

	public static int day11p2() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);
			int destStep = 0;

			int[][] map = new int[10][10];

			for (int i = 0; i < 10; i++) {
				String s = sc.nextLine();
				if (s.equals("quit"))
					break;

				String[] si = s.split("");
				for (int j = 0; j < 10; j++)
					map[i][j] = Integer.parseInt(si[j]);
			}
			sc.close();

			for (int step = 1; step <= 1000; step++) {
				for (int i = 0; i < 10; i++) {
					for (int j = 0; j < 10; j++) {
						map[i][j]++;
					}
				}

				int fCount = 0;

				List<Pair<Integer>> modified = new ArrayList<>();
				List<Pair<Integer>> justModified = new ArrayList<>();
				do {
					justModified.clear();
					for (int i = 0; i < 10; i++) {
						for (int j = 0; j < 10; j++) {
							if (modified.contains(Pair.of(i, j)))
								continue;
							if (map[i][j] > 9) {
								map[i][j] = 0;
								fCount++;
								justModified.add(Pair.of(i, j));

								for (int m = -1; m <= 1; m++) {
									for (int n = -1; n <= 1; n++) {
										if (m == 0 && n == 0)
											continue;
										if (modified.contains(Pair.of(i + m, j + n))
												|| justModified.contains(Pair.of(i + m, j + n))) {
											// System.out.println("ignoring " + (i+m) + ", " + (j+n) + " for flash " + i
											// + " " + j);
											continue;
										} else {
											// System.out.println("adding " + (i+m) + ", " + (j+n) + " for flash " + i +
											// " " + j);
										}

										try {
											map[i + m][j + n]++;
										} catch (ArrayIndexOutOfBoundsException e) {
										}
									}
								}
							}
						}
					}
					modified.addAll(justModified);
				} while (justModified.size() > 0);

				System.out.println("Step " + step + ": " + modified.size());
				if (step < 10)
					System.out.println(Arrays.deepToString(map).replace("],", "\n"));

				if (fCount == 100) {
					return step;
				}
			}

			return destStep;
		} catch (FileNotFoundException e) {
			return -1;
		}
	}

	public static int day11p1() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);
			int count = 0;

			int[][] map = new int[10][10];

			for (int i = 0; i < 10; i++) {
				String s = sc.nextLine();
				if (s.equals("quit"))
					break;

				String[] si = s.split("");
				for (int j = 0; j < 10; j++)
					map[i][j] = Integer.parseInt(si[j]);
			}
			sc.close();

			for (int step = 1; step <= 100; step++) {
				for (int i = 0; i < 10; i++) {
					for (int j = 0; j < 10; j++) {
						map[i][j]++;
					}
				}

				List<Map.Entry<Integer, Integer>> modified = new ArrayList<>();
				List<Map.Entry<Integer, Integer>> justModified = new ArrayList<>();
				do {
					justModified.clear();
					for (int i = 0; i < 10; i++) {
						for (int j = 0; j < 10; j++) {
							if (modified.contains(new AbstractMap.SimpleEntry<>(i, j)))
								continue;
							if (map[i][j] > 9) {
								map[i][j] = 0;
								count++;
								justModified.add(new AbstractMap.SimpleEntry<>(i, j));

								for (int m = -1; m <= 1; m++) {
									for (int n = -1; n <= 1; n++) {
										if (m == 0 && n == 0)
											continue;
										if (modified.contains(new AbstractMap.SimpleEntry<>(i + m, j + n))
												|| justModified.contains(new AbstractMap.SimpleEntry<>(i + m, j + n))) {
											// System.out.println("ignoring " + (i+m) + ", " + (j+n) + " for flash " + i
											// + " " + j);
											continue;
										} else {
											// System.out.println("adding " + (i+m) + ", " + (j+n) + " for flash " + i +
											// " " + j);
										}

										try {
											map[i + m][j + n]++;
										} catch (ArrayIndexOutOfBoundsException e) {
										}
									}
								}
							}
						}
					}
					modified.addAll(justModified);
				} while (justModified.size() > 0);

				System.out.println("Step " + step + ": " + modified.size());
				if (step < 10)
					System.out.println(Arrays.deepToString(map).replace("],", "\n"));
			}

			return count;
		} catch (FileNotFoundException e) {
			return -1;
		}
	}

	public static long day10p2() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);

			List<Long> total = new ArrayList<>();

			while (sc.hasNextLine()) {
				String s = sc.nextLine();
				if (s.equals("quit"))
					break;

				char[] c = s.toCharArray();
				Deque<Character> dq = new ArrayDeque<>();

				char invalid = ' ';

				out: for (int i = 0; i < c.length; i++) {
					switch (c[i]) {
						case '(':
						case '[':
						case '{':
						case '<':
							dq.add(c[i]);
							break;
						case ')':
							if (dq.peekLast() == '(') {
								dq.removeLast();
								break;
							}
							invalid = ')';
							break out;
						case ']':
							if (dq.peekLast() == '[') {
								dq.removeLast();
								break;
							}
							invalid = ']';
							break out;
						case '}':
							if (dq.peekLast() == '{') {
								dq.removeLast();
								break;
							}
							invalid = '}';
							break out;
						case '>':
							if (dq.peekLast() == '<') {
								dq.removeLast();
								break;
							}
							invalid = '>';
							break out;
						default:
							break;
					}
				}

				if (invalid != ' ') {
					continue;
				}

				long score = 0L;

				while (!dq.isEmpty()) {
					score *= 5;
					char ch = dq.pollLast();

					switch (ch) {
						case '(':
							score += 1;
							break;
						case '[':
							score += 2;
							break;
						case '{':
							score += 3;
							break;
						case '<':
							score += 4;
							break;
						default:
							break;
					}
				}

				total.add(score);
			}
			sc.close();

			total.sort(Collections.reverseOrder());

			return total.get(total.size() / 2);
		} catch (FileNotFoundException e) {
			return -1L;
		}
	}

	public static long day10p1() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);

			long total = 0;

			while (sc.hasNextLine()) {
				String s = sc.nextLine();
				if (s.equals("quit"))
					break;

				char[] c = s.toCharArray();
				Deque<Character> dq = new ArrayDeque<>();

				char invalid = ' ';

				out: for (int i = 0; i < c.length; i++) {
					switch (c[i]) {
						case '(':
						case '[':
						case '{':
						case '<':
							dq.add(c[i]);
							break;
						case ')':
							if (dq.peekLast() == '(') {
								dq.removeLast();
								break;
							}
							invalid = ')';
							break out;
						case ']':
							if (dq.peekLast() == '[') {
								dq.removeLast();
								break;
							}
							invalid = ']';
							break out;
						case '}':
							if (dq.peekLast() == '{') {
								dq.removeLast();
								break;
							}
							invalid = '}';
							break out;
						case '>':
							if (dq.peekLast() == '<') {
								dq.removeLast();
								break;
							}
							invalid = '>';
							break out;
						default:
							break;
					}
				}

				if (invalid != ' ') {
					switch (invalid) {
						case ')':
							total += 3;
							break;
						case ']':
							total += 57;
							break;
						case '}':
							total += 1197;
							break;
						case '>':
							total += 25137;
							break;
					}
				}
			}
			sc.close();

			return total;
		} catch (FileNotFoundException e) {
			return -1L;
		}
	}

	public static long day9p2() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);
			List<Long> totals = new ArrayList<>();

			List<List<Integer>> map = new ArrayList<>();

			while (sc.hasNextLine()) {
				String s = sc.nextLine();
				if (s.equals("quit"))
					break;

				List<Integer> toAdd = new ArrayList<>();
				for (String si : s.split(""))
					toAdd.add(Integer.parseInt(si));

				map.add(toAdd);
			}
			sc.close();

			for (int i = 0; i < map.size(); i++) {
				List<Integer> arr = map.get(i);

				for (int j = 0; j < arr.size(); j++) {
					boolean lessThanAllSides = true;
					try {
						lessThanAllSides = lessThanAllSides && (arr.get(j) < arr.get(j - 1));
					} catch (IndexOutOfBoundsException e) {
					}
					try {
						lessThanAllSides = lessThanAllSides && (arr.get(j) < arr.get(j + 1));
					} catch (IndexOutOfBoundsException e) {
					}
					try {
						lessThanAllSides = lessThanAllSides && (map.get(i - 1).get(j) > arr.get(j));
					} catch (IndexOutOfBoundsException e) {
					}
					try {
						lessThanAllSides = lessThanAllSides && (map.get(i + 1).get(j) > arr.get(j));
					} catch (IndexOutOfBoundsException e) {
					}

					if (!lessThanAllSides)
						continue;

					Queue<Map.Entry<Integer, Integer>> q = new LinkedList<>();
					q.add(new AbstractMap.SimpleEntry<>(i, j));

					long count = 0;
					int[][] dirs = { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

					while (q.size() > 0) {
						Map.Entry<Integer, Integer> e = q.poll();

						int prev = map.get(e.getKey()).get(e.getValue());

						if (prev == -1)
							continue;

						map.get(e.getKey()).set(e.getValue(), -1);
						count++;

						// if (i == 86 && j == 48)
						// System.out.println("Counting " + e.getKey() + " " + e.getValue() + ": " +
						// prev);

						for (int k = 0; k < 4; k++) {
							try {
								int x = e.getKey() + dirs[k][0];
								int y = e.getValue() + dirs[k][1];

								int val = map.get(x).get(y);
								if (val != 9 && val >= 0) {
									q.offer(new AbstractMap.SimpleEntry<>(x, y));
								}
							} catch (IndexOutOfBoundsException ex) {
								continue;
							}
						}
					}

					System.out.println(i + " " + j + ": " + count);
					totals.add(count);
				}
			}

			totals.sort(Collections.reverseOrder());
			return totals.get(0) * totals.get(1) * totals.get(2);
		} catch (FileNotFoundException e) {
			return -1L;
		}
	}

	public static int day9p1() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);
			int totalLow = 0;

			List<List<Integer>> map = new ArrayList<>();

			while (sc.hasNextLine()) {
				String s = sc.nextLine();
				if (s.equals("quit"))
					break;

				List<Integer> toAdd = new ArrayList<>();
				for (String si : s.split(""))
					toAdd.add(Integer.parseInt(si));

				map.add(toAdd);
			}
			sc.close();

			for (int i = 0; i < map.size(); i++) {
				List<Integer> arr = map.get(i);

				for (int j = 0; j < arr.size(); j++) {
					boolean lessThanAllSides = true;
					try {
						lessThanAllSides = lessThanAllSides && (arr.get(j) < arr.get(j - 1));
					} catch (IndexOutOfBoundsException e) {
					}
					try {
						lessThanAllSides = lessThanAllSides && (arr.get(j) < arr.get(j + 1));
					} catch (IndexOutOfBoundsException e) {
					}
					try {
						lessThanAllSides = lessThanAllSides && (map.get(i - 1).get(j) > arr.get(j));
					} catch (IndexOutOfBoundsException e) {
					}
					try {
						lessThanAllSides = lessThanAllSides && (map.get(i + 1).get(j) > arr.get(j));
					} catch (IndexOutOfBoundsException e) {
					}

					if (lessThanAllSides)
						totalLow += arr.get(j) + 1;
				}
			}

			return totalLow;
		} catch (FileNotFoundException e) {
			return -1;
		}
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

	public static Set<Character> convertToSet(char[] charArray) {

		// Result hashset
		Set<Character> resultSet = new HashSet<>();

		for (int i = 0; i < charArray.length; i++) {
			resultSet.add(Character.valueOf(charArray[i]));
		}

		// Return result
		return resultSet;
	}

	public static <V, K> Map<V, K> invert(Map<K, V> map) {
		return map.entrySet().stream().collect(Collectors.toMap(Map.Entry::getValue, Map.Entry::getKey));
	}

	public static long day8p2() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);
			// Scanner sc = new Scanner(System.in);
			long total = 0;
			while (sc.hasNextLine()) {
				String sio = sc.nextLine();
				if (sio.equals("quit"))
					break;
				String[] input = sio.split(" \\| ")[0].split(" ");
				String[] output = sio.split(" \\| ")[1].split(" ");

				Map<String, Character> charMap = new HashMap<>();

				String one = ""; // len 2
				String seven = ""; // len 3
				String four = ""; // len 4
				// String eight = ""; // len 7
				List<String> sixLong = new ArrayList<>();
				List<String> fiveLong = new ArrayList<>();

				for (String s : input) {
					switch (s.length()) {
						case 2:
							one = s;
							break;
						case 3:
							seven = s;
							break;
						case 4:
							four = s;
							break;
						case 7:
							// eight = s;
							break;
						case 5:
							fiveLong.add(s);
							break;
						case 6:
							sixLong.add(s);
							break;
						default:
							break;
					}
				}

				Set<Character> temp = convertToSet(seven.toCharArray());
				temp.removeAll(convertToSet(one.toCharArray()));
				charMap.put("top", temp.iterator().next());

				temp = convertToSet(four.toCharArray());
				temp.removeAll(convertToSet(one.toCharArray()));
				// middle and top-left
				Set<Character> middle_TopLeft = temp;

				String three = "";
				Set<Character> middle_Bottom = new HashSet<Character>();

				for (String s : fiveLong) {
					Set<Character> o = convertToSet(s.toCharArray());
					if (!o.containsAll(convertToSet(seven.toCharArray())))
						continue;
					three = s;

					o.removeAll(convertToSet(seven.toCharArray()));
					middle_Bottom.addAll(o);
					break;
				}

				fiveLong.remove(three);

				temp = new HashSet<Character>(middle_TopLeft);
				temp.retainAll(middle_Bottom);
				charMap.put("middle", temp.iterator().next());

				middle_TopLeft.removeAll(temp);
				charMap.put("topLeft", middle_TopLeft.iterator().next());

				middle_Bottom.removeAll(temp);
				charMap.put("bottom", middle_Bottom.iterator().next());

				String five = "";

				for (String s : fiveLong) {
					Set<Character> o = convertToSet(s.toCharArray());
					if (o.contains(charMap.get("top")) && o.contains(charMap.get("topLeft"))) {
						five = s;

						o.remove(charMap.get("top"));
						o.remove(charMap.get("topLeft"));
						o.remove(charMap.get("middle"));
						o.remove(charMap.get("bottom"));

						charMap.put("bottomRight", o.iterator().next());

						break;
					}
				}

				fiveLong.remove(five);
				String two = fiveLong.get(0);

				temp = convertToSet(one.toCharArray());
				temp.remove(charMap.get("bottomRight"));
				charMap.put("topRight", temp.iterator().next());

				temp = convertToSet(two.toCharArray());
				temp.remove(charMap.get("top"));
				temp.remove(charMap.get("topRight"));
				temp.remove(charMap.get("middle"));
				temp.remove(charMap.get("bottom"));
				charMap.put("bottomLeft", temp.iterator().next());

				// System.out.println(charMap.toString());

				// Map<Character, String> charLookup = invert(charMap);
				String outDigit = "";

				Map<Set<Character>, Integer> NUM_LOOKUP = new HashMap<>();

				{
					NUM_LOOKUP.put(Set.of(charMap.get("top"), charMap.get("topLeft"), charMap.get("topRight"),
							charMap.get("bottomLeft"), charMap.get("bottomRight"), charMap.get("bottom")), 0);
					NUM_LOOKUP.put(Set.of(charMap.get("topRight"), charMap.get("bottomRight")), 1);
					NUM_LOOKUP.put(Set.of(charMap.get("top"), charMap.get("topRight"), charMap.get("middle"),
							charMap.get("bottomLeft"), charMap.get("bottom")), 2);
					NUM_LOOKUP.put(Set.of(charMap.get("top"), charMap.get("topRight"), charMap.get("middle"),
							charMap.get("bottomRight"), charMap.get("bottom")), 3);
					NUM_LOOKUP.put(Set.of(charMap.get("topLeft"), charMap.get("topRight"), charMap.get("middle"),
							charMap.get("bottomRight")), 4);
					NUM_LOOKUP.put(Set.of(charMap.get("top"), charMap.get("topLeft"), charMap.get("middle"),
							charMap.get("bottomRight"), charMap.get("bottom")), 5);
					NUM_LOOKUP.put(Set.of(charMap.get("top"), charMap.get("topLeft"), charMap.get("middle"),
							charMap.get("bottomLeft"), charMap.get("bottomRight"), charMap.get("bottom")), 6);
					NUM_LOOKUP.put(Set.of(charMap.get("top"), charMap.get("topRight"), charMap.get("bottomRight")), 7);
					NUM_LOOKUP.put(Set.of(charMap.get("top"), charMap.get("topLeft"), charMap.get("topRight"),
							charMap.get("middle"), charMap.get("bottomLeft"), charMap.get("bottomRight"),
							charMap.get("bottom")), 8);
					NUM_LOOKUP.put(Set.of(charMap.get("top"), charMap.get("topLeft"), charMap.get("topRight"),
							charMap.get("middle"), charMap.get("bottomRight"), charMap.get("bottom")), 9);
				}

				for (String s : output) {
					outDigit += String.valueOf(NUM_LOOKUP.getOrDefault(convertToSet(s.toCharArray()), -1));
				}

				// System.out.println(outDigit);

				total += Integer.parseInt(outDigit);
			}
			sc.close();

			return total;
		} catch (Exception e) {
			System.err.println(e);
			return -1L;
		}
	}

	public static int day8p1() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);
			int count = 0;
			while (sc.hasNextLine()) {
				String sio = sc.nextLine();
				if (sio.equals("quit"))
					break;
				// String input = sio.split(" \\| ")[0];
				String output = sio.split(" \\| ")[1];

				for (String s : output.split(" ")) {
					if (s.length() == 2 || s.length() == 3 || s.length() == 4 || s.length() == 7)
						count++;
				}
			}
			sc.close();

			return count;
		} catch (FileNotFoundException e) {
			return -1;
		}
	}

	public static String day7p2() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);
			String s = sc.nextLine();
			sc.close();

			List<Integer> crabs = new ArrayList<>();

			for (String str : s.split(",")) {
				crabs.add(Integer.parseInt(str));
			}

			int bestNum = -1;
			long prevTotalDistance = 10000000000L;

			for (int i = 0; i < 2000; i++) {
				long total = 0;
				for (int crab : crabs) {
					int dist = Math.abs(crab - i);
					total += dist * (dist + 1) / 2L;
				}
				System.out.println(i + ": " + total);

				if (total < prevTotalDistance) {
					prevTotalDistance = total;
					bestNum = i;
				}
			}

			return bestNum + " " + prevTotalDistance;
		} catch (Exception e) {
			return "not found";
		}
	}

	public static int day7p1() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);
			String s = sc.nextLine();
			sc.close();

			List<Integer> crabs = new ArrayList<>();

			for (String str : s.split(",")) {
				crabs.add(Integer.parseInt(str));
			}

			int prevTotalDistance = 1000000;

			for (int i = 0; i < 2000; i++) {
				int total = 0;
				for (int crab : crabs) {
					total += Math.abs(crab - i);
				}
				System.out.println(i + ": " + total);

				if (total < prevTotalDistance) {
					prevTotalDistance = total;
				}
			}

			return prevTotalDistance;
		} catch (Exception e) {
			return 0;
		}
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

		while (sum.compareTo(new BigInteger("150000000000000000000000000000000000000000000000000000000")
				.divide(new BigInteger("4"))) < 0) {
			Map<Integer, BigInteger> newMap = new HashMap<>();
			for (int i = 1; i <= 8; i++) {
				newMap.put(i - 1, fishMap.getOrDefault(i, BigInteger.ZERO));
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

		List<byte[]> fish = temp.stream().map((val) -> new byte[] { Byte.parseByte(val) }).collect(Collectors.toList());

		for (int day = 1; day <= 256; day++) {
			List<byte[]> toAdd = new ArrayList<>();
			for (byte[] daysLeft : fish) {
				if (daysLeft[0] == 0) {
					toAdd.add(new byte[] { 8 });
					daysLeft[0] = 6;
				} else
					daysLeft[0]--;
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

			boardsList: for (Map<Integer, Boolean> board : boards) {
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

		Map<Integer, Boolean> winningBoard = null;
		String winMethod = "";
		int lastNum = 0;

		out: for (int i = 0; i < nums.size(); i++) {
			int num = nums.get(i);
			lastNum = num;

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
						winningBoard = board;
						winMethod = "row " + (j + 1);
						break out;
					}
				}

				// columns
				for (int j = 0; j < 5; j++) {
					final int temp = j;
					if (Arrays.stream(new int[] { 0, 1, 2, 3, 4 }).mapToObj(k -> boardNums.get(k * 5 + temp))
							.allMatch(e -> e.getValue())) {
						winningBoard = board;
						winMethod = "column " + (j + 1);
						break out;
					}
				}
			}
		}

		List<Map.Entry<Integer, Boolean>> boardNums = new ArrayList<>(winningBoard.entrySet());

		int unmarkedNumbersTotal = sum(
				boardNums.stream().filter(e -> e.getValue() != true).map(e -> e.getKey()).collect(Collectors.toList()));

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
				if (s.equals("quit"))
					break;
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
				if (s.toCharArray()[i] == '1')
					positiveBits++;
			}

			if (positiveBits == modified.size() || positiveBits == 0)
				continue;
			System.out.println(positiveBits + " " + modified.size());

			char checkFor = (positiveBits >= (modified.size() / 2.0)) ? '1' : '0';
			System.out.println(checkFor);

			List<String> toRemove = new ArrayList<>();

			for (String s : modified) {
				if (s.toCharArray()[i] != checkFor)
					toRemove.add(s);
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
				if (s.toCharArray()[i] == '0')
					positiveBits++;
			}

			if (positiveBits == modified.size() || positiveBits == 0)
				continue;
			System.out.println(positiveBits + " " + modified.size());

			char checkFor = (positiveBits <= (modified.size() / 2.0)) ? '0' : '1';
			System.out.println(checkFor);

			List<String> toRemove = new ArrayList<>();

			for (String s : modified) {
				if (s.toCharArray()[i] != checkFor)
					toRemove.add(s);
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
				if (s.equals("quit"))
					break;
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
				if (chars[i] == '1')
					positiveBits[i]++;
			}
		}

		String outputGamma = "";
		String outputOther = "";

		for (int i = 0; i < bitLength; i++) {
			if (positiveBits[i] > (l.size() / 2.0)) {
				outputGamma += "1";
				outputOther += "0";
			} else {
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
			if (s.equals("quit"))
				break;

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
			if (s.equals("quit"))
				break;

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
				if (l.size() > 3)
					l.poll();

				if (l.size() < 3)
					continue;
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

// Utility
class Node {
	static Map<String, Node> nodes = new HashMap<>();

	private boolean isVisited = false;
	public final boolean isBigNode;
	public final String name;

	public static Node twoSmall = null;
	public int twoSmallCounter = 0;

	final Set<Node> connections = new HashSet<>();

	private Node(String name) {
		this.isBigNode = name.equals(name.toUpperCase());
		this.name = name.toLowerCase();
		nodes.put(name.toLowerCase(), this);
	}

	public static Node of(String name) {
		if (nodes.containsKey(name.toLowerCase())) {
			return nodes.get(name.toLowerCase());
		}
		return new Node(name);
	}

	public static void resetAll() {
		for (Node n : nodes.values()) {
			n.reset(true);
		}
	}

	public boolean getVisited() {
		return this.isVisited;
	}
	public Node setVisited() {
		if (!this.isBigNode) {
			if (this == twoSmall) {
				this.twoSmallCounter++;
				this.isVisited = this.twoSmallCounter >= 2;
			}
			else this.isVisited = true;
		}
		return this;
	}
	public Node reset(boolean resetTwoSmall) {
		this.isVisited = false;
		if (resetTwoSmall)
			this.twoSmallCounter = 0;
		return this;
	}

	/**
	 * @return the original node, for chaining
	 */
	public Node addConnection(Node newNode) {
		this.connections.add(newNode);
		newNode.connections.add(this);
		return this;
	}
}

class Coords {

	int x;
	int y;

	public Coords(Integer x, Integer y) {
		this.x = x;
		this.y = y;
	}
	
	public static Coords of(int x, int y) {
		return new Coords(x, y);
	}

	public Coords left() {
		return Coords.of(x-1, y);
	}
	public Coords right() {
		return Coords.of(x+1, y);
	}
	public Coords up() {
		return Coords.of(x, y-1);
	}
	public Coords down() {
		return Coords.of(x, y+1);
	}

	@Override
	public boolean equals(Object obj) {
		return obj instanceof Coords && (((Coords) obj).x == this.x) && (((Coords) obj).y == this.y);
	}

	@Override
	public String toString() {
		return "(" + this.x + ", " + this.y + ")";
	}
}

class OptionalPair implements Cloneable {
	Object a = null;
	Object b = null;
	OptionalPair parent = null;
	int indexFromParent = -1;

	int readIndex = 0;

	public OptionalPair(OptionalPair parent) {
		this.parent = parent;
	}

	public OptionalPair(OptionalPair parent, int a, int b) {
		this(parent);
		this.a = a;
		this.b = b;
	}

	public OptionalPair(OptionalPair parent, int a, OptionalPair b) {
		this(parent);
		this.a = a;
		b.indexFromParent = 1;
		this.b = b;
	}

	public OptionalPair(OptionalPair parent, OptionalPair a, int b) {
		this(parent);
		a.indexFromParent = 0;
		this.a = a;
		this.b = b;
	}

	public OptionalPair(OptionalPair parent, OptionalPair a, OptionalPair b) {
		this(parent);
		a.indexFromParent = 0;
		this.a = a;
		b.indexFromParent = 1;
		this.b = b;
	}

	public void close() {
		this.readIndex = -1;
	}

	/*
	public int indexOf(Object obj) {
		if (a.equals(obj)) return 0;
		else if (b.equals(obj)) return 1;
		else return -1;
	}
	*/

	public OptionalPair setIndex(int i) {
		this.indexFromParent = i;
		return this;
	}

	public Object getFromIndex(int i) {
		if (i == 0) return a;
		if (i == 1) return b;
		throw new IllegalArgumentException("invalid index: " + i);
	}

	public void reduce() {
		out: while (true) {
			// Check explode criteria
			int depth = 0;
			OptionalPair currentRoot = this;
			List<OptionalPair> checked = new ArrayList<>();

			// System.out.println(this);

			while (currentRoot != null) {
				// System.out.println(
				// 	// depth + " " + currentRoot.indexFromParent + " " + 
				// 	currentRoot);
				if (depth >= 4 && currentRoot.a instanceof Integer && currentRoot.b instanceof Integer) {
					// Find left number
					OptionalPair temp = currentRoot;
					leftCheck: while (temp.parent != null) {
						if (temp.indexFromParent == 1) {
							if (temp.parent.a instanceof Integer) {
								temp.parent.a = (int) temp.parent.a + (int) currentRoot.a;
								break leftCheck;
							} else {
								// look for rightmost number
								OptionalPair temp2 = (OptionalPair) temp.parent.a;
								while (temp2.b instanceof OptionalPair) {
									temp2 = (OptionalPair) temp2.b;
								}
								// System.out.println(this);
								// System.out.println(currentRoot);
								temp2.b = (int) temp2.b + (int) currentRoot.a;
								break leftCheck;
							}
						} else {
							temp = temp.parent;
						}
					}

					// Find right number
					temp = currentRoot;
					rightCheck: while (temp.parent != null) {
						if (temp.indexFromParent == 0) {
							if (temp.parent.b instanceof Integer) {
								temp.parent.b = (int) temp.parent.b + (int) currentRoot.b;
								break rightCheck;
							} else {
								// look for rightmost number
								OptionalPair temp2 = (OptionalPair) temp.parent.b;
								while (temp2.a instanceof OptionalPair) {
									temp2 = (OptionalPair) temp2.a;
								}
								temp2.a = (int) temp2.a + (int) currentRoot.b;
								break rightCheck;
							}
						} else {
							temp = temp.parent;
						}
					}

					// Set current pair to 0
					if (currentRoot.indexFromParent == 0) {
						currentRoot.parent.a = 0;
					} else if (currentRoot.indexFromParent == 1) {
						currentRoot.parent.b = 0;
					} else {
						throw new IllegalStateException("currentRoot not found in parent!");
					}

					continue out;
				}
				
				if (currentRoot.a instanceof OptionalPair && !checked.contains(currentRoot.a)) {
					if (depth < 4)
						checked.add((OptionalPair) currentRoot.a);

					depth++;
					currentRoot = (OptionalPair) currentRoot.a;
					continue;
				} else if (currentRoot.b instanceof OptionalPair && !checked.contains(currentRoot.b)) {
					if (depth < 4)
						checked.add((OptionalPair) currentRoot.b);

					depth++;
					currentRoot = (OptionalPair) currentRoot.b;
					continue;
				} else {
					checked.add(currentRoot);

					depth--;
					currentRoot = currentRoot.parent;
					continue;
				}
			}

			// Check split criteria
			currentRoot = this;
			checked = new ArrayList<>();

			while (currentRoot != null) {
				// Check left
				if (currentRoot.a instanceof Integer && ((int) currentRoot.a) >= 10) {
					currentRoot.a = new OptionalPair(currentRoot, 
							(int) (Math.floor(((int) currentRoot.a) / 2.0D)),
							(int) (Math.ceil (((int) currentRoot.a) / 2.0D)))
									.setIndex(0);
					
					continue out;
				}
				if (currentRoot.a instanceof OptionalPair && !checked.contains(currentRoot.a)) {
					checked.add((OptionalPair) currentRoot.a);
					currentRoot = (OptionalPair) currentRoot.a;
					continue;
				}

				// Check right
				if (currentRoot.b instanceof Integer && ((int) currentRoot.b) >= 10) {
					currentRoot.b = new OptionalPair(currentRoot, 
							(int) (Math.floor(((int) currentRoot.b) / 2.0D)),
							(int) (Math.ceil (((int) currentRoot.b) / 2.0D)))
									.setIndex(1);
					
					continue out;
				}

				if (currentRoot.b instanceof OptionalPair && !checked.contains(currentRoot.b)) {
					checked.add((OptionalPair) currentRoot.b);
					currentRoot = (OptionalPair) currentRoot.b;
					continue;
				}

				if (!checked.contains(currentRoot))
					checked.add(currentRoot);
				currentRoot = currentRoot.parent;
				continue;
			}

			break;
		}
	}

	public long getMagnitude() {
		long sum = 0L;
		if (this.a instanceof Integer)
			sum += 3 * (int) this.a;
		else
			sum += 3 * ((OptionalPair) this.a).getMagnitude();
		if (this.b instanceof Integer)
			sum += 2 * (int) this.b;
		else
			sum += 2 * ((OptionalPair) this.b).getMagnitude();
		return sum;
	}

	public OptionalPair copy() {
		OptionalPair ret = new OptionalPair(this.parent);
		ret.readIndex = this.readIndex;
		ret.indexFromParent = this.indexFromParent;
		if (this.a instanceof OptionalPair) {
			ret.a = ((OptionalPair) this.a).copy();
			((OptionalPair) ret.a).parent = ret;
		} else {
			ret.a = this.a;
		}
		if (this.b instanceof OptionalPair) {
			ret.b = ((OptionalPair) this.b).copy();
			((OptionalPair) ret.b).parent = ret;
		} else {
			ret.b = this.b;
		}

		return ret;
	}

	@Override
	public String toString() {
		return "[" + String.valueOf(a) + "," + String.valueOf(b) + "]";
	}

	@Override
	public Object clone() throws CloneNotSupportedException {
		return super.clone();
	}

	@Override
	public boolean equals(Object obj) {
		if (!(obj instanceof OptionalPair))
			return false;
		OptionalPair pair = (OptionalPair) obj;
		boolean ret = a.equals(pair.a) && 
					  b.equals(pair.b);
		if (!ret) return false;
		// are parents equal (w/o recursion)?
		if (parent == null && pair.parent == null) return true;
		if (parent == null || pair.parent == null) return false;
		int index = this.indexFromParent;
		if (index != pair.indexFromParent) return false;
		index ^= 1; // flip 0 to 1, vice versa
		return parent.hashCode() == pair.parent.hashCode();
	}
}

class Pair<T> extends Entry<T, T> {
	private static final long serialVersionUID = 1L;

	public Pair(T obj1, T obj2) {
		super(obj1, obj2);
	}

	public static <V> Pair<V> of(V obj1, V obj2) {
		return new Pair<V>(obj1, obj2);
	}

	@Override
	public boolean equals(Object obj) {
		return obj instanceof Pair && (((Pair<?>) obj).obj1 == this.obj1) && (((Pair<?>) obj).obj2 == this.obj2);
	}

	@Override
	public String toString() {
		return this.obj1.toString() + ", " + this.obj2.toString();
	}
}

class Entry<T, U> extends AbstractMap.SimpleEntry<T, U> {
	private static final long serialVersionUID = 10190290L;
	public T obj1;
	public U obj2;

	public Entry(T obj1, U obj2) {
		super(obj1, obj2);
		this.obj1 = obj1;
		this.obj2 = obj2;
	}

	@Override
	public boolean equals(Object obj) {
		if (obj instanceof Entry) {
			Entry<?, ?> p = (Entry<?, ?>) obj;
			return p.obj1.equals(this.obj1) && p.obj2.equals(this.obj2);
		} else if (obj instanceof Map.Entry) {
			Map.Entry<?, ?> p = (Map.Entry<?, ?>) obj;
			return p.getKey().equals(this.obj1) && p.getValue().equals(this.obj2);
		}
		return super.equals(obj);
	}

	@Override
	public U setValue(U value) {
		this.obj2 = value;
		return super.setValue(value);
	}
}

class OperatorPacket extends Packet {
	public final int MODE;

	public final List<Packet> subpackets = new ArrayList<>();

	public OperatorPacket(int v, int t, int mode) {
		super(v, t);
		this.MODE = mode;
	}

	/**
	 * @return the resulting string after parsing
	 */
	public String parseSubpackets(String binary) {
		if (this.MODE == 0) {
			String[] temp = AoC2021.splice(binary, 15);
			binary = temp[1];
			int totalLength = Integer.parseInt(temp[0], 2);
			temp = AoC2021.splice(binary, totalLength);
			binary = temp[1];

			String remaining = temp[0];
			while (remaining.length() > 0) {
				Entry<Packet, String> e = Packet.parse(remaining);
				subpackets.add(e.getKey());
				remaining = e.getValue();
			}

			return binary;
		} else {
			String[] temp = AoC2021.splice(binary, 11);
			binary = temp[1];
			int numOfSubpackets = Integer.parseInt(temp[0], 2);

			for (int i = 0; i < numOfSubpackets; i++) {
				Entry<Packet, String> e = Packet.parse(binary);
				subpackets.add(e.getKey());
				binary = e.getValue();
			}
			return binary;
		}
	}

	@Override
	public List<Packet> getPackets() {
		List<Packet> res = new ArrayList<>(Arrays.asList(this));
		for (Packet p : subpackets) {
			res.addAll(p.getPackets());
		}
		return res;
	}

	@Override
	public long getValue() {
		switch (this.TYPE) {
			case 0:
				return subpackets.stream().mapToLong(Packet::getValue).sum();
			case 1:
				return subpackets.stream().mapToLong(Packet::getValue).reduce(1, (a,b) -> (a*b));
			case 2:
				return subpackets.stream().mapToLong(Packet::getValue).min().orElseThrow();
			case 3:
				return subpackets.stream().mapToLong(Packet::getValue).max().orElseThrow();
			case 5:
				return Boolean.compare(subpackets.get(0).getValue() > subpackets.get(1).getValue(), false);
			case 6:
				return Boolean.compare(subpackets.get(0).getValue() < subpackets.get(1).getValue(), false);
			case 7:
				return Boolean.compare(subpackets.get(0).getValue() == subpackets.get(1).getValue(), false);
			default:
				throw new UnsupportedOperationException();
		}
	}
}

class LiteralPacket extends Packet {
	public static final int TYPE = 4;

	public long value = 0;

	public LiteralPacket(int v) {
		super(v, LiteralPacket.TYPE);
	}

	public LiteralPacket setValue(long val) {
		this.value = val;
		return this;
	}

	/**
	 * @return the resulting string after parsing
	 */
	public String setValue(String binary) {
		// System.out.println(binary);
		boolean shouldContinue = true;
		String values = "";
		while (shouldContinue) {
			String[] temp = AoC2021.splice(binary, 5);
			binary = temp[1];
			// System.out.println(binary);
			temp = AoC2021.splice(temp[0], 1);
			shouldContinue = (temp[0].equals("1"));
			values += temp[1];
			// System.out.println(values);
		}

		this.value = Long.parseLong(values, 2);
		// System.out.println(this.value);
		return binary;
	}

	@Override
	public long getValue() {
		return value;
	}
}

abstract class Packet {
	public final int VERSION;
	public final int TYPE;

	public Packet(int v, int t) {
		this.VERSION = v;
		this.TYPE = t;
	}

	public static Entry<Packet, String> parse(String binary) {
		String[] temp = AoC2021.splice(binary, 3);
		int version = Integer.parseInt(temp[0], 2);
		binary = temp[1];
		temp = AoC2021.splice(binary, 3);
		int type = Integer.parseInt(temp[0], 2);
		binary = temp[1];

		return newPacket(version, type, binary);
	}

	public static Entry<Packet, String> newPacket(int v, int t, String data) {
		if (t == LiteralPacket.TYPE) {
			LiteralPacket res = new LiteralPacket(v);
			String leftover = res.setValue(data);
			return new Entry<>(res, leftover);
		} else {
			String[] temp = AoC2021.splice(data, 1);
			OperatorPacket res = new OperatorPacket(v, t, Integer.parseInt(temp[0]));
			String leftover = res.parseSubpackets(temp[1]);
			return new Entry<>(res, leftover);
		}
	}

	@Override
	public String toString() {
		return "[PACKET] version: " + VERSION + "; type: " + TYPE + "; size: " + getPackets().size();
	}

	public List<Packet> getPackets() {
		return new ArrayList<>(Arrays.asList(this));
	}

	public abstract long getValue();
}

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
