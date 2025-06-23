
package registrationhandler;
import java.util.Scanner;

// Factory Method Pattern Implementation
interface RegistrationHandler {
    User register(RegistrationData data);
}

class EmailRegistrationHandler implements RegistrationHandler {
    @Override
    public User register(RegistrationData data) {
        User user = new User();
        user.setFirstName(data.getFirstName());
        user.setLastName(data.getLastName());
        user.setEmail(data.getEmail());
        user.setPassword(data.getPassword()); // In real app, hash the password
        user.setLocation(data.getLocation());
        user.setCanOfferHelp(data.isOfferHelp());
        user.setCanRequestHelp(data.isRequestHelp());
        return user;
    }
}

class SocialRegistrationHandler implements RegistrationHandler {
    private final String provider;
    
    public SocialRegistrationHandler(String provider) {
        this.provider = provider;
    }

    @Override
    public User register(RegistrationData data) {
        User user = new User();
        user.setEmail(data.getEmail());
        user.setFirstName(data.getFirstName() != null ? data.getFirstName() : "User");
        user.setLastName(data.getLastName() != null ? data.getLastName() : provider);
        user.setPassword("social_auth_" + provider); // Simplified for demo
        user.setCanOfferHelp(true);
        user.setCanRequestHelp(true);
        return user;
    }
}

interface RegistrationHandlerFactory {
    RegistrationHandler createHandler(String type);
}

class RegistrationHandlerFactoryImpl implements RegistrationHandlerFactory {
    @Override
    public RegistrationHandler createHandler(String type) {
        switch (type.toLowerCase()) {
            case "email":
                return new EmailRegistrationHandler();
            case "google":
            case "facebook":
                return new SocialRegistrationHandler(type);
            default:
                throw new IllegalArgumentException("Unknown registration type");
        }
    }
}

// Data Models
class User {
    private String firstName;
    private String lastName;
    private String email;
    private String password;
    private String location;
    private boolean canOfferHelp;
    private boolean canRequestHelp;

    // Getters and setters
    public String getFirstName() { return firstName; }
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public String getLastName() { return lastName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public boolean isCanOfferHelp() { return canOfferHelp; }
    public void setCanOfferHelp(boolean canOfferHelp) { this.canOfferHelp = canOfferHelp; }
    public boolean isCanRequestHelp() { return canRequestHelp; }
    public void setCanRequestHelp(boolean canRequestHelp) { this.canRequestHelp = canRequestHelp; }

    @Override
    public String toString() {
        return "User{" +
                "firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", email='" + email + '\'' +
                ", location='" + location + '\'' +
                ", canOfferHelp=" + canOfferHelp +
                ", canRequestHelp=" + canRequestHelp +
                '}';
    }
}

class RegistrationData {
    private String firstName;
    private String lastName;
    private String email;
    private String password;
    private String confirmPassword;
    private String location;
    private boolean offerHelp = true;
    private boolean requestHelp = true;
    private boolean termsAgreed;

    // Getters and setters
    public String getFirstName() { return firstName; }
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public String getLastName() { return lastName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
    public String getConfirmPassword() { return confirmPassword; }
    public void setConfirmPassword(String confirmPassword) { this.confirmPassword = confirmPassword; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public boolean isOfferHelp() { return offerHelp; }
    public void setOfferHelp(boolean offerHelp) { this.offerHelp = offerHelp; }
    public boolean isRequestHelp() { return requestHelp; }
    public void setRequestHelp(boolean requestHelp) { this.requestHelp = requestHelp; }
    public boolean isTermsAgreed() { return termsAgreed; }
    public void setTermsAgreed(boolean termsAgreed) { this.termsAgreed = termsAgreed; }
}

// Main Application
public class LocalAidRegistration {
    private static final Scanner scanner = new Scanner(System.in);
    private static final RegistrationHandlerFactory handlerFactory = new RegistrationHandlerFactoryImpl();

    public static void main(String[] args) {
        showWelcomeScreen();
        
        System.out.println("Choose registration method:");
        System.out.println("1. Email registration");
        System.out.println("2. Google registration");
        System.out.println("3. Facebook registration");
        System.out.print("Enter choice (1-3): ");
        
        int choice = scanner.nextInt();
        scanner.nextLine(); // consume newline
        
        RegistrationHandler handler;
        RegistrationData data = new RegistrationData();
        
        switch (choice) {
            case 1:
                handler = handlerFactory.createHandler("email");
                collectEmailRegistrationData(data);
                break;
            case 2:
                handler = handlerFactory.createHandler("google");
                collectSocialRegistrationData(data, "Google");
                break;
            case 3:
                handler = handlerFactory.createHandler("facebook");
                collectSocialRegistrationData(data, "Facebook");
                break;
            default:
                System.out.println("Invalid choice");
                return;
        }
        
        User user = handler.register(data);
        System.out.println("\nRegistration successful!");
        System.out.println("User details: " + user);
    }

    private static void showWelcomeScreen() {
        System.out.println("***************************************");
        System.out.println("*                                     *");
        System.out.println("*          Welcome to LocalAid        *");
        System.out.println("*                                     *");
        System.out.println("***************************************");
        System.out.println();
    }

    private static void collectEmailRegistrationData(RegistrationData data) {
        System.out.println("\nEmail Registration");
        System.out.println("-----------------");
        
        System.out.print("First Name: ");
        data.setFirstName(scanner.nextLine());
        
        System.out.print("Last Name: ");
        data.setLastName(scanner.nextLine());
        
        System.out.print("Email: ");
        data.setEmail(scanner.nextLine());
        
        System.out.print("Password: ");
        data.setPassword(scanner.nextLine());
        
        System.out.print("Confirm Password: ");
        data.setConfirmPassword(scanner.nextLine());
        
        System.out.print("Neighborhood/Zip Code: ");
        data.setLocation(scanner.nextLine());
        
        System.out.print("Offer help to others? (Y/N): ");
        data.setOfferHelp(scanner.nextLine().equalsIgnoreCase("Y"));
        
        System.out.print("Request help when needed? (Y/N): ");
        data.setRequestHelp(scanner.nextLine().equalsIgnoreCase("Y"));
        
        System.out.print("Agree to terms? (Y/N): ");
        data.setTermsAgreed(scanner.nextLine().equalsIgnoreCase("Y"));
    }

    private static void collectSocialRegistrationData(RegistrationData data, String provider) {
        System.out.println("\n" + provider + " Registration");
        System.out.println("---------------------");
        
        // Social registration might get most data from the provider's API
        // Here we just simulate minimal input
        System.out.print("Email (from " + provider + "): ");
        data.setEmail(scanner.nextLine());
        
        System.out.print("First Name (optional): ");
        data.setFirstName(scanner.nextLine());
        
        System.out.print("Last Name (optional): ");
        data.setLastName(scanner.nextLine());
        
        System.out.print("Neighborhood/Zip Code: ");
        data.setLocation(scanner.nextLine());
        
        data.setOfferHelp(true);
        data.setRequestHelp(true);
        data.setTermsAgreed(true);
    }
}

