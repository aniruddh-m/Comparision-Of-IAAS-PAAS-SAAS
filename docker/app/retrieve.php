<?php  
    $result = array("1", "2"); #this ensures that the error message is not shown when the page is first loaded
    if(array_key_exists('submit', $_POST)){
      $result = retrieve();
    }


  
    function retrieve(){

      $pdo = new PDO('mysql:host=mysql;dbname=students;charset=utf8', 'root', 'root');
      $stmt = $pdo->prepare("
          select records.name, records.usn, records.dept
          from records
          where records.usn='". $_POST['USN']  ."'
      ");
      $stmt->execute();
      $students = $stmt->fetchAll(PDO::FETCH_ASSOC);
      return $students;
    
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
        "RETRIEVE" operation
      </h1>
    </div>
    <div class="s01"  style="padding-right:20px;">
      <form name="CreateForm" method="POST">
        <div class="inner-form">

          <div class="input-field first-wrap">
            <input id="USN" type="text" placeholder="USN" name="USN"/>
          </div>          
          <div class="input-field third-wrap" >
            <button class="btn-search" type="submit" name="submit">Enter</button>
          </div>
        </div>
      </form>
      <?php 
      if(count($result)==1){
        ?>
        <table style="border-spacing:0.5rem; border:1px solid black; border-collapse:collapse;margin-left:50px;">
        <caption><b>Student Details</b></caption>
          <thead>
            <tr>
              <th style="border:1px solid black; ">Name</th>
              <th style="border:1px solid black; ">USN</th>
              <th style="border:1px solid black; ">Branch</th>
            </tr>
          </thead>  

          <tbody>
            <?foreach($result as $r):?>
            
              <tr >
                <td style="padding-left:10px; padding-right:10px;border:1px solid black;"><?echo $r['name']?></td>
                <td style="padding-left:10px; padding-right:10px;border:1px solid black;"><?echo $r['usn']?></td>
                <td style="padding-left:10px; padding-right:10px;border:1px solid black;"><?echo $r['dept']?></td>
              </tr>
              <?php endforeach?>
          </tbody>
        </table>
      <?}
      else if(count($result)==0){
        echo '<script>alert("This student does not exist")</script>';
      }
    ?>
    </p>
    </div>
    

  


  </body>
</html>