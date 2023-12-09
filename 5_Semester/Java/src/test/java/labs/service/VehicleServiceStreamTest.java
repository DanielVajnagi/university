package labs.service;


import labs.Car;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import java.util.ArrayList;
import java.util.List;
import static org.testng.Assert.assertEquals;

public class VehicleServiceStreamTest {

    @Test(dataProvider = "sortingByBrandData")
    public void testSortByBrand(List<Car> inputCars, List<String> expectedBrandsOrder) {
        VehicleServiceStream vehicleService = new VehicleServiceStream(inputCars);
        List<Car> sortedCars = vehicleService.sortByBrand();

        for (int i = 0; i < sortedCars.size(); i++) {
            assertEquals(expectedBrandsOrder.get(i), sortedCars.get(i).getBrand());
        }
    }

    @DataProvider(name = "sortingByBrandData")
    public Object[][] provideCarsForSortingByBrand() {
        Car car1 = new Car.Builder("Toyota",2020,"yellow").setNumberOfDoors(4).build();
        Car car2 = new Car.Builder("Honda",2019,"red").setNumberOfDoors(4).build();
        Car car3 = new Car.Builder("BMW",2022,"blue").setNumberOfDoors(2).build();

        List<Car> cars = new ArrayList<>();
        cars.add(car1);
        cars.add(car2);
        cars.add(car3);

        return new Object[][] {
                { cars, List.of("BMW", "Honda", "Toyota") }
        };
    }

    @Test(dataProvider = "filterByYearData")
    public void testFilterByYear(List<Car> inputCars, int year, List<Car> expectedFilteredCars) {
        VehicleServiceStream vehicleService = new VehicleServiceStream(inputCars);
        List<Car> filteredCars = vehicleService.filterByYear(year);

        assertEquals(filteredCars, expectedFilteredCars);
    }

    @DataProvider(name = "filterByYearData")
    public Object[][] provideFilterByYearData() {
        Car car1 = new Car.Builder("Toyota", 2020, "yellow").setNumberOfDoors(4).build();
        Car car2 = new Car.Builder("Honda", 2019, "blue").setNumberOfDoors(4).build();
        Car car3 = new Car.Builder("BMW", 2022, "black").setNumberOfDoors(2).build();
        Car car4 = new Car.Builder("Audi", 2022, "white").setNumberOfDoors(4).build();

        List<Car> cars = new ArrayList<>();
        cars.add(car1);
        cars.add(car2);
        cars.add(car3);
        cars.add(car4);

        return new Object[][] {
                { cars, 2022, List.of(car3, car4) },
                { cars, 2019, List.of(car2) },
                { cars, 2023, List.of() }
        };
    }

    @Test(dataProvider = "filterByNumberOfDoorsData")
    public void testFilterByNumberOfDoors(List<Car> inputCars, int minNumberOfDoors, List<Car> expectedFilteredCars) {
        VehicleServiceStream vehicleService = new VehicleServiceStream(inputCars);
        List<Car> filteredCars = vehicleService.filterByNumberOfDoors(minNumberOfDoors);

        assertEquals(filteredCars, expectedFilteredCars);
    }

    @DataProvider(name = "filterByNumberOfDoorsData")
    public Object[][] provideFilterByNumberOfDoorsData() {
        Car car1 = new Car.Builder("Toyota", 2020, "yellow").setNumberOfDoors(4).build();
        Car car2 = new Car.Builder("Honda", 2019, "blue").setNumberOfDoors(4).build();
        Car car3 = new Car.Builder("BMW", 2022, "black").setNumberOfDoors(2).build();
        Car car4 = new Car.Builder("Audi", 2022, "white").setNumberOfDoors(4).build();

        List<Car> cars = new ArrayList<>();
        cars.add(car1);
        cars.add(car2);
        cars.add(car3);
        cars.add(car4);

        return new Object[][] {
                { cars, 2, List.of(car1, car2,car3, car4) },  // Вибираємо авто з 3 і більше дверей
                { cars, 4, List.of(car1, car2, car4) },  // Вибираємо авто з 4 і більше дверей
                { cars, 5, List.of() }  // Немає авто з 5 і більше дверей
        };
    }


    @Test(dataProvider = "sortByYearData")
    public void testSortByYear(List<Car> inputCars, List<Car> expectedSortedCars) {
        VehicleServiceStream vehicleService = new VehicleServiceStream(inputCars);
        List<Car> sortedCars = vehicleService.sortByYear();

        assertEquals(sortedCars, expectedSortedCars);
    }

    @DataProvider(name = "sortByYearData")
    public Object[][] provideSortByYearData() {
        Car car1 = new Car.Builder("Toyota", 2020, "yellow").setNumberOfDoors(4).build();
        Car car2 = new Car.Builder("Honda", 2019, "blue").setNumberOfDoors(4).build();
        Car car3 = new Car.Builder("BMW", 2022, "black").setNumberOfDoors(2).build();
        Car car4 = new Car.Builder("Audi", 2023, "white").setNumberOfDoors(4).build();

        List<Car> cars = new ArrayList<>();
        cars.add(car1);
        cars.add(car2);
        cars.add(car3);
        cars.add(car4);

        List<Car> sortedCars = new ArrayList<>();
        sortedCars.add(car2);
        sortedCars.add(car1);
        sortedCars.add(car3);
        sortedCars.add(car4);

        return new Object[][] {
                { cars, sortedCars }
        };
    }
}
