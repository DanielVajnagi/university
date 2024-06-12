using System.Collections.Immutable;

namespace Main;

internal abstract class Program {
    public static void Main(string[] args) {
        Edition firstEdition = new(), secondEdition = new();
        
        Console.WriteLine($"Are the objects the same? {firstEdition == secondEdition}");
        Console.WriteLine($"Have the objects the same reference? {ReferenceEquals(firstEdition, secondEdition)}");
        
        Console.WriteLine($"First edition hash: {firstEdition.GetHashCode()}");
        Console.WriteLine($"Second edition hash: {secondEdition.GetHashCode()}");

        try {
            firstEdition.CirculationNumber = -342;
        } catch (Exception e) {
            Console.WriteLine(e + "\n");
        }

        Magazine magazine = new() {
            Name = "Forbes",
            PublicationFrequency = Frequency.Monthly,
            PublicationDate = new DateTime(2024, 02, 27),
            CirculationNumber = 235
        };

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
        
        magazine.AddEditors(
            new Person("Emmy", "Edison", new DateTime(1992, 10, 3)),
            new Person("Timothy", "Carlson", new DateTime(1983, 1, 12)),
            new Person("Helen", "Zuckerberg", new DateTime(1999, 9, 16)),
            authors[1]
        );
        
        Console.WriteLine(magazine);

        Magazine magazineCopy = (Magazine) magazine.DeepCopy();

        magazine.Name = "Times";
        magazine.PublicationDate = new DateTime(2024, 3, 1);
        magazine.CirculationNumber = 104;
        magazine.AddArticles(new Article());
        
        Console.WriteLine($"Original (changed): {magazine}");
        Console.WriteLine($"Copy: {magazineCopy}");
        
        Console.WriteLine("\nArticle with rating more than 4:");
        foreach (var article in magazineCopy.GetArticlesWithHigherRating(4)) {
            Console.WriteLine("- " + article);
        }
        
        Console.WriteLine("\nArticle with titles about Ukraine:");
        foreach (var article in magazineCopy.GetArticlesWithMatchedTitle("Ukraine")) {
            Console.WriteLine("- " + article);
        }
        
        Console.WriteLine("\nArticles where author is not editor:");
        foreach (var article in magazineCopy.GetArticlesWithNonEditorAuthor()) {
            Console.WriteLine("- " + article);
        }
        
        Console.WriteLine("\nArticles where author is editor:");
        foreach (var article in magazineCopy.GetArticlesWithEditorAuthor()) {
            Console.WriteLine("- " + article);
        }
        
        Console.WriteLine("\nEditors that do not have articles:");
        foreach (var editor in magazineCopy.GetEditorsWithoutArticles()) {
            Console.WriteLine("- " + editor);
        }
    }
}