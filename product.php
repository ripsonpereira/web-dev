<?php
	$id=$_POST["id"];
	$name=$_POST["name"];
	$price=$_POST["price"];
	$info=$_POST["description"];
	$query = $_POST["query"];
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "products";
	$conn = mysqli_connect($servername, $username, $password,$dbname);
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
	if ($query == 'CREATE') {
		$sql="CREATE TABLE product (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL, price INT(10) NOT NULL, description VARCHAR(200)NOT NULL)";
		if (mysqli_query($conn, $sql)) {
			echo "New table created successfully";
		}
		else {
			echo "Error: " . $sql . "<br>" . mysqli_error($conn);
		}
	}
	if ($query == "ADD") {
		$sql = "INSERT INTO product (id, name, price,description) values ('$id', '$name', '$price','$info')";
		if (mysqli_query($conn, $sql)) {
			echo "New record created successfully";
		}
		else {
			echo "Error: " . $sql . "<br>" . mysqli_error($conn);
		}
	}
	if ($query == "DELETE") {
		$sql = "DELETE FROM `product` WHERE id='$id'";
		if (mysqli_query($conn, $sql)) {
			echo "Record deleted successfully";
		}
		else {
			echo "Error: " . $sql . "<br>" . mysqli_error($conn);
		}
	}
	mysqli_close($conn);
?>