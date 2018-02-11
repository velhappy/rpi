
<html>
	<head>
	<meta http-equiv="refresh" content="2"/>

	</head>
	<body>
<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "iot";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT * FROM sensor_data ORDER BY id DESC";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Temp: " . $row["temp_sensor"]."<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>
</body>
</html>
