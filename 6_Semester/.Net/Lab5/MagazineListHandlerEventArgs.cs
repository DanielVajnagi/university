using System.Text;

namespace Main;

public class MagazineListHandlerEventArgs : EventArgs {
    public string CollectionName { get; } = default!;
    public string TypeOfChange { get; } = default!;
    public int NumberOfElement { get; }

    public MagazineListHandlerEventArgs(string collectionName, string typeOfChange, int numberOfElement) {
        CollectionName = collectionName;
        TypeOfChange = typeOfChange;
        NumberOfElement = numberOfElement;
    }

    public override string ToString() {
        StringBuilder sb = new();

        sb.Append($"Collection name: {CollectionName}; ");
        sb.Append($"Type of change: {TypeOfChange}; ");
        sb.Append($"Number of element: {NumberOfElement};");

        return sb.ToString();
    }
}
