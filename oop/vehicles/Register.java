package vehicles;

public class Register {
  private String vinNumber;
  private String accountNumber;

  public Register() {
    super();
  }

  public void setVinNumber(String vin) {
    this.vinNumber = vin;
  }

  public String getVinNumber() {
    return this.vinNumber;
  }
}
