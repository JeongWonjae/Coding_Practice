<?php

    $id=$_POST['id'];
    $user_id=$_POST['user_id'];
    $name=$_POST['name'];
    $pw=$_POST['pw'];
    $memo=$_POST['memo'];

    $date=date("Y. m. d. H : i : s", time());
    $ip=getenv("REMOTE_ADDR");

    $connect=mysqli_connect("localhost","root","root");
    mysqli_select_db($connect, "phptest");

    if(!$connect)
    {
        echo "Failed connect mysql.". mysqli_error();
    }

    $query="INSERT INTO board(id, user_id, name, pw, memo, date, ip) VALUES('$id', '$user_id', '$name', '$pw', '$memo', '$date', '$ip')";
    if(mysqli_query($connect, $query))
    {
        echo "Success SQL query.";
    }
    else
    {
        echo "Failed SQL query.";
    }
    mysqli_close($connect);
?>