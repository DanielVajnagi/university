package labs.service;

import labs.Car;
import labs.interfaces.VehicleServiceInterface;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class VehicleServiceStream implements VehicleServiceInterface {
    private final List<Car> cars;
    public VehicleServiceStream(List<Car> cars) {
        this.cars = cars;
    }
    public List<Car> sortByBrand() {
        return cars.stream()
                .sorted(Comparator.comparing(Car::getBrand))
                .collect(Collectors.toList());
    }

    public List<Car> filterByYear(int year) {
        return cars.stream()
                .filter(car -> car.getYear() == year)
                .collect(Collectors.toList());
    }
    public List<Car> filterByNumberOfDoors(int minNumberOfDoors) {
        return cars.stream()
                .filter(car -> car.getNumberOfDoors() >= minNumberOfDoors)
                .collect(Collectors.toList());
    }

    public List<Car> sortByYear() {
        return cars.stream()
                .sorted(Comparator.comparing(Car::getYear))
                .collect(Collectors.toList());
    }

}

