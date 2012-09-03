<?php
ini_set('error_reporting', E_ALL);
ini_set('display_errors', 'On');
try {
  $database = new SQLiteDatabase('../../../sql/tapwatch.sqlite', 0666, $error);
  $query = "SELECT * FROM subscriber";
  if ($result = $database->query($query, SQLITE_BOTH, $error)) {
    while($row = $result->fetch()) {
      print $row['email'] . ' ' . $row['signupdatetime'] . '<br />';
    }
  } else {
    die($error);
  }
} catch(Exception $e) {
  die($error);
}
?>
