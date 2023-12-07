package labs.service;


import labs.Car;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import java.util.ArrayList;
import java.util.List;
import static org.testng.Assert.assertEquals;

public class VehicleServiceTest {

    @Test(dataProvider = "sortingByBrandData")
    public void testSortByBrand(List<Car> inputCars, List<String> expectedBrandsOrder) {
        VehicleService vehicleService = new VehicleService(inputCars);
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
                // Додайте інші тестові набори, якщо потрібно
        };
    }
}
