package labs;

import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertNotEquals;

import org.testng.annotations.Test;

public class VehicleTest {

    @Test
    public void testVehicleEquality() {
        Vehicle vehicle1 = new Vehicle.Builder("Toyota",2020,"yellow").build();

        Vehicle vehicle2 = new Vehicle.Builder("Toyota",2020,"yellow").build();

        assertEquals(vehicle1.equals(vehicle2), true);
        assertEquals(vehicle1.hashCode(), vehicle2.hashCode());
    }

    @Test
    public void testVehicleInequality() {
        Vehicle vehicle1 = new Vehicle.Builder("Toyota",2020,"yellow").build();

        Vehicle vehicle2 = new Vehicle.Builder("Honda",2021,"yellow").build();

        assertNotEquals(vehicle1.equals(vehicle2), true);
        assertNotEquals(vehicle1.hashCode(), vehicle2.hashCode());
    }

    @Test
    public void testVehicleToString() {
        Vehicle vehicle = new Vehicle.Builder("Toyota",2020,"yellow").build();

        assertEquals(vehicle.toString(), "Vehicle: Toyota, 2020 year, yellow");
    }
}
