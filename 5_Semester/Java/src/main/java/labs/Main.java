package labs;




public class Main {
    public static void main(String[] args) {

        // Створення об'єкта Vehicle
        Vehicle myVehicle = new Vehicle.Builder("Toyota",2020,"21").build();

        System.out.println(myVehicle);

    }
}