# 🛠️ XAMPP Installation Checklist

This guide walks you through installing XAMPP, verifying MySQL setup, and testing with a sample PHP script that connects to a test database.

---

## ✅ Step 1: Download & Install XAMPP

1. Visit [https://www.apachefriends.org](https://www.apachefriends.org)
2. Download the latest version of **XAMPP for Windows/Linux/Mac**
3. Run the installer and follow default prompts
4. Launch **XAMPP Control Panel**
5. Start **Apache** and **MySQL** services

---

## ✅ Step 2: Verify Installation

- Open browser and go to:  
  `http://localhost` → You should see the XAMPP dashboard  
- Click **phpMyAdmin** → You should see the MySQL interface

---

## ✅ Step 3: Create Test Script — `test-xampp.php`

Place this file inside your `htdocs` folder (e.g., `C:\xampp\htdocs\test-xampp.php`):

```php
<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "test_db";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Create DB if not exists
$conn->query("CREATE DATABASE IF NOT EXISTS $dbname");
$conn->select_db($dbname);

// Create table
$conn->query("CREATE TABLE IF NOT EXISTS sample_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
)");

// Insert sample row
$conn->query("INSERT INTO sample_table (name) VALUES ('XAMPP Test')");

// Fetch and display
$result = $conn->query("SELECT * FROM sample_table");
while($row = $result->fetch_assoc()) {
    echo "ID: " . $row["id"] . " | Name: " . $row["name"] . "<br>";
}

$conn->close();
?>
```

---

## ✅ Step 4: Run the Test

- Open browser and visit:  
  `http://localhost/test-xampp.php`  
- You should see:  
  `ID: 1 | Name: XAMPP Test`

---

## 🧪 Outcome

- XAMPP is installed and running  
- MySQL is accessible via `phpMyAdmin`  
- PHP can connect to MySQL and perform basic operations  
- Your local dev environment is ready for database-backed GenAI apps

