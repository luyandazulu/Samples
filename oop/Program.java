import vehicles.Bus;
import vehicles.Car;
import vehicles.Opel;
import vehicles.Register;
import vehicles.Vehicle;

public class Program {
  public static void main(String[] args) {
    // Vehicle microbus = new Bus();
    // Vehicle sedan = new Car();
    Bus bus = new Bus();
    Opel astra = new Opel("Astra");

    Vehicle[] cars = { bus, astra };
    for (int i = 0; i < cars.length; i++) {
      System.out.println(cars[i].getWeight());
    }

  }
}
