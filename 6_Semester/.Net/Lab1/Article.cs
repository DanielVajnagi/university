namespace Main;

public class Article {
    public Person Author { get; init; } = default!;
    public string ArticleTitle { get; init; } = default!;
    public double Rating { get; set; }

    public Article(Person author, string articleTitle, double rating) {
        Author = author;
        ArticleTitle = articleTitle;
        Rating = rating;
    }

    public Article() : this( new Person(), "New Article", 0) { }

    public override string ToString() {
        return $"{ArticleTitle} by {Author}; Rating: {Rating}";
    }
}