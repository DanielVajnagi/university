namespace Main;

public class EditionCirculationComparer : IComparer<Edition> {
    public int Compare(Edition? x, Edition? y) {
        if (x is null && y is null) return 0;
        if (x is null) return -1;
        if (y is null) return 1;

        return x.CirculationNumber.CompareTo(y.CirculationNumber);
    }
}