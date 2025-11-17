<?php
/**
 * check_mysql_connection.php
 *
 * Purpose:
 *   Validate MySQL connectivity using PDO.
 *   Ensures the target database exists (creates it if not).
 *   Prints a success message if connection is established,
 *   otherwise exits with an error message.
 *
 * Usage:
 *   php check_mysql_connection.php
 *
 * Expected Output:
 *   ✅ Database 'test' created or already exists
 *   ✅ Connected successfully to MySQL (PDO)
 *
 * Notes:
 *   - Ensure MySQL server is running locally.
 *   - Update $servername, $username, $password, and $dbname as needed.
 *   - Default credentials assume root user with no password.
 */

// Database configuration (adjust as per your environment)
$servername = "localhost";
$username   = "root";
$password   = "";
$dbname     = "test";

try {
    // Connect to MySQL server (without specifying DB first)
    $pdo = new PDO("mysql:host=$servername", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Create database if it does not exist
    $sql = "CREATE DATABASE IF NOT EXISTS `$dbname` CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci";
    $pdo->exec($sql);
    echo "✅ Database '$dbname' created or already exists\n";

    // Connect to the specific database
    $pdo = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    echo "✅ Connected successfully to MySQL (PDO)\n";

    // Close connection (optional in PDO, handled by garbage collector)
    $pdo = null;

} catch (PDOException $e) {
    die("❌ Connection failed: " . $e->getMessage() . "\n");
}
?>
