<html>
    <head>
        <title>CIS 322 REST-api demo: Laptop list</title>
    </head>

    <body>
        <h1>List All</h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service:5000/listAll');
            $obj = json_decode($json);
	          $laptops = $obj->Times;
            foreach ($laptops as $l) {
                echo "<li>$l</li>";
            }
            ?>
        </ul>

        <h1>List Open Only</h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service:5000/listOpenOnly');
            $obj = json_decode($json);
	          $laptops = $obj->openTime;
            foreach ($laptops as $l) {
                echo "<li>$l</li>";
            }
            ?>
        </ul>

        <h1>List Close Only</h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service:5000/listCloseOnly');
            $obj = json_decode($json);
	          $laptops = $obj->closeTime;
            foreach ($laptops as $l) {
                echo "<li>$l</li>";
            }
            ?>
        </ul>

        <h1>List All JSON</h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service:5000/listAll/json');
            $obj = json_decode($json);
	          $laptops = $obj->Times;
            foreach ($laptops as $l) {
                echo "<li>$l</li>";
            }
            ?>
        </ul>

        <h1>List Open Only JSON</h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service:5000/listOpenOnly/json');
            $obj = json_decode($json);
	          $laptops = $obj->openTime;
            foreach ($laptops as $l) {
                echo "<li>$l</li>";
            }
            ?>
        </ul>

        <h1>List Close Only JSON</h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service:5000/listCloseOnly/json');
            $obj = json_decode($json);
	          $laptops = $obj->closeTime;
            foreach ($laptops as $l) {
                echo "<li>$l</li>";
            }
            ?>
        </ul>

        <h1>List Open All CSV</h1>
        <ul>
          <?php
          $json = file_get_contents('http://laptop-service:5000/listAll/csv');
          $obj = str_getcsv($json);
          foreach ($obj as $l) {
              echo "<li>$l</li>";
          }
          ?>
        </ul>

        <h1>List Open Only CSV</h1>
        <ul>
          <?php
          $json = file_get_contents('http://laptop-service:5000/listOpenOnly/csv');
          $obj = str_getcsv($json);
          foreach ($obj as $l) {
              echo "<li>$l</li>";
          }
          ?>
        </ul>

        <h1>List Close Only CSV</h1>
        <ul>
          <?php
          $json = file_get_contents('http://laptop-service:5000/listCloseOnly/csv');
          $obj = str_getcsv($json);
          foreach ($obj as $l) {
              echo "<li>$l</li>";
          }
          ?>
        </ul>

        <h1>List Open Only JSON Top 5</h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service:5000/listOpenOnly/json?top=5');
            $obj = json_decode($json);
            $laptops = $obj->openTime;
            foreach ($laptops as $l) {
                echo "<li>$l</li>";
            }
            ?>
        </ul>

        <h1>List Close Only JSON Top 4</h1>
        <ul>
            <?php
            $json = file_get_contents('http://laptop-service:5000/listCloseOnly/json?top=4');
            $obj = json_decode($json);
	          $laptops = $obj->closeTime;
            foreach ($laptops as $l) {
                echo "<li>$l</li>";
            }
            ?>
        </ul>

        <h1>List Open Only CSV Top 3</h1>
        <ul>
          <?php
          $json = file_get_contents('http://laptop-service:5000/listOpenOnly/csv?top=3');
          $obj = str_getcsv($json);
          foreach ($obj as $l) {
              echo "<li>$l</li>";
          }
          ?>
        </ul>

        <h1>List Close Only CSV Top 6</h1>
        <ul>
          <?php
          $json = file_get_contents('http://laptop-service:5000/listCloseOnly/csv?top=6');
          $obj = str_getcsv($json);
          foreach ($obj as $l) {
              echo "<li>$l</li>";
          }
          ?>
        </ul>
    </body>
</html>
