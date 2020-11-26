<?php
?>

<!doctype html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="author" content="colorlib.com">
    <link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet" />
    <link href="style.css" rel="stylesheet"/>
    <title>CRUD Homepage</title>
  </head>

<body>

<div>
    <div class="topbar" style="height: 80px; background-color: dimgrey;">   
      <h1 style="text-align: center; padding-top: 20px; color: white">
        CRUD Homepage
      </h1>
    </div>

    <div class="btn-group" style="width:100%; padding-top:200px; padding-left:50px; padding-right:50px;">
        <a href="create.php"><button style="width:49.5%; padding:50px; background-color:dimgrey; color:white;">Create a new Record</button></a>
        <a href="delete.php"><button style="width:49.5%; padding:50px;background-color:dimgrey; color:white;">Delete a Record</button></a>
    </div>
    <div class="btn-group" style="width:100%; padding-top:200px; padding-left:50px; padding-right:50px;">
        <a href="update.php"><button style="width:49.5%; padding:50px;background-color:dimgrey;color:white;">Update an existing Record</button></a>
        <a href="retrieve.php"><button style="width:49.5%; padding:50px;background-color:dimgrey;color:white;">Retrieve an existing Record</button></a>
    </div>
</div>
</body>
</html>