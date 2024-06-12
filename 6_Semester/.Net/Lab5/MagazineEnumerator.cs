using System.Collections;

namespace Main;

public class MagazineEnumerator : IEnumerator {
    private int _position = -1;

    object IEnumerator.Current { get => Current; }

    public Article Current {
        get {
            try {
                return _magazine.Articles[_position];
            } catch (IndexOutOfRangeException) {
                throw new InvalidOperationException();
            }
        }
    }

    private readonly Magazine _magazine = default!;

    public MagazineEnumerator(Magazine magazine) {
        _magazine = magazine;
    }

    public void Reset() {
        _position = -1;
    }

    public bool MoveNext() {
        _position++;

        while (_position < _magazine.Articles.Count && _magazine.Editors.Contains(Current.Author)) {
            _position++;
        }

        return _position < _magazine.Articles.Count;
    }
}
