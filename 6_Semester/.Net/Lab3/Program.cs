using System.Text;

namespace Main;

internal abstract class Program {
    public static string PrintCollection(IEnumerable<Magazine> collection) {
        StringBuilder sb = new();
        
        foreach (var item in collection) {
            sb.Append(item.ToShortString() + '\n');
        }
        
        return sb.ToString();
    }
    
    public static void Main(string[] args) {
        MagazineCollection magazineCollection = new();
        magazineCollection.AddDefaults();
        
        Console.WriteLine("============ Sorting ============");
        
        magazineCollection.SortByName();
        Console.WriteLine("Sort by name: \n" + magazineCollection.ToShortString());
        
        magazineCollection.SortByPublicationDate();
        Console.WriteLine("Sort by publication date: \n" + magazineCollection.ToShortString());
        
        magazineCollection.SortByCirculation();
        Console.WriteLine("Sort by circulation: \n" + magazineCollection.ToShortString());
        
        Console.WriteLine("============ LINQ operations ============");
        
        Console.WriteLine("Max average rating: " + magazineCollection.MaxRating);
        Console.WriteLine("Magazines with monthly frequency: \n" + PrintCollection(magazineCollection.MonthlyMagazines));
        Console.WriteLine("Rating groups: " + PrintCollection(magazineCollection.RatingGroup(4)));
        
        Console.WriteLine("============ Benchmarks ============");
        
        TestCollections testCollections = new(10_000);
        testCollections.Benchmarks();
    }
}