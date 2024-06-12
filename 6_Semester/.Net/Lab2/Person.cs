namespace Main;

public class Person {
    private string _firstName = default!;
    private string _lastName = default!;
    private DateTime _birthday;

    public string FirstName { get => _firstName; init => _firstName = value; }
    public string LastName { get => _lastName; init => _lastName = value; }
    public DateTime Birthday { get => _birthday; init => _birthday = value; }

    public int YearOfBirth {
        get => _birthday.Year;
        set => _birthday = new DateTime(value, _birthday.Month, _birthday.Day);
    }

    public Person() : this(
        "Jane",
        "Doe",
        new DateTime(1970, 1, 1)
    ) { }

    public Person(string firstName, string lastName, DateTime birthday) {
        FirstName = firstName;
        LastName = lastName;
        Birthday = birthday;
    }

    public override string ToString() {
        return $"{FirstName} {LastName}, {Birthday}";
    }

    public string ToShortString() {
        return FirstName + " " + LastName;
    }

    public override bool Equals(object? obj) {
        if (obj == null || obj is not Person)
            return false;
        
        Person person = (Person) obj;
        return person.FirstName == FirstName && 
               person.LastName == LastName &&
               person.Birthday == Birthday;
    }
    
    public static bool operator==(Person first, Person second) {
        return first.Equals(second);
    }
    
    public static bool operator!=(Person first, Person second) {
        return !(first == second);
    }

    public override int GetHashCode() {
        return HashCode.Combine(FirstName, LastName, Birthday);
    }

    public object DeepCopy() {
        return (Person) MemberwiseClone();
    }
}
