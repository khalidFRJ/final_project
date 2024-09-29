**Project Report and Reflection**

This project involved developing a Library Management System API using Django and Django Rest Framework (DRF), focusing on CRUD operations for books and users, handling book check-out and return functionality, and ensuring a smooth and secure user experience through authentication. The system meets key functional and technical requirements while providing an organized structure for book and user management within a library.

### **Books Management (CRUD)**:
For managing books, I implemented Create, Read, Update, and Delete (CRUD) operations. Each book has the following attributes: Title, Author, ISBN, Published Date, and Number of Copies Available. The ISBN field is enforced as unique to avoid duplication and ensure the system maintains accurate book records. Validation checks were implemented to ensure proper data handling, such as ensuring books can only be added with a valid ISBN and ensuring sufficient stock when books are checked out. The use of Django ORM allowed efficient interaction with the database, simplifying the management of complex queries.

### **Users Management (CRUD)**:
For user management, CRUD operations were implemented, allowing the creation, updating, reading, and deletion of library users. Each user has a unique username, email, date of membership, and active status. This enables librarians to easily manage user records and track active members. The system also enforces uniqueness for usernames and email addresses, ensuring no duplicate user accounts are created.

### **Check-Out and Return Books**:
A key feature of the system is the ability for users to check out and return books. I developed an endpoint that allows users to check out a book, reducing the number of available copies of that book. Validation checks ensure that users can only check out books when copies are available, and only one copy can be checked out by a user at a time. Upon returning a book, another endpoint was developed to handle increasing the number of available copies. Additionally, a transaction model was created to log the dates when books were checked out and returned, providing a complete borrowing history for each user. This history is accessible to users through the authentication system.

### **View Available Books**:
The API includes an endpoint to view all available books and allows optional query filters to search by Title, Author, or ISBN. Users can filter books by availability, ensuring they can easily find books with available copies. This feature enhances the overall user experience by allowing precise searches and reducing the time spent browsing unavailable books.

### **Authentication**:
For security, I implemented Django’s built-in user authentication system. Users can register, log in, and access their borrowing history. The system ensures that only authenticated users can check out and return books, providing an additional layer of control and security. Optionally, I considered token-based authentication using JWT to further enhance security, especially for production environments where scalability and robustness are critical.

### **API Design**:
The API follows RESTful principles, ensuring well-structured and intuitive endpoints. CRUD operations for books and users make use of appropriate HTTP methods (GET, POST, PUT, DELETE), and the API returns proper status codes to reflect the result of each request. Error handling is also in place, ensuring meaningful feedback when a user attempts invalid actions, such as checking out a book when no copies are available.

### **Deployment**:
I deployed the API on Heroku, ensuring it is accessible, functional, and secure. The deployment process involved setting up environment variables for database configuration and configuring Django settings for production mode. The API is now available for use, with secure HTTPS connections and proper handling of static files.

### **Reflection**:
This project provided a comprehensive experience in designing and implementing a full-featured API using Django and DRF. I gained valuable insights into Django ORM, particularly in handling complex relationships between models (such as books, users, and transactions). Additionally, the project helped me solidify my understanding of REST principles, ensuring API endpoints are well-designed and intuitive.

One of the challenges was ensuring data consistency, especially when managing book check-outs and returns, where inventory levels had to be accurately tracked. Another challenge was integrating user authentication to restrict access to sensitive endpoints, which I overcame by leveraging Django’s robust authentication system.

Although the core functionality is implemented, there is potential for further enhancement. For example, I could introduce user roles (Admin, Member), which would allow more granular control over who can manage books and users. Additionally, tracking overdue books and adding notifications for late returns would provide more real-world functionality.




