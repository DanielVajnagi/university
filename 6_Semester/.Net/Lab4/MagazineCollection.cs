using System.Text;
using System.Collections.Immutable;

namespace Main;

public class MagazineCollection {
    private List<Magazine> _magazines = [];
    public List<Magazine> Magazines { get => _magazines; }
    
    public double MaxRating {
        get {
            if (Magazines.Count == 0 || Magazines is null) return 0;
            return Magazines.Max(magazine => magazine.Rating);
        }
    }

    public IEnumerable<Magazine> MonthlyMagazines {
        get {
            return Magazines.Where(magazine => magazine.PublicationFrequency == Frequency.Monthly);
        }
    }

    public List<Magazine> RatingGroup(double value) {
        return Magazines.GroupBy(magazine => magazine.Rating >= value)
            .Where(g => g.Key)
            .Select(g => g.ToList())
            .LastOrDefault() ?? [];
    }

    public void AddDefaults() {
        ImmutableArray<Person> authors = [
            new Person("Alison", "Durkee", new DateTime(1990, 2, 15)),
            new Person("Javier", "Paz", new DateTime(1995, 10, 11)),
            new Person("Hank", "Tucker", new DateTime(1983, 9, 16)),
        ];
        
        for (int i = 0; i < 2; i++) {
            Magazine magazine = new Magazine($"Magazine #{i}", Frequency.Monthly, DateTime.Now, i);
            
            magazine.AddArticles([
                new Article(new Person(), $"Article #{i}", new Random().Next(1, 6))
            ]);
            
            Magazines.Add(magazine);
        }
        
        Magazine forbes = new() {
            Name = "Forbes",
            PublicationFrequency = Frequency.Yearly,
            PublicationDate = new DateTime(2024, 02, 27),
            CirculationNumber = 235
        };
        
        forbes.AddArticles(
            new Article(authors[0], "Senate Passes $95 Billion Aid Bill For Ukraine And Israel", 4.9),
            new Article(authors[1], "What Is The Future Of Bitcoin Futures?", 3.1),
            new Article(authors[2], "The Future Of Wall Street And Enterprise: Fintech 50 2024", 4.4)
        );
        
        Magazines.Add(forbes);
        Magazines.Add(new Magazine());
    }
    
    public void AddMagazines(params Magazine[] magazines) {
        foreach (var magazine in magazines) {
            Magazines.Add(magazine);
        }
    }

    public void SortByName() {
        Magazines.Sort((x, y) => x.CompareTo(y));
    }
    
    public void SortByPublicationDate() {
        Magazines.Sort((x, y) => x.Compare(x, y));
    }

    public void SortByCirculation() {
        EditionCirculationComparer comparer = new();
        Magazines.Sort((x, y) => comparer.Compare(x, y));
    }
    
    public override string ToString() {
        StringBuilder text = new StringBuilder();
        
        if (Magazines is null || Magazines.Count == 0) return text.ToString();

        foreach (var magazine in Magazines) { 
            text.Append($"Magazine:\n{magazine}");   
        }
        
        return text.ToString();
    }
    
    public string ToShortString() {
        StringBuilder text = new StringBuilder();
        
        if (Magazines is null || Magazines.Count == 0) return text.ToString();

        foreach (var magazine in Magazines) { 
            text.Append($"Magazine:\n{magazine.ToShortString()}");   
        }
        
        return text.ToString();
    }
}