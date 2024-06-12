namespace Main;

public class ListEntry {
    public string CollectionName { get; } = default!;
    public string EventInfo { get; } = default!;
    public int NumberOfElement { get; }

    public ListEntry(string collectionName, string eventInfo, int numberOfElement) {
        CollectionName = collectionName;
        EventInfo = eventInfo;
        NumberOfElement = numberOfElement;
    }

    public override string ToString() {
        return $"Collection: {CollectionName}; Event: {EventInfo}; Index: {NumberOfElement};";
    }
}
