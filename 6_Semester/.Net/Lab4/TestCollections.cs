using System.Collections.Immutable;

namespace Main;

public class TestCollections {
    private readonly List<Edition> _list = [];
    private readonly Dictionary<Edition, Magazine> _dict = [];
    
    private readonly SortedList<Edition, Magazine> _sortedList = [];
    private readonly SortedDictionary<Edition, Magazine> _sortedDict = [];
    
    private ImmutableList<Edition> _immutableList = [];
    private ImmutableDictionary<Edition, Magazine> _immutableDict = ImmutableDictionary<Edition, Magazine>.Empty;

    
    private void GenerateCollections(int length) {
        Random rand = new();
        
        var immutableListBuilder = ImmutableList.CreateBuilder<Edition>();
        var immutableDictBuilder = ImmutableDictionary.CreateBuilder<Edition, Magazine>();
        
        for (int i = 0; i < length; i++) {
            Edition edition = new($"Edition #{i}", DateTime.Now, rand.Next(100, 999));
            Magazine magazine = GenerateRandomMagazine();
            
            _list.Add(edition);
            _sortedList.Add(edition, magazine);
            
            _dict.Add(edition, magazine);
            _sortedDict.Add(edition, magazine);
            
            immutableListBuilder.Add(edition);
            immutableDictBuilder.Add(edition, magazine);
        }

        _immutableList = immutableListBuilder.ToImmutable();
        _immutableDict = immutableDictBuilder.ToImmutable();
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
        
        Console.WriteLine("List:");
        MeasureTime("First", () => _list.FirstOrDefault());
        MeasureTime("Middle", () => _list.ElementAt(_list.Count / 2));
        MeasureTime("Last", () => _list.LastOrDefault());
        MeasureTime("Not listed", () => _list.Contains(another));
        
        Console.WriteLine("Immutable List:");
        MeasureTime("First", () => _immutableList.FirstOrDefault());
        MeasureTime("Middle", () => _immutableList.ElementAt(_immutableList.Count / 2));
        MeasureTime("Last", () => _immutableList.LastOrDefault());
        MeasureTime("Not listed", () => _immutableList.Contains(another));
        
        Console.WriteLine("Sorted List:");
        MeasureTime("First", () => _sortedList.FirstOrDefault().Value);
        MeasureTime("Middle", () => _sortedList.ElementAt(_sortedList.Count / 2).Value);
        MeasureTime("Last", () => _sortedList.LastOrDefault().Value);
        MeasureTime("Not listed", () => _sortedList.ContainsKey(another));

        Console.WriteLine("Dictionary:");
        MeasureTime("First", () => _dict.FirstOrDefault().Value);
        MeasureTime("Middle", () => _dict.ElementAt(_dict.Count / 2).Value);
        MeasureTime("Last", () => _dict.LastOrDefault().Value);
        MeasureTime("Not listed", () => _dict.ContainsKey(another));
        
        Console.WriteLine("Immutable Dictionary:");
        MeasureTime("First", () => _immutableDict.FirstOrDefault().Value);
        MeasureTime("Middle", () => _immutableDict.ElementAt(_immutableDict.Count / 2).Value);
        MeasureTime("Last", () => _immutableDict.LastOrDefault().Value);
        MeasureTime("Not listed", () => _immutableDict.ContainsKey(another));
        
        Console.WriteLine("Sorted Dictionary:");
        MeasureTime("First", () => _sortedDict.FirstOrDefault().Value);
        MeasureTime("Middle", () => _sortedDict.ElementAt(_sortedDict.Count / 2).Value);
        MeasureTime("Last", () => _sortedDict.LastOrDefault().Value);
        MeasureTime("Not listed", () => _sortedDict.ContainsKey(another));
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