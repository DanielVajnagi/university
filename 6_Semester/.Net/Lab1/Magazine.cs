using System.Text;

namespace Main;

public class Magazine {
    private string _name = default!;
    private Frequency _frequency; 
    private DateTime _publicationDate;
    private int _circulationNumber;
    private Article[] _articles = default!;

    public string Name { get => _name; set => _name = value; }
    public Frequency PublicationFrequency { get => _frequency; set => _frequency = value; }
    public DateTime PublicationDate { get => _publicationDate; set => _publicationDate = value; }
    public int CirculationNumber { get => _circulationNumber; set => _circulationNumber = value; }
    public Article[] Articles { get => _articles; private set => _articles = value; }

    public double OverallRating {
        get {
            if (Articles is null || Articles.Length == 0) return 0;

            double totalRating = 0;
            foreach (var article in Articles) {
                totalRating += article.Rating;
            }
            
            return totalRating / Articles.Length;
        }
    }

    public bool this[Frequency idx] => idx == PublicationFrequency;

    public Magazine(string name, Frequency frequency, DateTime publicationDate, int circulationNumber) {
        Name = name;
        PublicationFrequency = frequency;
        PublicationDate = publicationDate;
        CirculationNumber = circulationNumber;
        Articles = Array.Empty<Article>();
    }
    
    public Magazine() : this("Famous Magazine", Frequency.Monthly, DateTime.Today, 1) { }

    public void AddArticles(params Article[] articles) {
        if (articles is null || articles.Length == 0) return;

        if (Articles is null || Articles.Length == 0) {
            Articles = articles;
            return;
        }
        
        Article[] newArticles = new Article[Articles.Length + articles.Length];
        Articles.CopyTo(newArticles, 0);
        articles.CopyTo(newArticles, Articles.Length);

        Articles = newArticles;
    }
    
    public override string ToString() {
        StringBuilder text = new StringBuilder($"The {PublicationFrequency.ToString().ToLower()} magazine \"{Name}\" ");
        text.Append($"№{CirculationNumber}. Date: {PublicationDate}.\n");

        if (Articles is null || Articles.Length == 0) return text.ToString();
        
        text.Append("List of articles:\n");
        
        foreach (var article in Articles) {
            text.Append($"\t- {article}\n");
        }
        
        return text.ToString();
    }

    public string ToShortString() {
        StringBuilder text = new StringBuilder($"The {PublicationFrequency.ToString().ToLower()} magazine \"{Name}\" ");
        text.Append($"№{CirculationNumber}. Date: {PublicationDate}. ");

        if (OverallRating == 0) return text.ToString();
        text.Append($"Rating: {Math.Round(OverallRating, 2)}.");

        return text.ToString();
    }
}