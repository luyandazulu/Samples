package vehicles;

public class Opel extends Car {
  public Opel(String model) {
    super();
    this.manufacturer = "Opel";
    this.model = model;
  }

  public void hoot() {
    System.out.println("boop");
  }
}
