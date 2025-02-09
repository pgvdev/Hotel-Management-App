<h1 style="text-align: center;">Overview of the <strong>Lemon Tree Hotel Management Booking App</strong></h1><div><strong><br /></strong></div>
<p>The <strong>Lemon Tree Hotel Management Booking App</strong> is designed to assist hotel employees, particularly <strong>receptionists</strong>, in efficiently managing hotel reservations. It provides an intuitive <strong>GUI-based</strong> system that simplifies the process of <strong>room bookings, customer management, and reservations tracking</strong>. The system is intended to enhance <strong>efficiency, accuracy, and customer satisfaction</strong> by streamlining the reservation workflow.</p>
<hr />
<h4><strong>Key Features</strong></h4>
<ol>
<li>
<p><strong>Dashboard</strong></p>
<ul>
<li>Employees can access the system through a user-friendly interface.</li>
<li>Main dashboard with quick navigation to key functions.</li>
</ul>
</li>
<li>
<p><strong>Customer Management</strong></p>
<ul>
<li>Add, update, and delete customer details.</li>
<li>Store customer information such as name, contact, address, and customer type (Standard/Premium).</li>
<li>Premium customers receive booking rewards.</li>
</ul>
</li>
<li>
<p><strong>Room Management</strong></p>
<ul>
<li>Manage hotel rooms, including room type, floor, and pricing.</li>
<li>Availability tracking to prevent double bookings.</li>
<li>Support for Single and Double room types.</li>
</ul>
</li>
<li>
<p><strong>Reservation System</strong></p>
<ul>
<li>Employees can enter reservation details and generate a booking confirmation.</li>
<li>Customers specify the purpose of stay (Leisure/Business).</li>
<li>Automatic discount calculation for premium customers.</li>
<li>Option to cancel reservations.</li>
</ul>
</li>
<li>
<p><strong>Search &amp; Filtering</strong></p>
<ul>
<li>Find customer and booking records using multiple filters such as <strong>name, phone number, room type, and booking ID</strong>.</li>
<li>Advanced search for managing room availability.</li>
</ul>
</li>
<li>
<p><strong>Payment &amp; Billing</strong></p>
<ul>
<li>Calculates total booking cost, including VAT and discounts.</li>
<li>Supports multiple payment methods (Cash, Credit Card, PayPal, etc.).</li>
</ul>
</li>
<li>
<p><strong>Undo &amp; Modification Functions</strong></p>
<ul>
<li>Employees can <strong>update or undo reservation changes</strong> if necessary.</li>
<li>History of bookings is maintained for review.</li>
</ul>
</li>
<li>
<p><strong>Graphical User Interface (GUI)</strong></p>
<ul>
<li>Developed using <strong>Tkinter (Python GUI library)</strong>.</li>
<li>Image-based navigation with buttons for <strong>Customers, Reservations, and Room Management</strong>.</li>
</ul>
</li>
<li>
<p><strong>Database Integration</strong></p>
<ul>
<li>Uses <strong>MySQL</strong> for managing customer and reservation data.</li>
<li>Ensures <strong>data consistency and security</strong>.</li>
<li>Efficient data retrieval and update mechanisms.</li>
</ul>
</li>
<li>
<p><strong>Design Patterns Implementation</strong></p>
</li>
</ol>
<ul>
<li><strong>Factory Method</strong>: Used for dynamic customer object creation.</li>
<li><strong>Singleton</strong>: Ensures a single instance for room availability tracking.</li>
<li><strong>Observer Pattern</strong>: Allows real-time UI updates.</li>
<li><strong>Model-View-Controller (MVC)</strong>: Separates business logic from the UI.</li>
<li><strong>Command Pattern</strong>: Implements undo functionality for reservations.</li>
</ul>
<hr />
<h4><strong>Intended Users</strong></h4>
<ul>
<li><strong>Hotel Receptionists</strong>: Primary users who manage customer check-ins, reservations, and room availability.</li>
<li><strong>Hotel Managers</strong>: Oversee booking trends and generate reports.</li>
<li><strong>IT Administrators</strong>: Maintain the system, database, and infrastructure.</li>
</ul>
<hr />
<p><br /></p>
