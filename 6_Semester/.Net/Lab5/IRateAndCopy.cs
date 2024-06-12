namespace Main;

public interface IRateAndCopy {
    public double Rating { get; }
    public object DeepCopy();
}
