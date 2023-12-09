package labs.service;

import labs.Car;
import labs.interfaces.VehicleServiceInterface;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

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

    public List<Car> filterByYear(int year) {
        List<Car> result = new ArrayList<>();
        for (Car car : cars) {
            if (car.getYear() == year) {
                result.add(car);
            }
        }
        return result;
    }
    public List<Car> filterByNumberOfDoors(int minNumberOfDoors) {
        List<Car> filteredCars = new ArrayList<>();
        for (Car car : cars) {
            if (car.getNumberOfDoors() >= minNumberOfDoors) {
                filteredCars.add(car);
            }
        }
        return filteredCars;
    }

    public List<Car> sortByYear() {
        List<Car> sortedCars = new ArrayList<>(cars);
        sortedCars.sort(Comparator.comparingInt(Car::getYear));
        return sortedCars;
    }

}

