<?php
ini_set('error_reporting', E_ALL);
ini_set('display_errors', 'On');
if ($db = sqlite_open('../sql/tapwatch.sqlite', 0666, $sqliteerror)) {
$email = $_GET['email'];

$sql = "INSERT INTO subscriber (email, signupdatetime) VALUES('" . $email . "', " . time() . ")";
// print $sql;
$result = sqlite_exec($db, $sql);

if (!$result) {
  $_SESSION['error'][] = "There was an error signing you up!";
} else {
  $_SESSION['message'][] = "Signup successful!";
}
} else {
  die($sqliteerror);
}
header('location: index.php');
