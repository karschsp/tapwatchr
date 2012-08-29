<?php
ini_set('error_reporting', E_ALL);
ini_set('display_errors', 'On');

?>
<html>
  <head>
    <title>Tapwatchr</title>
    <style type="text/css">

    </style>
    <script type="text/javascript">

    </script>
  
  </head>
  <body>
    <h1>Tapwatchr</h1>
    <form name="signup" id="signup" method="POST" action="signup.php">
      <input type="email" id="email" name="email" placeholder="you@example.com" />
      <input type="submit" value="Signup" />
    </form>
    <h2>Taps we're watching</h2>
    <?php
    $taps_json = file_get_contents('../json/taps.json');
    $taps = json_decode($taps_json);
    foreach ($taps->Taps as $tap) {
      print '<h3>' . $tap->Name . '</h3>';
      $tap_json = file_get_contents('../json/' . $tap->ShortName . '.json');
      $beers = json_decode($tap_json);
      foreach ($beers as $beer) {
        print '<li>' . $beer . '</li>';
      }
    }
    ?>
    <blockquote>beer...the cause of, and solution to, all of life's problems.</blockquote>
<a href="https://twitter.com/tapwatchr" class="twitter-follow-button" data-show-count="false" data-size="large">Follow @tapwatchr</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
  </body>
</html>
