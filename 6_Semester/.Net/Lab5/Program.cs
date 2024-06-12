namespace Main;

internal static class Program {
    public static void Main(string[] args) {
        MagazineCollection firstCollection = new MagazineCollection {
            CollectionName = "Collection 1"
        };

        MagazineCollection secondCollection = new MagazineCollection {
            CollectionName = "Collection 2"
        };

        Listener firstListener = new Listener();
        firstCollection.MagazineAdded += firstListener.OnMagazineAdded;
        firstCollection.MagazineReplaced += firstListener.OnMagazineReplaced;

        Listener secondListener = new Listener();
        firstCollection.MagazineAdded += secondListener.OnMagazineAdded;
        firstCollection.MagazineReplaced += secondListener.OnMagazineReplaced;

        secondCollection.MagazineAdded += secondListener.OnMagazineAdded;
        secondCollection.MagazineReplaced += secondListener.OnMagazineReplaced;

        firstCollection.AddDefaults();
        firstCollection.Replace(0, new Magazine("Times", Frequency.Yearly, DateTime.Now, 123));

        secondCollection.AddMagazines(new Magazine("Beauty and fashion", Frequency.Monthly, DateTime.Now, 456));

        Console.WriteLine("Changes in the first listener");
        Console.WriteLine(firstListener);

        Console.WriteLine("Changes in the second listener");
        Console.WriteLine(secondListener);
    }
}
