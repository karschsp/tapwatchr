<?php
ini_set('error_reporting', E_ALL);
ini_set('display_errors', 'On');

?>
<!DOCTYPE html>
<html>
  <head>
    <title>Tapwatchr</title>
    <meta name="viewport" content="width=device-width, initial-scale=1"> 
    <link rel="stylesheet" href="http://code.jquery.com/mobile/1.2.0-alpha.1/jquery.mobile-1.2.0-alpha.1.min.css" />
    <script src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
    <script src="http://code.jquery.com/mobile/1.2.0-alpha.1/jquery.mobile-1.2.0-alpha.1.min.js"></script>
</head>     
  
  </head>
  <body>
    <div data-role="page">
      <div data-role="header">
        <h1>Tapwatchr</h1>
        <form name="signup" id="signup" method="POST" action="signup.php">
          <input type="email" id="email" name="email" placeholder="you@example.com" />
          <input type="submit" value="Signup" />
        </form>
      </div>
      <div data-role="content">
        <h2>Taps we're watching</h2>
        <?php
        $taps_json = file_get_contents('../json/taps.json');
        $taps = json_decode($taps_json);
        foreach ($taps->Taps as $tap) {
          print '<div class="tap" id="tap-' . $tap->ShortName . '" data-role="collapsible" data-theme="b" data-content-theme="d" data-inset="false">';
          print '<h3>' . $tap->Name . '</h3>';
          $tap_json = file_get_contents('../json/taps/' . $tap->ShortName . '.json');
          $beers = json_decode($tap_json);
          print('<ul>');
          foreach ($beers as $beer) {
            print '<li>' . $beer . '</li>';
          }
          print('</ul>');
          print '</div>';
        }
        ?>
      </div>
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-34427877-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>

    <footer>
      <blockquote>beer...the cause of, and solution to, all of life's problems.</blockquote>
<a href="https://twitter.com/tapwatchr" class="twitter-follow-button" data-show-count="false" data-size="large">Follow @tapwatchr</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
    </footer>
  </body>
</html>
