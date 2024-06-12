using System.ComponentModel.DataAnnotations;

namespace Main;

public class Edition : IComparable, IComparer<Edition> {
    protected string _name = default!;
    protected DateTime _publicationDate;
    protected int _circulationNumber;

    public string Name { get => _name; set => _name = value; }
    public DateTime PublicationDate { get => _publicationDate; set => _publicationDate = value; }
    public int CirculationNumber {
        get => _circulationNumber;
        set {
            if (value < 0) {
                throw new ValidationException("The circulation number must be greater than or equal to zero!");
            }
            
            _circulationNumber = value;
        }
    }


    public Edition(string name, DateTime publicationDate, int circulationNumber) {
        Name = name;
        PublicationDate = publicationDate;
        CirculationNumber = circulationNumber;
    }

    public Edition() : this("Unknown Edition", DateTime.Today, 1) { }

    public int CompareTo(object? obj) {
        if (obj is null) return 1;

        Edition otherEdition = obj as Edition;
        if (otherEdition is not null) {
            return String.Compare(Name, otherEdition.Name, StringComparison.Ordinal);
        }

        throw new ArgumentException("Object is not an Edition");
    }

    public int Compare(Edition? x, Edition? y) {
        if (x is null && y is null) return 0;
        if (x is null) return -1;
        if (y is null) return 1;

        return x.PublicationDate.CompareTo(y.PublicationDate);
    }

    public override bool Equals(object? obj) {
        if (obj == null || obj is not Edition)
            return false;
        
        Edition edition = (Edition) obj;
        return edition.Name == Name &&
               edition.PublicationDate == PublicationDate &&
               edition.CirculationNumber == CirculationNumber;
    }
    
    public static bool operator==(Edition first, Edition second) {
        return first.Equals(second);
    }
    
    public static bool operator!=(Edition first, Edition second) {
        return !(first == second);
    }

    public override int GetHashCode() {
        return HashCode.Combine(Name, PublicationDate, CirculationNumber);
    }

    public virtual object DeepCopy() {
        return (Edition) MemberwiseClone();
    }

    public override string ToString() {
        return $"{Name}, №{CirculationNumber}. Date: {PublicationDate}";
    }
}