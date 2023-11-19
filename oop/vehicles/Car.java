package vehicles;

public class Car implements Vehicle {
  public String manufacturer;
  public String model;
  public Integer wheels;

  public Car() {
    this.wheels = 4;
  }

  public void hoot() {
    System.out.println("beep");
  }

  public void move() {

  }

  public String registrationNumber() {
    return "";
  }

  public Integer getWeight() {
    return 2000;
  }

  public Integer getMilage() {
    return 22222;
  }
}
