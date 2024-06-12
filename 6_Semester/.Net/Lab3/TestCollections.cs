namespace Main;

public class TestCollections {
    private readonly List<Edition> _editions = [];
    private readonly List<string> _strings = [];
    private readonly Dictionary<Edition, Magazine> _editionsDict = [];
    private readonly Dictionary<string, Magazine> _stringsDict = [];
    
    private void GenerateCollections(int length) {
        Random rand = new();
        
        for (int i = 0; i < length; i++) {
            Edition edition = new($"Edition #{i}", DateTime.Now, rand.Next(100, 999));
            _editions.Add(edition);
            _strings.Add(edition.ToString());
            
            Magazine magazine = GenerateRandomMagazine();
            _editionsDict.Add(edition, magazine);
            _stringsDict.Add(edition.ToString(), magazine);
        }
    }

    public static Magazine GenerateRandomMagazine() {
        Random rand = new();
        
        return new Magazine() {
            Name = $"Magazine #{Guid.NewGuid().ToString()}",
            PublicationFrequency = (Frequency) rand.Next(3),
            PublicationDate = DateTime.Now,
            CirculationNumber = rand.Next(100, 999)
        };
    }

    public TestCollections(int length) {
        GenerateCollections(length);
    }

   public void Benchmarks() {
        Edition another = new("Another Edition", DateTime.Now, 1234);
        
        Console.WriteLine("Editions list:");
        MeasureTime("First", () => _editions.FirstOrDefault());
        MeasureTime("Middle", () => _editions.ElementAt(_editions.Count / 2));
        MeasureTime("Last", () => _editions.LastOrDefault());
        MeasureTime("Not listed", () => _editions.Contains(another));

        Console.WriteLine("Strings list:");
        MeasureTime("First", () => _strings.FirstOrDefault());
        MeasureTime("Middle", () => _strings.ElementAt(_strings.Count / 2));
        MeasureTime("Last", () => _strings.LastOrDefault());
        MeasureTime("Not listed", () => _strings.Contains(another.ToString()));

        Console.WriteLine("Editions dictionary:");
        MeasureTime("First", () => _editionsDict.FirstOrDefault().Value);
        MeasureTime("Middle", () => _editionsDict.ElementAt(_editions.Count / 2).Value);
        MeasureTime("Last", () => _editionsDict.LastOrDefault().Value);
        MeasureTime("Not listed", () => _editionsDict.ContainsKey(another));

        Console.WriteLine("Strings dictionary");
        MeasureTime("First", () => _stringsDict.FirstOrDefault().Value);
        MeasureTime("Middle", () => _stringsDict.ElementAt(_strings.Count / 2).Value);
        MeasureTime("Last", () => _stringsDict.LastOrDefault().Value);
        MeasureTime("Not listed", () => _stringsDict.ContainsKey(another.ToString()));
    }

    private static void MeasureTime<T>(string operation, Func<T> action) {
        Console.Write($"Time to find {operation}: ");
        
        DateTime startTime = DateTime.Now;
        T _ = action();
        DateTime endTime = DateTime.Now;
        
        TimeSpan elapsedTime = endTime - startTime;
        Console.WriteLine($"{elapsedTime.TotalMilliseconds} ms");
    }
}