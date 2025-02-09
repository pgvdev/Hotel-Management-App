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


<h2><span style="font-family: times;">Step-by-Step Installation and Configuration Guide</span></h2>
<h3><span style="font-family: times;">1. </span><span style="font-family: times;">Prerequisites</span></h3>
<p><span style="font-family: times; font-weight: normal;">Before installing the Lemon Tree Hotel Management Booking App, ensure your system meets the following requirements:</span></p>
<h4><span style="font-family: times; font-weight: normal;">Software Requirements</span></h4>
<ul>
<li><span style="font-family: times; font-weight: normal;">Operating System: Windows 10/11 or macOS/Linux</span></li>
<li><span style="font-family: times; font-weight: normal;">Python: Version 3.7+</span></li>
<li><span style="font-family: times; font-weight: normal;">MySQL Server: Version 8.0+ (Ensure MySQL Workbench is installed)</span></li>
<li><span style="font-family: times; font-weight: normal;">Required Python Libraries:
</span><ul>
<li><span style="font-family: times; font-weight: normal;"><code inline="">tkinter</code> (for GUI)</span></li>
<li><span style="font-family: times; font-weight: normal;"><code inline="">PIL</code> (<code inline="">pillow</code> for image processing)</span></li>
<li><span style="font-family: times; font-weight: normal;"><code inline="">mysql-connector-python</code> (for database connectivity)</span></li>
<li><span style="font-family: times; font-weight: normal;"><code inline="">tkcalendar</code> (for date selection)</span></li>
<li><span style="font-family: times; font-weight: normal;"><code inline="">random, datetime, time</code> (built-in libraries)</span></li>
</ul>
</li>
</ul>
<h4><span style="font-family: times; font-weight: normal;">Hardware Requirements</span></h4>
<ul>
<li><span style="font-family: times; font-weight: normal;">Minimum 4GB RAM (Recommended 8GB)</span></li>
<li><span style="font-family: times; font-weight: normal;">Minimum 500MB Free Storage for database and application files</span></li>
</ul>
<hr />
<h3><span style="font-family: times;">2. Installing Required Dependencies</span></h3>
<ol>
<li>
<p><span style="font-family: times; font-weight: normal;">Install Python (if not installed)</span></p>
<ul>
<li><span style="font-family: times; font-weight: normal;">Download and install Python 3.7+ from <a href="https://www.python.org/downloads/">Python Official Website</a>.</span></li>
<li><span style="font-family: times; font-weight: normal;">During installation, select Add Python to PATH.</span></li>
</ul>
</li>
<li>
<p><span style="font-family: times; font-weight: normal;">Install Required Python Libraries
Open Command Prompt (Windows) / Terminal (Mac/Linux) and run:</span></p>
<pre><code class="language-sh"><span style="font-family: times; font-weight: normal;">pip install pillow mysql-connector-python tkcalendar
</span></code></pre>
</li>
</ol>
<hr />
<h3><span style="font-family: times;">3. Setting Up MySQL Database</span></h3>
<ol>
<li>
<p><span style="font-family: times; font-weight: normal;">Install MySQL Server (if not installed)</span></p>
<ul>
<li><span style="font-family: times; font-weight: normal;">Download and install <a href="https://dev.mysql.com/downloads/mysql/">MySQL Community Server</a>.</span></li>
<li><span style="font-family: times; font-weight: normal;">During installation, set the root password and remember it.</span></li>
</ul>
</li>
<li>
<p><span style="font-family: times; font-weight: normal;">Configure the Database</span></p>
<ul>
<li><span style="font-family: times; font-weight: normal;">Open MySQL Workbench.</span></li>
<li><span style="font-family: times; font-weight: normal;">Create a new database by running the provided SQL script:
</span><ol>
<li><span style="font-family: times; font-weight: normal;">Open MySQL Workbench.</span></li>
<li><span style="font-family: times; font-weight: normal;">Select a database connection.</span></li>
<li><span style="font-family: times; font-weight: normal;">Create a new query window.</span></li>
<li><span style="font-family: times; font-weight: normal;">Run the SQL script found in the <code inline="">MySQL Database.sql</code> file.</span></li>
</ol>
</li>
<li><span style="font-family: times; font-weight: normal;">Ensure MySQL credentials in the Python files match your setup:
</span><pre><code class="language-python"><span style="font-family: times; font-weight: normal;">conn = mysql.connector.connect(host="localhost", user="root", password="yourpassword", database="management")
</span></code></pre>
</li>
<li><span style="font-family: times; font-weight: normal;">Replace <code inline="">yourpassword</code> with your actual MySQL root password.</span></li>
</ul>
</li>
</ol>
<hr />
<h3><span style="font-family: times;">4. Running the Application</span></h3>
<ol>
<li><span style="font-family: times; font-weight: normal;">Extract all the project files into a preferred directory.</span></li>
<li><span style="font-family: times; font-weight: normal;">Navigate to the directory in Command Prompt or Terminal:
</span><pre><code class="language-sh"><span style="font-family: times; font-weight: normal;">cd /path/to/hotel-management-app
</span></code></pre>
</li>
<li><span style="font-family: times; font-weight: normal;">Run the main application file:
</span><pre><code class="language-sh"><span style="font-family: times; font-weight: normal;">python hotel.py
</span></code></pre>
</li>
<li><span style="font-family: times; font-weight: normal;">The Hotel Management System window should open.</span></li>
</ol>
<hr />
<h3><span style="font-family: times;">5. Authentication and User Access</span></h3>
<ul>
<li><span style="font-family: times; font-weight: normal;">No authentication required for running the app.</span></li>
<li><span style="font-family: times; font-weight: normal;">The hotel receptionist is the primary user.</span></li>
<li><span style="font-family: times; font-weight: normal;">Database authentication is managed via MySQL credentials.</span></li>
</ul>
<hr />
<h3><span style="font-family: times;">6. Additional Customization</span></h3>
<ul>
<li><span style="font-family: times; font-weight: normal;">Modify image paths in Python files if needed.</span></li>
<li><span style="font-family: times; font-weight: normal;">Update database credentials in:
</span><ul>
<li><code inline=""><span style="font-family: times; font-weight: normal;">hotel.py</span></code></li>
<li><code inline=""><span style="font-family: times; font-weight: normal;">room.py</span></code></li>
<li><code inline=""><span style="font-family: times; font-weight: normal;">reservations.py</span></code></li>
<li><code inline=""><span style="font-family: times; font-weight: normal;">customer.py</span></code></li>
</ul>
</li>
</ul>
<hr />
<h3><span style="font-family: times;">7. Troubleshooting</span></h3>
<ul>
<li><span style="font-family: times; font-weight: normal;">If MySQL fails to connect, ensure:
</span><ul>
<li><span style="font-family: times; font-weight: normal;">MySQL Server is running.</span></li>
<li><span style="font-family: times; font-weight: normal;">The correct username/password is provided.</span></li>
<li><span style="font-family: times; font-weight: normal;">The database "management" exists.</span></li>
</ul>
</li>
<li><span style="font-family: times; font-weight: normal;">If Python dependencies are missing, reinstall them:
</span><pre><code class="language-sh"><span style="font-family: times; font-weight: normal;">pip install --upgrade pillow mysql-connector-python tkcalendar
</span></code></pre>
</li>
</ul>
<hr />


<h2 style="text-align: center;">User Interaction Guide</h2><h3>
<h3 style="text-align: left;">1. Launching the Application</h3>
<ol>
<li><span style="font-weight: normal;">Open Command Prompt (Windows) or Terminal (Mac/Linux).</span></li>
<li><span style="font-weight: normal;">Navigate to the project directory:
</span><pre><code class="language-sh" style="font-weight: normal;">cd /path/to/hotel-management-app
</code></pre>
</li>
<li><span style="font-weight: normal;">Run the main application:
</span><pre><code class="language-sh" style="font-weight: normal;">python hotel.py
</code></pre>
</li>
<li><span style="font-weight: normal;">The Hotel Management System window will open, displaying the main dashboard.</span></li>
</ol>
<hr />
<h2>2. Common Workflows &amp; User Actions</h2><h3><span style="font-weight: normal;">A. Customer Management</span></h3>

<ul>
<li><span style="font-weight: normal;">Navigate to the "Customer Management" section by clicking the Customer Button.</span></li>
<li><span style="font-weight: normal;">Actions Available:
</span><ul>
<li><span style="font-weight: normal;">Add a new customer</span></li>
<li><span style="font-weight: normal;">Search for a customer</span></li>
<li><span style="font-weight: normal;">Update customer details</span></li>
<li><span style="font-weight: normal;">Delete customer records</span></li>
<li><span style="font-weight: normal;">View all customers in a table</span></li>
</ul>
</li>
</ul>
<h4><span style="font-weight: normal;">Example Workflow: Adding a Customer</span></h4>
<ol>
<li><span style="font-weight: normal;">Open the Customer Management window.</span></li>
<li><span style="font-weight: normal;">Fill in customer details:
</span><ul>
<li><span style="font-weight: normal;">Full Name</span></li>
<li><span style="font-weight: normal;">Date of Birth</span></li>
<li><span style="font-weight: normal;">Phone Number</span></li>
<li><span style="font-weight: normal;">Email Address</span></li>
<li><span style="font-weight: normal;">Customer Type (Standard/Premium)</span></li>
</ul>
</li>
<li><span style="font-weight: normal;">Click "Submit Details" to save.</span></li>
<li><span style="font-weight: normal;">The customer is added to the database, and a confirmation message appears.</span></li>
</ol>
<p><span style="font-weight: normal;">Command (if applicable in a future CLI version):</span></p>
<pre><code class="language-sh" style="font-weight: normal;">add_customer --name "John Doe" --dob "1990-05-15" --phone "123456789" --email "john.doe@example.com" --type "Premium"
</code></pre>
<hr />
<h3><span style="font-weight: normal;">B. Room Management</span></h3>
<ul>
<li><span style="font-weight: normal;">Navigate to "Room Management" via the Rooms Button.</span></li>
<li><span style="font-weight: normal;">Actions Available:
</span><ul>
<li><span style="font-weight: normal;">Add new rooms</span></li>
<li><span style="font-weight: normal;">Update room details</span></li>
<li><span style="font-weight: normal;">Delete room records</span></li>
<li><span style="font-weight: normal;">Search rooms by type, floor, or price</span></li>
<li><span style="font-weight: normal;">View available rooms</span></li>
</ul>
</li>
</ul>
<h4><span style="font-weight: normal;">Example Workflow: Adding a Room</span></h4>
<ol>
<li><span style="font-weight: normal;">Select room details:
</span><ul>
<li><span style="font-weight: normal;">Room Type (Single/Double/Deluxe)</span></li>
<li><span style="font-weight: normal;">Floor Number</span></li>
<li><span style="font-weight: normal;">Room Price</span></li>
</ul>
</li>
<li><span style="font-weight: normal;">Click "Add" to register the new room in the system.</span></li>
<li><span style="font-weight: normal;">The room is successfully added and visible in the database.</span></li>
</ol>
<p><span style="font-weight: normal;">Command (if applicable in a CLI version):</span></p>
<pre><code class="language-sh" style="font-weight: normal;">add_room --type "Double" --floor 2 --price 150
</code></pre>
<hr />
<h3><span style="font-weight: normal;">C. Making a Reservation</span></h3>
<ul>
<li><span style="font-weight: normal;">Navigate to the "Reservation Management" section using the Reservation Button.</span></li>
<li><span style="font-weight: normal;">Actions Available:
</span><ul>
<li><span style="font-weight: normal;">Create a new reservation</span></li>
<li><span style="font-weight: normal;">Search for a reservation</span></li>
<li><span style="font-weight: normal;">Modify existing reservations</span></li>
<li><span style="font-weight: normal;">Cancel a reservation</span></li>
<li><span style="font-weight: normal;">Calculate the total bill</span></li>
</ul>
</li>
</ul>
<h4><span style="font-weight: normal;">Example Workflow: Booking a Room</span></h4>
<ol>
<li><span style="font-weight: normal;">Select a customer (search by ID or Name).</span></li>
<li><span style="font-weight: normal;">Choose:
</span><ul>
<li><span style="font-weight: normal;">Check-in &amp; Check-out Dates</span></li>
<li><span style="font-weight: normal;">Room Type</span></li>
<li><span style="font-weight: normal;">Room Number (only available ones are displayed)</span></li>
<li><span style="font-weight: normal;">Purpose of Stay (Leisure/Business)</span></li>
<li><span style="font-weight: normal;">Number of Adults &amp; Children</span></li>
</ul>
</li>
<li><span style="font-weight: normal;">Click "Add" to confirm the booking.</span></li>
<li><span style="font-weight: normal;">The system generates a unique Booking ID and a confirmation message.</span></li>
</ol>
<p><span style="font-weight: normal;">Command (CLI Example):</span></p>
<pre><code class="language-sh" style="font-weight: normal;">book_room --customer "John Doe" --checkin "2024-06-15" --checkout "2024-06-20" --room "Double" --guests 2
</code></pre>
<hr />
<h3><span style="font-weight: normal;">D. Cancelling a Reservation</span></h3>
<ul>
<li><span style="font-weight: normal;">Search for an existing reservation using Booking ID or Customer Name.</span></li>
<li><span style="font-weight: normal;">Click "Delete" to cancel the reservation.</span></li>
<li><span style="font-weight: normal;">The system removes the reservation from the database.</span></li>
</ul>
<p><span style="font-weight: normal;">Command (CLI Example):</span></p>
<pre><code class="language-sh" style="font-weight: normal;">cancel_reservation --booking_id 1005
</code></pre>
<hr />
<h3><span style="font-weight: normal;">E. Checking Out &amp; Payments</span></h3>
<ul>
<li><span style="font-weight: normal;">Before checkout, the system calculates the total cost:
</span><ul>
<li><span style="font-weight: normal;">Room Rate × Number of Nights</span></li>
<li><span style="font-weight: normal;">Discount for premium customers</span></li>
<li><span style="font-weight: normal;">VAT (if applicable)</span></li>
</ul>
</li>
<li><span style="font-weight: normal;">Choose a Payment Method:
</span><ul>
<li><span style="font-weight: normal;">Cash, Credit Card, PayPal, etc.</span></li>
</ul>
</li>
<li><span style="font-weight: normal;">Click "Check Out" to finalize the payment.</span></li>
</ul>
<p><span style="font-weight: normal;">Command (CLI Example):</span></p>
<pre><code class="language-sh" style="font-weight: normal;">checkout --booking_id 1005 --payment "Credit Card"
</code></pre>
<hr />
<h2>3. Searching &amp; Filtering</h2>
<p><span style="font-weight: normal;">Each module (Customer, Rooms, Reservations) supports search &amp; filter functionality.</span></p>
<h3><span style="font-weight: normal;">A. Searching for a Customer</span></h3>
<ul>
<li><span style="font-weight: normal;">Open Customer Management.</span></li>
<li><span style="font-weight: normal;">Select search filter (Name, Email, or Phone).</span></li>
<li><span style="font-weight: normal;">Enter the keyword and click Search.</span></li>
</ul>
<p><span style="font-weight: normal;">Command (CLI Example):</span></p>
<pre><code class="language-sh" style="font-weight: normal;">search_customer --name "John Doe"
</code></pre>
<hr />
<h3><span style="font-weight: normal;">B. Searching for a Room</span></h3>
<ul>
<li><span style="font-weight: normal;">Open Room Management.</span></li>
<li><span style="font-weight: normal;">Select room type or floor level.</span></li>
<li><span style="font-weight: normal;">Click Search.</span></li>
</ul>
<p><span style="font-weight: normal;">Command (CLI Example):</span></p>
<pre><code class="language-sh" style="font-weight: normal;">search_room --type "Double"
</code></pre>
<hr />
<h3><span style="font-weight: normal;">C. Searching for a Reservation</span></h3>
<ul>
<li><span style="font-weight: normal;">Open Reservation Management.</span></li>
<li><span style="font-weight: normal;">Select a filter (Booking ID, Check-in Date, Customer Name).</span></li>
<li><span style="font-weight: normal;">Enter the search term and click Search.</span></li>
</ul>
<p><span style="font-weight: normal;">Command (CLI Example):</span></p>
<pre><code class="language-sh" style="font-weight: normal;">search_reservation --customer "John Doe"
</code></pre>
<hr />
<h2>4. Additional Functionalities</h2> <h3><span style="font-weight: normal;">Undo Last Action</span></h3>

<ul>
<li><span style="font-weight: normal;">If a user accidentally modifies or deletes a reservation, the system supports Undo functionality.</span></li>
</ul>
<p><span style="font-weight: normal;">Command (CLI Example):</span></p>
<pre><code class="language-sh" style="font-weight: normal;">undo_last_action
</code></pre>
<hr />
<h3><span style="font-weight: normal;">Real-Time UI Updates</span></h3>
<ul>
<li><span style="font-weight: normal;">When a new reservation is made, the available rooms list updates automatically.</span></li>
<li><span style="font-weight: normal;">If a room is deleted, it is removed from the availability search instantly.</span></li>
</ul>
<hr />
<br />




<h1 style="text-align: center;"><span style="font-family: times;">Configuring and Customizing the Lemon Tree Hotel Management Booking App</span></h1><div><span style="font-family: times;"><br /></span></div>
<p style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">The Lemon Tree Hotel Management Booking App allows users to modify settings, customize behaviors, and personalize system configurations. This includes database connections, UI elements, room settings, and reservation policies.</span></span></p>
<hr style="text-align: left;" />
<h2><span style="font-family: times;">1. Configuring Database &amp; Authentication Settings</span></h2><h3><span style="font-weight: normal;"><span style="font-family: times;">A. Modify MySQL Connection Settings</span></span></h3>

<p style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">By default, the app connects to a local MySQL database. Users can change the database host, username, and password inside the Python files.</span></span></p>
<h4><span style="font-weight: normal;"><span style="font-family: times;">Steps to Update Database Credentials</span></span></h4>
<ol>
<li><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Open the following Python files:</span></span></div><ul>
<li style="text-align: left;"><code inline="" style="font-weight: normal;"><span style="font-family: times;">hotel.py</span></code></li>
<li style="text-align: left;"><code inline="" style="font-weight: normal;"><span style="font-family: times;">room.py</span></code></li>
<li style="text-align: left;"><code inline="" style="font-weight: normal;"><span style="font-family: times;">reservations.py</span></code></li>
<li style="text-align: left;"><code inline="" style="font-weight: normal;"><span style="font-family: times;">customer.py</span></code></li>
</ul>
</li>
<li><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Locate the database connection section:</span></span></div><pre><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">conn = mysql.connector.connect(</span></span></div><code class="language-python" style="font-weight: normal;"><span style="font-family: times;"><div style="text-align: left;">    host="localhost",</div><div style="text-align: left;">    user="root",</div><div style="text-align: left;">    password="yourpassword",</div><div style="text-align: left;">    database="management"</div><div style="text-align: left;">)</div></span></code></pre>
</li>
<li><div style="text-align: left;"><span style="font-family: times;"><span style="font-weight: normal;">Update the values</span><span style="font-weight: normal;"> to match your MySQL settings:</span></span></div><pre><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">conn = mysql.connector.connect(</span></span></div><code class="language-python" style="font-weight: normal;"><span style="font-family: times;"><div style="text-align: left;">    host="your-server-ip",</div><div style="text-align: left;">    user="admin_user",</div><div style="text-align: left;">    password="securepassword",</div><div style="text-align: left;">    database="hotel_db"</div><div style="text-align: left;">)</div></span></code></pre>
</li>
<li style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Save the changes and restart the app.</span></span></li>
</ol>
<hr style="text-align: left;" />
<h3><span style="font-weight: normal;"><span style="font-family: times;">B. Change Database Name</span></span></h3>
<p style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">By default, the database is named "management". To use a different database:</span></span></p>
<ol>
<li style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Open MySQL Workbench or another MySQL tool.</span></span></li>
<li><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Rename the database or create a new one:</span></span></div><pre style="text-align: left;"><code class="language-sql" style="font-weight: normal;"><span style="font-family: times;">CREATE DATABASE hotel_system;
</span></code></pre>
</li>
<li><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Update all Python files to reflect the new name:</span></span></div><pre style="text-align: left;"><code class="language-python" style="font-weight: normal;"><span style="font-family: times;">database="hotel_system"
</span></code></pre>
</li>
</ol>
<hr style="text-align: left;" />
<h2><span style="font-family: times;">2. UI Customization (Changing App Appearance)</span></h2><h3><span style="font-weight: normal;"><span style="font-family: times;">A. Modify Window Size &amp; Layout</span></span></h3>

<ul>
<li><div style="text-align: left;"><span style="font-family: times;"><span style="font-weight: normal;">The </span><span style="font-weight: normal;">default window size</span><span style="font-weight: normal;"> is set in </span><code inline="" style="font-weight: normal;">hotel.py</code><span style="font-weight: normal;">:</span></span></div><pre style="text-align: left;"><code class="language-python" style="font-weight: normal;"><span style="font-family: times;">self.master.geometry("1440x900+0+0")  # Width x Height + X Position + Y Position
</span></code></pre>
</li>
<li><div style="text-align: left;"><span style="font-family: times;"><span style="font-weight: normal;">Change the </span><span style="font-weight: normal;">window dimensions</span><span style="font-weight: normal;"> as needed:</span></span></div><pre style="text-align: left;"><code class="language-python" style="font-weight: normal;"><span style="font-family: times;">self.master.geometry("1280x720+100+50")  # Adjusted for 720p screens
</span></code></pre>
</li>
</ul>
<h3><span style="font-weight: normal;"><span style="font-family: times;">B. Update Background Colors &amp; Themes</span></span></h3>
<ul>
<li><div style="text-align: left;"><span style="font-family: times;"><span style="font-weight: normal;">The </span><span style="font-weight: normal;">default color</span><span style="font-weight: normal;"> for forms is set in </span><code inline="" style="font-weight: normal;">room.py</code><span style="font-weight: normal;">, </span><code inline="" style="font-weight: normal;">reservations.py</code><span style="font-weight: normal;">, and </span><code inline="" style="font-weight: normal;">customer.py</code><span style="font-weight: normal;">:</span></span></div><pre style="text-align: left;"><code class="language-python" style="font-weight: normal;"><span style="font-family: times;">self.master.configure(bg="#d84c42")  # Red color
</span></code></pre>
</li>
<li><div style="text-align: left;"><span style="font-family: times;"><span style="font-weight: normal;">Change the </span><span style="font-weight: normal;">background color</span><span style="font-weight: normal;"> by replacing the </span><span style="font-weight: normal;">hex code</span><span style="font-weight: normal;">:</span></span></div><pre style="text-align: left;"><code class="language-python" style="font-weight: normal;"><span style="font-family: times;">self.master.configure(bg="#2c3e50")  # Dark Blue theme
</span></code></pre>
</li>
</ul>
<h3><span style="font-weight: normal;"><span style="font-family: times;">C. Replace Button &amp; Banner Images</span></span></h3>
<p style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">The UI loads images for banners, buttons, and logos from local files.</span></span></p>
<ul>
<li><div style="text-align: left;"><span style="font-family: times;"><span style="font-weight: normal;">Example (from </span><code inline="" style="font-weight: normal;">hotel.py</code><span style="font-weight: normal;">):</span></span></div><pre style="text-align: left;"><code class="language-python" style="font-weight: normal;"><span style="font-family: times;">img1 = Image.open("/Users/pop/Downloads/travelbanner.png")
</span></code></pre>
</li>
<li><div style="text-align: left;"><span style="font-family: times;"><span style="font-weight: normal;">To </span><span style="font-weight: normal;">use a different image</span><span style="font-weight: normal;">, update the file path:</span></span></div><pre style="text-align: left;"><code class="language-python" style="font-weight: normal;"><span style="font-family: times;">img1 = Image.open("assets/new_banner.png")
</span></code></pre>
</li>
<li><div style="text-align: left;"><span style="font-family: times;"><span style="font-weight: normal;">Recommended </span><span style="font-weight: normal;">image size</span><span style="font-weight: normal;">:</span></span></div><ul>
<li style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Top Banner: <code inline="">1440x200 pixels</code></span></span></li>
<li style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Button Icons: <code inline="">94x29 pixels</code></span></span></li>
<li style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Main Background: <code inline="">1440x668 pixels</code></span></span></li>
</ul>
</li>
</ul>
<hr style="text-align: left;" />
<h2><span style="font-family: times;">3. Room &amp; Reservation Settings</span></h2><h3><span style="font-weight: normal;"><span style="font-family: times;">A. Change Available Room Types</span></span></h3>

<p style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">By default, the system supports Single and Double rooms. To add more:</span></span></p>
<ol>
<li><div style="text-align: left;"><span style="font-family: times;"><span style="font-weight: normal;">Open </span><code inline="" style="font-weight: normal;">room.py</code><span style="font-weight: normal;"> and find:</span></span></div><pre style="text-align: left;"><code class="language-python" style="font-weight: normal;"><span style="font-family: times;">combobox_room_type["value"] = ("Single", "Double")
</span></code></pre>
</li>
<li><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Add new room types:</span></span></div><pre style="text-align: left;"><code class="language-python" style="font-weight: normal;"><span style="font-family: times;">combobox_room_type["value"] = ("Single", "Double", "Queen Suite", "King Suite")
</span></code></pre>
</li>
</ol>
<h3><span style="font-weight: normal;"><span style="font-family: times;">B. Set Default Room Prices</span></span></h3>
<p style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">The system does not store default room rates, but you can add pricing logic.</span></span></p>
<ol>
<li><div style="text-align: left;"><span style="font-family: times;"><span style="font-weight: normal;">Open </span><code inline="" style="font-weight: normal;">reservations.py</code><span style="font-weight: normal;"> and find the pricing dictionary:</span></span></div><pre><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">room_type_rates = {</span></span></div><code class="language-python" style="font-weight: normal;"><span style="font-family: times;"><div style="text-align: left;">    "Single": 100,</div><div style="text-align: left;">    "Double": 150</div><div style="text-align: left;">}</div></span></code></pre>
</li>
<li><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Add new rates:</span></span></div><pre><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">room_type_rates = {</span></span></div><code class="language-python" style="font-weight: normal;"><span style="font-family: times;"><div style="text-align: left;">    "Single": 100,</div><div style="text-align: left;">    "Double": 150,</div><div style="text-align: left;">    "Queen Suite": 200,</div><div style="text-align: left;">    "King Suite": 300</div><div style="text-align: left;">}</div></span></code></pre>
</li>
<li style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">The system will now calculate room costs automatically.</span></span></li>
</ol>
<hr style="text-align: left;" />
<h2><span style="font-family: times;">4. Reservation &amp; Payment Customization</span></h2><h3><span style="font-weight: normal;"><span style="font-family: times;">A. Modify VAT &amp; Discounts</span></span></h3>

<ul>
<li style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Premium customers automatically receive a discount. To change it:</span></span></li>
</ul>
<ol>
<li><div style="text-align: left;"><span style="font-family: times;"><span style="font-weight: normal;">Open </span><code inline="" style="font-weight: normal;">reservations.py</code><span style="font-weight: normal;"> and find:</span></span></div><pre><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">if customer_type == "premium":</span></span></div><code class="language-python" style="font-weight: normal;"><div style="text-align: left;"><span style="font-family: times;">    discount_value = "10"  # 10% discount</span></div></code></pre>
</li>
<li><div style="text-align: left;"><span style="font-family: times;"><span style="font-weight: normal;">Change the value (e.g., </span><span style="font-weight: normal;">15% discount</span><span style="font-weight: normal;">):</span></span></div><pre style="text-align: left;"><code class="language-python" style="font-weight: normal;"><span style="font-family: times;">discount_value = "15"
</span></code></pre>
</li>
</ol>
<ul>
<li><div style="text-align: left;"><span style="font-family: times;"><span style="font-weight: normal;">The default </span><span style="font-weight: normal;">VAT rate</span><span style="font-weight: normal;"> is </span><code inline="" style="font-weight: normal;">20%</code><span style="font-weight: normal;">. To change it:</span></span></div><pre style="text-align: left;"><code class="language-python" style="font-weight: normal;"><span style="font-family: times;">self.var_VAT.set("15")  # Set VAT to 15%
</span></code></pre>
</li>
</ul>
<hr style="text-align: left;" />
</h2><h3><span style="font-weight: normal;"><span style="font-family: times;">B. Change Payment Methods</span></span></h3>
<p style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">By default, the system supports Cash, Credit Card, and PayPal.</span></span></p>
<ol>
<li><div style="text-align: left;"><span style="font-family: times;"><span style="font-weight: normal;">Open </span><code inline="" style="font-weight: normal;">reservations.py</code><span style="font-weight: normal;"> and find:</span></span></div><pre style="text-align: left;"><code class="language-python" style="font-weight: normal;"><span style="font-family: times;">combobox_payment_method["value"] = ("Cash", "Credit Card", "Debit Card", "Google Pay", "Apple Pay", "PayPal")
</span></code></pre>
</li>
<li><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Add new methods:</span></span></div><pre style="text-align: left;"><code class="language-python" style="font-weight: normal;"><span style="font-family: times;">combobox_payment_method["value"] = ("Cash", "Credit Card", "Crypto", "Payoneer")
</span></code></pre>
</li>
</ol>
<hr style="text-align: left;" />
<h2><span style="font-family: times;">5. Enabling Security Features</span></h2><h3><span style="font-weight: normal;"><span style="font-family: times;">A. Restrict User Access with Login System</span></span></h3>

<p style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Currently, the app does not require authentication. To enable login:</span></span></p>
<ol>
<li><div style="text-align: left;"><span style="font-family: times;"><span style="font-weight: normal;">Add a login screen</span><span style="font-weight: normal;"> before opening the main dashboard:</span></span></div><pre><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">from tkinter import simpledialog</span></span></div><code class="language-python" style="font-weight: normal;"><span style="font-family: times;"><div style="text-align: left;">username = simpledialog.askstring("Login", "Enter Username:")</div><div style="text-align: left;">password = simpledialog.askstring("Login", "Enter Password:", show="*")</div><div style="text-align: left;">if username != "admin" or password != "password123":</div><div style="text-align: left;">    exit()</div></span></code></pre>
</li>
<li style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Modify credentials as needed.</span></span></li>
</ol>
<hr style="text-align: left;" />
<h2><span style="font-family: times;">6. Backup &amp; Restore Data</span></h2><h3><span style="font-weight: normal;"><span style="font-family: times;">A. Automatic Database Backup</span></span></h3>

<p style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">To enable backups, modify <code inline="">hotel.py</code>:</span></span></p>
<ol>
<li><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Import necessary modules:</span></span></div><pre><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">import os</span></span></div><code class="language-python" style="font-weight: normal;"><div style="text-align: left;"><span style="font-family: times;">import datetime</span></div></code></pre>
</li>
<li><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Add a function to create backups:</span></span></div><pre><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">def backup_database():</span></span></div><code class="language-python" style="font-weight: normal;"><span style="font-family: times;"><div style="text-align: left;">    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")</div><div style="text-align: left;">    os.system(f"mysqldump -u root -pYOURPASSWORD management &gt; backup_{timestamp}.sql")</div></span></code></pre>
</li>
<li style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Call <code inline="">backup_database()</code> at application startup.</span></span></li>
</ol>
<hr style="text-align: left;" />
<h3><span style="font-weight: normal;"><span style="font-family: times;">B. Restoring Data from Backup</span></span></h3>
<ol>
<li style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Open MySQL Workbench.</span></span></li>
<li><div style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">Run the following SQL command:</span></span></div><pre style="text-align: left;"><code class="language-sql" style="font-weight: normal;"><span style="font-family: times;">SOURCE /path/to/backup.sql;
</span></code></pre>
</li>
<li style="text-align: left;"><span style="font-weight: normal;"><span style="font-family: times;">The database will be restored.</span></span></li>
</ol>
<hr style="text-align: left;" />
<br />
