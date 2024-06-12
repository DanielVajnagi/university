using System.Collections;
using System.Text;

namespace Main;

public class Magazine : Edition, IRateAndCopy {
    private Frequency _frequency;
    private List<Person> _editors = default!;
    private List<Article> _articles = default!; 
    
    public Frequency PublicationFrequency { get => _frequency; init => _frequency = value; }
    public List<Person> Editors { get => _editors; private init => _editors = value; }
    public List<Article> Articles { get => _articles; private init => _articles = value; }

    public Edition Edition {
        get => new Edition(Name, PublicationDate, CirculationNumber);
        init {
            Name = value.Name;
            PublicationDate = value.PublicationDate;
            CirculationNumber = value.CirculationNumber;
        }
    }

    public double Rating {
        get {
            if (Articles is null || Articles.Count == 0) return 0;

            double totalRating = 0;
            foreach (var article in Articles) {
                totalRating += ((Article) article).Rating;
            }
            
            return totalRating / Articles.Count;
        }
    }

    public bool this[Frequency idx] => idx == PublicationFrequency;

    public Magazine(string name, Frequency frequency, DateTime publicationDate, int circulationNumber) 
            : base(name, publicationDate, circulationNumber) {
        PublicationFrequency = frequency;
        Editors = new List<Person>();
        Articles = new List<Article>();
    }
    
    public Magazine() : this("Famous Magazine", Frequency.Monthly, DateTime.Today, 1) { }

    public void AddArticles(params Article[] articles) {
        foreach (var article in articles) {
            Articles.Add(article);   
        }
    }
    
    public void AddEditors(params Person[] editors) {
        foreach (var editor in editors) {
            Editors.Add(editor);   
        }
    }
    
    public override string ToString() {
        StringBuilder text = new StringBuilder($"The {PublicationFrequency.ToString().ToLower()} magazine \"{Name}\" ");
        text.Append($"№{CirculationNumber}. Date: {PublicationDate}.\n");

        if (Articles is null || Articles.Count == 0) return text.ToString();
        
        text.Append("List of articles:\n");
        foreach (Article article in Articles) {
            text.Append($"\t- {article}\n");
        }

        if (Editors is null || Editors.Count == 0) return text.ToString();
        
        text.Append("List of editors:\n");
        foreach (Person editor in Editors) {
            text.Append($"\t- {editor}\n");
        }
        
        return text.ToString();
    }

    public string ToShortString() {
        StringBuilder text = new StringBuilder($"The {PublicationFrequency.ToString().ToLower()} magazine \"{Name}\" ");
        text.Append($"№{CirculationNumber}. Date: {PublicationDate}. ");
        text.Append($"Rating: {Rating}.");

        return text.ToString();
    }
    
    public override bool Equals(object? obj) {
        if (obj == null || obj is not Magazine)
            return false;
        
        Magazine magazine = (Magazine) obj;

        bool articlesAreTheSame = true;
        bool articlesExists = magazine.Articles is not null && Articles is not null;
        
        if (articlesExists && magazine.Articles.Count != Articles.Count) {
            for (int i = 0; i < Articles.Count; i++) {
                if (magazine.Articles[i] != Articles[i]) {
                    articlesAreTheSame = false;
                    break;
                }
            }
        }
        
        bool editorsAreTheSame = true;
        bool editorsExists = magazine.Editors is not null && Editors is not null;
        
        if (editorsExists && magazine.Editors.Count != Editors.Count) {
            for (int i = 0; i < Editors.Count; i++) {
                if (magazine.Editors[i] != Editors[i]) {
                    editorsAreTheSame = false;
                    break;
                }
            }
        }

        return magazine.Name == Name &&
               magazine.PublicationFrequency == PublicationFrequency && 
               magazine.PublicationDate == PublicationDate &&
               magazine.CirculationNumber == CirculationNumber &&
               articlesAreTheSame && editorsAreTheSame;
    }
    
    public static bool operator==(Magazine first, Magazine second) {
        return first.Equals(second);
    }
    
    public static bool operator!=(Magazine first, Magazine second) {
        return !(first == second);
    }

    public override int GetHashCode() {
        return HashCode.Combine(Name, PublicationFrequency, PublicationDate, CirculationNumber, Articles, Editors); // TODO check if works
    }
    
    public override object DeepCopy() {
        Magazine copyInstance = new Magazine(Name, PublicationFrequency, PublicationDate, CirculationNumber); 
        
        List<Article> articlesCopy = new List<Article>(Articles);
        foreach (Article article in articlesCopy) {
            copyInstance.AddArticles((Article) article.DeepCopy());   
        }
        
        List<Person> editorsCopy = new List<Person>(Editors);
        foreach (Person editor in editorsCopy) {
            copyInstance.AddEditors((Person) editor.DeepCopy());   
        }
        
        return copyInstance;
    }

    public IEnumerable<Article> GetArticlesWithHigherRating(double rating) {
        IEnumerator enumerator = Articles.GetEnumerator();

        while (enumerator.MoveNext()) {
            Article article = (Article) enumerator.Current!;
            if (article.Rating > rating) {
                yield return article;
            }
        }
    }
    
    public IEnumerable<Article> GetArticlesWithMatchedTitle(string search) {
        IEnumerator enumerator = Articles.GetEnumerator();

        while (enumerator.MoveNext()) {
            Article article = (Article) enumerator.Current!;
            if (article.ArticleTitle.Contains(search)) {
                yield return article;
            }
        }
    }
    
    public IEnumerable<Article> GetArticlesWithNonEditorAuthor() {
        MagazineEnumerator enumerator = new MagazineEnumerator(this);

        while (enumerator.MoveNext()) {
            yield return enumerator.Current;
        }
    }
    
    public IEnumerable<Article> GetArticlesWithEditorAuthor() {
        IEnumerator enumerator = Articles.GetEnumerator();

        while (enumerator.MoveNext()) {
            Article article = (Article) enumerator.Current!;
            if (Editors.Contains(article.Author)) {
                yield return article;
            }
        }
    }
    
    public IEnumerable<Person> GetEditorsWithoutArticles() {
        IEnumerator enumerator = Editors.GetEnumerator();

        while (enumerator.MoveNext()) {
            Person editor = (Person) enumerator.Current!;
            bool hasArticles = false;

            foreach (Article article in Articles) {
                if (article.Author == editor) {
                    hasArticles = true;
                    break;
                }
            }
            
            if (!hasArticles) {
                yield return editor;
            }
        }
    }
}