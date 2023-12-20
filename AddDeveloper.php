<html>
  <head>
    <title>Game Database: Add Developer</title>
  </head>

  <body>
      <div id = "links" align = "middle" >
        <h2>Welcome to the database!</h2> <br>
        <a href = "/~scanales/GameDB/home.html">Home</a> |
        <a href = "/~scanales/GameDB/AddPlatform.php">Add a Platform</a> | 
        <a href = "/~scanales/GameDB/AddDeveloper.php">Add a Developer</a> |
				<a href = "/~scanales/GameDB/AddGame.php">Add a Game</a> |
				<a href = "/~scanales/GameDB/ViewGames.php">View All Games</a> |
        <a href = "/~scanales/GameDB/ViewPlatform.php">View All Platform</a> |
				<a href = "/~scanales/GameDB/SelectDeveloper.php">View Games from Developer</a> |
        <a href = "/~scanales/GameDB/SearchBestSeller.php">Best Seller From Developer</a>
      </div>

    <h3>Enter information about an item to add to the database:</h3>

    <form action="AddDeveloper.php" method="post">
      Name: <input type="text" name="NAME"><br>
      Creation: <input type="text" name="CREATION"><br>
      Games: <input type="text" name="GAMES"><br>
      Location: <input type="text" name="Location"><br>
      <input name="submit" type="submit" >
    </form>
    <br><br>

  </body>
</html>

<?php
if (isset($_POST['submit'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $NAME = escapeshellarg($_POST[NAME]);
    $CREATION = escapeshellarg($_POST[CREATION]);
    $GAMES = escapeshellarg($_POST[GAMES]);
		$Location = escapeshellarg($_POST[Location]);
		

    $command = 'python3 Insert_Developer.py' . ' '.  $NAME . ' ' . $CREATION . ' ' .  $GAMES . ' ' . $Location;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<p>command: $command <p>"; 
    // run insert_new_item.py
    system($escaped_command);           
}
?>
