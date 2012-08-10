<?php
print 'hey';
if ($db = sqlite_open('tapwatch.sqlite', 0666, $sqliteerror)) {
print 'now';
$email = $_POST['email'];

$sql = "INSERT INTO subscriber (email, signupdatetime) VALUES('" . $email . "', " . date() . ")";
print $sql;
$result = sqlite_exec($db, $sql);



if (!$result) {
  $_SESSION['error'][] = "There was an error signing you up!";
} else {
  $_SESSION['message'][] = "Signup successful!";
}
} else {
  die($sqliteerror);
}
