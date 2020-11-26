<?php 
  
  if(array_key_exists('submit', $_POST)){
    del_from_db();
  }

  function del_from_db(){
    $pdo = new PDO('mysql:host=mysql;dbname=students;charset=utf8', 'root', 'root');
    $usn = $_POST['USN'];

    $stmt = $pdo->prepare('delete from records where usn = "'. $usn .'";');
    $stmt->execute();

    echo '<script>alert("Successfully deleted from the database")</script>';
  }
?>

<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="author" content="colorlib.com">
    <link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet" />
    <link href="style.css" rel="stylesheet"/>
  </head>

  <body>
    <div class="topbar" style="height: 80px; background-color: dimgrey;">
      <h1 style="text-align: center; padding-top: 20px; color: white">
        "DELETE" operation
      </h1>
    </div>
    <div class="s01">
      <form name="CreateForm" method="POST">
        <div class="inner-form">

          <div class="input-field first-wrap">
            <input id="USN" type="text" placeholder="USN" name="USN"/>
          </div>          
          <div class="input-field third-wrap">
            <button class="btn-search" type="submit" name="submit">Enter</button>
          </div>
        </div>
      </form>
    </div>
  </body>
</html>