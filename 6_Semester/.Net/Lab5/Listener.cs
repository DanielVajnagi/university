using System.Text;

namespace Main;

public class Listener {
    private readonly List<ListEntry> _changes = [];

    public void OnMagazineAdded(object _, MagazineListHandlerEventArgs args) {
        var entry = new ListEntry(args.CollectionName, args.TypeOfChange, args.NumberOfElement);
        _changes.Add(entry);
    }

    public void OnMagazineReplaced(object _, MagazineListHandlerEventArgs args) {
        var entry = new ListEntry(args.CollectionName, args.TypeOfChange, args.NumberOfElement);
        _changes.Add(entry);
    }

    public override string ToString() {
        var sb = new StringBuilder();

        sb.Append("List of changes:\n");

        foreach (var entry in _changes) {
            sb.Append(entry + "\n");
        }

        return sb.ToString();
    }
}
