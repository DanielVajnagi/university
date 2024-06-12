# Using a default font instead since "arial" is not available

# Create a blank image
from PIL import Image, ImageDraw, ImageFont


width, height = 2400, 3200
background_color = "white"
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Font settings
font_size = 18
font = ImageFont.load_default()

# Text settings
margin = 20
line_height = 24

# Class Diagram content
class_diagram = {
    "Passenger": {
        "attributes": ["id: int", "name: String", "email: String", "phoneNumber: String", "ticket: Ticket"],
        "operations": ["createRequest(): void", "buyTicket(): void", "viewTicket(): void", "getNotifications(): void", "cancelTicket(): void"]
    },
    "BookingWebsite": {
        "attributes": ["url: String", "availableTickets: List<Ticket>", "paymentSystem: PaymentSystem", "notificationSystem: NotificationSystem", "database: Database"],
        "operations": ["searchTickets(): void", "requestPayment(): void", "confirmBooking(): void", "sendTicket(): void", "updateTicketStatus(): void"]
    },
    "TicketDatabase": {
        "attributes": ["tickets: List<Ticket>", "connection: String", "lastUpdated: Date", "manager: DatabaseManager", "accessRights: String"],
        "operations": ["checkAvailability(): void", "updateTicketStatus(): void", "fetchTicketDetails(): void", "addTicket(): void", "deleteTicket(): void"]
    },
    "PaymentSystem": {
        "attributes": ["provider: String", "transactionId: int", "amount: double", "status: String", "method: String"],
        "operations": ["processPayment(): void", "confirmPayment(): void", "refundPayment(): void", "validatePaymentDetails(): void", "getTransactionStatus(): void"]
    },
    "NotificationSystem": {
        "attributes": ["channels: List<String>", "messageQueue: List<Message>", "deliveryStatus: String", "messageTemplate: String", "systemStatus: String"],
        "operations": ["sendNotification(): void", "receiveConfirmation(): void", "queueMessage(): void", "trackDelivery(): void", "updateTemplate(): void"]
    },
    "StationWebsite": {
        "attributes": ["url: String", "serviceRequests: List<ServiceRequest>", "customerServiceSystem: CustomerServiceSystem", "technicalStaff: List<TechnicalStaff>", "notificationSystem: NotificationSystem"],
        "operations": ["createServiceRequest(): void", "viewServiceRequests(): void", "updateServiceRequestStatus(): void", "notifyStaff(): void", "notifyPassenger(): void"]
    },
    "RequestDatabase": {
        "attributes": ["requests: List<ServiceRequest>", "connection: String", "lastUpdated: Date", "manager: DatabaseManager", "accessRights: String"],
        "operations": ["addRequest(): void", "updateRequestStatus(): void", "fetchRequestDetails(): void", "deleteRequest(): void", "getRequests(): void"]
    },
    "CustomerServiceSystem": {
        "attributes": ["serviceRequests: List<ServiceRequest>", "staff: List<CustomerServiceRep>", "notificationSystem: NotificationSystem", "status: String", "workingHours: String"],
        "operations": ["assignRequest(): void", "resolveRequest(): void", "notifyPassenger(): void", "escalateRequest(): void", "logInteraction(): void"]
    },
    "TechnicalStaff": {
        "attributes": ["id: int", "name: String", "skillSet: List<String>", "assignedRequests: List<ServiceRequest>", "availability: String"],
        "operations": ["acceptRequest(): void", "updateRequestStatus(): void", "completeRequest(): void", "reportIssue(): void", "notifyCustomerService(): void"]
    },
    "StationManager": {
        "attributes": ["id: int", "name: String", "contactInfo: String", "managedStations: List<Station>", "notifications: List<Notification>"],
        "operations": ["login(): void", "manageStation(): void", "updateSchedule(): void", "sendDelayNotifications(): void", "checkNotificationStatus(): void"]
    },
    "Ticket": {
        "attributes": ["ticketId: int", "passengerName: String", "trainNumber: String", "departureTime: DateTime", "status: String"],
        "operations": ["reserve(): void", "cancel(): void", "updateStatus(): void", "getDetails(): void", "validate(): void"]
    },
    "ServiceRequest": {
        "attributes": ["requestId: int", "passengerId: int", "description: String", "status: String", "assignedTo: String"],
        "operations": ["create(): void", "updateStatus(): void", "assignToStaff(): void", "close(): void", "getRequestDetails(): void"]
    }
}

# Starting coordinates
x, y = margin, margin

# Function to draw class box
def draw_class_box(class_name, class_details):
    global x, y
    # Draw class name
    draw.text((x, y), class_name, font=font, fill="black")
    y += line_height
    # Draw attributes
    for attribute in class_details["attributes"]:
        draw.text((x, y), f"- {attribute}", font=font, fill="black")
        y += line_height
    # Draw operations
    for operation in class_details["operations"]:
        draw.text((x, y), f"+ {operation}", font=font, fill="black")
        y += line_height
    # Add some space between classes
    y += margin

# Draw each class
for class_name, class_details in class_diagram.items():
    draw_class_box(class_name, class_details)

# Save the image
image_path = "class_diagram.png"
image.save(image_path)
image.show()
image_path
