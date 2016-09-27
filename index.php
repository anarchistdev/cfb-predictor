<?php
error_reporting(E_ALL);
ini_set('display_errors','On');

include 'setbuilder.php';

$filename = "teams.txt";
// Open the file
$fp = @fopen($filename, 'r');
$teams = array();

// Add each line to an array
if ($fp) {
   $teams = explode("\n", fread($fp, filesize($filename)));
}

if (isset($_POST['submit'])) {
    $team1 = trim($_POST['team1']);
    $team2 = trim($_POST['team2']);
    
    $builder = new SetBuilder($team1);
    $builder->buildSet();
    echo $builder->team->generatePoints() . '  ' . $builder->team->name;
    
    if (isset($team2)) {
        $builder = new SetBuilder($team2);
        $builder->buildSet();
        echo '<br>' . $builder->team->generatePoints() . '  ' . $builder->team->name;
    }

}

?>
<!DOCTYPE html>
<head>
	<link rel="stylesheet" href="./css/chosen.css">

</head>

<body>

<form action="" method="POST" style="padding: 8px;">

    <select name="team1" data-placeholder="Choose a Team..." class="chosen-select" style="width:350px;" tabindex="2">
        <option value = ""></option>
        <?php
        foreach ($teams as $team) {
            echo "<option value='". $team . "'>  " . $team . "  </option>";
        }
        ?>
    </select>

    <select name="team2" data-placeholder="Choose a Team..." class="chosen-select" style="width:350px;" tabindex="2">
        <option value = ""></option>
        <?php
        foreach ($teams as $team) {
            echo "<option value='". $team . "'>  " . $team . "  </option>";
        }
        ?>
    </select>
    
<input type="submit" value="Go" name="submit" style="margin-left: 11%;" />
    
</form>


</body>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js" type="text/javascript"></script>
  <script src="./js/chosen.jquery.js" type="text/javascript"></script>
  
  
  <script type="text/javascript">
    var config = {
      '.chosen-select'           : {},
      '.chosen-select-deselect'  : {allow_single_deselect:true},
      '.chosen-select-no-single' : {disable_search_threshold:10},
      '.chosen-select-no-results': {no_results_text:'Oops, nothing found!'},
      '.chosen-select-width'     : {width:"95%"}
    }
    for (var selector in config) {
      $(selector).chosen(config[selector]);
    }
  </script>

</html>
