package labs.service;

import labs.Car;
import labs.interfaces.VehicleServiceInterface;

import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class VehicleService implements VehicleServiceInterface {


    private final List<Car> cars;

    public VehicleService(List<Car> cars) {
        this.cars = cars;
    }

    @Override
    public List<Car> sortByBrand() {
        Collections.sort(cars, new Comparator<Car>() {
            @Override
            public int compare(Car car1, Car car2) {
                return car1.getBrand().compareTo(car2.getBrand());
            }
        });

        return cars;
    }

    @Override
    public List<Car> filterByYear(int year) {
        // Реалізація фільтрації за роком
        // Повертає список автомобілів, які відповідають заданому року
        return null;
    }

    @Override
    public List<Car> filterByNumberOfDoors(int minNumberOfDoors) {
        // Реалізація фільтрації за кількістю дверей
        // Повертає список автомобілів, які мають не менше дверей, ніж вказано
        return null;
    }

    @Override
    public List<Car> sortByYear() {
        // Реалізація сортування за роком
        // Наприклад, використовуючи Comparator і Collections.sort()
        // Повертає відсортований список
        return null;
    }
}
