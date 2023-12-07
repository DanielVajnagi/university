package labs.interfaces;



import labs.*;

import java.util.List;


public interface VehicleServiceInterface {
    List<Car> sortByBrand();

    List<Car> filterByYear(int year);

    List<Car> filterByNumberOfDoors(int minNumberOfDoors);

    List<Car> sortByYear();
}
