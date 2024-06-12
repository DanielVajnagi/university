using System.Collections.Immutable;

namespace Main;

internal abstract class Program {
    public static void Main(string[] args) {
        TestArrays();
        TestMagazine();
    }

    private static int CountJaggedArrayElements<T>(T[][] jaggedArray) {
        int numberOfElements = 0;

        for (var i = 0; i < jaggedArray.Length; i++) {
            numberOfElements += jaggedArray[i].Length;
        }
        
        return numberOfElements;
    }
    
    private static void TestArrays() { 
        Console.WriteLine("====== Arrays =====");
        
        /* Read user input */
        Console.Write("Please, input array size (two numbers split with space, comma or semicolon): ");
        string? readText = Console.ReadLine();
        if (readText is null) return;
        
        /* Get size */
        int[] sizes = Array.ConvertAll(readText.Split([' ', ',', ';']), int.Parse);
        int nRows = sizes[0], nColumns = sizes[1];
        
        /* Create arrays */
        
        /* One dimensional array */
        Article[] simpleArray = new Article[nRows * nColumns];
        for (var i = 0; i < nRows * nColumns; i++) {
            simpleArray[i] = new Article();
        }
        
        /* 2D rectangular array (matrix) */
        Article[,] rectangularArray = new Article[nRows, nColumns];
        for (var i = 0; i < nRows; i++) {
            for (var j = 0; j < nColumns; j++) {
                rectangularArray[i, j] = new Article();
            }
        }
        
        /* Jagged array
         * 
         * To calculate the initial length, we have to do some math:
         * The sum of the first n positive integers: S = n * (n + 1) / 2;
         * `S` value must be less than or equal to nRows * nColumns: S <= nRows * nColumns;
         * n * (n + 1) / 2 <= nRows * nColumns;
         * n^2 + n <= 2 * nRows * nColumns;
         * 
         * Quadratic equation: n^2 + n - 2 * nRows * nColumns = 0;
         * Discriminant: D = 1^2 - 4 * 1 * (-2 * nRows * nColumns) = 1 + 8 * nRows * nColumns;
         * n = round((-1 + sqrt(D)) / 2) - the upper bound of the number n, round to the nearest integer.
         */
        int discriminant = 1 + 8 * nRows * nColumns;
        int initialLength = (int) Math.Round((-1 + Math.Sqrt(discriminant)) / 2);
        
        Article[][] jaggedArray = new Article[initialLength][];
        int numberOfElements = 0;

        for (var i = 0; i < initialLength; i++) {
            int innerArraySize = (i != initialLength - 1) ? i + 1 : nRows * nColumns - numberOfElements;
            jaggedArray[i] = new Article[innerArraySize];
            numberOfElements += i + 1;

            for (var j = 0; j < innerArraySize; j++) {
                jaggedArray[i][j] = new Article();
            }
        }

        /* Comparison of operations execution time */
        
        int simpleArrayStart = Environment.TickCount;
        for (var i = 0; i < simpleArray.Length; i++) {
            simpleArray[i].Rating = 5;
        }
        int simpleArrayEnd = Environment.TickCount;
        Console.WriteLine($"Time for the one dimensional array ({simpleArray.Length}): {simpleArrayEnd - simpleArrayStart} ms");
        
        int rectangularArrayStart = Environment.TickCount;
        for (var i = 0; i < rectangularArray.GetLength(0); i++) {
            for (var j = 0; j < rectangularArray.GetLength(1); j++) {
                rectangularArray[i, j].Rating = 5;
            }
        }
        int rectangularArrayEnd = Environment.TickCount;
        Console.WriteLine($"Time for the rectangular array ({nRows}x{nColumns}): {rectangularArrayEnd - rectangularArrayStart} ms");
        
        int jaggedArrayStart = Environment.TickCount;
        for (var i = 0; i < jaggedArray.Length; i++) {
            for (var j = 0; j < jaggedArray[i].Length; j++) {
                jaggedArray[i][j].Rating = 5;
            }
        }
        int jaggedArrayEnd = Environment.TickCount;
        Console.WriteLine($"Time for the jagged array ({CountJaggedArrayElements(jaggedArray)}): {jaggedArrayEnd - jaggedArrayStart} ms");
    }

    private static void TestMagazine() {
        Console.WriteLine("\n====== Magazine ======");
        Magazine magazine = new Magazine();
        
        Console.WriteLine(magazine.ToShortString() + "\n");
        
        Console.WriteLine("Indexer:");
        Console.WriteLine($"magazine[Frequency.Weekly] = {magazine[Frequency.Weekly]};");
        Console.WriteLine($"magazine[Frequency.Monthly] = {magazine[Frequency.Monthly]};");
        Console.WriteLine($"magazine[Frequency.Yearly] = {magazine[Frequency.Yearly]};\n");
 
        magazine.Name = "Forbes";       
        magazine.PublicationFrequency = Frequency.Monthly;
        magazine.PublicationDate = new DateTime(2024, 02, 17);
        magazine.CirculationNumber = 235;
        
        Console.WriteLine(magazine);  // Method ToString() is calling explicitly
        
        ImmutableArray<Person> authors = [
            new Person("Alison", "Durkee", new DateTime(1990, 2, 15)),
            new Person("Javier", "Paz", new DateTime(1995, 10, 11)),
            new Person("Hank", "Tucker", new DateTime(1983, 9, 16)),
        ];
        
        magazine.AddArticles(
            new Article(authors[0], "Senate Passes $95 Billion Aid Bill For Ukraine And Israel", 4.9),
            new Article(authors[1], "What Is The Future Of Bitcoin Futures?", 3.1),
            new Article(authors[2], "The Future Of Wall Street And Enterprise: Fintech 50 2024", 4.4)
        );
        
        Console.WriteLine(magazine);    
    }
}