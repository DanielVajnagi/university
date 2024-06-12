namespace Main;

public class Article : IRateAndCopy {
    public Person Author { get; init; } = default!;
    public string ArticleTitle { get; init; } = default!;
    public double Rating { get; }

    public Article(Person author, string articleTitle, double rating) {
        Author = author;
        ArticleTitle = articleTitle;
        Rating = rating;
    }

    public Article() : this(new Person(), "New Article", 0) { }

    public override string ToString() {
        return $"{ArticleTitle} by {Author}; Rating: {Rating}";
    }
    
    public override bool Equals(object? obj) {
        if (obj == null || obj is not Article)
            return false;
        
        Article article = (Article) obj;
        return article.Author == Author && 
               article.ArticleTitle == ArticleTitle && 
               Math.Abs(article.Rating - Rating) < Double.Epsilon;
    }
    
    public static bool operator==(Article first, Article second) {
        return first.Equals(second);
    }
    
    public static bool operator!=(Article first, Article second) {
        return !(first == second);
    }

    public override int GetHashCode() {
        return HashCode.Combine(Author, ArticleTitle);
    }
    
    public object DeepCopy() {
        return new Article((Person) Author.DeepCopy(), ArticleTitle, Rating);
    }
}