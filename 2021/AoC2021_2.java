import java.io.*;
import java.util.*;
import java.util.function.*;
import java.util.stream.*;
import java.math.*;

public class AoC2021_2
{
	public static void main(String[] args) {
		long startTime = System.currentTimeMillis();
		System.out.println(day21p2());
		long endTime = System.currentTimeMillis();

		System.out.println("Elapsed: " + (endTime - startTime) + "ms.");
	}

	public static long day21p2() {
		Scanner sc = new Scanner(System.in);

		List<Map<Pair<Integer>, Long>> pos_scores = new ArrayList<>();
		pos_scores.add(new HashMap<>());
		pos_scores.add(new HashMap<>());
		System.out.print("P1 start: ");
		pos_scores.get(0).put(Pair.of(sc.nextInt(), 0), 1L);

		System.out.print("P2 start: ");
		pos_scores.get(1).put(Pair.of(sc.nextInt(), 0), 1L);

		sc.close();

		long[] playerWins = new long[2];

		int currentPlayer = 0;

		// After each roll, the frequencies are multipled by this
		Map<Integer, Long> BELL_CURVE = new HashMap<>();
		for (int i = 1; i <= 3; i++) {
			for (int j = 1; j <= 3; j++) {
				for (int k = 1; k <= 3; k++) {
					BELL_CURVE.put(i + j + k, BELL_CURVE.getOrDefault(i + j + k, 0L) + 1);
				}
			}
		}

		for (Map.Entry<Integer, Long> bc : BELL_CURVE.entrySet())
			System.out.println(bc);

		do {
			System.out.println("Player " + currentPlayer);
			Map<Pair<Integer>, Long> tempPosScores = new HashMap<>();
			for (Map.Entry<Pair<Integer>, Long> e : pos_scores.get(currentPlayer).entrySet()) {
				System.out.println("Initial value: (" + e.getKey() + ") - " + e.getValue());
				for (Map.Entry<Integer, Long> bc : BELL_CURVE.entrySet()) {
					int posToPut = ((e.getKey().obj1 - 1 + bc.getKey()) % 10) + 1;
					long valToPut = e.getValue() * bc.getValue();

					Pair<Integer> retKey = Pair.of(posToPut, e.getKey().obj2+posToPut);
					long retVal = tempPosScores.getOrDefault(posToPut, 0L) + valToPut;

					System.out.println(bc.getKey() + ": (" + retKey + ") - " + retVal);

					tempPosScores.put(retKey, retVal);
				}
			}

			pos_scores.set(currentPlayer, tempPosScores);

			// Check whether this player's turn has just made them win
			Iterator<Map.Entry<Pair<Integer>, Long>> it = pos_scores.get(currentPlayer).entrySet().iterator();
			while (it.hasNext()) {
				Map.Entry<Pair<Integer>, Long> entry = it.next();
				int score = entry.getKey().obj2;
				long universes = entry.getValue();

				if (score >= 21) {
					// Add up all of the universes of the other player
					long otherPlayerUniverses = pos_scores.get(currentPlayer^1).values().stream().reduce(0L, Long::sum);
					playerWins[currentPlayer] += universes * otherPlayerUniverses;

					it.remove();
				}
			}

			currentPlayer ^= 1;
		} while (!pos_scores.get(0).isEmpty() && !pos_scores.get(1).isEmpty());

		System.out.println(playerWins[0] + " + " + playerWins[1] + " = " + (playerWins[0] + playerWins[1]));
		return Math.max(playerWins[0], playerWins[1]);
	}

	public static long day21p1() {
		Scanner sc = new Scanner(System.in);

		int[] poses = new int[2];
		System.out.print("P1 start: ");
		poses[0] = sc.nextInt();

		System.out.print("P2 start: ");
		poses[1] = sc.nextInt();

		sc.close();

		int[] scores = new int[2];
		int diceRolls = 0;

		int currentDice = 1;
		int currentPlayer = 0;

		while (scores[0] < 1000 && scores[1] < 1000) {
			int toAdd = 0;
			for (int i = 0; i < 3; i++) {
				toAdd += currentDice++;
				if (currentDice > 100) currentDice = 1;

				diceRolls++;
			}

			poses[currentPlayer] = ((poses[currentPlayer] - 1 + toAdd) % 10) + 1;
			scores[currentPlayer] += poses[currentPlayer];

			currentPlayer ^= 1;
		}

		return Math.min(scores[0], scores[1]) * (long) diceRolls;
	}

	public static long day20() {
		try {
			File f = new File("/Users/colinwong/Downloads/input.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);
			
			int[] enhance = Arrays.stream(sc.nextLine().split(""))
					.mapToInt(c -> c.equals("#") ? 1 : 0)
					.toArray();
			System.out.println("Enhancement string length: " + enhance.length);

			sc.nextLine();

			int[][] img = new int[200][200];

			for (int i = 0; i < 100; i++) {
				String str = sc.nextLine();
				for (int j = 0; j < 100; j++) {
					img[i+50][j+50] = str.charAt(j) == '#' ? 1 : 0;
				}
			}

			sc.close();

			// System.out.println(Arrays.deepToString(img).replace("[[", "").replace("]]", "").replace("], [", "\n").replace(", ", ""));
			// System.out.println();

			int boundaryDefault = 0;

			// Change step for p1/2
			for (int step = 1; step <= 2; step++) {
				int[][] newImg = new int[img.length][img[0].length];
				for (int i = 0; i < img.length; i++) {
					for (int j = 0; j < img[i].length; j++) {
						String enhanceIndex = "";
						for (int m = -1; m <= 1; m++) {
							for (int n = -1; n <= 1; n++) {
								try {
									enhanceIndex += img[i+m][j+n];
								} catch (ArrayIndexOutOfBoundsException e) {
									enhanceIndex += boundaryDefault;
								}
							}
						}

						newImg[i][j] = enhance[Integer.parseInt(enhanceIndex, 2)];
					}
				}

				img = newImg;
				boundaryDefault ^= 1;

				System.out.println("Step " + step + ":");
				// System.out.println(Arrays.deepToString(img).replace("[[", "").replace("]]", "").replace("], [", "\n").replace(", ", ""));
			}

			return Arrays.stream(img).flatMapToInt(Arrays::stream).filter(i -> i == 1).count();
		} catch (FileNotFoundException e) {
			return -1L;
		}
	}

	public static long day19p1() {
		try {
			File f = new File("/Users/colinwong/Downloads/input_example.txt");
			System.out.println(f.getAbsolutePath());
			Scanner sc = new Scanner(f);
			List<Coords3DList> scannerPoses = new ArrayList<>();
			List<Coords3DList> scannerRel = new ArrayList<>();

			Coords3DList currentScanner = null;
			long beaconCount = 0L;

			while (sc.hasNextLine()) {
				String s = sc.nextLine();
				if (s.equals("quit"))
					break;
				if (s.isEmpty())
					continue;

				if (s.startsWith("---")) {
					if (currentScanner != null) {
						scannerPoses.add(currentScanner);
						beaconCount += currentScanner.size();
					}
					currentScanner = new Coords3DList();
					s = s.replace("---", "").replace("scanner", "").trim();

					continue;
				}

				currentScanner.add(Coords3D.of(Arrays.stream(s.split(",")).mapToInt(Integer::parseInt).toArray()));
			}

			// add last one
			if (!scannerPoses.contains(currentScanner)) {
				scannerPoses.add(currentScanner);
				beaconCount += currentScanner.size();
			}

			System.out.println(beaconCount);
			sc.close();

			long totalRels = 0L;
			for (Coords3DList scanner : scannerPoses) {
				Coords3DList scannerRels = new Coords3DList();

				// get pair of beacons
				for (int i = 0; i < scanner.size(); i++) {
					for (int j = i + 1; j < scanner.size(); j++) {
						Coords3D beacon1 = scanner.get(i);
						Coords3D beacon2 = scanner.get(j);

						scannerRels.add(Coords3D.of(
							beacon1.x - beacon2.x, 
							beacon1.y - beacon2.y, 
							beacon1.z - beacon2.z));
						scannerRels.add(Coords3D.of(
							beacon2.x - beacon1.x, 
							beacon2.y - beacon1.y, 
							beacon2.z - beacon1.z));
					}
				}

				scannerRel.add(scannerRels);
				totalRels += scannerRels.size();
			}

			System.out.println(scannerRel.size() + " relative scanner lists");
			System.out.println(totalRels + " total relations");

			Map<Pair<Integer>, Integer> sizes = new HashMap<>();
			long common = 0L;
			for (int i = 0; i < scannerRel.size(); i++) {
				for (int j = i + 1; j < scannerRel.size(); j++) {
					System.out.println(i + " " + j);
					Coords3DList scannerRels1 = new Coords3DList(scannerRel.get(i));
					Coords3DList scannerRels2 = new Coords3DList(scannerRel.get(j));

					scannerRels1.retainAll(scannerRels2);
					common += scannerRels1.size();
					if (scannerRels1.size() > 0)
						sizes.put(Pair.of(i, j), scannerRels1.size());
				}
			}

			sizes.entrySet().stream()
					.filter(e -> e.getValue() >= 132)
					.flatMap(e -> Stream.of(e, new Entry<>(Pair.of(e.getKey().getValue(), e.getKey().getKey()), e.getValue())))
					.sorted((c1, c2) -> Integer.compare(c1.getKey().getKey(), c2.getKey().getKey()))
					.forEach(entry -> {
						System.out.println(
							"("+entry.getKey().getKey()+","+entry.getKey().getValue()+"): "+entry.getValue()
						);
					});
			long totalOver12 = sizes.values().stream()
					.filter(i -> i >= 132)
					.mapToInt(i -> (int) Math.ceil(Math.sqrt(i))).sum();
			long count = sizes.values().stream()
					.filter(i -> i >= 132)
					.count();
			System.out.println(beaconCount+"-"+totalOver12+"("+count+")="+(beaconCount-totalOver12));
			return common;
		} catch (FileNotFoundException e) {
			return -1L;
		}
	}

	public static String[] splice(String str, int numOfChars) {
		return new String[]{ 
			str.substring(0, numOfChars), 
			str.substring(numOfChars) 
		};
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

	public static <V, K> Map<V, K> invert(Map<K, V> map) {
		return map.entrySet().stream().collect(Collectors.toMap(Map.Entry::getValue, Map.Entry::getKey));
	}
}

// Utility

class Coords3D {
	int x;
	int y;
	int z;

	public static final Function<Coords3D, List<Coords3D>> ROTATIONS = (coords) -> Arrays.asList(
			Coords3D.of(coords.x,coords.y,coords.z),
			Coords3D.of(coords.x,-coords.y,-coords.z),
			Coords3D.of(coords.x,coords.z,-coords.y),
			Coords3D.of(coords.x,-coords.z,coords.y),
			Coords3D.of(-coords.x,coords.y,-coords.z),
			Coords3D.of(-coords.x,-coords.y,coords.z),
			Coords3D.of(-coords.x,coords.z,coords.y),
			Coords3D.of(-coords.x,-coords.z,-coords.y),
			Coords3D.of(coords.y,coords.x,-coords.z),
			Coords3D.of(coords.y,-coords.x,coords.z),
			Coords3D.of(coords.y,coords.z,coords.x),
			Coords3D.of(coords.y,-coords.z,-coords.x),
			Coords3D.of(-coords.y,coords.x,coords.z),
			Coords3D.of(-coords.y,-coords.x,-coords.z),
			Coords3D.of(-coords.y,coords.z,-coords.x),
			Coords3D.of(-coords.y,-coords.z,coords.x),
			Coords3D.of(coords.z,coords.y,-coords.x),
			Coords3D.of(coords.z,-coords.y,coords.x),
			Coords3D.of(coords.z,coords.x,coords.y),
			Coords3D.of(coords.z,-coords.x,-coords.y),
			Coords3D.of(-coords.z,coords.y,coords.x),
			Coords3D.of(-coords.z,-coords.y,-coords.x),
			Coords3D.of(-coords.z,coords.x,-coords.y),
			Coords3D.of(-coords.z,-coords.x,coords.y)
		);

	public Coords3D(int x, int y, int z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}

	public static Coords3D of(int x, int y, int z) {
		return new Coords3D(x, y, z);
	}

	public static Coords3D of(int[] vals) {
		if (vals.length < 3) throw new IllegalArgumentException("invalid array length for Coords3D: " + vals.length);
		return new Coords3D(vals[0], vals[1], vals[2]);
	}

	@Override
	public boolean equals(Object obj) {
		return (obj instanceof Coords3D)
				&& this.x == ((Coords3D) obj).x
				&& this.y == ((Coords3D) obj).y
				&& this.z == ((Coords3D) obj).z;
	}

	public boolean equalsWithRotation(Object obj){
		if (!(obj instanceof Coords3D)) return false;
		Coords3D coords = (Coords3D) obj;
		return ROTATIONS.apply(this).contains(coords);// || ROTATIONS.apply(coords).contains(this);
	}

	@Override
	public String toString() {
		return "(" + x + ", " + y + ", " + z + ")";
	}
}

class Coords3DList extends ArrayList<Coords3D> {
	private static final long serialVersionUID = 1L;

	public Coords3DList() {
		super();
	}

	public Coords3DList(Coords3DList coords3dList) {
		super(coords3dList);
	}

	@Override
	public int indexOf(Object o) {
		Object[] es = toArray();
		if (o == null) {
			for (int i = 0; i < size(); i++) {
				if (es[i] == null) {
					return i;
				}
			}
		} else {
			for (int i = 0; i < size(); i++) {
				if (((Coords3D) o).equalsWithRotation(es[i])) {
					return i;
				}
			}
		}
		return -1;
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
		return "(" + this.obj1.toString() + ", " + this.obj2.toString() + ")";
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
